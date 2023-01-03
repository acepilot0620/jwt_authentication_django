from django.urls import path
from .views import LedgerViewSet

# Blog 목록 보여주기
ledger_list = LedgerViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

# Blog detail 보여주기 + 수정 + 삭제
ledger_detail = LedgerViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns =[
    path('', ledger_list),
    path('<int:pk>/', ledger_detail),
]