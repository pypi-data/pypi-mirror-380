from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, List, Optional, cast

from ....types import UnitTestCase, UnitTestSuite
from .test import TestInterface

if TYPE_CHECKING:
    from ...unit_testers.unit_tester import UnitTesterInterface


class UnitTestInterface(TestInterface, ABC):

    def __init__(self):
        super().__init__()
        self._tester: Optional[UnitTesterInterface] = None
        self._run: bool = False
        self._stdin: str = ""

    def set_input(self, stdin: str) -> None:
        self._stdin = stdin

    def get_input(self) -> str:
        return self._stdin

    @abstractmethod
    def collect_tests(self) -> UnitTestSuite:
        pass

    def get_score(self) -> float:
        tests = self.collect_tests()
        if not self._run:
            self.add_to_output("unit-tests", tests)
            self._run = True

        cases: List[UnitTestCase] = []
        suites: List[UnitTestSuite] = [tests]
        while suites:
            suite = suites.pop()
            for test in suite["cases"]:
                if "success" in test.keys():
                    cases.append(cast(UnitTestCase, test))
                else:
                    suites.append(cast(UnitTestSuite, test))

        outputs: List[bool] = [test["success"] for test in cases]
        tests_passed: int = sum(outputs)
        tests_total: int = max(len(outputs), 1)

        return (tests_passed / tests_total) * self.get_max_score() * self.get_weight()

    def get_tester(self) -> UnitTesterInterface:
        assert self._tester is not None
        return self._tester

    def set_tester(self, tester: UnitTesterInterface):
        self._tester = tester
