# github-readme-crawler

## 목표

- 신프디아 3기 수강생 분들의 깃허브 페이지에서 인스타그램, 블로그, 링크드인 주소 등을 추출해 flask 페이지에 띄우기

## 실행 Tip

1. 사용하는 IDE에 맞게 가상환경을 설정해줍니다!
  - [pycharm 참고](https://uiandwe.tistory.com/1215)

2. 아래 명령어로 터미널에서 필요한 패키지를 다운로드합니다.
```bash
pip freeze > requirements.txt
```
3. app.py 파일을 실행합니다.

## 결과물

- `http://127.0.0.1:5000/`
  <img width="1440" alt="스크린샷 2024-01-05 오후 1 56 28" src="https://github.com/youhyeoneee/youhyeoneee/assets/37354574/82096c2d-6927-4fa0-ad1e-5776121e74ce">


- `http://127.0.0.1:5000/user/<깃허브 아이디>` ex. `user/youhyeoneee`
  
  <img width="523" alt="image" src="https://github.com/youhyeoneee/youhyeoneee/assets/37354574/80e2ebc5-486a-4471-bc14-949f4837b412">
