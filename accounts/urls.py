from django.db import router
from django.urls import path, include
from accounts import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('actions', views.ActionViewSet)
router.register('accounts', views.AccountViewSet)

app_name = 'accounts'

urlpatterns = [
    path('', include(router.urls)),
]
