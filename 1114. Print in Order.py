from enum import Enum
from threading import Condition
from typing import Callable


class State(Enum):
    ONE = 1
    TWO = 2
    THREE = 3


class Foo:
    def __init__(self):
        self.state = State.ONE
        self.cond = Condition()

    def first(self, print_first: Callable[[], None]) -> None:
        with self.cond:
            while self.state != State.ONE:
                self.cond.wait()
            self.state = State.TWO
            self.cond.notifyAll()
            print_first()

    def second(self, print_second: Callable[[], None]) -> None:
        with self.cond:
            while self.state != State.TWO:
                self.cond.wait()
            self.state = State.THREE
            self.cond.notifyAll()
            print_second()

    def third(self, print_third: Callable[[], None]) -> None:
        with self.cond:
            while self.state != State.THREE:
                self.cond.wait()
            self.state = State.ONE
            self.cond.notifyAll()
            print_third()
