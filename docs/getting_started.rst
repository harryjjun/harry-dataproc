Getting Started
===============

dataproc은 데이터 처리에 자주 쓰이는 변환 유틸리티 함수를 제공하는 학습용 파이썬 라이브러리다.

설치
----

개발자용 설치:

.. code-block:: bash

   git clone https://github.com/harryjjun/harry-dataproc
   cd harry-dataproc
   pipenv install --dev
   pipenv install -e .


기본 사용법
-----------

문자열을 datetime 객체로 변환:

.. code-block:: python

   from dataproc.transform import str_to_datetime

   dt = str_to_datetime("2024-05-01T10:30:00")
   print(dt)
   # 2024-05-01 10:30:00

   dt = str_to_datetime("2024-05-01 10:30")
   print(dt)
   # 2024-05-01 10:30:00


문자열을 microseconds 단위 unix timestamp로 변환:

.. code-block:: python

   from dataproc.transform import str_to_unixtime

   ts = str_to_unixtime("2024-05-01 10:30")
   print(ts)
   # 1714527000000000


지원하는 입력 포맷
------------------

ISO 8601 표준과 그 변형들을 지원한다:

* ``2024-05-01T10:30:00.000100`` (T 구분, microseconds 포함)
* ``2024-05-01 10:30:10`` (공백 구분, 초까지)
* ``2024-05-01 10:30`` (공백 구분, 초 생략)


에러 처리
---------

ISO 8601 포맷이 아닌 입력은 ``ValueError`` 를 발생시킨다:

.. code-block:: python

   from dataproc.transform import str_to_datetime

   try:
       str_to_datetime("2024/05/01 10:30")
   except ValueError as e:
       print(f"포맷 오류: {e}")


또한 현재 시각보다 미래인 입력도 ``ValueError`` 를 발생시킨다:

.. code-block:: python

   try:
       str_to_datetime("2099-12-31T23:59:59")
   except ValueError as e:
       print(f"미래 시각: {e}")


다음 단계
---------

각 함수의 자세한 명세는 :doc:`API Reference <autoapi/index>` 에서 확인할 수 있다.
