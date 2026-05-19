"""dataproc CLI 테스트.

cli.py는 다음 STEP 3에서 구현 예정 (TDD 의도)
이 시점에는 모든 테스트가 실패해야 정상 (RED)
"""

from click.testing import CliRunner

from dataproc.cli import cli


def test_cli_help_works():
    """--help 호출 시 정상 출력하고 exit code 0."""
    runner = CliRunner()
    result = runner.invoke(cli, ["--help"])

    assert result.exit_code == 0
    assert "Usage:" in result.output


def test_cli_to_unixtime_valid():
    """유효한 문자열 => unix timestamp 출력 (숫자)."""
    runner = CliRunner()
    result = runner.invoke(cli, ["to-unixtime", "2024-05-01 10:30"])

    assert result.exit_code == 0
    # 출력은 microseconds 단위 정수
    assert result.output.strip().isdigit()


def test_cli_to_datetime_valid():
    """유효한 문자열 => datetime 출력."""
    runner = CliRunner()
    result = runner.invoke(cli, ["to-datetime", "2024-05-01T10:30:00"])

    assert result.exit_code == 0
    # datetime의 문자열 표현 포함
    assert "2024-05-01" in result.output


def test_cli_to_unixtime_invalid():
    """잘못된 포맷 => exit code != 0."""
    runner = CliRunner()
    result = runner.invoke(cli, ["to-unixtime", "2024/05/01 10:30"])

    assert result.exit_code != 0


def test_cli_to_datetime_invalid():
    """잘못된 포맷 => exit code != 0."""
    runner = CliRunner()
    result = runner.invoke(cli, ["to-datetime", "2024/05/01 10:30"])

    assert result.exit_code != 0
