# 어떤 입력 포맷을 받아야 하나?
#     - "2026-05-06T11:30:12.365233"  (ISO 8601 표준)
#     - "2024-05-01 10:30:10.000100"  (ISO 변형: 공백 구분)
#     - "2024-05-01 10:30"             (ISO 변형: 초·micro 없음)
#     - "2024/05/01 10:30"             (거부 대상)

# ValueError를 발생시켜야 하는 경우는?
#     - 위 포맷에 안 맞는 입력
#     - 미래 시각 (오늘보다 이후)

# 어떻게 파싱?
#     - datetime.fromisoformat?
#     - datetime.strptime?
#     - 둘의 차이는?
#     - fixture의 입력들은 모두 ISO 8601 변형(- 구분, T 또는 공백, micro 포함/생략)이라 fromisoformat이 가장 자연스러움
#     - fromisoformat이 슬래시 케이스를 알아서 거부


# """_summary_

# Args:                              <= Google 스타일
#     date_string (str): ...

# Raises
# ------                             <= NumPy 스타일
# ValueError: ...
# """

"""문자열을 datetime/unixtime으로 변환하는 유틸리티"""

from datetime import datetime

import numpy as np


def str_to_datetime(date_string: str) -> datetime:
    """ISO 8601 문자열을 datetime 객체로 변환한다.

    Parameters
    ----------
    date_string : str
        ISO 8601 또는 그 변형 포맷 문자열.
        예: "2024-05-01T10:30:00", "2024-05-01 10:30:10.000100", "2024-05-01 10:30".

    Returns
    -------
    datetime
        변환된 datetime 객체.

    Raises
    ------
    ValueError
        지원하지 않는 포맷이거나 현재 시각보다 미래인 경우.

    Examples
    --------
    >>> str_to_datetime("2024-05-01T10:30:00")
    datetime.datetime(2024, 5, 1, 10, 30)
    """
    try:
        result = datetime.fromisoformat(date_string)
    except ValueError as e:
        raise ValueError(f"지원하지 않는 포맷: {date_string}") from e

    if result > datetime.now():
        raise ValueError(f"미래 시각은 허용되지 않음: {date_string}")

    return result


def str_to_unixtime(date_string: str) -> np.int64:
    """ISO 8601 문자열을 microseconds 단위 unix timestamp로 변환한다.

    내부적으로 str_to_datetime을 호출하여 검증 로직을 재사용한다.

    Parameters
    ----------
    date_string : str
        ISO 8601 또는 그 변형 포맷 문자열.

    Returns
    -------
    numpy.int64
        microseconds 단위 unix timestamp.

    Raises
    ------
    ValueError
        지원하지 않는 포맷이거나 현재 시각보다 미래인 경우.

    Examples
    --------
    >>> str_to_unixtime("2024-05-01 10:30")
    1714527000000000
    """
    # 재사용. 같은 검증 로직을 중복 작성하지 않음.
    dt = str_to_datetime(date_string)
    # microseconds 단위로 가려면 * 1_000_000을 해야 함.
    return np.int64(dt.timestamp() * 1_000_000)
