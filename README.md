# github-readme-crawler

## 목차

- [1. flask에 띄우기](#1-flask에-띄우기)
- [2. CSV 파일로 다운로드 하기](#2-csv-파일로-다운로드-하기)
- [3. CSV 파일을 읽고 DB에 업로드하기](#3-csv-파일을-읽고-db에-업로드하기)

## 1. flask에 띄우기 

- 신프디아 3기 수강생 분들의 깃허브 페이지에서 인스타그램, 블로그, 링크드인 주소 등을 추출해 flask 페이지에 띄우기

### 실행 방법

1. 사용하는 IDE에 맞게 가상환경을 설정해줍니다!
  - [pycharm 참고](https://uiandwe.tistory.com/1215)

2. 아래 명령어로 터미널에서 필요한 패키지를 다운로드합니다.
```bash
pip freeze > requirements.txt
```
3. app.py 파일의 `run_flask()` 메서드를 실행합니다.

### 결과물

- `http://127.0.0.1:5000/`
  <img width="1440" alt="스크린샷 2024-01-05 오후 1 56 28" src="https://github.com/youhyeoneee/youhyeoneee/assets/37354574/82096c2d-6927-4fa0-ad1e-5776121e74ce">


- `http://127.0.0.1:5000/user/<깃허브 아이디>` ex. `user/youhyeoneee`
  
  <img width="523" alt="image" src="https://github.com/youhyeoneee/youhyeoneee/assets/37354574/80e2ebc5-486a-4471-bc14-949f4837b412">

## 2. CSV 파일로 다운로드 하기

- 신프디아 3기 수강생 분들의 깃허브 페이지에서 인스타그램, 블로그, 링크드인 주소 등을 추출해 csv 파일로 다운로드 하기

### 실행 방법

1. app.py 파일의 `run_csv()` 메서드를 실행합니다.

### 결과물

<img width="459" alt="스크린샷 2024-01-08 오후 2 46 12" src="https://github.com/youhyeoneee/github-readme-crawler/assets/37354574/7caeb35f-896c-4d84-8ecb-4d7a4171794d">


## 3. CSV 파일을 읽고 DB에 업로드하기 

- 다운로드 한 csv 파일을 DB에 업로드하기

### 실행 방법

1. upload_db.py 파일의 `#RDS info` 부분을 설정해줍니다.
   ```python
   host = "@@@@.ap-northeast-2.rds.amazonaws.com" # RDS 엔드포인트
   port = 3306
   username = "admin" # 설정하신 호스트 네임
   database = "test" # 만드신 데이터베이스 이름
   password = "pw" # 설정하신 비밀번호
   table_name = "USER" # 만드신 테이블 이름
   ```
2. upload_db.py 파일을 실행합니다.

### 결과물

<img width="957" alt="image" src="https://github.com/youhyeoneee/github-readme-crawler/assets/37354574/56cfdc4e-bb7b-4537-ac41-4c59ef5570a0">


