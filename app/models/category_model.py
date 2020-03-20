from django.db import models
from .abstract_model import AbstractModel
from .user_model import User


class Category(AbstractModel):

  class Meta:
    db_table = "category"
    verbose_name = "カテゴリー"
    verbose_name_plural = "カテゴリー"

  name = models.CharField(max_length=100, null=False, verbose_name="カテゴリー名")
  description = models.CharField(max_length=1000, null=True, verbose_name="詳細")
  user = models.ForeignKey(User, on_delete=models.PROTECT,
                           null=False, verbose_name="ユーザー")

  def __str__(self):
    return self.name
