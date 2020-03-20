from django.db import models
from .abstract_model import AbstractModel
from .user_model import User


class TaskStatus(AbstractModel):

  class Meta:
    db_table = "task_status"
    verbose_name = "タスクステータス"
    verbose_name_plural = "タスクステータス"

  name = models.CharField(max_length=100, null=False, verbose_name="ステータス名")
  description = models.CharField(max_length=1000, null=True, verbose_name="詳細")
  user = models.ForeignKey(User, on_delete=models.PROTECT,
                           null=False, verbose_name="ユーザー")

  def __str__(self):
    return self.name
