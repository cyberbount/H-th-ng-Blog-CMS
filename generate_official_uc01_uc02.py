import os
import zlib
import urllib.request

def render_plantuml(puml_code, output_png_path):
    zlibbed_str = zlib.compress(puml_code.encode("utf-8"))
    compressed_string = zlibbed_str[2:-4]
    
    mapping = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_"
    
    def _encode6bit(b):
        return mapping[b & 0x3f]
        
    def _append3bytes(b1, b2, b3):
        c1 = b1 >> 2
        c2 = ((b1 & 0x3) << 4) | (b2 >> 4)
        c3 = ((b2 & 0xF) << 2) | (b3 >> 6)
        c4 = b3 & 0x3F
        return _encode6bit(c1) + _encode6bit(c2) + _encode6bit(c3) + _encode6bit(c4)
        
    res = ""
    i = 0
    while i < len(compressed_string):
        b1 = compressed_string[i]
        b2 = compressed_string[i+1] if i+1 < len(compressed_string) else 0
        b3 = compressed_string[i+2] if i+2 < len(compressed_string) else 0
        res += _append3bytes(b1, b2, b3)
        i += 3
        
    encoded = res
    url = f"http://www.plantuml.com/plantuml/png/{encoded}"
    print(f"Fetching from PlantUML server ({len(puml_code)} chars)...")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="ignore")
        print(f"❌ HTTP Error {e.code}: {err_body[:500]}")
        raise e
        
    with open(output_png_path, "wb") as f:
        f.write(data)
    print(f"✅ Successfully generated: {output_png_path} ({len(data):,} bytes)")

# ==============================================================================
# UC01: BIÊN SOẠN VÀ XUẤT BẢN BÀI VIẾT KỸ THUẬT (SEQUENCE DIAGRAM)
# ==============================================================================
seq_uc01 = r"""@startuml
!theme plain
skinparam defaultFontName "Segoe UI"
skinparam defaultFontSize 11
skinparam roundcorner 6
skinparam shadowing true
skinparam responseMessageBelowArrow true
autonumber "<b>[00]</b>"

title **BIỂU ĐỒ TUẦN TỰ UC01: BIÊN SOẠN VÀ XUẤT BẢN BÀI VIẾT KỸ THUẬT**

actor "Tác giả (Author)\n[User: tacgia_k23]" as Author #FEF3C7
participant "Trình duyệt Web\n(Gutenberg Block Editor)" as Browser #BAE6FD
participant "blog-npm\n(Nginx Ingress Gateway :443)" as NPM #93C5FD
participant "blog-wordpress\n(WordPress REST API :80)" as WP #DBEAFE
participant "Named Volume\n(wp_data /wp-content/uploads/)" as Storage #FFFBEB
database "blog-mysql\n(MySQL 8.0 InnoDB)" as DB #FED7AA
participant "blog-promtail\n(Log Collector)" as Promtail #D1FAE5

== BƯỚC 1: KHỞI TẠO VÀ SOẠN THẢO BÀI VIẾT BẰNG GUTENBERG ==

Author -> Browser : Truy cập Menu Bài viết ➔ Chọn "Thêm bài mới"
activate Browser
Browser -> NPM : HTTPS GET /wp-admin/post-new.php (TLS 1.3)
activate NPM
NPM -> WP : Reverse Proxy HTTP GET :80 (blog_frontend_net)
activate WP
WP -> WP : Kiểm tra Capability: current_user_can('edit_posts')\nSinh Cryptographic Nonce (_wpnonce) cho phiên soạn thảo
WP --> NPM : HTTP 200 OK (Giao diện Block Editor Gutenberg)
deactivate WP
NPM --> Browser : Trả về mã HTML & Javascript Gutenberg Engine
deactivate NPM
Browser --> Author : Hiển thị khung soạn thảo trực quan

Author -> Browser : Nhập Tiêu đề, phân đoạn nội dung,\nchèn khối Code Block (cú pháp Docker/Python)

== BƯỚC 2: TẢI LÊN ẢNH ĐẠI DIỆN (FEATURED IMAGE) ==

Author -> Browser : Chọn tải lên ảnh bìa đại diện bài viết
Browser -> NPM : HTTPS POST /wp-json/wp/v2/media (Multipart Form-Data)\n[Header: X-WP-Nonce, Cookie: wordpress_logged_in_*]
activate NPM
NPM -> WP : Reverse Proxy HTTP POST :80
activate WP
WP -> WP : Xác thực Nonce, kiểm tra phần mở rộng (MIME Type: image/jpeg, image/png)\nKhử khuẩn tên tệp và tạo các kích thước Thumbnail (crop)
WP -> Storage : Ghi tệp vật lý vào volume: /var/www/html/wp-content/uploads/2026/10/
WP -> DB : INSERT INTO wp_posts (post_type='attachment', post_mime_type='image/png')
activate DB
DB --> WP : Trả về Attachment ID = 105
deactivate DB
WP --> NPM : HTTP 201 Created (JSON: attachment_id=105, url="...")
deactivate WP
NPM --> Browser : Trả về dữ liệu ảnh đã tải lên
deactivate NPM
Browser --> Author : Hiển thị ảnh xem trước tại ô "Ảnh đại diện"

== BƯỚC 3: GÁN CHUYÊN MỤC VÀ THỰC THI XUẤT BẢN BÀI VIẾT (TRANSACTION) ==

Author -> Browser : Chọn chuyên mục "DevOps & Cloud" (term_id=2)\nvà nhấn nút "Đăng" (Publish)
Browser -> NPM : HTTPS POST /wp-json/wp/v2/posts\n[Payload: {"title": "Triển khai Docker", "content": "...", "status": "publish", "categories": [2], "featured_media": 105}]
activate NPM
NPM -> NPM : Kiểm tra WAF (block-exploits.conf)\nLọc bỏ mã độc XSS và kiểm tra quyền hạn tác giả
NPM -> WP : Reverse Proxy HTTP POST :80
activate WP

WP -> WP : Làm sạch nội dung qua wp_filter_post_kses()\nXác định quyền hạn: current_user_can('publish_posts')
WP -> DB : START TRANSACTION
activate DB

WP -> DB : INSERT INTO wp_posts (\n  post_author=2, post_title='Triển khai Docker',\n  post_content='...', post_status='publish',\n  post_name='trien-khai-docker', post_date=NOW()\n)
DB --> WP : Trả về bài viết mới new_post_id = 9

WP -> DB : INSERT INTO wp_term_relationships (object_id=9, term_taxonomy_id=2)
DB --> WP : Đã liên kết Chuyên mục "DevOps & Cloud"

WP -> DB : INSERT INTO wp_postmeta (post_id=9, meta_key='_thumbnail_id', meta_value=105)
DB --> WP : Đã gắn Ảnh đại diện Featured Image

WP -> DB : COMMIT TRANSACTION
DB --> WP : Giao dịch CSDL hoàn tất thành công
deactivate DB

WP -> WP : Xóa cache trang chủ (Purge Object Cache / Rewrite Rules)
WP --> NPM : HTTP 201 Created (JSON: post_id=9, link="https://localhost/trien-khai-docker/")
deactivate WP

NPM -> Promtail : Ghi log xuất bản bài viết thành công (HTTP 201)
NPM --> Browser : Phản hồi HTTP 201 Created
deactivate NPM

Browser --> Author : Thông báo: "Bài viết đã được xuất bản thành công!"\nHiển thị nút "Xem bài viết" trực tiếp trên trang chủ
deactivate Browser

@enduml"""

# ==============================================================================
# UC02: GỬI VÀ PHẢN HỒI BÌNH LUẬN LỒNG NHAU ĐA CẤP (SEQUENCE DIAGRAM)
# ==============================================================================
seq_uc02 = r"""@startuml
!theme plain
skinparam defaultFontName "Segoe UI"
skinparam defaultFontSize 11
skinparam roundcorner 6
skinparam shadowing true
skinparam responseMessageBelowArrow true
autonumber "<b>[00]</b>"

title **BIỂU ĐỒ TUẦN TỰ UC02: GỬI VÀ PHẢN HỒI BÌNH LUẬN LỒNG NHAU ĐA CẤP**

actor "Độc giả (Reader)\n[User: docgia_k23]" as Reader #BAE6FD
actor "Tác giả (Author)\n[User: tacgia_k23]" as Author #FEF3C7
participant "Trình duyệt Web\n(Giao diện Bài viết)" as Browser #E0F2FE
participant "blog-npm\n(Nginx Ingress :443)" as NPM #93C5FD
participant "blog-wordpress\n(WordPress Core :80)" as WP #DBEAFE
database "blog-mysql\n(MySQL 8.0: wp_comments)" as DB #FED7AA
participant "blog-promtail\n(Log Collector)" as Promtail #D1FAE5

== GIAI ĐOẠN 1: ĐỘC GIẢ GỬI BÌNH LUẬN GỐC CẤP 1 (ROOT COMMENT) ==

Reader -> Browser : Đọc bài viết, cuộn xuống ô thảo luận\nNhập nội dung: "Bài viết rất hay, Docker stats lấy từ cAdvisor đúng không?"
activate Browser
Reader -> Browser : Nhấn nút "Gửi bình luận" (Post Comment)

Browser -> NPM : HTTPS POST /wp-comments-post.php\n[Payload: comment_post_ID=9, comment="...", comment_parent=0, _wpnonce=...]
activate NPM
NPM -> NPM : Kiểm tra WAF (block-exploits.conf)\nLọc bỏ ký tự SQLi, kiểm tra flood request
NPM -> WP : Reverse Proxy HTTP POST :80 (blog_frontend_net)
activate WP

WP -> WP : Kiểm tra Nonce, xác thực danh tính Độc giả qua Cookie\nLàm sạch nội dung bình luận qua wp_filter_kses()
WP -> WP : Kiểm tra cài đặt thảo luận: comment_parent = 0 (Bình luận gốc cấp 1)\nTự động phê duyệt (approved = 1) do tài khoản đã đăng nhập

WP -> DB : INSERT INTO wp_comments (\n  comment_post_ID=9, comment_author='docgia_k23',\n  comment_content='...', comment_parent=0,\n  comment_approved=1, comment_date=NOW()\n)
activate DB
DB --> WP : Trả về new_comment_id = 2
deactivate DB

WP -> DB : UPDATE wp_posts SET comment_count = comment_count + 1 WHERE ID = 9
activate DB
DB --> WP : Cập nhật tổng số bình luận thành công
deactivate DB

WP --> NPM : HTTP 302 Redirect về /trien-khai-docker/#comment-2
deactivate WP
NPM -> Promtail : Ghi log đăng bình luận thành công (HTTP 302)
NPM --> Browser : Chuyển hướng về vị trí bình luận vừa đăng
deactivate NPM
Browser --> Reader : Hiển thị bình luận Cấp 1 của docgia_k23 dưới bài viết
deactivate Browser

== GIAI ĐOẠN 2: TÁC GIẢ PHẢN HỒI BÌNH LUẬN TẠO CÂY ĐA CẤP (THREADED REPLY) ==

Author -> Browser : Truy cập bài viết cá nhân, phát hiện bình luận của docgia_k23
activate Browser
Author -> Browser : Nhấn nút "Trả lời" (Reply) ngay bên dưới comment ID=2
Browser -> Browser : Nhúng ô nhập phản hồi lồng bên dưới comment 2\nThiết lập trường ẩn: comment_parent = 2

Author -> Browser : Nhập nội dung: "Chào bạn, đúng rồi, cAdvisor đo CPU/RAM còn docker-stats đo mạng!"\nNhấn "Phản hồi"
Browser -> NPM : HTTPS POST /wp-comments-post.php\n[Payload: comment_post_ID=9, comment="...", comment_parent=2, _wpnonce=...]
activate NPM
NPM -> WP : Reverse Proxy HTTP POST :80
activate WP

WP -> WP : Kiểm tra Nonce, xác thực tài khoản Tác giả (tacgia_k23)\nKiểm tra hợp lệ ID bình luận cha (comment_parent = 2)

WP -> DB : INSERT INTO wp_comments (\n  comment_post_ID=9, comment_author='tacgia_k23',\n  comment_content='Chào bạn, đúng rồi...',\n  comment_parent=2, comment_approved=1, comment_date=NOW()\n)
activate DB
DB --> WP : Trả về new_comment_id = 3 (Bình luận con)
deactivate DB

WP -> DB : UPDATE wp_posts SET comment_count = comment_count + 1 WHERE ID = 9
activate DB
DB --> WP : Cập nhật tổng số bình luận = 2
deactivate DB

WP --> NPM : HTTP 302 Redirect về /trien-khai-docker/#comment-3
deactivate WP
NPM -> Promtail : Ghi log phản hồi bình luận thành công
NPM --> Browser : Chuyển hướng về vị trí bình luận con
deactivate NPM

Browser -> Browser : Render cây bình luận phân tầng (Threaded Tree):\nBình luận ID=3 thụt lề (indent level 1) lồng dưới bình luận ID=2\nHiển thị huy hiệu "Tác giả bài viết" bên cạnh tên tacgia_k23
Browser --> Author : Hiển thị cấu trúc thảo luận phân cấp hoàn chỉnh
deactivate Browser

@enduml"""

# ==============================================================================
# SƠ ĐỒ USE CASE TỔNG QUÁT CHUẨN XÁC THEO HÌNH 3.1 VÀ BÁO CÁO K23A
# ==============================================================================
uc_official_puml = r"""@startuml
!theme plain
left to right direction
skinparam defaultFontName "Segoe UI"
skinparam defaultFontSize 11
skinparam roundcorner 8
skinparam shadowing true
skinparam packageStyle rectangle
skinparam arrowColor #334155
skinparam arrowThickness 1.2

skinparam actor {
    BackgroundColor #F8FAFC
    BorderColor #1E293B
    FontColor #0F172A
    FontStyle bold
}

skinparam usecase {
    BackgroundColor #FFFFFF
    BorderColor #2563EB
    FontColor #0F172A
    BorderThickness 1.5
}

title **SƠ ĐỒ USE CASE TỔNG QUÁT HỆ THỐNG BLOG CMS LYXLAB (CHUẨN HÓA BÁO CÁO K23A)**

actor "Khách vãng lai\n(Guest - Chưa đăng nhập)" as Guest #E0F2FE
actor "Độc giả thành viên\n(Reader / Subscriber)" as Reader #BAE6FD
actor "Tác giả (Author)\n[Kỹ sư / Biên tập viên]" as Author #FEF3C7
actor "Quản trị viên (Admin)\n[Trưởng Lab / DevOps]" as Admin #FEE2E2

' Kế thừa vai trò người dùng (Generalization)
Guest <|-- Reader
Reader <|-- Author
Author <|-- Admin

rectangle "HỆ THỐNG BLOG CMS LYXLAB (WORDPRESS & INFRASTRUCTURE)" {

    package "Phân hệ Độc giả & Khách vãng lai" #F0F9FF {
        usecase "Xem & Tìm kiếm bài viết" as UC_ViewSearch
        usecase "Lọc bài viết theo Chuyên mục & Tag" as UC_Filter
        usecase "Đăng nhập & Xác thực phiên" as UC_Auth
        usecase "UC02: Gửi và Phản hồi bình luận lồng nhau" as UC02
    }

    package "Phân hệ Tác giả & Biên tập nội dung" #FFFBEB {
        usecase "UC01: Biên soạn và Xuất bản bài viết kỹ thuật" as UC01
        usecase "Tải lên hình ảnh Media & Featured Image" as UC_Media
        usecase "Quản lý & Chỉnh sửa bài viết của mình" as UC_ManageSelf
    }

    package "Phân hệ Quản trị & Vận hành Hạ tầng" #FEF2F2 {
        usecase "Quản lý Người dùng & Ma trận RBAC" as UC_RBAC
        usecase "Kiểm duyệt toàn bộ Bài viết & Bình luận" as UC_Moderate
        usecase "Cấu hình Nginx SSL (TLS 1.3) & Proxy Host" as UC_NPM
        usecase "Quản trị CSDL Cấp cao (phpMyAdmin)" as UC_PMA
        usecase "Giám sát Metrics (Prometheus) & LogQL (Loki)" as UC_Monitor
    }
}

' Liên kết Khách & Độc giả
Guest --> UC_ViewSearch
Guest --> UC_Filter
Guest --> UC_Auth

Reader --> UC02

' Liên kết Tác giả
Author --> UC01
Author --> UC_Media
Author --> UC_ManageSelf
Author --> UC02

' Liên kết Quản trị viên
Admin --> UC_RBAC
Admin --> UC_Moderate
Admin --> UC_NPM
Admin --> UC_PMA
Admin --> UC_Monitor

' Quan hệ Phụ thuộc & Mở rộng
UC01 ..> UC_Media : <<extend>>
UC01 ..> UC_Filter : <<include>>
UC02 ..> UC_Auth : <<include>>
UC01 ..> UC_Auth : <<include>>

legend right
  |<#E0F2FE>| Khách vãng lai (Chưa đăng nhập, chỉ đọc & tìm kiếm) |
  |<#BAE6FD>| Độc giả thành viên (docgia_k23 - Thảo luận, bình luận) |
  |<#FEF3C7>| Tác giả (tacgia_k23 - Soạn bài, tải ảnh, phản hồi bình luận) |
  |<#FEE2E2>| Quản trị viên (bount - Toàn quyền nội dung, RBAC & hạ tầng) |
  |<#2563EB>| UC01 & UC02: Hai Use Case trọng tâm của Báo cáo Chuyên đề K23A |
endlegend
@enduml"""

def main():
    output_dir = "docs/architecture"
    os.makedirs(output_dir, exist_ok=True)
    artifact_dir = "/home/cyberbount/.gemini/antigravity/brain/de78f41e-e732-4572-9c45-484dc7900b08"
    
    # Render UC01
    p1 = os.path.join(output_dir, "uc01_publish_post_sequence.puml")
    with open(p1, "w", encoding="utf-8") as f:
        f.write(seq_uc01.strip())
    png1 = os.path.join(output_dir, "uc01_publish_post_sequence.png")
    render_plantuml(seq_uc01.strip(), png1)
    
    # Render UC02
    p2 = os.path.join(output_dir, "uc02_threaded_comment_sequence.puml")
    with open(p2, "w", encoding="utf-8") as f:
        f.write(seq_uc02.strip())
    png2 = os.path.join(output_dir, "uc02_threaded_comment_sequence.png")
    render_plantuml(seq_uc02.strip(), png2)
    
    # Render Official UC Master
    p3 = os.path.join(output_dir, "system_usecase_diagram_official.puml")
    with open(p3, "w", encoding="utf-8") as f:
        f.write(uc_official_puml.strip())
    png3 = os.path.join(output_dir, "system_usecase_diagram_official.png")
    render_plantuml(uc_official_puml.strip(), png3)
    
    # Copy to artifact dir
    if os.path.exists(artifact_dir):
        os.system(f"cp {png1} {artifact_dir}/")
        os.system(f"cp {png2} {artifact_dir}/")
        os.system(f"cp {png3} {artifact_dir}/")
        print("✅ Copied all official diagrams to artifact directory!")

if __name__ == "__main__":
    main()

