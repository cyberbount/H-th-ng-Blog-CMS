from report_core import add_p, add_h1, add_h2, add_h3, add_callout, add_code_block, add_figure, add_styled_table

def render_chapter4(doc):
    add_h1(doc, "CHƯƠNG 4. XÂY DỰNG, TRIỂN KHAI VÀ QUẢN TRỊ HỆ THỐNG")
    
    add_h2(doc, "4.1 Sơ đồ Kiến trúc Tổng thể Hệ thống do Archify thiết kế")
    add_p(doc, "Để trực quan hóa một cách chính xác, chuẩn mực và thẩm mỹ toàn bộ cấu trúc phân tầng, các ranh giới an ninh cũng như luồng dữ liệu (Data Path) của 13 dịch vụ container, nhóm đã áp dụng kỹ năng Archify (Agent Skill chuyên biệt về kiến trúc trực quan) để thiết kế và xuất bản sơ đồ kiến trúc tổng thể của hệ thống LyxLab Blog CMS:")

    add_figure(doc, "docs/architecture/lyxlab-architecture.png", "Hình 4.1: Sơ đồ Kiến trúc Tổng thể Hệ thống Blog CMS do Archify thiết kế")

    add_p(doc, "Sơ đồ kiến trúc do Archify kết xuất phản ánh rõ ràng 3 luồng dữ liệu chính của hệ thống:")
    add_p(doc, "1. Luồng Nghiệp vụ Khách hàng (Client Request Path): Người dùng và quản trị viên gửi yêu cầu HTTPS cổng 443 tới Nginx Proxy Manager. Tại đây, Nginx xử lý giải mã TLS bằng chứng chỉ SSL SAN tự ký, áp dụng các tiêu đề Security Headers và chuyển tiếp yêu cầu HTTP vào mạng nội bộ `blog_frontend_net` tới WordPress CMS (cổng 8080) hoặc phpMyAdmin (cổng 8081). WordPress thực thi xử lý logic nghiệp vụ và kết nối truy vấn cơ sở dữ liệu MySQL 8.0 (cổng 3306) thông qua mạng cô lập `blog_backend_net`.")
    add_p(doc, "2. Luồng Giám sát Chuỗi thời gian (Metrics Observability Path): Cụm 5 Exporters liên tục đo lường trạng thái tài nguyên phần cứng máy chủ, container, cơ sở dữ liệu và máy chủ web. Định kỳ mỗi 15 giây, Prometheus Server gửi yêu cầu HTTP GET cào số liệu metrics qua mạng `blog_monitor_net`. Grafana kết nối trực tiếp vào Prometheus để thực thi các câu truy vấn PromQL và hiển thị lên 4 Dashboard trực quan.")
    add_p(doc, "3. Luồng Thu thập Nhật ký Tập trung (Centralized Logging Path): Promtail Agent được gắn kết trực tiếp vào Docker daemon socket (`/var/run/docker.sock`) và thư mục tệp tin nhật ký của Nginx (`/data/logs/`). Toàn bộ dòng log được tự động gắn nhãn (labeling) và đẩy về Grafana Loki 3.0 qua mạng `blog_logging_net`. Người quản trị sử dụng giao diện Grafana Explore để thực thi các câu truy vấn LogQL bóc tách sự cố thời gian thực.")

    add_h2(doc, "4.2 Thiết kế cấu trúc thư mục và Docker Compose Module hóa")
    add_p(doc, "Một sai lầm phổ biến khi triển khai hệ thống lớn trên Docker là dồn toàn bộ cấu hình của hàng chục dịch vụ vào một tệp `docker-compose.yml` duy nhất dài hàng trăm dòng, dẫn đến việc khó đọc, khó kiểm soát lỗi và xung đột khi nâng cấp. Dự án LyxLab áp dụng kiến trúc Module hóa (Modular Compose) theo chuẩn công nghiệp:")
    
    add_code_block(doc, """
/home/cyberbount/QTHT_K23A/DA_CUOIKHOA/
├── compose/
│   ├── docker-compose.app.yml          # Module 1: Ứng dụng lõi (WordPress, MySQL, phpMyAdmin, NPM)
│   ├── docker-compose.monitoring.yml   # Module 2: Giám sát (Prometheus, Grafana, 5 Exporters)
│   └── docker-compose.logging.yml      # Module 3: Thu thập Log (Loki, Promtail)
├── docker-compose.yml                  # Root Compose sử dụng include nạp cả 3 modules
├── custom-design/
│   ├── lyxlab-hero.php                 # Must-use plugin render Banner trạng thái hệ thống
│   └── lyxlab-modern-design.css        # Hệ thống Design System CSS hiện đại
├── monitoring/
│   ├── prometheus/prometheus.yml       # Cấu hình 5 scrape jobs của Prometheus
│   ├── mysqld-exporter/.my.cnf         # Credentials bảo mật của MySQL Exporter
│   └── grafana/provisioning/           # Tự động nạp sẵn Datasources & Dashboards
├── logging/
│   ├── loki-config.yaml                # Cấu hình lưu trữ chunks và retention của Loki
│   └── promtail-config.yaml            # Cấu hình cào Docker socket & Nginx logs
├── nginx/
│   ├── custom/stub_status.conf         # Endpoint metrics lưu lượng Nginx
│   └── ssl/                            # Chứng chỉ SSL SAN tự ký (crt + key)
├── .env.example                        # Mẫu tham số cấu hình môi trường
└── README.md                           # Báo cáo kỹ thuật chi tiết
    """)

    add_p(doc, "Mô hình mạng 4 phân vùng bridge network độc lập bảo đảm sự cách ly an ninh chặt chẽ giữa các tầng:")

    add_figure(doc, "docs/figures/fig4_2_network.png", "Hình 4.2: Mô hình phân vùng mạng 4 Bridge Network độc lập trong Docker Compose")

    add_p(doc, "Tại tệp cấu hình gốc `docker-compose.yml`, dự án tận dụng cú pháp `include:` hiện đại của Docker Compose v2 để nạp hợp nhất cả 3 module, đồng thời tập trung toàn bộ khai báo mạng và volume tại một nơi duy nhất, triệt tiêu hoàn toàn lỗi xung đột tài nguyên:")

    add_code_block(doc, """
# docker-compose.yml (Root Composition)
include:
  - compose/docker-compose.app.yml
  - compose/docker-compose.monitoring.yml
  - compose/docker-compose.logging.yml

networks:
  frontend_net:
    name: blog_frontend_net
    driver: bridge
  backend_net:
    name: blog_backend_net
    driver: bridge
  monitor_net:
    name: blog_monitor_net
    driver: bridge
  logging_net:
    name: blog_logging_net
    driver: bridge

volumes:
  mysql_data:
  wp_data:
  npm_data:
  npm_ssl:
  prometheus_data:
  grafana_data:
  loki_data:
    """)

    add_h2(doc, "4.3 Quản lý mã nguồn theo 3 mốc Git Commit nghiêm ngặt")
    add_p(doc, "Đáp ứng chính xác tiêu chí đánh giá số 2 của giảng viên Nguyễn Anh Chuyên, toàn bộ quá trình xây dựng hệ thống được quản lý chặt chẽ trên kho lưu trữ GitHub tại địa chỉ `https://github.com/cyberbount/H-th-ng-Blog-CMS.git`, phân chia thành đúng 3 mốc commit có ý nghĩa logic rõ rệt:")

    commit_data = [
        ["Mốc commit", "Mã Commit Hash", "Thông điệp Commit (Git Message)", "Nội dung kỹ thuật triển khai chi tiết"],
        ["Commit 1", "f12b685", "feat: initial project structure with WordPress, MySQL, phpMyAdmin and Nginx Reverse Proxy", "• Xây dựng cấu trúc thư mục module hóa `compose/docker-compose.app.yml`.\n• Triển khai WordPress (PHP 8.2), MySQL 8.0, phpMyAdmin.\n• Thiết lập Nginx Proxy Manager và cấu hình SSL tự ký chuẩn SAN."],
        ["Commit 2", "be9a13a", "feat: integrate Prometheus and Grafana for infrastructure and service monitoring", "• Triển khai module `compose/docker-compose.monitoring.yml`.\n• Cấu hình Prometheus TSDB cào metrics chu kỳ 15s.\n• Tích hợp cụm 5 Exporters: Node, cAdvisor, MySQL, Nginx, Docker Stats.\n• Tự động nạp sẵn Data Source Prometheus và 4 Dashboards trên Grafana."],
        ["Commit 3", "fee569c", "feat: integrate Loki and Promtail for centralized logging with LogQL and system hardening", "• Triển khai module `compose/docker-compose.logging.yml`.\n• Cấu hình Promtail cào Docker socket và Nginx access logs.\n• Tích hợp Grafana Loki 3.0 và nạp Data Source Loki trên Grafana.\n• Áp dụng Hardening: cờ no-new-privileges, giới hạn CPU/RAM, cô lập mạng."]
    ]
    add_styled_table(doc, commit_data[0], commit_data[1:], "Bảng 4.2: Tóm tắt 3 mốc Git Commit triển khai theo quy định của học phần")

    add_figure(doc, "/home/cyberbount/.gemini/antigravity/brain/de78f41e-e732-4572-9c45-484dc7900b08/.user_uploaded/media_1792726388596_848903c5.png", "Hình 4.3: Lịch sử quản lý mã nguồn Git tuân thủ nghiêm ngặt 3 mốc commit")

    add_h2(doc, "4.4 Triển khai Nginx Gateway, Tích hợp SSL SAN và Security Headers")
    add_p(doc, "Để đảm bảo kết nối HTTPS hoạt động trơn tru trong môi trường cục bộ (localhost) mà không bị trình duyệt từ chối kết nối, nhóm đã thực hiện quy trình sinh chứng chỉ SSL tự ký có Subject Alternative Name (SAN) bằng lệnh OpenSSL chuyên dụng:")

    add_code_block(doc, """
# Lệnh OpenSSL tạo chứng chỉ tự ký hỗ trợ SAN cho localhost và 127.0.0.1
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \\
  -keyout nginx/ssl/nginx-selfsigned.key \\
  -out nginx/ssl/nginx-selfsigned.crt \\
  -subj "/C=VN/ST=ThaiNguyen/L=ThaiNguyen/O=ICTU/OU=K23A/CN=localhost" \\
  -addext "subjectAltName=DNS:localhost,DNS:lyxlab.local,IP:127.0.0.1"
    """)

    add_p(doc, "Trên giao diện Nginx Proxy Manager (`http://localhost:81`), nhóm tạo một Proxy Host cho tên miền `localhost`, cấu hình chuyển tiếp tới máy chủ `wordpress` qua cổng nội bộ 8080, gắn tệp chứng chỉ SSL tự ký và kích hoạt các cờ bảo vệ: Block Common Exploits, Websockets Support, và HSTS.")

    add_figure(doc, "/home/cyberbount/.gemini/antigravity/brain/de78f41e-e732-4572-9c45-484dc7900b08/.user_uploaded/media_1792725379086_f52c0601.png", "Hình 4.4: Giao diện quản lý cổng Nginx Proxy Manager và cấu hình SSL tự ký")

    add_h2(doc, "4.5 Cấu hình hệ thống Giám sát Metrics (Prometheus + Grafana Dashboards)")
    add_p(doc, "Tệp cấu hình `monitoring/prometheus/prometheus.yml` được thiết kế để tự động thu thập số liệu từ toàn bộ 5 nhóm exporter với chu kỳ `scrape_interval: 15s`. Đoạn cấu hình các Job cốt lõi:")

    add_code_block(doc, """
# monitoring/prometheus/prometheus.yml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']

  - job_name: 'node-exporter'
    static_configs:
      - targets: ['node-exporter:9100']

  - job_name: 'cadvisor'
    static_configs:
      - targets: ['cadvisor:8080']

  - job_name: 'mysqld-exporter'
    static_configs:
      - targets: ['mysqld-exporter:9104']

  - job_name: 'nginx-exporter'
    static_configs:
      - targets: ['nginx-exporter:9113']

  - job_name: 'docker-stats'
    static_configs:
      - targets: ['docker-stats-exporter:9487']
    """)

    add_figure(doc, "docs/figures/fig4_5_monitoring.png", "Hình 4.5: Kiến trúc thu thập Metrics đa tầng với Prometheus TSDB và 5 Exporters")

    add_p(doc, "Nhằm tự động hóa 100% quá trình cài đặt mà không yêu cầu cấu hình thủ công qua giao diện chuột, Grafana được thiết lập cơ chế Provisioning tự động: Tệp `monitoring/grafana/provisioning/datasources/datasources.yml` tự động nạp sẵn Data Source Prometheus (`http://prometheus:9090`) và Data Source Loki (`http://loki:3100`). Đồng thời, thư mục `monitoring/grafana/provisioning/dashboards/` nạp sẵn 4 bộ Dashboard giám sát chuyên nghiệp.")

    add_h2(doc, "4.6 Cấu hình đường ống thu thập Log tập trung (Promtail + Loki + LogQL)")
    add_p(doc, "Đường ống thu thập nhật ký của Promtail (`logging/promtail-config.yaml`) được chia thành 2 luồng công việc chính:")
    add_p(doc, "1. Luồng Docker Socket: Promtail kết nối vào `/var/run/docker.sock`, lắng nghe sự kiện từ Docker Engine, tự động trích xuất thuộc tính `container_name` để gán nhãn `container` cho mỗi dòng log. Nhờ đó, người quản trị có thể truy vấn lọc riêng từng container bằng cú pháp `{container='blog-wordpress'}`.")
    add_p(doc, "2. Luồng Nginx Access Logs: Promtail theo dõi tệp nhật ký `/data/logs/*_*.log` do Nginx Proxy Manager xuất ra máy chủ host, gán nhãn `job='nginx'` phục vụ việc giám sát mã trạng thái phản hồi HTTP.")

    add_code_block(doc, """
# logging/promtail-config.yaml
server:
  http_listen_port: 9080
  grpc_listen_port: 0

positions:
  filename: /tmp/positions.yaml

clients:
  - url: http://loki:3100/loki/api/v1/push

scrape_configs:
  - job_name: docker-containers
    docker_sd_configs:
      - host: unix:///var/run/docker.sock
        refresh_interval: 5s
    relabel_configs:
      - source_labels: ['__meta_docker_container_name']
        regex: '/(.*)'
        target_label: 'container'

  - job_name: nginx-logs
    static_configs:
      - targets: ['localhost']
        labels:
          job: nginx
          __path__: /data/logs/*_*.log
    """)

    add_figure(doc, "docs/figures/fig4_6_logging.png", "Hình 4.6: Đường ống thu thập nhật ký tập trung Promtail cào Docker Socket đẩy về Loki")

    add_h2(doc, "4.7 Thực thi các biện pháp Bảo mật Hardening thực tế")
    add_p(doc, "Tuân thủ nghiêm ngặt các nguyên tắc an toàn thông tin, hệ thống đã cấu hình giới hạn tài nguyên trần trong `compose/docker-compose.app.yml`:")

    hardening_data = [
        ["Tên dịch vụ container", "Giới hạn CPU (cpus)", "Trần bộ nhớ (memory limit)", "Bộ nhớ dự phòng (reservation)", "Cờ leo thang đặc quyền"],
        ["blog-mysql", "1.0 Core", "1024 MB (1.0 GB)", "256 MB", "no-new-privileges: true"],
        ["blog-wordpress", "1.0 Core", "512 MB", "128 MB", "no-new-privileges: true"],
        ["blog-phpmyadmin", "0.5 Core", "256 MB", "64 MB", "no-new-privileges: true"],
        ["blog-npm", "1.0 Core", "512 MB", "128 MB", "no-new-privileges: true"],
        ["blog-prometheus", "0.8 Core", "512 MB", "128 MB", "no-new-privileges: true"],
        ["blog-loki", "0.8 Core", "512 MB", "128 MB", "no-new-privileges: true"]
    ]
    add_styled_table(doc, hardening_data[0], hardening_data[1:], "Bảng 4.3: Các tham số cấu hình Giới hạn tài nguyên phần cứng (Resource Limits)")

    add_h2(doc, "4.8 Quy trình vận hành, bảo trì, kiểm tra sức khỏe và sao lưu dữ liệu")
    add_p(doc, "Hệ thống cung cấp quy trình vận hành 1-click chuẩn mực, hỗ trợ kiểm tra sức khỏe và bảo trì định kỳ:")
    add_p(doc, "• Lệnh khởi động toàn bộ cụm 13 containers trong chế độ nền:")
    add_code_block(doc, "docker compose up -d")
    add_p(doc, "• Lệnh kiểm tra trạng thái sống và các cổng mở:")
    add_code_block(doc, "docker compose ps")
    add_p(doc, "• Lệnh kiểm tra tính toàn vẹn của kết nối HTTPS nội bộ:")
    add_code_block(doc, "curl -k -I https://localhost/")
    add_p(doc, "• Quy trình sao lưu cơ sở dữ liệu MySQL định kỳ không làm gián đoạn hệ thống:")
    add_code_block(doc, "docker exec blog-mysql mysqldump -u wp_user -p'WP_SecurePassword2026!' wordpress_db > backup_$(date +%Y%m%d).sql")

    print("Chapter 4 completed.")
