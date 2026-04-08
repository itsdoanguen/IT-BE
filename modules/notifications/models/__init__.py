from django.db import models


class ThongBao(models.Model):
	class LoaiThongBao(models.TextChoices):
		TIN_MOI = "tin_moi", "Tin moi"
		MATCH_THANH_CONG = "match_thanh_cong", "Match thanh cong"
		TIN_NHAN_MOI = "tin_nhan_moi", "Tin nhan moi"

	thong_bao_id = models.AutoField(primary_key=True)
	user = models.ForeignKey(
		"accounts.NguoiDung",
		on_delete=models.CASCADE,
		db_column="user_id",
		related_name="thong_bao",
	)
	loai_thong_bao = models.CharField(max_length=30, choices=LoaiThongBao.choices)
	noi_dung = models.TextField()
	da_doc = models.BooleanField(default=False)
	tao_luc = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = "THONG_BAO"
