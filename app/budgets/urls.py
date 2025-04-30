from django.urls import path
from app.budgets import views


app_name = 'budgets'
urlpatterns = [
    path('', views.top, name='top'),
]