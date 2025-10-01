import random
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Callable


@dataclass
class RetryPolicy(ABC):
    max_retries: int = 3

    @abstractmethod
    def calculate_delay(self, attempt: int) -> float:
        pass

    def should_retry(self, attempt: int, error: Exception) -> bool:
        return attempt < self.max_retries


class FixedDelayRetryPolicy(RetryPolicy):

    def __init__(self, max_retries: int = 3, delay_seconds: float = 5.0):
        super().__init__(max_retries)
        self.delay_seconds = delay_seconds

    def calculate_delay(self, attempt: int) -> float:
        return self.delay_seconds


class ExponentialBackoffRetryPolicy(RetryPolicy):

    def __init__(
        self,
        max_retries: int = 3,
        base_delay: float = 1.0,
        max_delay: float = 300.0,
        jitter: bool = True
    ):
        super().__init__(max_retries)
        self.base_delay = base_delay
        self.max_delay = max_delay
        self.jitter = jitter

    def calculate_delay(self, attempt: int) -> float:
        delay = self.base_delay * (2 ** attempt)
        delay = min(delay, self.max_delay)

        if self.jitter:
            jitter_amount = delay * 0.25
            delay += random.uniform(-jitter_amount, jitter_amount)

        return max(0, delay)


class LinearRetryPolicy(RetryPolicy):

    def __init__(self, max_retries: int = 3, delay_increment: float = 5.0):
        super().__init__(max_retries)
        self.delay_increment = delay_increment

    def calculate_delay(self, attempt: int) -> float:
        return attempt * self.delay_increment


class CustomRetryPolicy(RetryPolicy):

    def __init__(self, max_retries: int = 3, delay_func: Callable[[int], float] = None):
        super().__init__(max_retries)
        self.delay_func = delay_func or (lambda attempt: attempt * 2.0)

    def calculate_delay(self, attempt: int) -> float:
        return self.delay_func(attempt)
