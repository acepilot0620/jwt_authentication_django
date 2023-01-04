from rest_framework.test import APITestCase
from rest_framework.views import status

from common.factories import UserFactory

class UserSignUpTestCase(APITestCase):
    def setUp(self):
        self.url = '/signup'
        self.data = {
            "email": "example1@naver.com",
            "password1": "1q2w3e4r!",
            "password2": "1q2w3e4r!",
            }
    
    # 회원가입 성공
    def test_signup_success(self):
        response = self.client.post(self.url, data=self.data, format='json')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # 비밀번호가 다른 경우
    def test_signup_password_error(self):
        data = {
            "email": "example2@naver.com",
            "password1": "1q2w3e4r!",
            "password2": "1q2w3e4r",
            }
        response = self.client.post(self.url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    # 이미 가입한 사용자가 회원가입하려고 하는 경우
    def test_signup_duplicate_email(self):
        data = {
            "email": "example1@naver.com",
            "password1": "1q2w3e4r!",
            "password2": "1q2w3e4r!",
            }
        self.client.post(self.url, data=self.data, format='json')
        response = self.client.post(self.url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
class UserLoginTestCase(APITestCase):
    def setUp(self):
        self.url = '/login'
        self.user = UserFactory()
    
    # 로그인 성공
    def test_login_success(self):
        data = {
            "email": self.user.email,
            "password": "1q2w3e4r!",
        }
        response = self.client.post(self.url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    # e-mail이 등록되어있지 않음
    def test_login_email_not_registered(self):
        data = {
            "email": "example1@naver.com",
            "password": "1q2w3e4r!",
        }
        response = self.client.post(self.url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    # 비밀번호가 틀림
    def test_login_pw_error(self):
        data = {
            "email": self.user.email,
            "password": "wrong_password",
        }
        response = self.client.post(self.url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
class UserLogoutTestCase(APITestCase):
    def setUp(self):
        self.url = '/logout'
        self.user = UserFactory()
        # 로그인
        login_data = {
            "email": self.user.email,
            "password": "1q2w3e4r!",
        }
        login_response = self.client.post('/login', data=login_data, format='json')
        self.access_token = login_response.data['access_token']
        self.refresh_token = login_response.data['refresh_token']
    
    # 로그아웃 성공 테스트
    def test_logout_success(self):
        data = {"refresh":self.refresh_token}
        response = self.client.post(path=self.url, HTTP_AUTHORIZATION=f'Bearer {self.access_token}', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Refresh token이 없는 경우
    def test_logout_refresh_token_missing(self):
        response = self.client.post(path=self.url, HTTP_AUTHORIZATION=f'Bearer {self.access_token}', format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
