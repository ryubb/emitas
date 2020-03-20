from django.db import models
from .abstract_model import AbstractModel
from .task_model import Task


class TaskTime(AbstractModel):

  class Meta:
    db_table = "task_time"
    verbose_name = "タスク時間"
    verbose_name_plural = "タスク時間"

  task = models.ForeignKey(Task, on_delete=models.CASCADE, null=False)
  start_time = models.DateTimeField(null=True)
  end_time = models.DateTimeField(null=True)
  total_time = models.DurationField(null=True)

  def __str__(self):
    return self.name
