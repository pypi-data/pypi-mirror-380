from pathlib import Path


class PathConfig:
    DEFAULT_ROOT_PATH: Path = Path("/autograder")
    DEFAULT_SOURCE_PATH: Path = Path("/autograder/source")
    DEFAULT_SUBMISSION_PATH: Path = Path("/autograder/submission")
    DEFAULT_RESULT_PATH: Path = Path("/autograder/results/results.json")
