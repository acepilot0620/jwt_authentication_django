
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import status
from rest_framework.decorators import action
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny,IsAuthenticatedOrReadOnly
from django.conf import settings
from django.shortcuts import redirect

from . import utils
from .models import Ledger
from .serializers import LedgerSerializer, LedgerReadOnlySerializer, LedgerEditSerializer
from common.pagination import LedgerPageNumberPagination

class LedgerViewSet(viewsets.ModelViewSet):
    queryset = Ledger.objects.all()
    serializer_class = LedgerSerializer
    permission_classes_per_method = {
        "share" : [AllowAny],
    }
    pagination_class = LedgerPageNumberPagination
    
    def get_queryset(self):
        if self.action == 'share':
            queryset = self.queryset
        else:
            queryset = self.queryset.filter(user = self.request.user)
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            # 가계부 목록 리스트를 볼 때는 수입, 지출, 메모 3가지만 간략화
            return LedgerReadOnlySerializer
        elif self.action == 'update':
            return LedgerEditSerializer
        else:
            return self.serializer_class

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        response_data = {'ledgers': serializer.data}
        return Response(response_data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        ledger_id = instance.id
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT, data={"msg":f'사용자 {request.user.email}님의 ledger(id={ledger_id}) 삭제'})
    
    @action(methods=['POST'], detail=True)
    def duplicate(self, request, *args, **kwargs):
        target_ledger = self.get_object()
        target_ledger.pk = target_ledger.id = None
        target_ledger.save()
        return Response(self.serializer_class(target_ledger).data)
    
    @action(methods=['GET'], detail=True)
    def generate_url(self, request, *args, **kwargs):
        target_ledger = self.get_object()
        original_link = settings.SITE_URL + f'/ledger/share/{target_ledger.id}/'
        hash = utils.url_shortener(original_link)
        sharing_url = settings.SITE_URL + f'/{hash}'
        data = {'sharing_url' : sharing_url}
        return Response(data=data)

    @action(methods=['GET'], detail=True)
    def share(self, request, *args, **kwargs):
        target_ledger = self.get_object()
        data = {
            "ledger": {
                "created" : target_ledger.created,
                "amount" : target_ledger.amount,
                "place" : target_ledger.place,
                "memo" : target_ledger.memo,
                "ledger_type" : target_ledger.ledger_type,
                }
        }
        return Response(data=data)

    @action(methods=['GET'], detail=True)
    def redirect_hash(self, request, url_hash):
        original_url = utils.load_url(url_hash=url_hash).original_url
        validity = utils.load_url(url_hash=url_hash).validity
        if utils.validity_check(validity):
            return redirect(original_url)
        else:
            return Response({"msg":"만료된 URL 입니다"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)