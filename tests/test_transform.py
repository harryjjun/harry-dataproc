from contextlib import nullcontext
from datetime import datetime

import pandas as pd
import pytest

from dataproc.transform import str_to_datetime, str_to_unixtime

# 명세 참고자료의 DATASTRINGS
DATASTRINGS = [
    (
        "2026-05-06T11:30:12.365233",
        datetime(2026, 5, 6, 11, 30, 12, 365233),
        1778034612365233,
        nullcontext(),
    ),
    (
        "2024-05-01 10:30:10.000100",
        datetime(2024, 5, 1, 10, 30, 10, 100),
        1714527010000100,
        nullcontext(),
    ),
    (
        "2024-05-01 10:30",
        datetime(2024, 5, 1, 10, 30),
        1714527000000000,
        nullcontext(),
    ),
    (
        "2024/05/01 10:30",
        datetime(2024, 5, 1, 10, 30),
        1714527000000000,
        pytest.raises(ValueError),
    ),
]


# @pytest.mark.parametrize
# 목적 : 같은 테스트 함수를 여러 입력으로 반복 실행
# 출력 : 4개 케이스 = 4개 독립 테스트


# 1. test_str_to_datetime 함수 (parameterized)
@pytest.mark.parametrize(
    "input_str, expected_dt, expected_unix, expectation",
    DATASTRINGS,
)
def test_str_to_datetime(input_str, expected_dt, expected_unix, expectation):
    """str_to_datetime 함수의 parameterized 테스트.

    정상 케이스와 ValueError 발생 케이스를 nullcontext / pytest.raises로 통합.
    """
    # 같은 인터페이스로 두 시나리오(정상 케이스, ValueError 발생 케이스) 처리
    with expectation:
        result = str_to_datetime(input_str)
        assert result == expected_dt


# 2. test_str_to_unixtime 함수 (parameterized)
@pytest.mark.parametrize(
    "input_str, expected_dt, expected_unix, expectation",
    DATASTRINGS,
)
def test_str_to_unixtime(input_str, expected_dt, expected_unix, expectation):
    """str_to_unixtime 함수의 parameterized 테스트."""
    with expectation:
        result = str_to_unixtime(input_str)
        assert result == expected_unix


# 명세 참고자료의 fixture
# 목적 : 테스트들이 공통으로 쓰는 데이터·환경 제공
# 출력 : 1개 테스트 = DataFrame 한 번 받음
# 3. test_str_to_datetime_with_df 함수 (fixture 사용)
@pytest.fixture
def sample_datetime_string_df():
    data = {
        "datetime_string": [
            "2026-05-06T11:30:12.365233",
            "2024-05-01 10:30:10.000100",
            "2024-05-01 10:30",
            "2024/05/01 10:30",
        ],
        "expected": [
            datetime(2026, 5, 6, 11, 30, 12, 365233),
            datetime(2024, 5, 1, 10, 30, 10, 100),
            datetime(2024, 5, 1, 10, 30),
            None,  # ValueError 케이스는 None
        ],
        "should_raise": [False, False, False, True],
    }
    return pd.DataFrame(data)


def test_str_to_datetime_with_df(sample_datetime_string_df):
    """fixture로 받은 DataFrame을 행별로 순회하며 검증.

    슬래시 케이스('2024/05/01 10:30')는 ValueError를 발생시키므로 별도 처리.
    """
    for _, row in sample_datetime_string_df.iterrows():
        if row["should_raise"]:
            with pytest.raises(ValueError):
                str_to_datetime(row["datetime_string"])
        else:
            assert str_to_datetime(row["datetime_string"]) == row["expected"]
