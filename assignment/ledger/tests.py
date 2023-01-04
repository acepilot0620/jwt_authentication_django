from rest_framework.test import APITestCase
from rest_framework.views import status
from django.urls import reverse

from core.factories import UserFactory, LedgerFactory
from .models import Ledger

class LedgerTestCase(APITestCase):
    def setUp(self):
        self.url = '/ledger/'
        self.user = UserFactory()
        # 로그인
        login_data = {
            "email": self.user.email,
            "password": "1q2w3e4r!",
        }
        login_response = self.client.post('/login/', data=login_data, format='json')
        self.access_token = login_response.data['access_token']
    
    # 가계부에 오늘 사용한 돈의 금액과 관련된 메모를 남길 수 있습니다. 
    def test_ledger_create(self):
        data = {
            'amount' : 10000,
            'place' : "카페",
            'memo' : "라떼랑 케익",
            'ledger_type' : "EXP"
        }
        response = self.client.post(self.url, HTTP_AUTHORIZATION=f'Bearer {self.access_token}', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # 가계부에서 수정을 원하는 내역은 금액과 메모를 수정 할 수 있습니다. 
    def test_ledger_edit(self):
        ledger = LedgerFactory(user=self.user)
        url = self.url +f'{ledger.id}/'
        data = {
            # 'amount' : 8000,
            # 'place' : "편의점",
            'memo' : "라면이랑 삼각김밥",
            # 'ledger_type' : "EXP"
        }
        response = self.client.put(url, HTTP_AUTHORIZATION=f'Bearer {self.access_token}', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # 가계부에서 삭제를 원하는 내역은 삭제 할 수 있습니다.
    def test_ledger_delete(self):
        ledger = LedgerFactory(user=self.user)
        url = self.url + f'{ledger.id}/'
        response = self.client.delete(url, HTTP_AUTHORIZATION=f'Bearer {self.access_token}', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Ledger.objects.filter(id=ledger.id).exists(), False)

    # 가계부에서 이제까지 기록한 가계부 리스트를 볼 수 있습니다. 
    def test_ledger_get(self):
        data = {}
        LedgerFactory.create_batch(size=10, user=self.user)
        response = self.client.get(self.url, HTTP_AUTHORIZATION=f'Bearer {self.access_token}', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    # # 가계부에서 상세한 세부 내역을 볼 수 있습니다. 
    def test_ledger_detail(self):
        ledger = LedgerFactory(user=self.user)
        url = self.url+f'{ledger.id}/'
        response = self.client.get(url, HTTP_AUTHORIZATION=f'Bearer {self.access_token}', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # 가계부의 세부 내역을 복제할 수 있습니다.
    def test_ledger_detail_duplicate(self):
        ledger = LedgerFactory(user=self.user)
        url = self.url + f'duplicate/{ledger.id}/'
        response = self.client.post(url, HTTP_AUTHORIZATION=f'Bearer {self.access_token}', format='json')
        copy_result = Ledger.objects.get(id=response.data['id'])
        self.assertEqual(ledger.user, copy_result.user)
        self.assertEqual(ledger.amount, copy_result.amount)
        self.assertEqual(ledger.place, copy_result.place)
        self.assertEqual(ledger.memo, copy_result.memo)
    
    # # 가계부의 특정 세부 내역을 공유할 수 있게 단축 URL을 만들 수 있습니다.
    def test_ledger_detail_share(self):
        ledger = LedgerFactory(user=self.user)
        # 단축된 공유 URL 생성
        generate_url = self.url + f'generate_url/{ledger.id}/'
        response = self.client.get(generate_url, HTTP_AUTHORIZATION=f'Bearer {self.access_token}', format='json')
        sharing_url = response.data['sharing_url']
        # 타 사용자 로그인
        new_user = UserFactory.create()
        login_data = {
            "email": new_user.email,
            "password": "1q2w3e4r!",
        }
        login_response = self.client.post('/login/', data=login_data, format='json')
        access_token = login_response.data['access_token']
        # 단축된 공유 URL로 가계부 특정 세부내역 확인
        redirection = self.client.get(sharing_url,HTTP_AUTHORIZATION=f'Bearer {access_token}', format='json')
        reverse(redirection)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


