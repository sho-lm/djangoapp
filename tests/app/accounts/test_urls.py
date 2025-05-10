from django.test import TestCase
from django.urls import reverse, resolve
from app.accounts.views import *


class TestUrls(TestCase):
    """疎通確認用のテスト 不要になったら削除する"""
    def test_test_url(self):
        url = reverse('accounts:test') # 「urlsのapp名:viewsの関数名」の形式
        self.assertEqual(resolve(url).func, test)