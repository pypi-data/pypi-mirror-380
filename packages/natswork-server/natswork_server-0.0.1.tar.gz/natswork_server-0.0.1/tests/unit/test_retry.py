from natswork_server.retry import (
    CustomRetryPolicy,
    ExponentialBackoffRetryPolicy,
    FixedDelayRetryPolicy,
    LinearRetryPolicy,
)


def test_fixed_delay_retry_policy():
    policy = FixedDelayRetryPolicy(max_retries=3, delay_seconds=5.0)

    assert policy.calculate_delay(0) == 5.0
    assert policy.calculate_delay(1) == 5.0
    assert policy.calculate_delay(2) == 5.0


def test_exponential_backoff_retry_policy():
    policy = ExponentialBackoffRetryPolicy(
        max_retries=3,
        base_delay=1.0,
        max_delay=300.0,
        jitter=False
    )

    assert policy.calculate_delay(0) == 1.0
    assert policy.calculate_delay(1) == 2.0
    assert policy.calculate_delay(2) == 4.0
    assert policy.calculate_delay(3) == 8.0


def test_exponential_backoff_with_jitter():
    policy = ExponentialBackoffRetryPolicy(
        max_retries=3,
        base_delay=1.0,
        jitter=True
    )

    delay = policy.calculate_delay(1)
    assert 1.5 <= delay <= 2.5


def test_linear_retry_policy():
    policy = LinearRetryPolicy(max_retries=3, delay_increment=5.0)

    assert policy.calculate_delay(0) == 0.0
    assert policy.calculate_delay(1) == 5.0
    assert policy.calculate_delay(2) == 10.0
    assert policy.calculate_delay(3) == 15.0


def test_custom_retry_policy():
    policy = CustomRetryPolicy(
        max_retries=3,
        delay_func=lambda attempt: attempt * 3.0
    )

    assert policy.calculate_delay(1) == 3.0
    assert policy.calculate_delay(2) == 6.0


def test_should_retry():
    policy = FixedDelayRetryPolicy(max_retries=3)

    assert policy.should_retry(0, Exception()) is True
    assert policy.should_retry(2, Exception()) is True
    assert policy.should_retry(3, Exception()) is False
