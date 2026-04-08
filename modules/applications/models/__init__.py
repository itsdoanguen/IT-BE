from django.db import models


class UngTuyen(models.Model):
	class TrangThai(models.TextChoices):
		CHO_DUYET = "cho_duyet", "Cho duyet"
		CHAP_NHAN = "chap_nhan", "Chap nhan"
		TU_CHOI = "tu_choi", "Tu choi"
		HOAN_THANH = "hoan_thanh", "Hoan thanh"

	ung_tuyen_id = models.AutoField(primary_key=True)
	tin = models.ForeignKey(
		"jobs.TinTuyenDung",
		on_delete=models.CASCADE,
		db_column="tin_id",
		related_name="ung_tuyen",
	)
	ung_vien = models.ForeignKey(
		"profiles.HoSoUngVien",
		on_delete=models.CASCADE,
		db_column="ung_vien_id",
		related_name="ung_tuyen",
	)
	trang_thai = models.CharField(max_length=20, choices=TrangThai.choices, default=TrangThai.CHO_DUYET)
	thoi_gian_ung_tuyen = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = "UNG_TUYEN"
