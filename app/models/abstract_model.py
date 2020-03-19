from django.db import models
from .manager.abstract_manager import AbstractManager


class AbstractModel(models.Model):  # 全モデル共通の処理を実装する場合に、機能を実装するクラス
  created_at = models.DateTimeField(
      null=False, auto_now_add=True, verbose_name="作成日時")
  updated_at = models.DateTimeField(
      null=False, auto_now=True, verbose_name="更新日時")

  class Meta:
    abstract = True

  objects = AbstractManager()
