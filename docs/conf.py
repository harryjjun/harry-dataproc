# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "dataproc"
copyright = "2026, Harry"
author = "Harry"
release = "0.0.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "autoapi.extension",
    "sphinxcontrib.mermaid",
    "sphinx_design",
    "myst_parser",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]

# -- Path setup --------------------------------------------------------------
# autoapi가 패키지 소스를 찾기 위해 경로 추가
import os
import sys

sys.path.insert(0, os.path.abspath("../src"))

# -- AutoAPI configuration ---------------------------------------------------
# sphinx-autoapi가 어디서 파이썬 소스를 읽을지 지정
autoapi_dirs = ["../src/dataproc"]

# 어떤 형식으로 표시할지
autoapi_options = [
    "members",  # 클래스·함수·모듈 멤버
    "undoc-members",  # docstring 없는 멤버도 표시
    "show-inheritance",  # 클래스 상속 관계 표시
    "show-module-summary",  # 모듈 요약 표시
    "imported-members",  # import한 멤버 표시
]

# docstring 스타일 (numpy로 작성했으므로)
autodoc_typehints = "description"  # type hint를 description에 포함
napoleon_numpy_docstring = True
napoleon_google_docstring = False

# -- HTML output -------------------------------------------------------------
# pydata-sphinx-theme 사용
html_theme = "pydata_sphinx_theme"

# 테마 옵션 (선택)
html_theme_options = {
    "show_toc_level": 2,
}

# -- 언어 설정 (한국어로 작성한 docstring과 일관) -------------------------
language = "ko"
