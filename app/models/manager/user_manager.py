from django.contrib.auth.models import BaseUserManager


# 下記の記事を参考（ほぼまるパクリ）
# https://qiita.com/okoppe8/items/10ae61808dc3056f9c8e
class UserManager(BaseUserManager):
  def create_user(self, email, password=None):
    """
    Creates and saves a User with the given email and password.
    """
    if not email:
      raise ValueError('Users must have an email address')

    user = self.model(
        email=self.normalize_email(email),
    )

    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self, email, password=None):
    """
    Creates and saves a superuser with the given email, date of
    birth and password.
    """
    user = self.create_user(
        email,
        password=password,
    )
    user.is_staff = True
    user.save(using=self._db)
    return user
