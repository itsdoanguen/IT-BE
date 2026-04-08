-- Tạo database nếu chưa có và sử dụng nó
CREATE DATABASE IF NOT EXISTS baito_link CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE baito_link;

-- 1. Bảng Người dùng (Gốc)
CREATE TABLE IF NOT EXISTS NGUOI_DUNG (
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT 'Mã người dùng',
    email VARCHAR(255) NOT NULL UNIQUE COMMENT 'Email đăng nhập',
    mat_khau VARCHAR(255) NOT NULL COMMENT 'Mật khẩu mã hóa',
    vai_tro ENUM('ung_vien', 'cong_ty', 'admin') NOT NULL COMMENT 'Vai trò người dùng',
    tao_luc DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT 'Thời gian tạo'
) ENGINE=InnoDB;

-- 2. Bảng Hồ sơ ứng viên
CREATE TABLE IF NOT EXISTS HO_SO_UNG_VIEN (
    ung_vien_id INT PRIMARY KEY COMMENT 'Khóa chính, trỏ về NGUOI_DUNG.id',
    ho_ten VARCHAR(255) NOT NULL COMMENT 'Họ và tên',
    so_dien_thoai VARCHAR(20) COMMENT 'Số điện thoại liên hệ',
    ky_nang TEXT COMMENT 'Kỹ năng chuyên môn/Mềm',
    vi_tri_mong_muon VARCHAR(255) COMMENT 'Khu vực muốn làm việc',
    thoi_gian_ranh VARCHAR(255) COMMENT 'Khung giờ có thể làm',
    luong_mong_muon DECIMAL(10, 2) COMMENT 'Mức lương giờ mong muốn',
    FOREIGN KEY (ung_vien_id) REFERENCES NGUOI_DUNG(id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- 3. Bảng Hồ sơ công ty
CREATE TABLE IF NOT EXISTS HO_SO_CONG_TY (
    cong_ty_id INT PRIMARY KEY COMMENT 'Khóa chính, trỏ về NGUOI_DUNG.id',
    ten_cong_ty VARCHAR(255) NOT NULL COMMENT 'Tên doanh nghiệp',
    linh_vuc VARCHAR(255) COMMENT 'Ngành nghề kinh doanh',
    lich_su TEXT COMMENT 'Lịch sử hình thành',
    lien_he VARCHAR(255) COMMENT 'Thông tin liên hệ chung',
    dia_chi TEXT COMMENT 'Địa chỉ công ty',
    FOREIGN KEY (cong_ty_id) REFERENCES NGUOI_DUNG(id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- 4. Bảng Tin tuyển dụng
CREATE TABLE IF NOT EXISTS TIN_TUYEN_DUNG (
    tin_id INT AUTO_INCREMENT PRIMARY KEY COMMENT 'Mã tin tuyển dụng',
    cong_ty_id INT NOT NULL COMMENT 'Mã công ty đăng tin',
    tieu_de VARCHAR(255) NOT NULL COMMENT 'Tiêu đề công việc',
    noi_dung TEXT NOT NULL COMMENT 'Mô tả công việc',
    bat_dau_lam DATETIME NOT NULL COMMENT 'Thời gian bắt đầu',
    ket_thuc_lam DATETIME NOT NULL COMMENT 'Thời gian kết thúc',
    luong_theo_gio DECIMAL(10, 2) NOT NULL COMMENT 'Mức lương / giờ',
    dia_diem_lam_viec VARCHAR(255) NOT NULL COMMENT 'Nơi làm việc cụ thể',
    trang_thai ENUM('dang_mo', 'da_dong') DEFAULT 'dang_mo' COMMENT 'Trạng thái tin',
    tao_luc DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT 'Thời gian đăng',
    FOREIGN KEY (cong_ty_id) REFERENCES HO_SO_CONG_TY(cong_ty_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- 5. Bảng Ứng tuyển (Matching)
CREATE TABLE IF NOT EXISTS UNG_TUYEN (
    ung_tuyen_id INT AUTO_INCREMENT PRIMARY KEY COMMENT 'Mã ứng tuyển',
    tin_id INT NOT NULL COMMENT 'Mã tin tuyển dụng',
    ung_vien_id INT NOT NULL COMMENT 'Mã ứng viên',
    trang_thai ENUM('cho_duyet', 'chap_nhan', 'tu_choi', 'hoan_thanh') DEFAULT 'cho_duyet' COMMENT 'Trạng thái ứng tuyển',
    thoi_gian_ung_tuyen DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT 'Thời điểm nộp',
    FOREIGN KEY (tin_id) REFERENCES TIN_TUYEN_DUNG(tin_id) ON DELETE CASCADE,
    FOREIGN KEY (ung_vien_id) REFERENCES HO_SO_UNG_VIEN(ung_vien_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- 6. Bảng Chat
CREATE TABLE IF NOT EXISTS CHAT (
    tin_nhan_id INT AUTO_INCREMENT PRIMARY KEY COMMENT 'Mã tin nhắn',
    nguoi_gui_id INT NOT NULL COMMENT 'ID người gửi',
    nguoi_nhan_id INT NOT NULL COMMENT 'ID người nhận',
    noi_dung_tin_nhan TEXT NOT NULL COMMENT 'Nội dung',
    thoi_gian_gui DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT 'Thời gian gửi',
    FOREIGN KEY (nguoi_gui_id) REFERENCES NGUOI_DUNG(id) ON DELETE CASCADE,
    FOREIGN KEY (nguoi_nhan_id) REFERENCES NGUOI_DUNG(id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- 7. Bảng Đánh giá
CREATE TABLE IF NOT EXISTS DANH_GIA (
    danh_gia_id INT AUTO_INCREMENT PRIMARY KEY COMMENT 'Mã đánh giá/Review',
    ung_tuyen_id INT NOT NULL COMMENT 'Dựa trên lần làm việc nào',
    nguoi_danh_gia_id INT NOT NULL COMMENT 'ID người viết',
    nguoi_nhan_danh_gia_id INT NOT NULL COMMENT 'ID người bị đánh giá',
    diem_so TINYINT NOT NULL CHECK(diem_so >= 1 AND diem_so <= 5) COMMENT 'Từ 1 đến 5 sao',
    nhan_xet TEXT COMMENT 'Bình luận chi tiết',
    tao_luc DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT 'Thời gian đánh giá',
    FOREIGN KEY (ung_tuyen_id) REFERENCES UNG_TUYEN(ung_tuyen_id) ON DELETE CASCADE,
    FOREIGN KEY (nguoi_danh_gia_id) REFERENCES NGUOI_DUNG(id) ON DELETE CASCADE,
    FOREIGN KEY (nguoi_nhan_danh_gia_id) REFERENCES NGUOI_DUNG(id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- 8. Bảng Thông báo
CREATE TABLE IF NOT EXISTS THONG_BAO (
    thong_bao_id INT AUTO_INCREMENT PRIMARY KEY COMMENT 'Mã thông báo',
    user_id INT NOT NULL COMMENT 'Người nhận thông báo',
    loai_thong_bao ENUM('tin_moi', 'match_thanh_cong', 'tin_nhan_moi') NOT NULL COMMENT 'Phân loại thông báo',
    noi_dung TEXT NOT NULL COMMENT 'Nội dung hiển thị',
    da_doc BOOLEAN DEFAULT FALSE COMMENT 'Trạng thái đọc (0: chưa, 1: rồi)',
    tao_luc DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT 'Thời gian tạo',
    FOREIGN KEY (user_id) REFERENCES NGUOI_DUNG(id) ON DELETE CASCADE
) ENGINE=InnoDB;