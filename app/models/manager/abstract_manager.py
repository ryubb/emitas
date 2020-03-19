from django.db import models


# 全モデルマネジャーに適用できるルールを、このクラスに適用する
# モデルマネジャーを継承する時、必ずこのクラスを継承する
class AbstractManager(models.Manager):
    def get_queryset(self):
        return super(AbstractManager, self).get_queryset()
