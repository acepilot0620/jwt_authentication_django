from django.urls import path
from .views import LedgerViewSet

# 가계부 목록 보여주기
ledger_list = LedgerViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

# 가계부 상세 보여주기 + 수정 + 삭제
ledger_detail = LedgerViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

# 가계부 세부 내역 복제
ledger_duplicate = LedgerViewSet.as_view({
    'post' : 'duplicate',
})

urlpatterns =[
    path('', ledger_list),
    path('<int:pk>/', ledger_detail),
    path('duplicate/<int:pk>/',ledger_duplicate),
]