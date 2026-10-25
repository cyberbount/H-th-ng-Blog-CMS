from docx.shared import Pt, Inches, RGBColor
from report_core import add_p, add_h1, add_h2, add_h3, add_callout, add_code_block, add_figure, add_styled_table, set_font

def render_conclusions_and_appendices(doc):
    add_h1(doc, "KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN")
    
    add_h2(doc, "1. Kết quả đạt được")
    add_p(doc, "Sau thời gian nghiên cứu lý thuyết, thiết kế hệ thống và tiến hành triển khai thực nghiệm nghiêm túc, đề tài 'Xây dựng, Triển khai và Quản trị Hệ thống Blog CMS' mang tên LyxLab đã hoàn thành xuất sắc toàn bộ các mục tiêu đề ra:")
    add_p(doc, "1. Về mặt Hạ tầng Ảo hóa (Containerization): Đóng gói và điều phối thành công 13 dịch vụ container độc lập trên nền tảng Docker Compose v2. Cấu trúc mã nguồn được phân rã thành các module chuyên trách (`app.yml`, `monitoring.yml`, `logging.yml`), giúp việc quản lý, mở rộng và bảo trì trở nên vô cùng thuận tiện.")
    add_p(doc, "2. Về mặt Nghiệp vụ Blog CMS: Thiết lập hoàn chỉnh cổng thông tin LyxLab với giao diện tiếng Việt hiện đại, tối ưu trải nghiệm người dùng với theme Astra và Design System tokens. Hệ thống đã xuất bản 8 bài viết kỹ thuật phân bố trên 4 chuyên mục công nghệ, thực thi luồng tương tác bình luận lồng nhau đa cấp và phân quyền 3 vai trò người dùng (Admin, Author, Subscriber) rành mạch.")
    add_p(doc, "3. Về mặt Định tuyến và An ninh mạng (Ingress & Security): Triển khai cổng Nginx Proxy Manager làm Gateway duy nhất, bảo vệ hệ thống bằng chứng chỉ số SSL tự ký hỗ trợ Subject Alternative Name (SAN), áp dụng các tiêu đề HTTP Security Headers và phân vùng 4 mạng bridge biệt lập để cô lập an toàn cơ sở dữ liệu MySQL.")
    add_p(doc, "4. Về mặt Giám sát và Đo lường (Observability): Xây dựng hệ sinh thái giám sát tự động với Prometheus TSDB và cụm 5 Exporters với 100% mục tiêu đạt trạng thái UP. Vận hành 7 bộ Dashboard tiêu chuẩn công nghiệp trên Grafana (1 dashboard nạp tự động qua Provisioning và 6 dashboard import từ thư viện Grafana Labs) để theo dõi tải phần cứng máy chủ, container, cơ sở dữ liệu và proxy.")
    add_p(doc, "5. Về mặt Quản lý Nhật ký tập trung (Centralized Logging): Tích hợp thành công Promtail cào log Docker socket và Nginx đẩy về Loki 3.0, hỗ trợ truy vấn LogQL thời gian thực để phát hiện sớm các mã lỗi HTTP 4xx/5xx.")
    add_p(doc, "6. Về mặt Quản lý Dự án: Tuân thủ nghiêm ngặt quy định quản lý mã nguồn trên kho lưu trữ GitHub với 3 mốc commit có ý nghĩa phản ánh đúng tiến trình xây dựng (Core ➔ Monitoring ➔ Logging) kèm 1 commit tài liệu, và hệ thống tài liệu kỹ thuật README.md chi tiết 11 mục.")

    add_h2(doc, "2. Bài học kinh nghiệm rút ra")
    add_p(doc, "Quá trình thực hiện đề tài đã trang bị cho sinh viên những bài học thực tiễn vô cùng sâu sắc:")
    add_p(doc, "• Bài học về tư duy phân tầng: Hiểu rõ việc tách rời giữa tầng logic ứng dụng (Stateless App) và tầng lưu trữ dữ liệu (Stateful DB) là chìa khóa để hệ thống có thể mở rộng quy mô (Horizontal Scaling) và bảo đảm an toàn dữ liệu.")
    add_p(doc, "• Bài học về an toàn container: Nhận thức rõ ràng việc chạy container với quyền root mặc định là một lỗ hổng nghiêm trọng; các cờ bảo vệ như `no-new-privileges` và phân vùng mạng nội bộ là những thực hành bắt buộc phải có trong môi trường thực tế.")
    add_p(doc, "• Bài học về khả năng quan sát (Observability): Hiểu được rằng hệ thống chỉ thực sự ổn định khi người quản trị có khả năng đo lường (Metrics) và truy vết (Logs) mọi hành vi của ứng dụng, chuyển từ thế bị động ứng phó sự cố sang thế chủ động phòng ngừa rủi ro.")

    add_h2(doc, "3. Hạn chế hiện tại và Hướng phát triển")
    add_p(doc, "• Hạn chế hiện tại: Do giới hạn phần cứng máy tính cá nhân trong phạm vi học phần, hệ thống mới được thử nghiệm trên môi trường máy chủ đơn (Single Host Docker). Chưa tích hợp kênh gửi cảnh báo tự động (Alerting) tới điện thoại hoặc ứng dụng OTT khi có sự cố.")
    add_p(doc, "• Hướng phát triển trong tương lai:")
    add_p(doc, "  - Mở rộng hạ tầng từ Docker Compose lên cụm điều phối phân tán Kubernetes (K8s) hoặc Docker Swarm.")
    add_p(doc, "  - Tích hợp Prometheus Alertmanager để gửi thông báo cảnh báo khẩn cấp tức thì (Alerting Rules) qua kênh Telegram Bot hoặc Discord Webhook khi CPU máy chủ vượt ngưỡng 85% hoặc MySQL bị ngắt kết nối.")
    add_p(doc, "  - Xây dựng đường ống tự động hóa CI/CD (Continuous Integration / Continuous Deployment) bằng GitHub Actions để tự động kiểm thử mã nguồn, quét lỗ hổng bảo mật và tự động triển khai (Auto-deploy) lên máy chủ mỗi khi có commit mới.")

    add_h1(doc, "TÀI LIỆU THAM KHẢO CHÍNH THỨC")
    refs = [
        "[1] Bộ môn Công nghệ Phần mềm – Khoa Công nghệ Thông tin, Trường Đại học Công nghệ Thông tin và Truyền thông (ICTU), Đề cương và Tiêu chí đánh giá học phần Triển khai và Quản trị Hệ thống Phần mềm (K23), 2026.",
        "[2] Nguyễn Anh Chuyên, Bài giảng và Hướng dẫn thực hành Triển khai và Quản trị Hệ thống Phần mềm, ICTU, 2026.",
        "[3] Docker Inc., Docker Engine and Docker Compose v2 Official Documentation, https://docs.docker.com/, Truy cập năm 2026.",
        "[4] The Linux Foundation / CNCF, Prometheus: From Metrics to Insight, https://prometheus.io/docs/, Truy cập năm 2026.",
        "[5] Grafana Labs, Grafana Documentation: Visualizations, Dashboards and Provisioning, https://grafana.com/docs/grafana/latest/, Truy cập năm 2026.",
        "[6] Grafana Labs, Grafana Loki: Like Prometheus, but for logs, https://grafana.com/docs/loki/latest/, Truy cập năm 2026.",
        "[7] Oracle Corporation, MySQL 8.0 Reference Manual: InnoDB Storage Engine & Performance Schema, https://dev.mysql.com/doc/refman/8.0/en/, Truy cập năm 2026.",
        "[8] Nginx Inc. / F5, NGINX Reverse Proxy and HTTP Load Balancing Administration Guide, https://docs.nginx.com/, Truy cập năm 2026.",
        "[9] WordPress Foundation, WordPress Developer Resources: Core Architecture, APIs and Security Best Practices, https://developer.wordpress.org/, Truy cập năm 2026.",
        "[10] OpenSSL Project, OpenSSL Cryptography and SSL/TLS Toolkit Documentation: Subject Alternative Name (SAN), https://www.openssl.org/docs/, Truy cập năm 2026."
    ]
    for r_item in refs:
        p = doc.add_paragraph()
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.space_after = Pt(4)
        r = p.add_run(r_item)
        set_font(r, "Times New Roman", 11, RGBColor(30, 41, 59))

    add_h1(doc, "PHỤ LỤC")
    
    add_h2(doc, "Phụ lục A: Hướng dẫn cài đặt và Khởi chạy 1-Click Hệ thống")
    add_p(doc, "Người chấm bài hoặc kỹ sư vận hành có thể tái lập toàn bộ môi trường LyxLab chỉ với 4 câu lệnh dòng lệnh chuẩn xác:")
    add_code_block(doc, """
# Bước 1: Sao chép kho mã nguồn chính thức từ GitHub
git clone https://github.com/cyberbount/H-th-ng-Blog-CMS.git
cd H-th-ng-Blog-CMS

# Bước 2: Thiết lập tệp cấu hình biến môi trường từ mẫu an toàn
cp .env.example .env

# Bước 3: Khởi chạy đồng bộ toàn bộ 13 containers trong chế độ nền
docker compose up -d

# Bước 4: Kiểm tra trạng thái hoạt động của toàn bộ dịch vụ
docker compose ps
    """)

    add_h2(doc, "Phụ lục B: Bảng Tra cứu Cổng Dịch vụ và Thông tin Tài khoản")
    access_data = [
        ["Tên Dịch vụ", "Địa chỉ URL truy cập", "Tài khoản / Mật khẩu mặc định", "Vai trò & Chức năng"],
        ["LyxLab Blog CMS", "https://localhost (Khuyên dùng)\nhttp://localhost:8080", "User: bount\nPass: Admin@LyxLab#2026!", "Trang chủ Blog tin tức và Cổng thông tin nghiên cứu kỹ thuật."],
        ["Tác giả biên tập", "https://localhost/wp-login.php", "User: tacgia_k23\nPass: TacGia@K23A#2026", "Tài khoản Tác giả soạn thảo bài viết và quản lý ảnh bìa."],
        ["Độc giả thảo luận", "https://localhost/wp-login.php", "User: docgia_k23\nPass: DocGia@K23A#2026", "Tài khoản Độc giả tham gia gửi bình luận và nhận phản hồi."],
        ["phpMyAdmin", "http://localhost:8081", "User: wp_user\nPass: WP_SecurePassword2026!", "Quản trị trực quan cơ sở dữ liệu quan hệ MySQL."],
        ["Nginx Proxy Manager", "http://localhost:81", "User: admin@example.com\nPass: changeme", "Giao diện cấu hình Reverse Proxy, chứng chỉ SSL và định tuyến."],
        ["Prometheus Server", "http://localhost:9090", "Truy cập trực tiếp (Không xác thực)", "Máy chủ TSDB, kiểm tra trạng thái Targets và chạy PromQL."],
        ["Grafana Dashboards", "http://localhost:3000", "User: admin\nPass: GrafanaAdminSecurePass2026!", "Trung tâm đồ thị giám sát Metrics và tra cứu nhật ký Explore."],
        ["Loki Log Server", "http://localhost:3100", "Endpoint HTTP nội bộ", "Kho lưu trữ và đánh chỉ mục nhật ký sự kiện tập trung."],
        ["MySQL Database", "Host: 127.0.0.1 - Port: 3308", "Root Pass: SuperRootSecurePass2026!\nDB: wordpress_db", "Máy chủ CSDL quan hệ lưu trữ dữ liệu thực tế."]
    ]
    add_styled_table(doc, access_data[0], access_data[1:], "Bảng Phụ lục B: Danh mục cổng truy cập và thông tin xác thực các dịch vụ")

    add_h2(doc, "Phụ lục C: Tập truy vấn PromQL và LogQL phục vụ Kiểm tra")
    add_p(doc, "1. Các câu truy vấn PromQL kiểm tra số liệu chuỗi thời gian (trên Prometheus / Grafana):")
    add_code_block(doc, """
# Kiểm tra trạng thái máy chủ cơ sở dữ liệu MySQL (1 = Hoạt động)
mysql_up == 1

# Kiểm tra trạng thái Reverse Proxy Nginx (1 = Hoạt động)
nginx_up == 1

# Tính phần trăm sử dụng CPU thực tế của máy chủ host
100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[1m])) * 100)

# Đếm tổng số lượng container đang hoạt động
count(container_last_seen)

# Tần suất truy vấn MySQL mỗi giây (Queries Per Second)
rate(mysql_global_status_queries[1m])
    """)

    add_p(doc, "2. Các câu truy vấn LogQL kiểm tra nhật ký sự kiện (trên Grafana Explore -> Loki):")
    add_code_block(doc, """
# 1. Xem toàn bộ dòng log của ứng dụng WordPress
{container="blog-wordpress"}

# 2. Lọc các yêu cầu HTTP gặp lỗi (Mã lỗi 4xx hoặc 5xx) từ Nginx
{container="blog-npm"} |~ "HTTP/[0-9.]+ (4[0-9]{2}|5[0-9]{2})"

# 3. Quét toàn bộ hệ thống bắt các dấu hiệu lỗi hoặc cảnh báo
{container=~".+"} |~ "(?i)error|warn|exception"

# 4. Vẽ biểu đồ tần suất phát sinh log của Nginx (Log rate theo phút)
rate({container="blog-npm"}[1m])
    """)

    print("Conclusions and appendices completed.")
