from django.urls import path
from app.accounts import views


app_name = 'accounts'
urlpatterns = [
    path('', views.test, name='test') # 疎通確認用
]
