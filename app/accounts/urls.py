from django.urls import path, include
from app.accounts import views
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, LoginViewSet

router = DefaultRouter()
urlpatterns = router.urls



router = DefaultRouter()
router.register(r'admin', LoginViewSet, basename='admin')
router.register(r'users', UserViewSet, basename='users')

app_name = 'accounts'
urlpatterns = [
    path(r'', include(router.urls)),
]
