# dataproc

데이터 처리에 자주 쓰이는 변환 유틸리티 함수를 제공하는 학습용 파이썬 라이브러리.

데이터 분석 스터디 Chapter 3 학습 과정에서 만드는 패키지.

---

## 설치

### 사용자용

```bash
pip install dataproc
```

### 개발자용

```bash
git clone https://github.com/harryjjun/harry-dataproc
cd harry-dataproc
pipenv install --dev
pipenv install -e .
```

---

## 빌드와 배포

이 패키지의 wheel을 빌드하려면:

```bash
pipenv install build --dev   # 처음 한 번만
python -m build
```

빌드 결과는 `dist/` 디렉토리에 생성된다.

- `dataproc-X.Y.Z-py3-none-any.whl` — 빌드된 배포물 (wheel)
- `dataproc-X.Y.Z.tar.gz` — 소스 배포물 (sdist)

빌드된 wheel을 다른 환경에서 설치하려면:

```bash
pip install path/to/dataproc-0.1.2-py3-none-any.whl
```


---

## 사용 예시

문자열을 datetime 객체로 변환:

```python
from dataproc import str_to_datetime

dt = str_to_datetime("2024-05-01T10:30:00")
# datetime.datetime(2024, 5, 1, 10, 30)
# print 호출시 : 2024-05-01 10:30:00

dt = str_to_datetime("2024-05-01 10:30")  # 공백 구분도 지원
```

문자열을 microseconds 단위 unix timestamp로 변환:

```python
from dataproc import str_to_unixtime

ts = str_to_unixtime("2024-05-01 10:30")
# 1714527000000000
```

지원하는 입력 포맷:
- `2024-05-01T10:30:00.000100` (T 구분, microseconds 포함)
- `2024-05-01 10:30:10` (공백 구분, 초까지)
- `2024-05-01 10:30` (공백 구분, 초 생략)

ISO 8601 포맷이 아닌 입력은 `ValueError`를 발생시킨다.

---

## 사용 예시 (CLI)

설치 후 `dataproc` 명령으로 셸에서 직접 사용:

```bash
# 문자열 => unix microseconds
$ dataproc to-unixtime "2024-05-01 10:30"
1714527000000000

# 문자열 => datetime
$ dataproc to-datetime "2024-05-01T10:30:00"
2024-05-01 10:30:00

# 도움말
$ dataproc --help
```

---

## 프로젝트 구조
```
dataproc/
├── src/dataproc/        # 라이브러리 소스 코드
│   ├── __init__.py      # public API 노출
│   ├── transform.py     # datetime/unixtime 변환 함수
│   └── io.py            # (예약)
├── tests/               # 유닛 테스트
├── docs/                # sphinx 프로젝트 문서
├── dist/                # 빌드 산출물 (wheel + sdist, gitignore)
├── pyproject.toml       # 패키지 메타 + 빌드 설정
├── Pipfile              # 개발 환경 의존성
├── Pipfile.lock         # 정확한 버전 잠금
└── README.md
```

---

## 개발 노트

### 의존성 관리

이 패키지의 의존성은 두 곳에서 관리된다.

**`pyproject.toml`의 `dependencies`** — 어떤 범위의 패키지가 호환되는지 명시한다. 예: `pandas>=2.0,<3.0`, `numpy>=2.0,<3.0`. 이것은 사용자가 본인 환경에 본인 버전의 pandas와 함께 dataproc을 설치할 때, 어디까지 호환을 보장할지 약속하는 부분이다. MAJOR 단위로 호환을 보장한다.

**`Pipfile.lock`** — 현재 개발 환경에 정확히 어떤 버전이 깔려 있는지 비트 단위로 기록한 스냅샷이다. 예: `pandas==2.3.3`. 이것은 개발팀 내에서 동일한 환경을 재현하기 위한 정보다. 라이브러리를 배포할 때는 이 lock 파일은 사용자에게 영향을 주지 않는다 (라이브러리 사용자는 `pyproject.toml`의 범위 안에서 자기 환경의 pandas 버전을 자유롭게 사용).

### 버전 정책

이 패키지는 [Semantic Versioning](https://semver.org/) 을 따른다. 
버전 번호는 `MAJOR.MINOR.PATCH` 형식이며 각 자리의 의미는 다음과 같다.

- **MAJOR**: 하위 호환이 깨지는 변경. 사용자가 코드 수정 없이 업그레이드할 수 없는 변경.
- **MINOR**: 하위 호환을 유지하는 기능 추가. 새 함수나 옵션 추가.
- **PATCH**: 하위 호환을 유지하는 버그 수정.

`v0.x.x`는 안정 버전 전임을 나타내며, API가 변경될 수 있다. 
`v1.0.0`부터 다음 MAJOR 업데이트까지 하위 호환을 약속한다.

버전은 git tag로 관리되며, `setuptools-scm`이 git tag로부터 자동으로 
패키지 버전을 추출한다. 즉 `git tag v0.1.0` 한 줄로 패키지 버전이 `0.1.0`이 된다.
