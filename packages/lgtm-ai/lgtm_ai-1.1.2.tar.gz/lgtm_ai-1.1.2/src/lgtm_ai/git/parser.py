import re
from typing import Literal

from lgtm_ai.git.exceptions import GitDiffParseError
from pydantic import BaseModel


class ModifiedLine(BaseModel):
    line: str
    line_number: int
    relative_line_number: int
    modification_type: Literal["added", "removed"]
    hunk_start_new: int | None = None
    hunk_start_old: int | None = None


class DiffFileMetadata(BaseModel):
    new_file: bool
    deleted_file: bool
    renamed_file: bool
    new_path: str
    old_path: str | None = None

    model_config = {"extra": "ignore"}


class DiffResult(BaseModel):
    metadata: DiffFileMetadata
    modified_lines: list[ModifiedLine]


def parse_diff_patch(metadata: DiffFileMetadata, diff_text: object) -> DiffResult:
    if not isinstance(diff_text, str):
        raise GitDiffParseError("Diff text is not a string")

    lines = diff_text.strip().splitlines()

    modified_lines = []

    old_line_num = 0
    new_line_num = 0
    rel_position = -1  # We just don't count the first hunk, but we do count the rest
    hunk_start_old = None
    hunk_start_new = None

    try:
        for line in lines:
            hunk_match = re.match(r"^@@ -(\d+),?\d* \+(\d+),?\d* @@", line)
            rel_position += 1
            if hunk_match:
                old_line_num = int(hunk_match.group(1))
                new_line_num = int(hunk_match.group(2))
                hunk_start_new = new_line_num
                hunk_start_old = old_line_num
                continue

            if line.startswith("+") and not line.startswith("+++"):
                modified_lines.append(
                    ModifiedLine(
                        line=line[1:],
                        line_number=new_line_num,
                        relative_line_number=rel_position,
                        modification_type="added",
                        hunk_start_new=hunk_start_new,
                        hunk_start_old=hunk_start_old,
                    )
                )
                new_line_num += 1

            elif line.startswith("-") and not line.startswith("---"):
                modified_lines.append(
                    ModifiedLine(
                        line=line[1:],
                        line_number=old_line_num,
                        relative_line_number=rel_position,
                        modification_type="removed",
                        hunk_start_new=hunk_start_new,
                        hunk_start_old=hunk_start_old,
                    )
                )
                old_line_num += 1

            else:
                old_line_num += 1
                new_line_num += 1
    except (ValueError, TypeError, KeyError) as err:
        raise GitDiffParseError("Failed to parse diff patch") from err

    return DiffResult(metadata=metadata, modified_lines=modified_lines)
