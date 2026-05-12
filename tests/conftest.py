"""pytest 설정. src 디렉토리를 sys.path에 추가."""

import sys
from pathlib import Path

# tests/conftest.py 기준 ../src
src_path = Path(__file__).parent.parent / "src"
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))
