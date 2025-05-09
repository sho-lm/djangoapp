from django.contrib import admin
from django.contrib.auth.models import Group

from .models import User

admin.site.register(User) # 管理画面用にユーザーを登録
admin.site.unregister(Group) # Groupモデルは使わない
