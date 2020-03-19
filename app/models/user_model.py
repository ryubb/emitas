from django.utils import timezone

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .abstract_model import AbstractModel
from .manager.user_manager import UserManager


class User(AbstractBaseUser, AbstractModel):

  class Meta:
    db_table = "user"
    verbose_name = "ユーザー"
    verbose_name_plural = "ユーザー"

  is_active = models.BooleanField(default=True, verbose_name="アクティブフラグ")
  is_staff = models.BooleanField(default=True, verbose_name="システム管理者フラグ")

  email = models.EmailField(
      null=False, max_length=255, unique=True, verbose_name="メールアドレス")
  name = models.CharField(null=True, max_length=100, verbose_name="名前")
  name_kana = models.CharField(null=True, max_length=200, verbose_name="ナマエ")

  is_delete = models.BooleanField(
      null=False, default=False, verbose_name="削除フラグ")
  deleted_at = models.DateTimeField(null=True, verbose_name="削除日時")

  objects = UserManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []

  def __str__(self):
    return self.name

  # これが何をしているか分からんが、これがないと管理画面でログインができなくなる
  def has_perm(self, perm, obj=None):
    "Does the user have a specific permission?"
    # Simplest possible answer: Yes, always
    return True

  # これが何をしているか分からんが、これがないと管理画面でログインができなくなる
  def has_module_perms(self, app_label):
    "Does the user have permissions to view the app `app_label`?"
    # Simplest possible answer: Yes, always
    return True

  # 論理削除に対応 Manager -> QuerySetクラスに移譲すべきか？
  def delete(self):
    self.is_delete = True
    self.deleted_at = timezone.now
    self.save()
