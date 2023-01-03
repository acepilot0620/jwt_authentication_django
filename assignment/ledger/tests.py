from rest_framework.test import APITestCase
from rest_framework.views import status

from assignment.factories import UserFactory, LedgerFactory
from .models import Ledger

class LedgerTestCase(APITestCase):
    def setUp(self):
        self.url = '/ledger'
        self.user = UserFactory()
        self.ledger = LedgerFactory.create(user=self.user)
        # 로그인
        login_data = {
            "email": self.user.email,
            "password": "1q2w3e4r!",
        }
        login_response = self.client.post('/login', data=login_data, format='json')
        self.access_token = login_response.data['access_token']
    
    # 가계부에 오늘 사용한 돈의 금액과 관련된 메모를 남길 수 있습니다. 
    def test_ledger_create(self):
        url = self.url + '/create'
        data = {
            'earning' : 10000,
            'spending' : 0,
            'place' : "카페",
            'memo' : "라떼랑 케익",
        }
        response = self.client.post(url, HTTP_AUTHORIZATION=f'Bearer {self.access_token}', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # 가계부에서 수정을 원하는 내역은 금액과 메모를 수정 할 수 있습니다. 
    def test_ledger_edit(self):
        url = self.url + '/edit'
        data = {
            'earning' : 8000,
            'spending' : 0,
            'place' : "편의점",
            'memo' : "라면이랑 삼각김밥",
        }
        response = self.client.post(url, HTTP_AUTHORIZATION=f'Bearer {self.access_token}', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # 가계부에서 삭제를 원하는 내역은 삭제 할 수 있습니다.
    def test_ledger_delete(self):
        create_url = self.url + '/create'
        data = {
            'earning' : 10000,
            'spending' : 0,
            'place' : "카페",
            'memo' : "라떼랑 케익",
        }
        create_response = self.client.post(url, data=data, format='json')
        ledger_id = create_response.data['id']
        url = self.url + f'/delete/{ledger_id}'
        response = self.client.post(url, HTTP_AUTHORIZATION=f'Bearer {self.access_token}', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # 가계부에서 이제까지 기록한 가계부 리스트를 볼 수 있습니다. 
    def test_ledger_get(self):
        url = self.url + '/get'
        data = {}
        LedgerFactory.create_batch(10, user=self.user, ledger=self.ledger)
        response = self.client.get(url, HTTP_AUTHORIZATION=f'Bearer {self.access_token}', data=data, format='json')
        ledgers = response.data['ledgers']
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    # 가계부에서 상세한 세부 내역을 볼 수 있습니다. 
    def test_ledger_detail(self):
        ledger = LedgerFactory()
        url = self.url + f'/detail/{ledger.id}'
        response = self.client.get(url, HTTP_AUTHORIZATION=f'Bearer {self.access_token}', format='json')
        ledger_detail = response.data['detail']
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # 가계부의 세부 내역을 복제할 수 있습니다.
    def test_ledger_detail_copy(self):
        ledger = LedgerFactory()
        url = self.url + f'/copy/{ledger.id}'
        response = self.client.post(url, HTTP_AUTHORIZATION=f'Bearer {self.access_token}', format='json')
        copy_result = Ledger.objects.get(id=response.data['copied_ledger']['id'])
        self.assertEqual(ledger.user, copy_result.user)
        self.assertEqual(ledger.spending, copy_result.spending)
        self.assertEqual(ledger.earning, copy_result.earning)
        self.assertEqual(ledger.place, copy_result.place)
        self.assertEqual(ledger.memo, copy_result.memo)
    
    # 가계부의 특정 세부 내역을 공유할 수 있게 단축 URL을 만들 수 있습니다.
    def test_ledger_detail_share(self):
        ledger = LedgerFactory()
        url = self.url + f'/share/{ledger.id}'
        response = self.client.post(url, HTTP_AUTHORIZATION=f'Bearer {self.access_token}', format='json')
        sharing_url = response.data['sharing_url']
        sharing_response = self.client.get(sharing_url, format='json')
        print(sharing_response.data['ledger'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)


