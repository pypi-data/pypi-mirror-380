from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, List, Optional, Sequence

from .simple import make_tests_from_strs
from .validation import validate_unique_argument

if TYPE_CHECKING:
    from ...builders.interfaces.builder import BuilderInterface
    from .output_tests import CLIOutputTest


def make_tests_from_files(
    *,  # kwargs-only; to avoid confusion with argument sequence.
    builder: BuilderInterface,
    names: Sequence[str],
    input_files: Optional[Sequence[Path]] = None,
    input_strs: Optional[Sequence[str]] = None,
    expected_output_files: Optional[Sequence[Path]] = None,
    expected_output_strs: Optional[Sequence[str]] = None,
    weights: Optional[Sequence[float]] = None,  # Defaults to equal-weight.
    flag_sets: Optional[Sequence[List[str]]] = None,
) -> List[CLIOutputTest]:

    # Ensure only one input is specified, then convert files to strs.
    validate_unique_argument(input_files=input_files, input_strs=input_strs)
    if input_strs is None:
        input_strs = []
        assert input_files is not None
        for input_file in input_files:
            with open(Path(input_file), "r") as f:
                input_strs.append(f.read())

    # Ensure only one expected output is specified, then convert files to strs.
    validate_unique_argument(
        expected_output_files=expected_output_files,
        expected_output_strs=expected_output_strs,
    )
    if expected_output_strs is None:
        expected_output_strs = []
        assert expected_output_files is not None
        for expected_output_file in expected_output_files:
            with open(Path(expected_output_file), "r") as f:
                expected_output_strs.append(f.read())

    return make_tests_from_strs(
        builder=builder,
        names=names,
        inputs=input_strs,
        expected_outputs=expected_output_strs,
        weights=weights,
        flag_sets=flag_sets,
    )
