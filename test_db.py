import os
import django
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from modules.applications.models import UngTuyen
print("--- DB STATE ---")
for ut in UngTuyen.objects.filter(ung_vien_id=3):
    print(f"Tin: {ut.tin_id}, TrangThai: {ut.trang_thai}")
