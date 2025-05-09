from django.urls import path
from app.accounts import views


app_name = 'accounts'
urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path("", views.IndexView.as_view(), name="index"),
    path('', views.test, name='test') # 疎通確認用
    
]
