# jaycode
[![PyPI version](https://img.shields.io/pypi/v/jaycode.svg)](https://pypi.org/project/jaycode/)
[![Downloads](https://img.shields.io/pypi/dm/jaycode.svg)](https://pypi.org/project/jaycode/)

`jaycode` 는 SSH, DB, File, Crawling 관련 작업을 쉽게 할 수 있는 파이썬 유틸리티 패키지입니다.  

---

## 📦 설치 (Installation)

```bash 
pip install jaycode
```

## 🚀 사용 예시 (Examples)
```
import jaycode

exam = jaycode.Init()
exam.SSH.connect(hostname=,username=,password=)
exam.DB.connect(user=,password=,database=)
exam.DB.insert(dict,'table_name')
```

## 🌲 구조도 (Tree 구조)

- jaycode
  - **ssh**
    - `connect()` ssh 연결함수
    - `get_file()` 연결된 서버에서 파일 가져오는 함수
  - **db**
    - `connect()` db 연결함수
    - `insert()`, `update()`, `delete()`, `query()` 등 CRUD 함수
  - **file**
    - `m4a_to_wav()` 파일 변환함수
  - **crawling**
      - `init()` 드라이버 초기화 함수
      - `open()` 페이지 오픈 함수
      - `quit()` 페이지 닫기 함수 