from django.db import models


class Chat(models.Model):
	tin_nhan_id = models.AutoField(primary_key=True)
	nguoi_gui = models.ForeignKey(
		"accounts.NguoiDung",
		on_delete=models.CASCADE,
		db_column="nguoi_gui_id",
		related_name="tin_nhan_da_gui",
	)
	nguoi_nhan = models.ForeignKey(
		"accounts.NguoiDung",
		on_delete=models.CASCADE,
		db_column="nguoi_nhan_id",
		related_name="tin_nhan_da_nhan",
	)
	noi_dung_tin_nhan = models.TextField()
	thoi_gian_gui = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = "CHAT"
