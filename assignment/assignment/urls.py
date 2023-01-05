from django.contrib import admin
from django.conf import settings
from django.urls import path, include, re_path
from dj_rest_auth.views import LoginView, LogoutView
from dj_rest_auth.registration.views import RegisterView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="페이히어 백엔드 개발자 과제 전형",
        default_version='v1',
        description="페이히어 Python 백엔드 개발자 과제전형 api 문서입니다",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="acepilot0620@naver.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 로그인/회원가입
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('signup/', RegisterView.as_view()),

    # 하위 앱
    path('', include('user.urls')),
    path('', include('ledger.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]