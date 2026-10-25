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
        
    url = f"http://www.plantuml.com/plantuml/png/{res}"
    print(f"Fetching from PlantUML ({len(puml_code)} chars)...")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
    except urllib.error.HTTPError as e:
        print(f"❌ Error {e.code}: {e.read().decode('utf-8', errors='ignore')[:400]}")
        raise e
        
    with open(output_png_path, "wb") as f:
        f.write(data)
    print(f"✅ Generated: {output_png_path} ({len(data):,} bytes)")

# ==============================================================================
# 1. SƠ ĐỒ USE CASE TỔNG QUAN THỐNG NHẤT TOÀN HỆ THỐNG (FULL-SYSTEM USE CASE)
# ==============================================================================
master_uc_puml = r"""@startuml
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

title **SƠ ĐỒ USE CASE THỐNG NHẤT TOÀN HỆ THỐNG BLOG CMS LYXLAB (FULL-STACK 13 CONTAINERS)**

actor "Khách vãng lai\n(Guest)" as Guest #E0F2FE
actor "Độc giả (Reader)\n[docgia_k23]" as Reader #BAE6FD
actor "Tác giả (Author)\n[tacgia_k23]" as Author #FEF3C7
actor "Quản trị viên (Admin)\n[bount]" as Admin #FEE2E2
actor "Kỹ sư Vận hành\n(DevOps / SRE)" as DevOps #F3E8FF

Guest <|-- Reader
Reader <|-- Author
Author <|-- Admin

rectangle "HỆ THỐNG TOÀN DIỆN BLOG CMS LYXLAB (APP + INFRA + OBSERVABILITY)" {

    package "1. Nhóm Nghiệp vụ Ứng dụng Web & Tương tác (App Tier)" #F0F9FF {
        usecase "UC03: Tra cứu & Lọc bài theo Chuyên mục\n(DevOps, Hệ thống, An toàn, Lab)" as UC03
        usecase "UC04: Đăng nhập & Xác thực phiên\n(TLS 1.3, Cookie HMAC, phpass)" as UC04
        usecase "UC01: Biên soạn & Xuất bản bài viết kỹ thuật\n(Gutenberg, Upload Media, Transaction)" as UC01 #FEF08A
        usecase "UC02: Gửi & Phản hồi bình luận lồng nhau đa cấp\n(Threaded Comments, Chống XSS, Parent ID)" as UC02 #FEF08A
        usecase "UC_Media: Quản lý & Tải lên tệp Media\n(Named Volume wp_data /uploads/)" as UC_Media
    }

    package "2. Nhóm Quản trị Hệ thống & Dữ liệu (Admin & DB Tier)" #FEF2F2 {
        usecase "UC05: Quản lý Người dùng & Ma trận RBAC\n(Capabilities: Admin, Author, Subscriber)" as UC05
        usecase "UC06: Quản trị CSDL quan hệ trực quan\n(phpMyAdmin :8081 -> MySQL :3306)" as UC06
        usecase "UC07: Quản trị Ingress, SSL SAN & WAF\n(Nginx Proxy Manager Dashboard :81)" as UC07
        usecase "UC_Mod: Kiểm duyệt bài viết & bình luận" as UC_Mod
    }

    package "3. Nhóm Đo lường & Quản trị Vận hành (SRE & Telemetry Tier)" #FAF5FF {
        usecase "UC08: Giám sát Chuỗi thời gian (Metrics PULL 15s)\n(Prometheus + 5 Exporters + 4 Grafana Dashboards)" as UC08
        usecase "UC09: Thu thập & Truy vết Nhật ký (Logs PUSH)\n(Docker Socket -> Promtail -> Loki LogQL)" as UC09
        usecase "UC_Hardening: Giám sát Bảo vệ & Ranh giới mạng\n(no-new-privileges, 4 Bridge Networks, Limits)" as UC_Hardening
    }
}

Guest --> UC03
Guest --> UC04

Reader --> UC02

Author --> UC01
Author --> UC02
Author --> UC_Media

Admin --> UC05
Admin --> UC06
Admin --> UC07
Admin --> UC_Mod

DevOps --> UC08
DevOps --> UC09
DevOps --> UC_Hardening

UC01 ..> UC_Media : <<include>>
UC01 ..> UC04 : <<include>>
UC02 ..> UC04 : <<include>>
UC08 ..> UC01 : <<trace telemetry>>
UC09 ..> UC01 : <<collect logs>>
UC08 ..> UC02 : <<trace telemetry>>
UC09 ..> UC02 : <<collect logs>>

legend right
  |<#FEF08A>| **UC01 & UC02: Hai Use Case hạt nhân phản ánh toàn bộ kiến trúc 4 tầng** |
  |<#E0F2FE>| Khách vãng lai & Độc giả thành viên |
  |<#FEF3C7>| Tác giả biên soạn nội dung phòng lab |
  |<#FEE2E2>| Quản trị viên toàn quyền hệ thống |
  |<#F3E8FF>| Kỹ sư vận hành DevOps / SRE |
endlegend
@enduml"""

# ==============================================================================
# 2. BIỂU ĐỒ TUẦN TỰ TOÀN HỆ THỐNG CHO UC01 (FULL-STACK SEQUENCE)
# ==============================================================================
seq_uc01_fullstack = r"""@startuml
!theme plain
skinparam defaultFontName "Segoe UI"
skinparam defaultFontSize 11
skinparam roundcorner 6
skinparam shadowing true
skinparam responseMessageBelowArrow true
autonumber "<b>[00]</b>"

title **BIỂU ĐỒ TUẦN TỰ ĐỐI CHIẾU TOÀN HỆ THỐNG — UC01: BIÊN SOẠN VÀ XUẤT BẢN BÀI VIẾT KỸ THUẬT**

box "TẦNG NGƯỜI DÙNG & GIAO DIỆN" #E0F2FE
actor "Tác giả (Author)\n[tacgia_k23]" as Author #FEF3C7
participant "Trình duyệt Web\n(Gutenberg Block Editor)" as Browser #BAE6FD
end box

box "TẦNG CỔNG VÀ BẢO MẬT (INGRESS TIER)" #F0FDF4
participant "blog-npm\n(Nginx Gateway :443)" as NPM #86EFAC
end box

box "TẦNG ỨNG DỤNG & LƯU TRỮ (APP & DB TIER)" #FFF7ED
participant "blog-wordpress\n(WordPress PHP 8.2 :80)" as WP #FED7AA
participant "Named Volume\n(wp_data)" as VolWP #FEF3C7
database "blog-mysql\n(MySQL 8.0 InnoDB :3306)" as DB #FDBA74
end box

box "TẦNG QUAN SÁT & NHẬT KÝ (OBSERVABILITY & LOGGING TIER)" #FAF5FF
participant "5 Exporters\n(MySQL/Nginx/cAdvisor)" as Exporters #E9D5FF
participant "blog-prometheus\n(TSDB Metrics :9090)" as Prom #D8B4FE
participant "blog-promtail\n(Log Shipper :9080)" as Promtail #A7F3D0
participant "blog-loki\n(Log Server :3100)" as Loki #6EE7B7
end box

== BƯỚC 1: XÁC THỰC PHIÊN VÀ NẠP TRÌNH SOẠN THẢO GUTENBERG ==

Author -> Browser : Truy cập Menu Bài viết ➔ Thêm bài mới
activate Browser
Browser -> NPM : HTTPS GET /wp-admin/post-new.php (TLS 1.3 SAN)
activate NPM
NPM -> WP : Reverse Proxy HTTP:80 qua mạng blog_frontend_net
activate WP
WP -> WP : Kiểm tra Role: Author & Capability: edit_posts\nSinh mã bảo mật Nonce (_wpnonce)
WP --> NPM : HTTP 200 OK (Gutenberg Block Editor HTML/JS)
deactivate WP
NPM --> Browser : Nạp giao diện soạn thảo trực quan
deactivate NPM

== BƯỚC 2: TẢI LÊN ẢNH ĐẠI DIỆN VÀO NAMED VOLUME WP_DATA ==

Author -> Browser : Chọn tải lên ảnh bìa bài viết (Featured Image)
Browser -> NPM : HTTPS POST /wp-json/wp/v2/media (Multipart Form-Data)
activate NPM
NPM -> WP : Chuyển tiếp tới REST API Media
activate WP
WP -> WP : Kiểm tra Nonce, xác thực định dạng ảnh an toàn (image/png)
WP -> VolWP : Ghi tệp vật lý vào /wp-content/uploads/2026/10/banner.png
WP -> DB : INSERT INTO wp_posts (post_type='attachment') qua blog_backend_net
activate DB
DB --> WP : Trả về Attachment ID = 105
deactivate DB
WP --> NPM : HTTP 201 Created (JSON: attachment_id=105)
deactivate WP
NPM --> Browser : Hiển thị ảnh đại diện bài viết
deactivate NPM

== BƯỚC 3: GÁN CHUYÊN MỤC VÀ XUẤT BẢN QUA GIAO DỊCH MYSQL ==

Author -> Browser : Chọn chuyên mục "DevOps & Cloud" (term_id=2)\nvà nhấn nút "Đăng" (Publish)
Browser -> NPM : HTTPS POST /wp-json/wp/v2/posts\n[Payload: title, content, status='publish', categories=[2], featured_media=105]
activate NPM
NPM -> NPM : Kiểm tra WAF (block-exploits.conf)
NPM -> WP : Chuyển tiếp yêu cầu xuất bản
activate WP

WP -> WP : Lọc thẻ độc hại qua wp_filter_post_kses()
WP -> DB : START TRANSACTION
activate DB
WP -> DB : 1. INSERT INTO wp_posts (title, content, status='publish', date=NOW())
DB --> WP : Sinh bài viết mới ID = 9
WP -> DB : 2. INSERT INTO wp_term_relationships (post_id=9, term_id=2)
WP -> DB : 3. INSERT INTO wp_postmeta (post_id=9, meta_key='_thumbnail_id', meta_value=105)
WP -> DB : COMMIT TRANSACTION
DB --> WP : Hoàn tất lưu trữ ACID trên volume mysql_data
deactivate DB

WP --> NPM : HTTP 201 Created (JSON: post_id=9, slug="trien-khai-docker")
deactivate WP
NPM --> Browser : Thông báo bài viết xuất bản thành công!
deactivate NPM
Browser --> Author : Hiển thị bài viết trực tiếp trên trang chủ LyxLab
deactivate Browser

== BƯỚC 4: ĐỒNG THỜI GHI NHẬN ĐO LƯỜNG VÀ NHẬT KÝ HỆ THỐNG ==

par Ghi nhận Đo lường Metrics (Prometheus PULL)
    Exporters -> DB : mysqld-exporter đo số câu lệnh INSERT & Transaction commit
    Exporters -> NPM : nginx-exporter đo số request HTTP 201 Created
    Prom -> Exporters : Scrape metrics định kỳ (15s) qua blog_monitor_net
    activate Prom
    Prom -> Prom : Lưu chuỗi thời gian vào TSDB (volume prometheus_data)
    deactivate Prom
else Thu thập Nhật ký Tập trung (Loki PUSH)
    NPM -> Promtail : Xả log truy cập vào /data/logs/proxy-host-1_access.log
    WP -> Promtail : Xả log Apache/PHP ra stdout
    activate Promtail
    Promtail -> Promtail : Đọc /var/run/docker.sock:ro, gắn nhãn container="blog-wordpress"
    Promtail -> Loki : PUSH Batch HTTP :3100 qua blog_logging_net
    activate Loki
    deactivate Promtail
    Loki -> Loki : Nén khối Snappy Chunks lưu vào volume loki_data
    deactivate Loki
end

@enduml"""

# ==============================================================================
# 3. BIỂU ĐỒ TUẦN TỰ TOÀN HỆ THỐNG CHO UC02 (FULL-STACK SEQUENCE)
# ==============================================================================
seq_uc02_fullstack = r"""@startuml
!theme plain
skinparam defaultFontName "Segoe UI"
skinparam defaultFontSize 11
skinparam roundcorner 6
skinparam shadowing true
skinparam responseMessageBelowArrow true
autonumber "<b>[00]</b>"

title **BIỂU ĐỒ TUẦN TỰ ĐỐI CHIẾU TOÀN HỆ THỐNG — UC02: GỬI VÀ PHẢN HỒI BÌNH LUẬN LỒNG NHAU ĐA CẤP**

box "TẦNG NGƯỜI DÙNG (ACTORS)" #E0F2FE
actor "Độc giả (Reader)\n[docgia_k23]" as Reader #BAE6FD
actor "Tác giả (Author)\n[tacgia_k23]" as Author #FEF3C7
participant "Trình duyệt Client\n(Thảo luận phân tầng)" as Browser #93C5FD
end box

box "TẦNG CỔNG & BẢO MẬT (INGRESS)" #F0FDF4
participant "blog-npm\n(Nginx Ingress :443)" as NPM #86EFAC
end box

box "TẦNG ỨNG DỤNG & CSDL (APP & DB)" #FFF7ED
participant "blog-wordpress\n(WP Core :80)" as WP #FED7AA
database "blog-mysql\n(MySQL :3306 - wp_comments)" as DB #FDBA74
end box

box "TẦNG QUAN SÁT & TRUY VẾT LOG (OBSERVABILITY)" #FAF5FF
participant "blog-promtail\n(Log Shipper :9080)" as Promtail #A7F3D0
participant "blog-loki\n(Centralized Log :3100)" as Loki #6EE7B7
participant "blog-grafana\n(LogQL Explore :3000)" as Grafana #D8B4FE
end box

== PHA 1: ĐỘC GIẢ GỬI BÌNH LUẬN GỐC CẤP 1 (PARENT_ID = 0) ==

Reader -> Browser : Đọc bài viết ID=9, nhập câu hỏi kỹ thuật\nNhấn "Gửi bình luận"
activate Browser
Browser -> NPM : HTTPS POST /wp-comments-post.php\n[comment_post_ID=9, comment="...", comment_parent=0, _wpnonce=...]
activate NPM
NPM -> NPM : Kiểm tra WAF (chặn payload SQLi & XSS)
NPM -> WP : Reverse Proxy HTTP POST :80 qua blog_frontend_net
activate WP

WP -> WP : Xác thực danh tính docgia_k23 qua Cookie\nLọc nội dung qua wp_filter_kses()
WP -> DB : INSERT INTO wp_comments (post_ID=9, author='docgia_k23', content='...', parent=0, approved=1)\nqua mạng cô lập blog_backend_net
activate DB
DB --> WP : Trả về comment_id = 2 (Gốc cấp 1)
deactivate DB
WP -> DB : UPDATE wp_posts SET comment_count = comment_count + 1 WHERE ID=9

WP --> NPM : HTTP 302 Found (Location: /trien-khai-docker/#comment-2)
deactivate WP
NPM -> Promtail : Ghi log POST 302
NPM --> Browser : Chuyển hướng tới vị trí bình luận
deactivate NPM
Browser --> Reader : Hiển thị bình luận Cấp 1 của Độc giả
deactivate Browser

== PHA 2: TÁC GIẢ PHẢN HỒI LỒNG NHAU TẠO CÂY ĐA CẤP (PARENT_ID = 2) ==

Author -> Browser : Xem bài viết, bấm "Trả lời" (Reply) ngay dưới comment ID=2
activate Browser
Browser -> Browser : Chèn form phản hồi lồng bên dưới, gán hidden input: comment_parent = 2
Author -> Browser : Nhập câu trả lời giải đáp kỹ thuật, nhấn "Phản hồi"

Browser -> NPM : HTTPS POST /wp-comments-post.php\n[comment_post_ID=9, comment="...", comment_parent=2, _wpnonce=...]
activate NPM
NPM -> WP : Reverse Proxy HTTP POST :80
activate WP
WP -> WP : Xác thực tài khoản tacgia_k23, kiểm tra comment_parent=2 hợp lệ
WP -> DB : INSERT INTO wp_comments (post_ID=9, author='tacgia_k23', content='...', parent=2, approved=1)
activate DB
DB --> WP : Trả về comment_id = 3 (Bình luận con)
deactivate DB
WP -> DB : UPDATE wp_posts SET comment_count = comment_count + 1 WHERE ID=9

WP --> NPM : HTTP 302 Found (Location: /trien-khai-docker/#comment-3)
deactivate WP
NPM -> Promtail : Ghi log POST 302
NPM --> Browser : Chuyển hướng tới vị trí bình luận con
deactivate NPM

Browser -> Browser : Render cây thảo luận phân cấp (Threaded Tree):\nComment ID=3 thụt lề dưới Comment ID=2\nHiển thị huy hiệu "Tác giả bài viết"
Browser --> Author : Thảo luận lồng nhau hiển thị chính xác
deactivate Browser

== PHA 3: TRUY VẾT NHẬT KÝ VẬN HÀNH BẰNG LOGQL ==

Promtail -> Loki : PUSH Batch dòng log chứa request /wp-comments-post.php (HTTP 302)
activate Loki
deactivate Promtail
Loki -> Loki : Đánh chỉ mục nhãn {container="blog-wordpress"}
deactivate Loki

actor "Kỹ sư DevOps" as DevOps #F3E8FF
DevOps -> Grafana : Mở giao diện Grafana Explore (LogQL)
activate Grafana
Grafana -> Loki : Thực thi truy vấn: {container="blog-wordpress"} |= "wp-comments-post.php"
activate Loki
Loki --> Grafana : Trả về danh sách log thời gian thực các tương tác bình luận
deactivate Loki
Grafana --> DevOps : Hiển thị trực quan tần suất gửi bình luận & IP người dùng
deactivate Grafana

@enduml"""

def main():
    output_dir = "docs/architecture"
    os.makedirs(output_dir, exist_ok=True)
    artifact_dir = "/home/cyberbount/.gemini/antigravity/brain/de78f41e-e732-4572-9c45-484dc7900b08"
    
    # 1. Master UC
    p1 = os.path.join(output_dir, "system_usecase_unified_master.puml")
    with open(p1, "w", encoding="utf-8") as f:
        f.write(master_uc_puml.strip())
    png1 = os.path.join(output_dir, "system_usecase_unified_master.png")
    render_plantuml(master_uc_puml.strip(), png1)
    
    # 2. UC01 Fullstack
    p2 = os.path.join(output_dir, "uc01_fullstack_unified_sequence.puml")
    with open(p2, "w", encoding="utf-8") as f:
        f.write(seq_uc01_fullstack.strip())
    png2 = os.path.join(output_dir, "uc01_fullstack_unified_sequence.png")
    render_plantuml(seq_uc01_fullstack.strip(), png2)
    
    # 3. UC02 Fullstack
    p3 = os.path.join(output_dir, "uc02_fullstack_unified_sequence.puml")
    with open(p3, "w", encoding="utf-8") as f:
        f.write(seq_uc02_fullstack.strip())
    png3 = os.path.join(output_dir, "uc02_fullstack_unified_sequence.png")
    render_plantuml(seq_uc02_fullstack.strip(), png3)
    
    # Copy to artifacts
    if os.path.exists(artifact_dir):
        os.system(f"cp {png1} {artifact_dir}/")
        os.system(f"cp {png2} {artifact_dir}/")
        os.system(f"cp {png3} {artifact_dir}/")
        print("✅ All full-stack unified diagrams copied to artifacts!")

if __name__ == "__main__":
    main()
