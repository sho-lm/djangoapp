from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def _create_user(self, account_id, password, **extra_fields):
        user = self.model(account_id=account_id, **extra_fields)
        user.set_password(password) # パスワードはこの関数で設定する
        user.save()

        return user

    def create_user(self, account_id, password=None, **extra_fields):
        return self._create_user(
            account_id=account_id,
            password=password,
            **extra_fields,
        )

    def create_superuser(self, account_id, password, **extra_fields):
        extra_fields['is_superuser'] = True
        return self._create_user(
            account_id=account_id,
            password=password,
            **extra_fields,
        )
    
class User(AbstractBaseUser):
    
    account_id = models.CharField(
        verbose_name='アカウントID',
        unique=True,
        max_length=10
    )
    is_superuser = models.BooleanField(
        verbose_name='スーパーユーザー',
        default=False
    )
    
    objects = UserManager() # User.objects.all()などの時に使用するORM(Object-RelationMapping)の設定
    
    USERNAME_FIELD = 'account_id' # ログイン時、ユーザー名の代わりにaccount_idを使用する
    
    def __str__(self):
        return self.account_id # インスタンス出力時の文字列、管理画面で表示するときの名前になる
