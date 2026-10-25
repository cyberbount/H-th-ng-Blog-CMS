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
    print(f"Fetching Use Case diagram from PlantUML server ({len(puml_code)} chars)...")
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

usecase_puml = r"""@startuml
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

title **SƠ ĐỒ USE CASE TỔNG QUÁT HỆ THỐNG BLOG CMS LYXLAB**

actor "Khách vãng lai\n(Guest)" as Guest #E0F2FE
actor "Độc giả thành viên\n(Reader / Subscriber)" as Reader #BAE6FD
actor "Tác giả / Biên tập\n(Author / Editor)" as Author #FEF3C7
actor "Quản trị viên\n(Administrator)" as Admin #FEE2E2
actor "Kỹ sư Vận hành\n(DevOps / SRE)" as DevOps #F3E8FF

Guest <|-- Reader
Reader <|-- Author
Author <|-- Admin

rectangle "HỆ THỐNG BLOG CMS LYXLAB" {

    package "1. Phân hệ Tương tác Độc giả & Khách" #F0F9FF {
        usecase "UC01: Xem Trang chủ & Danh mục" as UC_View
        usecase "UC02: Tìm kiếm & Lọc bài viết" as UC_Search
        usecase "UC03: Đăng ký / Đăng nhập" as UC_Auth
        usecase "UC04: Quản lý Hồ sơ cá nhân" as UC_Profile
        usecase "UC05: Gửi Bình luận bài viết" as UC_Comment
        usecase "UC06: Xác thực bảo mật Nonce & Cookie" as UC_SecToken
    }

    package "2. Phân hệ Tác giả & Quản lý Nội dung" #FFFBEB {
        usecase "UC07: Soạn thảo bài viết mới" as UC_CreatePost
        usecase "UC08: Tải lên & Quản lý Media" as UC_Media
        usecase "UC09: Xuất bản & Hẹn giờ bài viết" as UC_Publish
        usecase "UC10: Chỉnh sửa / Xóa bài của mình" as UC_EditSelf
        usecase "UC11: Gán Chuyên mục & Thẻ Tag" as UC_Taxonomy
    }

    package "3. Phân hệ Quản trị Hệ thống (Admin)" #FEF2F2 {
        usecase "UC12: Quản lý & Phân quyền Người dùng" as UC_UserMgmt
        usecase "UC13: Kiểm duyệt & Xóa Bình luận" as UC_CommentMod
        usecase "UC14: Quản lý Theme, Plugin & Layout" as UC_ThemeMgmt
        usecase "UC15: Quản trị CSDL Cấp cao (phpMyAdmin)" as UC_DBAdmin
        usecase "UC16: Cấu hình Ingress Proxy & SSL (NPM)" as UC_ProxySSL
    }

    package "4. Phân hệ Giám sát & Quản trị Nhật ký (Observability)" #FAF5FF {
        usecase "UC17: Giám sát Tài nguyên Host & Container" as UC_MonHost
        usecase "UC18: Giám sát Hiệu năng CSDL MySQL" as UC_MonDB
        usecase "UC19: Giám sát Lưu lượng Web Nginx" as UC_MonNginx
        usecase "UC20: Xem Dashboards Trực quan (Grafana)" as UC_Dashboards
        usecase "UC21: Truy vết & Phân tích Nhật ký (LogQL)" as UC_Logs
        usecase "UC22: Quản trị Vòng đời 13 Containers" as UC_DockerLife
    }
}

Guest --> UC_View
Guest --> UC_Search
Guest --> UC_Auth
Guest --> UC_Comment

Reader --> UC_Profile

Author --> UC_CreatePost
Author --> UC_EditSelf
Author --> UC_Publish

Admin --> UC_UserMgmt
Admin --> UC_CommentMod
Admin --> UC_ThemeMgmt
Admin --> UC_DBAdmin
Admin --> UC_ProxySSL

DevOps --> UC_MonHost
DevOps --> UC_MonDB
DevOps --> UC_MonNginx
DevOps --> UC_Dashboards
DevOps --> UC_Logs
DevOps --> UC_DockerLife

UC_Comment ..> UC_SecToken : <<include>>
UC_Auth ..> UC_SecToken : <<include>>
UC_CreatePost ..> UC_Media : <<extend>>
UC_CreatePost ..> UC_Taxonomy : <<include>>
UC_Publish ..> UC_CreatePost : <<include>>

UC_Dashboards ..> UC_MonHost : <<include>>
UC_Dashboards ..> UC_MonDB : <<include>>
UC_Dashboards ..> UC_MonNginx : <<include>>

legend right
  |<#E0F2FE>| Khách vãng lai & Độc giả thành viên (docgia_k23) |
  |<#FEF3C7>| Tác giả biên tập nội dung (tacgia_k23) |
  |<#FEE2E2>| Quản trị viên hệ thống (bount) |
  |<#F3E8FF>| Kỹ sư vận hành DevOps / SRE |
  |<#2563EB>| Quan hệ Kế thừa Actor: Guest -> Reader -> Author -> Admin |
endlegend
@enduml"""

def main():
    output_dir = "docs/architecture"
    os.makedirs(output_dir, exist_ok=True)
    
    puml_path = os.path.join(output_dir, "system_usecase_diagram.puml")
    with open(puml_path, "w", encoding="utf-8") as f:
        f.write(usecase_puml.strip())
    print(f"📄 Saved PUML: {puml_path}")
    
    png_path = os.path.join(output_dir, "system_usecase_diagram.png")
    render_plantuml(usecase_puml.strip(), png_path)
    
    artifact_dir = "/home/cyberbount/.gemini/antigravity/brain/de78f41e-e732-4572-9c45-484dc7900b08"
    if os.path.exists(artifact_dir):
        os.system(f"cp {png_path} {artifact_dir}/")
        print("✅ Copied rendered PNG to artifact directory!")

if __name__ == "__main__":
    main()

