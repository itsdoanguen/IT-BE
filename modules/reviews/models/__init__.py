from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class DanhGia(models.Model):
	danh_gia_id = models.AutoField(primary_key=True)
	ung_tuyen = models.ForeignKey(
		"applications.UngTuyen",
		on_delete=models.CASCADE,
		db_column="ung_tuyen_id",
		related_name="danh_gia",
	)
	nguoi_danh_gia = models.ForeignKey(
		"accounts.NguoiDung",
		on_delete=models.CASCADE,
		db_column="nguoi_danh_gia_id",
		related_name="danh_gia_da_viet",
	)
	nguoi_nhan_danh_gia = models.ForeignKey(
		"accounts.NguoiDung",
		on_delete=models.CASCADE,
		db_column="nguoi_nhan_danh_gia_id",
		related_name="danh_gia_da_nhan",
	)
	diem_so = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
	nhan_xet = models.TextField(null=True, blank=True)
	tao_luc = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = "DANH_GIA"
