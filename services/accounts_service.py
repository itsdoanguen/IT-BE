from modules.accounts.models import NguoiDung


def create_user(email: str, password: str, vai_tro: str = "ung_vien") -> NguoiDung:
    return NguoiDung.objects.create_user(email=email, password=password, vai_tro=vai_tro)
