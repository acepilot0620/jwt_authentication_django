 ## [페이히어] Python 백엔드 엔지니어 과제 전형

> **과제 전형 안내 링크 : https://payhere.notion.site/Python-6901edc926cf4df2b28319e30fdc5af1 **

## 사용 프레임워크 및 DB

<br>
<div align="center">
<img src="https://img.shields.io/badge/Python-blue?style=plastic&logo=Python&logoColor=white"/>
<img src="https://img.shields.io/badge/Django-092E20?style=plastic&logo=Django&logoColor=white"/>
<img src="https://img.shields.io/badge/Django Rest Framework-EE350F?style=plastic&logo=Django&logoColor=white"/>
<img src="https://img.shields.io/badge/MySQL-00979D?style=plastic&logo=MySQL&logoColor=white"/>
</div>

> **Development**
- #### 구현기능
  - 사용자 관리:
    - 회원가입
      ```
      > 사용자 회원가입 기능입니다.
      
      * dj-rest-auth 라이브러리를 활용했습니다.
      * 이메일, 패스워드는 필수 입력값입니다.
      * 이메일은 중복이 허용되지 않습니다.
      * 패스워드는 암호화 후 DB에 저장됩니다.
      ```
    - 로그인
      ```
      > 사용자 로그인 기능입니다.
      
      * dj-rest-auth 라이브러리를 활용했습니다.
      * DRF-SimpleJwt 라이브리러를 활용했습니다.
      * 이메일, 패스워드는 필수 입력값입니다.
      * 모든 유효성 검사에 통과하면 액세스토큰과 리프레시 토큰을 발급합니다.
      ```
    - 로그아웃
      ```
      > 사용자 로그아웃 기능입니다.
      
      * DRF-SimpleJwt 라이브리러를 활용했습니다.
      * 리프레시 토큰은 필수 입력값입니다.
      * 토큰의 타입이 유효한지 확인합니다.(리프레시 토큰만 허용)
      * 토큰의 기한이 만료되었는지 확인합니다.
      * 토큰의 유저정보와 API 요청자의 유저정보가 일치하는지 확인합니다.
      * 모든 유효성 검사에 통과하면, 요청받은 리프레시 토큰을 토큰 블랙리스트에 등록합니다.(사용 제한)
      * 또한, 기존에 발급받은 모든 리프레시 토큰도 함께 토큰 블랙리스트에 등록합니다.
      ```
  - 가계부:

    - 가계부 내역 생성
      ```
      > 로그인한 사용자는 가계부 내역을 생성
      
      - 가계부 내역 생성:
        * 금액, 사용처, 메모, 지출or수입 여부를 입력하여 생성할 수 있습니다.
      ```
    - 가계부 내역 조회
      ```
      - 가계부 내역 조회:
        * 본인의 가계부 내역만 조회 할 수 있습니다.
        * 가계부 목록 보다 더 자세한 내용(금액, 사용처, 메모, 지출or수입 여부)을 확인 할 수 있습니다.
      ```
    - 가계부 내역 목록
      ```
      > 로그인한 사용자는 본인 가계부의 리스트 정보를 조회할 수 있습니다.
      
      * 가계부 내역의 간략한 내용(금액, 메모, 지출or수입 여부)들로 이루어진 리스트
      * 페이지네이션 기능(한페이지에 15개씩 확인 가능)
      ```
    - 가계부 내역 수정
      ```
      - 가계부 수정:
        * 본인의 가계부만 수정 가능합니다.
        * 가계부의 모든 내용을 수정할 수 있습니다.
        * 가계부의 내용을 부분적으로 수정할 수 있습니다.
      ```
    - 가계부 내역 삭제
      ```
      - 가계부 삭제:
        * 본인의 가계부 내역만 삭제 가능합니다.
        * 이미 삭제된 가계부는 다시 삭제할 수 없습니다.
      ```
    - 가계부 내역 복제
      ```
      - 가계부 복제:
        * 본인의 가계부 내역만 복제 할 수 있습니다.
        * 선택한 가계부 내역과 같은 내용의 가계부 내역을 생성 합니다.
      ```
    - 가계부 내역 공유
      ```
       - 가계부 공유:
        * 본인의 가계부 내역만 공유 할 수 있습니다.
        * 공유를 위한 단축된 URL을 통해서 특정 가계부 내역에 대한 정보를 공유할 수 있습니다.
        * 공유 링크의 만료 시간은 30분입니다.
      ```
 
> **Modeling**
- #### 🚀 ERD 구조
  ![image](https://user-images.githubusercontent.com/49195475/210644127-7455c7bd-ae05-4e2a-a67f-911c80f65950.png)

<br> 

> **API Docs**
- #### 🌈 API Document

Postman API document url : https://documenter.getpostman.com/view/14871537/2s8Z72WC4d
  

## Etc

> **Guides**
- #### ⚙️ 프로젝트 설치방법
  
  1. 해당 프로젝트를 clone하고, 프로젝트 폴더로 이동합니다.
  <br>
  
  ```
  git clone https://github.com/acepilot0620/pay_here_assignment
  cd project directory
  ```
  
  2. 가상환경을 만들고, 프로젝트에 필요한 python package를 다운받습니다.
  <br>
  
  ```
  python -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  ```
  
  3. DB의 스키마(schema)를 최신 modeling에 맞게 동기화합니다.
  <br>
  
  ```
  python manage.py migrate
  ```
  
  4. 개발용 서버를 실행합니다.
  <br>
  
  ```
  python manage.py runserver
  ```
- #### ⚙️ API 테스트 방법
  1. Django app 별 test 파일 활용
  ```
  python manage.py test user
  python manage.py test ledger
  ```
  2. Postman 활용 ( 워크스페이스 링크 : https://www.postman.com/gold-capsule-784502/workspace/0234404f-dc75-40ed-a3f5-297d5328afca/collection/14871537-d2877f62-55f5-4850-be71-d26e788626e1?action=share&creator=14871537)
    * 회원가입, 로그인 후 response에 있는 access token을 모든 api Bearer token값으로 넣고 테스트를 진행해 주세요

## 코드에 대한 생각

  * 정확한 기획 의도를 이해하기 전에는 자의적으로 판단하기보다 기능 Description에 근거하여 개발하였습니다.
  * 만약 실제로 같이 일하는 상황이였다면 기획 의도를 확실하게 파악한 후 적절하게 확장성있는 개발을 했을 것입니다.
  * 테스트 코드(각 앱별 test.py)에 각 요구사항들을 주석으로 표기해 놓았습니다.

 

