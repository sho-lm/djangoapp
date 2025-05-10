from django.contrib import admin
from django.contrib.auth.models import Group

from .models import User

admin.site.register(User) # 管理画面で編集できるようにユーザーを登録
admin.site.unregister(Group) # Groupモデルは使わない
