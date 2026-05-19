FROM python:3.12-slim

WORKDIR /app

ENV SETUPTOOLS_SCM_PRETEND_VERSION=0.2.1

COPY pyproject.toml ./       
COPY README.md ./            
COPY src/ ./src/     

RUN pip install --no-cache-dir .

ENTRYPOINT ["dataproc"]
CMD ["--help"]
