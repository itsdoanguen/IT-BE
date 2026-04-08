from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models


class NguoiDungManager(BaseUserManager):
	def create_user(self, email, password=None, vai_tro="ung_vien", **extra_fields):
		if not email:
			raise ValueError("Email is required")
		user = self.model(email=self.normalize_email(email), vai_tro=vai_tro, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, password, **extra_fields):
		extra_fields.setdefault("is_staff", True)
		extra_fields.setdefault("is_superuser", True)
		extra_fields.setdefault("is_active", True)
		return self.create_user(email=email, password=password, vai_tro="admin", **extra_fields)


class NguoiDung(AbstractBaseUser, PermissionsMixin):
	class VaiTro(models.TextChoices):
		UNG_VIEN = "ung_vien", "Ung vien"
		CONG_TY = "cong_ty", "Cong ty"
		ADMIN = "admin", "Admin"

	id = models.AutoField(primary_key=True)
	email = models.EmailField(max_length=255, unique=True)
	password = models.CharField(max_length=255, db_column="mat_khau")
	vai_tro = models.CharField(max_length=20, choices=VaiTro.choices)
	tao_luc = models.DateTimeField(auto_now_add=True)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)

	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = []

	objects = NguoiDungManager()

	class Meta:
		db_table = "NGUOI_DUNG"

	def __str__(self):
		return self.email
