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
    print(f"Fetching Login Session Sequence from PlantUML server ({len(puml_code)} chars)...")
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

seq_auth = r"""@startuml
!theme plain
skinparam defaultFontName "Segoe UI"
skinparam defaultFontSize 11
skinparam roundcorner 6
skinparam shadowing true
skinparam responseMessageBelowArrow true
autonumber "<b>[00]</b>"

title **BIỂU ĐỒ TUẦN TỰ LUỒNG ĐĂNG NHẬP VÀ XÁC THỰC PHIÊN (AUTHENTICATION & SESSION FLOW)**

actor "Người dùng\n(bount / tacgia_k23)" as User #E0F2FE
participant "Trình duyệt Web\n(Browser & Cookie Jar)" as Client #BAE6FD
participant "blog-npm\n(Nginx Gateway :443)" as NPM #93C5FD
participant "blog-wordpress\n(PHP 8.2 / WP Core)" as WP #DBEAFE
database "blog-mysql\n(MySQL 8.0 InnoDB)" as DB #FED7AA
participant "blog-promtail\n(Log Shipper)" as Promtail #D1FAE5

== GIAI ĐOẠN 1: TẢI TRANG ĐĂNG NHẬP VÀ KHỞI TẠO TEST COOKIE ==

User -> Client : Mở đường dẫn https://localhost/wp-login.php
activate Client
Client -> NPM : HTTPS GET /wp-login.php (TLS 1.3)
activate NPM
NPM -> WP : Reverse Proxy HTTP GET :80 (mạng blog_frontend_net)
activate WP
WP -> WP : Sinh Cryptographic Nonce bảo vệ Form đăng nhập\nThiết lập wordpress_test_cookie=WP+Cookie+check
WP --> NPM : HTTP 200 OK (Set-Cookie: wordpress_test_cookie)
deactivate WP
NPM --> Client : Trả về HTML Form đăng nhập & Lưu test cookie
deactivate NPM
Client --> User : Hiển thị Form: Tên đăng nhập & Mật khẩu
deactivate Client

== GIAI ĐOẠN 2: GỬI THÔNG TIN VÀ XÁC THỰC MẬT KHẨU (PHPASS HMAC) ==

User -> Client : Nhập Username + Mật khẩu + Nhấn "Đăng nhập"
activate Client
Client -> NPM : HTTPS POST /wp-login.php\n[Payload: log=tacgia_k23&pwd=***&_wpnonce=...]
activate NPM
NPM -> NPM : Kiểm tra WAF (block-exploits.conf)\nLọc các chuỗi SQLi & XSS
NPM -> WP : Chuyển tiếp HTTP POST :80\nkèm header X-Forwarded-For, X-Forwarded-Proto
activate WP

WP -> WP : Kiểm tra hợp lệ Nonce & Test Cookie
WP -> DB : SELECT * FROM wp_users WHERE user_login = 'tacgia_k23'\n(Prepared Statements trên mạng blog_backend_net)
activate DB
DB --> WP : Trả về bản ghi user (ID, user_login, hash user_pass)
deactivate DB

alt Trường hợp 1: Mật khẩu chính xác (Login Success)
    WP -> WP : Xác thực mật mã: wp_check_password()\n(Giải thuật Portable PHP Password Hash / Salted MD5)
    WP -> DB : SELECT meta_key, meta_value FROM wp_usermeta\nWHERE user_id = 2 AND meta_key IN ('wp_capabilities', 'session_tokens')
    activate DB
    DB --> WP : Trả về Quyền hạn: {"author": true} & Session Token list
    deactivate DB
    
    WP -> WP : Sinh Session Verifier & Token bí mật\nKý HMAC với LOGGED_IN_KEY & SECURE_AUTH_KEY\nTạo Cookie: wordpress_logged_in_[hash] & wordpress_sec_[hash]\n(Thiết lập cờ: HttpOnly, Secure, SameSite=Lax)
    
    WP -> DB : UPDATE wp_usermeta SET meta_value = [new_session_token]\nWHERE user_id = 2 AND meta_key = 'session_tokens'
    activate DB
    DB --> WP : Cập nhật token thành công
    deactivate DB
    
    WP --> NPM : HTTP 302 Found\nSet-Cookie: wordpress_logged_in_...; HttpOnly; SameSite=Lax\nSet-Cookie: wordpress_sec_...; HttpOnly; Secure\nLocation: /wp-admin/
    deactivate WP
    
    NPM -> Promtail : Ghi log đăng nhập thành công 302 (/data/logs/*_access.log)
    NPM --> Client : HTTP 302 Redirect về /wp-admin/
    deactivate NPM
    
    Client -> Client : Lưu Cookie phiên vào Cookie Jar của Trình duyệt\n(Phạm vi: Domain localhost, áp dụng cho toàn bộ các Tab)

else Trường hợp 2: Sai mật khẩu hoặc Tên đăng nhập không tồn tại (Login Failure)
    WP -> WP : wp_check_password() trả về FALSE
    WP -> Promtail : Ghi log cảnh báo đăng nhập thất bại (IP, Username)
    WP --> NPM : HTTP 200 OK (Nạp thông báo lỗi: Invalid credentials)
    NPM --> Client : Trả về trang đăng nhập kèm cảnh báo lỗi
    Client --> User : Hiển thị: "LỖI: Mật khẩu bạn nhập cho tên người dùng không chính xác."
end

== GIAI ĐOẠN 3: XÁC THỰC PHIÊN VÀ KIỂM TRA PHÂN QUYỀN TRÊN MỖI YÊU CẦU ==

Client -> NPM : HTTPS GET /wp-admin/post-new.php\nCookie: wordpress_logged_in_[hash]=tacgia_k23|expiration|token|hmac
activate Client
activate NPM
NPM -> WP : Reverse Proxy HTTP GET :80 kèm Cookie xác thực
activate WP

WP -> WP : Phân tích Cookie (wp_parse_auth_cookie)\nTính toán lại HMAC dựa trên AUTH_SALT & SECURE_AUTH_SALT
WP -> WP : So sánh mã băm bằng hàm an toàn hash_equals()\nKiểm tra thời hạn hết hạn (Expiration Time)
WP -> DB : SELECT meta_value FROM wp_usermeta\nWHERE user_id = 2 AND meta_key = 'session_tokens'
activate DB
DB --> WP : Khớp Session Verifier trong CSDL
deactivate DB

WP -> WP : Thiết lập phiên làm việc toàn cục (wp_set_current_user)\nKiểm tra phân quyền: current_user_can('edit_posts') -> TRUE\nSinh Cryptographic Nonce cho phiên soạn thảo
WP --> NPM : HTTP 200 OK (Giao diện Quản trị / Trình soạn thảo Gutenberg)
deactivate WP
NPM --> Client : Trả về mã HTML Bảng điều khiển tác giả
deactivate NPM
Client --> User : Hiển thị Trang Quản trị Tác giả LyxLab
deactivate Client

@enduml"""

def main():
    output_dir = "docs/architecture"
    os.makedirs(output_dir, exist_ok=True)
    
    puml_path = os.path.join(output_dir, "login_session_sequence.puml")
    with open(puml_path, "w", encoding="utf-8") as f:
        f.write(seq_auth.strip())
    print(f"📄 Saved PUML: {puml_path}")
    
    png_path = os.path.join(output_dir, "login_session_sequence.png")
    render_plantuml(seq_auth.strip(), png_path)
    
    artifact_dir = "/home/cyberbount/.gemini/antigravity/brain/de78f41e-e732-4572-9c45-484dc7900b08"
    if os.path.exists(artifact_dir):
        os.system(f"cp {png_path} {artifact_dir}/")
        print("✅ Copied rendered PNG to artifact directory!")

if __name__ == "__main__":
    main()

