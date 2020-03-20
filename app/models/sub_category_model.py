from django.db import models
from .abstract_model import AbstractModel
from .user_model import User
from .category_model import Category


class SubCategory(AbstractModel):

  class Meta:
    db_table = "sub_category"
    verbose_name = "サブカテゴリー"
    verbose_name_plural = "サブカテゴリー"

  name = models.CharField(max_length=100, null=False, verbose_name="サブカテゴリー名")
  description = models.CharField(max_length=1000, null=True, verbose_name="詳細")
  user = models.ForeignKey(User, on_delete=models.PROTECT,
                           null=False, verbose_name="ユーザー")
  category = models.ForeignKey(Category, on_delete=models.CASCADE,
                               null=False, verbose_name="カテゴリー")

  def __str__(self):
    return self.name
