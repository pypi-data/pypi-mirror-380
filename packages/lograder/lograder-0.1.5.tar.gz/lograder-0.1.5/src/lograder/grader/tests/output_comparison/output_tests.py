from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, List, Optional, Tuple

from ....data.messages import MessageConfig
from ....os.cmd import run_cmd
from ..interfaces.cli_test import CLITest
from ..interfaces.output_test import OutputTestInterface

if TYPE_CHECKING:
    from ....types import Command
    from ...addons.addon import ExecAddonInterface
    from ...builders.interfaces.builder import BuilderInterface


class CLIOutputTest(CLITest, OutputTestInterface):
    def __init__(self):
        super().__init__()
        self._name: Optional[str] = None
        self._builder: Optional[BuilderInterface] = None

        self._expected_stdout: Optional[str] = None
        self._actual_stdout: Optional[str] = None
        self._stderr: Optional[str] = None

    @classmethod
    def make(
        cls,
        name: str,
        builder: BuilderInterface,
        stdin: str,
        expected_stdout: str,
        weight: float = 1.0,
        args: Optional[Command] = None,
        working_dir: Optional[Path] = None,
        wrap_args: bool = False,
    ) -> CLIOutputTest:
        test = cls()

        test.set_name(name)
        test.set_builder(builder)
        test.set_input(stdin)
        test.set_expected_stdout(expected_stdout)
        test.set_weight(weight)

        test.set_wrap_args(wrap_args)
        if working_dir is not None:
            test.set_working_dir(working_dir)
        if args is not None:
            test.set_args(args)

        return test

    def set_builder(self, builder: BuilderInterface) -> None:
        self._builder = builder

    def get_builder(self) -> BuilderInterface:
        assert self._builder is not None
        return self._builder

    def set_name(self, name: str):
        self._name = name

    def _run_test(self) -> Tuple[int, Command]:
        builder = self.get_builder()
        builder.build_project()
        if builder.get_build_error():
            self.force_fail()
            self.add_to_output("build-fail", {})
            return 1, []

        self.set_working_dir(builder.get_build_directory())

        args = self.get_args()
        command = builder.get_start_command()
        if not command:
            self.force_fail()
            self.get_builder().set_build_error(True)
            self.add_to_output("build-fail", {})
            return 1, []
        command += args

        _tmp_stdout: List[str] = []
        _tmp_stderr: List[str] = []
        try:
            result = run_cmd(
                command,
                self.get_input(),
                [],
                _tmp_stdout,
                _tmp_stderr,
                self.get_working_dir(),
            )
        except FileNotFoundError:
            self.force_fail()
            self.get_builder().set_build_error(True)
            self.add_to_output("build-fail", {})
            return 1, []

        self._actual_stdout = _tmp_stdout.pop()
        self._stderr = _tmp_stderr.pop()

        return result.returncode, command

    def set_expected_stdout(self, expected_stdout: str):
        self._expected_stdout = expected_stdout

    def get_expected_output(self) -> str:
        if self.get_builder().get_build_error():
            return MessageConfig.DEFAULT_BUILD_ERROR
        assert self._expected_stdout is not None
        return self._expected_stdout

    def get_actual_output(self) -> str:
        if self._actual_stdout is None:
            _, _ = self._run_test()
        if self.get_builder().get_build_error():
            return MessageConfig.DEFAULT_BUILD_ERROR
        assert self._actual_stdout is not None
        return self._actual_stdout

    def get_error(self) -> str:
        if self._stderr is None:
            _, _ = self._run_test()
        if self.get_builder().get_build_error():
            return MessageConfig.DEFAULT_BUILD_ERROR
        assert self._stderr is not None
        return self._stderr

    def get_score(self) -> float:
        if self.get_builder().get_build_error():
            if not self._run:
                self.add_to_output("build-fail", {})
                self._run = True
            return 0.0
        return OutputTestInterface.get_score(self)

    def get_name(self) -> str:
        assert self._name is not None
        return self._name

    def add_exec_addon(self, addon: ExecAddonInterface):
        addon.set_builder(self.get_builder())
        addon.set_args(self.get_args())
        addon.set_input(self.get_input())
        self.add_addon(addon)
