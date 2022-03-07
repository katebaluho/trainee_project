from django.contrib import admin
from django.urls import path, include
from accounts_app.api.router import api_router as account_router

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from accounts_app.api.views.auth_token import CustomAuthToken

urlpatterns = [
    path('api-token-auth/', CustomAuthToken.as_view(), name='api-token-auth'),
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
    path('accounts/', include(account_router.urls)),
]
