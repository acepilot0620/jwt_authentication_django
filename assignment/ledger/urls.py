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

# 가계부 세부내역 공유
ledger_share = LedgerViewSet.as_view({
    'get' : 'share',
})

# 가계부 세부 내역 공유 url 생성
ledger_generate_url = LedgerViewSet.as_view({
    'get' : 'generate_url',
})

# 단축 URL 리다이렉트
ledger_redirect_hash = LedgerViewSet.as_view({
    'get' : 'redirect_hash',
})

urlpatterns =[
    path('ledger/', ledger_list),
    path('ledger/<int:pk>/', ledger_detail),
    path('ledger/duplicate/<int:pk>/',ledger_duplicate),
    path('ledger/generate_url/<int:pk>/',ledger_generate_url),
    path('ledger/share/<int:pk>/', ledger_share),
    path('<str:url_hash>',ledger_redirect_hash),
]