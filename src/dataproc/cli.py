"""dataproc CLI 진입점.

dataproc 패키지를 셸 명령어로 노출한다. setuptools entry point로 등록되어
``dataproc to-unixtime "..."`` 같은 형태로 호출 가능.
"""

import logging
import sys

import click

from .transform import str_to_datetime, str_to_unixtime

logger = logging.getLogger(__name__)


@click.group()
def cli():
    """dataproc: datetime 문자열 변환 CLI 도구."""
    logging.basicConfig(level=logging.INFO, stream=sys.stderr)


@cli.command(name="to-unixtime")
@click.argument("date_string")
def to_unixtime_cmd(date_string):
    # \b는 click의 특수 마커. 이 줄 이후의 텍스트는 click이 자동 wrap하지 않는다는 의미
    """문자열을 microseconds 단위 unix timestamp로 변환한다.

    \b
    DATE_STRING은 ISO 8601 또는 그 변형 포맷이어야 한다.
    사용 예시:
        dataproc to-unixtime "2024-05-01T10:30:00"
        dataproc to-unixtime "01/05/24 10:30:00"
    """
    logger.info(f"Converting {date_string!r} to unix timestamp")
    try:
        result = str_to_unixtime(date_string)
    except ValueError as e:
        raise click.ClickException(str(e))
    click.echo(result)


@cli.command(name="to-datetime")
@click.argument("date_string")
def to_datetime_cmd(date_string):
    """문자열을 datetime 객체로 변환한다.

    \b
    DATE_STRING은 ISO 8601 또는 그 변형 포맷이어야 한다.
    사용 예시:
        dataproc to-datetime "01/05/24 10:30:00"
        dataproc to-datetime "2024-05-01T10:30:00.123456"
    """
    logger.info(f"Converting {date_string!r} to ISO datetime")
    try:
        result = str_to_datetime(date_string)
    except ValueError as e:
        raise click.ClickException(str(e))
    click.echo(result)


if __name__ == "__main__":
    cli()
