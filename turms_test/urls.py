from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
import os

urlpatterns = [
    re_path(r"^api/token/?$", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    re_path(r"^api/token/refresh/?$", TokenRefreshView.as_view(), name="token_refresh"),
]

urlpatterns += [
    re_path(r"^admin/", admin.site.urls),
    re_path(r"^api/user/", include("users.urls")),
]

if os.getenv("DJANGO_CONFIGURATION", "Dev") == "Dev":
    # serve static and media when develop
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # show api doc when develop
    urlpatterns += [
        re_path(r"^api/schema/?$", SpectacularAPIView.as_view(), name="schema"),
        re_path(r"^api/schema/swagger-ui/?$", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
        re_path(r"^api/schema/redoc/?$", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    ]
