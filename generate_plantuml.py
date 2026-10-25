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
# 1. SƠ ĐỒ TRIỂN KHAI VÀ ĐIỀU PHỐI KIẾN TRÚC HỆ THỐNG (DEPLOYMENT DIAGRAM)
# ==============================================================================
deployment_puml = r"""@startuml
!theme plain
skinparam defaultFontName "Segoe UI"
skinparam defaultFontSize 11
skinparam roundcorner 8
skinparam shadowing true
skinparam linetype ortho
skinparam packageStyle rectangle
skinparam componentStyle rectangle

skinparam node {
    BackgroundColor #F8FAFC
    BorderColor #1E293B
    FontColor #0F172A
    FontStyle bold
}

skinparam package {
    BackgroundColor #FFFFFF
    BorderColor #64748B
    FontColor #0F172A
    FontStyle bold
}

skinparam database {
    BackgroundColor #FFF7ED
    BorderColor #EA580C
    FontColor #9A3412
}

title **SƠ ĐỒ TRIỂN KHAI VÀ ĐIỀU PHỐI KIẾN TRÚC HỆ THỐNG BLOG CMS LYXLAB (13 CONTAINERS)**

actor "Quản trị viên (Admin)\n[User: bount]" as Admin #Fee2e2
actor "Tác giả (Author)\n[User: tacgia_k23]" as Author #Fef3c7
actor "Độc giả & Khách\n[docgia_k23 / Guest]" as Reader #E0f2fe
actor "Kỹ sư DevOps / SRE" as DevOps #F3e8ff

node "Máy chủ Vật lý Host OS: Windows 11 WSL2 / Ubuntu 24.04 LTS\n[Docker Engine v27.0.3 | Docker Compose v2.28.1]" as Host {

    package "blog_frontend_net (172.28.10.0/24) — Vùng đệm Ingress" as NetFrontend #F0F9FF {
        component "blog-npm\n<<jc21/nginx-proxy-manager>>\n--\n• Port 80/443 (Public Proxy)\n• Port 81 (Admin Dashboard)\n• SSL SAN Terminate (TLS 1.3)\n• WAF: block-exploits.conf\n• RAM Limit: 512MB" as NPM #E0F2FE
        component "blog-wordpress\n<<wordpress:6.7.1-php8.2-apache>>\n--\n• Port 8080:80 (Nội bộ :80)\n• Theme Astra + Design System\n• Plugin lyxlab-hero.php\n• Nonce & Cookie Auth\n• RAM Limit: 512MB" as WP #DBEAFE
        component "blog-phpmyadmin\n<<phpmyadmin:latest>>\n--\n• Port 8081:80 (Nội bộ :80)\n• GUI Database Inspection\n• User: wp_user\n• RAM Limit: 256MB" as PMA #FEF3C7
        component "blog-nginx-exporter\n<<nginx/nginx-prometheus-exporter>>\n--\n• Port 9113/metrics\n• Scrapes stub_status" as NGX_EXP #BAE6FD
    }

    package "blog_backend_net (172.28.20.0/24) — Vùng CSDL Cô Lập" as NetBackend #FFF7ED {
        database "blog-mysql\n<<mysql:8.0>>\n--\n• Port 3308:3306 (Nội bộ :3306)\n• InnoDB Buffer Pool\n• Charset: utf8mb4\n• Database: wordpress_db\n• User: wp_user (Least Privilege)\n• CẤM TRUY CẬP TỪ NPM\n• RAM Limit: 1024MB" as DB #FFEDD5
        component "blog-mysqld-exporter\n<<prom/mysqld-exporter:v0.15.1>>\n--\n• Port 9104/metrics\n• Credentials: .my.cnf\n• Đo Queries/s, InnoDB Threads" as DB_EXP #FED7AA
    }

    package "blog_monitor_net (172.28.30.0/24) — Kênh Giám Sát Metrics" as NetMonitor #FAF5FF {
        component "blog-prometheus\n<<prom/prometheus:v2.51.0>>\n--\n• Port 9090:9090\n• PULL Engine (Interval: 15s)\n• 100% Targets UP (5 Exporters)\n• PromQL Evaluation\n• RAM Limit: 512MB" as PROM #EDE9FE
        component "blog-grafana\n<<grafana/grafana:10.4.1>>\n--\n• Port 3000:3000\n• 4 Dashboards Tự Động\n• Nạp sẵn Datasource Prom & Loki\n• RAM Limit: 512MB" as GRAF #FCE7F3
        component "blog-node-exporter\n<<prom/node-exporter:v1.7.0>>\n--\n• Port 9100/metrics\n• CPU, RAM, Disk, Net Host OS" as NODE_EXP #F3E8FF
        component "blog-cadvisor\n<<gcr.io/cadvisor:v0.49.1>>\n--\n• Port 8080 (Nội bộ)\n• Đo CPU/RAM 13 Containers" as CADV #F3E8FF
        component "blog-docker-stats-exporter\n<<wyreve/docker-stats-exporter>>\n--\n• Port 9487/metrics\n• Sống/chết & Net I/O Containers" as DOCKER_EXP #F3E8FF
    }

    package "blog_logging_net (172.28.40.0/24) — Kênh Nhật Ký Loki" as NetLogging #ECFDF5 {
        component "blog-promtail\n<<grafana/promtail:3.0.0>>\n--\n• Port 9080\n• Socket: /var/run/docker.sock:ro\n• Log File: /data/logs/*_*.log\n• Tự động gắn nhãn (relabel)\n• PUSH Batch về Loki" as PROMTAIL #D1FAE5
        component "blog-loki\n<<grafana/loki:3.0.0>>\n--\n• Port 3100:3100\n• Đánh chỉ mục Nhãn (Labels)\n• Nén Chunks Snappy (Tiết kiệm 90% RAM)\n• LogQL Query Engine\n• RAM Limit: 512MB" as LOKI #A7F3D0
    }

    storage "TẦNG LƯU TRỮ BỀN VỮNG (7 DOCKER NAMED VOLUMES)" as Storage #FFFBEB {
        [mysql_data]
        [wp_data]
        [npm_data & npm_ssl]
        [prometheus_data]
        [grafana_data]
        [loki_data]
    }
}

Admin --> NPM : HTTPS :443 / Cấu hình :81
Author --> NPM : HTTPS :443 (Viết bài)
Reader --> NPM : HTTPS :443 (Đọc & Bình luận)

NPM --> WP : [HTTP:80] Reverse Proxy\n(frontend_net)
NPM ..> PMA : [HTTP:8081] Proxy Host
WP --> DB : [TCP:3306] Prepared Statements\n(backend_net)
PMA --> DB : [TCP:3306] Thao tác CSDL

DB ..> mysql_data : Ghi dữ liệu CSDL
WP ..> wp_data : Ghi ảnh Media
NPM ..> [npm_data & npm_ssl] : Ghi SSL Certs
PROM ..> prometheus_data : Ghi TSDB
GRAF ..> grafana_data : Ghi Dashboard cache
LOKI ..> loki_data : Ghi Chunks

PROM --> NODE_EXP : PULL :9100 (15s)
PROM --> CADV : PULL :8080 (15s)
PROM --> DOCKER_EXP : PULL :9487 (15s)
PROM --> NGX_EXP : PULL :9113 (15s)
PROM --> DB_EXP : PULL :9104 (15s)
GRAF --> PROM : PromQL Query :9090
DevOps --> GRAF : HTTP :3000 (Xem 4 Dashboards)

WP ..> PROMTAIL : stdout/stderr
NPM ..> PROMTAIL : /data/logs
PROMTAIL --> LOKI : PUSH Batch HTTP :3100\n(logging_net)
GRAF --> LOKI : LogQL Query :3100\n(Explore UI)

legend right
  |<#2563eb>| Luồng 1: Nghiệp vụ Web (HTTPS -> Nginx -> WordPress -> MySQL) |
  |<#7c3aed>| Luồng 2: Giám sát Đo lường (5 Exporters -> Prometheus -> Grafana) |
  |<#059669>| Luồng 3: Quản trị Nhật ký (Docker Socket -> Promtail -> Loki) |
  |<#ea580c>| Hardening: no-new-privileges, Cô lập mạng, Giới hạn CPU/RAM |
endlegend
@enduml"""

# ==============================================================================
# 2. SƠ ĐỒ TUẦN TỰ LUỒNG DỮ LIỆU END-TO-END (SEQUENCE FLOW DIAGRAM)
# ==============================================================================
sequence_puml = r"""@startuml
!theme plain
skinparam defaultFontName "Segoe UI"
skinparam defaultFontSize 11
skinparam roundcorner 6
skinparam shadowing true
autonumber "<b>[00]</b>"

title **BIỂU ĐỒ TUẦN TỰ LUỒNG DỮ LIỆU END-TO-END HỆ THỐNG BLOG CMS LYXLAB**

actor "Client / User\n(Trình duyệt)" as Client #E0F2FE
participant "blog-npm\n(Nginx Gateway :443)" as NPM #BAE6FD
participant "blog-wordpress\n(PHP 8.2 / Apache :80)" as WP #DBEAFE
database "blog-mysql\n(MySQL 8.0 :3306)" as DB #FFEDD5
database "Named Volume\n(mysql_data)" as Disk #FFFBEB
participant "5 Exporters\n(Node, cAdvisor, MySQL...)" as Exporters #F3E8FF
participant "blog-prometheus\n(TSDB Server :9090)" as Prom #EDE9FE
participant "blog-promtail\n(Log Shipper :9080)" as Promtail #D1FAE5
participant "blog-loki\n(Log Engine :3100)" as Loki #A7F3D0
participant "blog-grafana\n(Visual Dashboards :3000)" as Grafana #FCE7F3
actor "DevOps / SRE\n(Kỹ sư vận hành)" as DevOps #F3E8FF

== LUỒNG 1: NGHIỆP VỤ WEB, XÁC THỰC PHÂN QUYỀN & TRUY VẤN CSDL ==

Client -> NPM : HTTPS POST /wp-login.php (TLS 1.3 SAN)
activate NPM
NPM -> NPM : Kiểm tra WAF (block-exploits.conf) & Giải mã SSL
NPM -> WP : Reverse Proxy HTTP:80 qua mạng blog_frontend_net
activate WP
WP -> WP : Xác thực mật mã HMAC-MD5 (phpass salt)
WP -> DB : SELECT * FROM wp_users WHERE user_login = 'tacgia_k23'\n(Prepared Statements qua mạng blog_backend_net)
activate DB
DB --> WP : Trả về bản ghi user & hash user_pass
deactivate DB
WP -> WP : Sinh Cryptographic Nonce & Auth Cookie (HttpOnly, SameSite=Lax)
WP --> NPM : HTTP 302 Found (Set-Cookie: wordpress_logged_in_*)
deactivate WP
NPM --> Client : Chuyển hướng tới /wp-admin/
deactivate NPM

Client -> NPM : HTTPS POST /wp-json/wp/v2/posts (Tác giả đăng bài viết mới)
activate NPM
NPM -> WP : Chuyển tiếp yêu cầu ghi bài viết
activate WP
WP -> DB : START TRANSACTION\nINSERT INTO wp_posts (post_title, post_content, post_status='publish')
activate DB
DB -> Disk : Đồng bộ bản ghi xuống tệp InnoDB tablespace trên named volume mysql_data
DB --> WP : COMMIT TRANSACTION (Trả về new post ID)
deactivate DB
WP --> NPM : HTTP 201 Created (Bài viết đã xuất bản)
deactivate WP
NPM --> Client : Hiển thị bài viết trực tiếp trên trang chủ LyxLab
deactivate NPM

== LUỒNG 2: GIÁM SÁT CHUỖI THỜI GIAN (PROMETHEUS PULL MODEL 15S) ==

loop Định kỳ mỗi scrape_interval = 15 giây
    Prom -> Exporters : HTTP GET /metrics qua mạng blog_monitor_net
    activate Prom
    activate Exporters
    Exporters --> Prom : Trả về text metrics (CPU, RAM, Queries/s, Active Connections)
    deactivate Exporters
    Prom -> Prom : Nén khối dữ liệu thời gian (Gorilla Compression)
    Prom -> Disk : Ghi dữ liệu vào named volume prometheus_data
    deactivate Prom
end

DevOps -> Grafana : Truy cập giao diện giám sát http://localhost:3000
activate Grafana
Grafana -> Prom : Thực thi truy vấn PromQL: mysql_up == 1, rate(http_requests_total[5m])
activate Prom
Prom --> Grafana : Trả về chuỗi dữ liệu ma trận (Time-series Matrix)
deactivate Prom
Grafana --> DevOps : Trực quan hóa lên 4 Dashboards (Host, Containers, MySQL, Nginx)
deactivate Grafana

== LUỒNG 3: QUẢN TRỊ VÀ TRUY VẾT NHẬT KÝ TẬP TRUNG (LOKI PUSH MODEL) ==

WP -> Promtail : Xả nhật ký Apache & PHP ra stdout/stderr
activate Promtail
NPM -> Promtail : Ghi tệp nhật ký truy cập vào /data/logs/*_*.log
Promtail -> Promtail : Đọc socket /var/run/docker.sock:ro\nTự động gắn nhãn container="blog-wordpress", job="nginx"
Promtail -> Loki : PUSH Batch bản ghi qua HTTP:3100 (blog_logging_net)
activate Loki
deactivate Promtail
Loki -> Loki : Đánh chỉ mục Nhãn (Labels) vào TSDB, nén nội dung log (Snappy Chunks)
Loki -> Disk : Lưu trữ khối nén vào named volume loki_data
deactivate Loki

DevOps -> Grafana : Mở giao diện Grafana Explore (chọn Data Source: Loki)
activate Grafana
Grafana -> Loki : Thực thi truy vấn LogQL: {container="blog-npm"} |~ "HTTP/[0-9.]+ 404"
activate Loki
Loki --> Grafana : Trả về dòng log chứa mã lỗi HTTP 404 thời gian thực
deactivate Loki
Grafana --> DevOps : Hiển thị bảng Live Tail & Biểu đồ tốc độ phát sinh Log (Rate)
deactivate Grafana

@enduml"""

def main():
    output_dir = "docs/architecture"
    os.makedirs(output_dir, exist_ok=True)
    
    # Save PUML files
    puml_deploy_path = os.path.join(output_dir, "system_architecture_deployment.puml")
    with open(puml_deploy_path, "w", encoding="utf-8") as f:
        f.write(deployment_puml.strip())
    print(f"📄 Saved PlantUML: {puml_deploy_path}")
    
    puml_seq_path = os.path.join(output_dir, "system_end_to_end_sequence.puml")
    with open(puml_seq_path, "w", encoding="utf-8") as f:
        f.write(sequence_puml.strip())
    print(f"📄 Saved PlantUML: {puml_seq_path}")
    
    # Render PNGs via PlantUML Server
    png_deploy_path = os.path.join(output_dir, "system_architecture_deployment.png")
    render_plantuml(deployment_puml.strip(), png_deploy_path)
    
    png_seq_path = os.path.join(output_dir, "system_end_to_end_sequence.png")
    render_plantuml(sequence_puml.strip(), png_seq_path)

    # Copy to artifact folder for direct inline viewing
    artifact_dir = "/home/cyberbount/.gemini/antigravity/brain/de78f41e-e732-4572-9c45-484dc7900b08"
    if os.path.exists(artifact_dir):
        os.system(f"cp {png_deploy_path} {artifact_dir}/")
        os.system(f"cp {png_seq_path} {artifact_dir}/")
        print("✅ Copied rendered PNGs to artifact directory!")

if __name__ == "__main__":
    main()

