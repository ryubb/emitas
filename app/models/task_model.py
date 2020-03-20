from django.db import models
from .abstract_model import AbstractModel
from .user_model import User
from .task_status_model import TaskStatus
from .category_model import Category
from .sub_category_model import SubCategory


class Task(AbstractModel):

  class Meta:
    db_table = "task"
    verbose_name = "タスク"
    verbose_name_plural = "タスク"

  name = models.CharField(max_length=100, null=False, verbose_name="タスク名")
  description = models.CharField(max_length=1000, null=True, verbose_name="詳細")
  user = models.ForeignKey(User, on_delete=models.PROTECT,
                           null=False, verbose_name="ユーザー")
  status = models.ForeignKey(TaskStatus, on_delete=models.CASCADE,
                             null=True, verbose_name="ステータス")
  category = models.ForeignKey(Category, on_delete=models.CASCADE,
                               null=True, verbose_name="カテゴリー")
  sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE,
                                   null=True, verbose_name="サブカテゴリー")


def __str__(self):
  return self.name
