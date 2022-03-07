from rest_framework import routers

from accounts_app.api.views.account import UserCreateView, UserDetailView

api_router = routers.DefaultRouter()

api_router.register('create', UserCreateView)
api_router.register('users', UserDetailView)