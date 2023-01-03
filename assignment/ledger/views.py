
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import status
from rest_framework.decorators import action

from .models import Ledger
from .serializers import LedgerSerializer, LedgerReadOnlySerializer, LedgerEditSerializer

class LedgerViewSet(viewsets.ModelViewSet):
    queryset = Ledger.objects.all()
    serializer_class = LedgerSerializer
    
    def get_queryset(self):
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
    
    # @action(methods=['GET'], detail=True)
    # def share(self, request, *args, **kwargs):
    #     url = ''
    #     return Response(url)
