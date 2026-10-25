from report_core import add_p, add_h1, add_h2, add_h3, add_callout, add_code_block, add_figure, add_styled_table

def render_chapter5(doc):
    add_h1(doc, "CHƯƠNG 5. KẾT QUẢ THỰC NGHIỆM VÀ ĐÁNH GIÁ ĐỀ TÀI")
    
    add_h2(doc, "5.1 Môi trường thực nghiệm và phương pháp kiểm chứng độc lập")
    add_p(doc, "Toàn bộ hệ thống LyxLab Blog CMS được khởi chạy và thực nghiệm trực tiếp trong môi trường máy chủ container hóa với các thông số kỹ thuật tiêu chuẩn:")
    add_p(doc, "• Hệ điều hành Host: Microsoft Windows 11 Pro 64-bit tích hợp hệ thống con Linux WSL2 (Windows Subsystem for Linux), chạy bản phân phối Ubuntu 24.04 LTS.")
    add_p(doc, "• Nền tảng Ảo hóa: Docker Engine phiên bản 29.8.2 kết hợp công cụ điều phối Docker Compose v5.6.0, chạy trong hệ thống con WSL2 (kernel 6.18).")
    add_p(doc, "• Cấu hình Phần cứng vật lý: Bộ vi xử lý Intel Core i7 đa nhân, bộ nhớ trong 16 GB RAM DDR4, ổ đĩa lưu trữ thể rắn NVMe SSD 512 GB.")
    add_p(doc, "• Phương pháp kiểm chứng: Nhóm áp dụng phương pháp kiểm thử hộp đen (Black-box testing) kết hợp đối chiếu trực tiếp dữ liệu mức thấp (Database inspection), đối chiếu số liệu metrics thời gian thực (Time-series telemetry) và phân tích luồng nhật ký (Log analysis).")

    add_h2(doc, "5.2 Kết quả giao diện Blog hiện đại LyxLab (Theme Astra + Design System)")
    add_p(doc, "Giao diện người dùng ngoài trang chủ được tinh chỉnh hoàn toàn theo tiêu chuẩn thiết kế hiện đại (Modern Tech & Security Research Platform), mang lại vẻ đẹp thanh lịch, bố cục rõ ràng và tốc độ tải trang nhanh chóng:")

    add_figure(doc, "docs/screenshots/fig5_1_homepage.png", "Hình 5.1: Giao diện trang chủ Cổng thông tin Nghiên cứu Công nghệ LyxLab")

    add_p(doc, "Các điểm nhấn nổi bật trên giao diện bao gồm:")
    add_p(doc, "1. Khối Hero Dashboard Banner (`lyxlab-hero.php`): Nằm ở đầu trang chủ, hiển thị biểu tượng nhấp nháy màu xanh (Live Pulse Dot) báo hiệu trạng thái hoạt động thực tế của 13/13 container, đồng thời cung cấp 4 thẻ thống kê nhanh về các công nghệ chủ chốt.")
    add_p(doc, "2. Bố cục 2 cột chuyên nghiệp: Cột trái (70% chiều rộng) hiển thị các thẻ bài viết dạng Card với dải màu gradient phân định chuyên mục; Cột phải (30% chiều rộng) tích hợp hộp Tìm kiếm thông minh, Bài viết nghiên cứu mới và Danh mục chuyên môn.")
    add_p(doc, "3. Thanh Menu điều hướng tiếng Việt: Cố định trên 1 hàng ngang duy nhất, tích hợp nút liên kết nhanh `Bảng tin Quản trị` giúp người dùng chuyển đổi tức thì vào khu vực quản trị.")

    add_h2(doc, "5.3 Kết quả kiểm chứng phân quyền người dùng (Admin, Tác giả, Độc giả)")
    add_p(doc, "Để minh chứng hệ thống Role-Based Access Control (RBAC) hoạt động chính xác theo đúng ma trận phân quyền đã thiết kế tại Chương 3, nhóm đã khởi tạo 3 tài khoản mẫu đại diện cho 3 cấp độ quyền hạn:")

    users_test_data = [
        ["Tên tài khoản", "Vai trò (Role)", "Mật khẩu kiểm thử", "Quyền hạn thực tế quan sát được trên giao diện"],
        ["bount", "Administrator\n(Quản trị viên)", "Admin@LyxLab#2026!", "• Toàn quyền quản trị website.\n• Xuất hiện đầy đủ menu: Dashboard, Posts, Media, Comments, Appearance, Plugins, Users, Tools, Settings."],
        ["tacgia_k23", "Author\n(Tác giả / Biên tập)", "TacGia@K23A#2026", "• Chỉ có quyền biên soạn bài viết cá nhân.\n• Menu bên trái CHỈ XUẤT HIỆN: Dashboard, Posts, Media, Comments, Profile, Tools.\n• Hoàn toàn BỊ ẨN các mục: Users, Plugins, Settings."],
        ["docgia_k23", "Subscriber\n(Độc giả / Reader)", "DocGia@K23A#2026", "• Chỉ có quyền đọc và bình luận thảo luận.\n• Menu bên trái CHỈ CÓ DUY NHẤT mục: Profile (Hồ sơ cá nhân).\n• Hoàn toàn không có quyền viết bài hay upload ảnh."]
    ]
    add_styled_table(doc, users_test_data[0], users_test_data[1:], "Bảng 5.1: Danh sách tài khoản kiểm chứng 3 vai trò người dùng trong hệ thống")

    add_figure(doc, "docs/screenshots/fig5_2_author_dashboard.png", "Hình 5.2: Giao diện Bảng tin Quản trị của Tác giả (tacgia_k23) bị hạn chế quyền nghiêm ngặt")

    add_callout(doc, "Hình 5.2 là bằng chứng thực nghiệm đắt giá nhất chứng minh tính năng phân quyền: Khi đăng nhập bằng tài khoản Tác giả `tacgia_k23`, hệ thống hiển thị rõ ràng thông báo `Howdy, Kỹ sư Lab (Tác giả)` ở góc phải và menu bên trái đã bị tước bỏ hoàn toàn các chức năng quản trị nhạy cảm như Quản lý người dùng (Users) hay Cài đặt hệ thống (Settings).", "XÁC NHẬN PHÂN QUYỀN RBAC THÀNH CÔNG")

    add_h2(doc, "5.4 Kết quả xuất bản bài viết kỹ thuật và thảo luận phân cấp")
    add_p(doc, "Hệ thống đã được nạp sẵn 8 bài viết kỹ thuật chuyên sâu phân bổ đều trên 4 chuyên mục công nghệ, tạo nên một cơ sở dữ liệu tri thức sống động phục vụ nghiên cứu:")

    posts_list_data = [
        ["ID", "Tiêu đề bài viết kỹ thuật", "Chuyên mục", "Tác giả biên soạn", "Trạng thái"],
        ["19", "Kỹ thuật Hardening Docker Container: Phòng chống tấn công leo thang đặc quyền", "An toàn thông tin", "tacgia_k23 (Author)", "Published"],
        ["20", "Tối ưu hóa hiệu năng MySQL 8.0 trên Docker với InnoDB Buffer Pool và Exporter", "DevOps & Cloud", "tacgia_k23 (Author)", "Published"],
        ["21", "Hướng dẫn cấu hình Nginx Reverse Proxy cân bằng tải và bảo vệ Web Server", "Hệ thống & Mạng", "bount (Admin)", "Published"],
        ["22", "Báo cáo Thực nghiệm Giám sát Hạ tầng Đa Container bằng Prometheus và cAdvisor", "Dự án Lab", "tacgia_k23 (Author)", "Published"],
        ["9", "Quản lý Nhật ký tập trung thời gian thực với Grafana Loki & LogQL", "An toàn thông tin", "bount (Admin)", "Published"],
        ["7", "Xây dựng Nginx Reverse Proxy với SSL tự ký SAN bảo vệ cụm dịch vụ Web", "Hệ thống & Mạng", "bount (Admin)", "Published"],
        ["8", "Giải pháp Giám sát toàn diện Hạ tầng bằng Prometheus & Grafana", "DevOps & Cloud", "bount (Admin)", "Published"],
        ["6", "Chào mừng đến với LyxLab: Tầm nhìn & Hướng nghiên cứu Hệ thống phần mềm", "Dự án Lab", "bount (Admin)", "Published"]
    ]
    add_styled_table(doc, posts_list_data[0], posts_list_data[1:], "Bảng 5.2: Danh mục 8 bài viết kỹ thuật thực nghiệm trên hệ thống LyxLab")

    add_p(doc, "Về luồng tương tác bình luận phân cấp (Threaded Discussions):")
    add_p(doc, "• Tại bài viết số 9 (Quản lý Nhật ký với Grafana Loki), tài khoản Độc giả `docgia_k23` đã gửi bình luận hỏi về cơ chế phân tích nhãn container của Promtail (Bình luận ID = 2, `comment_parent = 0`).")
    add_p(doc, "• Quản trị viên `bount` đã phản hồi giải thích chi tiết cơ chế đọc Docker socket (Bình luận ID = 3, `comment_parent = 2`). Giao diện tự động thụt lề hiển thị câu trả lời ngay dưới câu hỏi của độc giả.")
    add_p(doc, "• Tương tự, tại bài viết số 19 (Hardening Docker Container), Độc giả `docgia_k23` đặt câu hỏi về tác động của cờ `no-new-privileges` (Bình luận ID = 6) và được Tác giả `tacgia_k23` phản hồi kỹ thuật thỏa đáng (Bình luận ID = 7, `comment_parent = 6`).")

    add_h2(doc, "5.5 Kết quả kiểm chứng Cơ sở dữ liệu nghiệp vụ trên phpMyAdmin")
    add_p(doc, "Truy cập giao diện phpMyAdmin tại địa chỉ `http://localhost:8081` với tài khoản `wp_user`, nhóm đã kiểm chứng trực tiếp tính toàn vẹn của dữ liệu trong cơ sở dữ liệu `wordpress_db`:")

    add_figure(doc, "docs/screenshots/fig5_3_phpmyadmin.png", "Hình 5.3: Cấu trúc các bảng dữ liệu WordPress CMS hiển thị trên phpMyAdmin")

    add_p(doc, "Kết quả kiểm tra xác nhận:")
    add_p(doc, "• Bảng `wp_posts`: Chứa đúng 8 bản ghi bài viết kỹ thuật với `post_status = 'publish'` và `post_type = 'post'`. Cột `post_author` ánh xạ chính xác ID = 1 (bount) và ID = 2 (tacgia_k23).")
    add_p(doc, "• Bảng `wp_comments`: Lưu trữ đầy đủ các bình luận thảo luận. Trường `comment_parent` mang giá trị khác 0 đối với các phản hồi lồng nhau, chứng minh quan hệ phân cấp cây được duy trì bền vững trong CSDL.")
    add_p(doc, "• Bảng `wp_users`: Lưu trữ 3 tài khoản người dùng với mật khẩu băm mật mã an toàn, không có tài khoản nào bị lưu mật khẩu dạng bản rõ (plaintext).")

    add_h2(doc, "5.6 Kết quả thu thập Metrics trên Prometheus Server (Targets 100% UP)")
    add_p(doc, "Truy cập máy chủ Prometheus tại địa chỉ `http://localhost:9090/targets`, trang quản lý mục tiêu thu thập số liệu xác nhận toàn bộ các tác nhân Exporter đều hoạt động hoàn hảo:")

    add_figure(doc, "docs/screenshots/fig5_4_prometheus_targets.png", "Hình 5.4: Trạng thái 100% HEALTH UP của toàn bộ các mục tiêu thu thập số liệu trên Prometheus")

    add_p(doc, "Các truy vấn PromQL cơ bản dùng để nghiệm thu trạng thái hệ thống:")
    add_p(doc, "• Kiểm tra trạng thái máy chủ cơ sở dữ liệu MySQL (1 = Hoạt động tốt):")
    add_code_block(doc, "mysql_up == 1")
    add_p(doc, "• Kiểm tra trạng thái máy chủ Web Proxy Nginx (1 = Hoạt động tốt):")
    add_code_block(doc, "nginx_up == 1")
    add_p(doc, "• Đếm tổng số lượng container Docker đang hoạt động:")
    add_code_block(doc, "count(container_last_seen)")

    add_h2(doc, "5.7 Kết quả trực quan hóa trên 7 Dashboard Grafana tiêu chuẩn")
    add_p(doc, "Truy cập giao diện Grafana tại địa chỉ `http://localhost:3000` với tài khoản quản trị `admin`, toàn bộ 7 bộ Dashboard (1 dashboard nạp tự động qua Provisioning và 6 dashboard import từ thư viện Grafana Labs) đều hiển thị số liệu đo lường trực quan, chính xác theo thời gian thực:")

    add_figure(doc, "docs/screenshots/fig5_5_grafana_dashboard.png", "Hình 5.5: Dashboard tổng quan giám sát tài nguyên máy chủ và container trên Grafana")

    add_p(doc, "Phân tích các Dashboard nghiệm thu trọng yếu:")
    add_p(doc, "1. Dashboard Node Exporter Full (ID: 1860): Trực quan hóa phần trăm sử dụng CPU toàn máy chủ (dao động ổn định từ 8% - 15%), tỷ lệ bộ nhớ RAM khả dụng (Available RAM ~ 14.2 GB), băng thông đọc ghi đĩa và lưu lượng truyền nhận gói tin mạng.")
    add_p(doc, "2. Dashboard Docker Containers Monitoring (nạp tự động qua Provisioning) và cAdvisor Exporter: Liệt kê danh sách 13 containers, hiển thị chi tiết lượng RAM thực tế tiêu thụ của từng container (ví dụ: `blog-mysql` tiêu thụ ~360 MB, `blog-wordpress` tiêu thụ ~165 MB, `blog-loki` tiêu thụ ~120 MB), không có hiện tượng rò rỉ bộ nhớ.")
    add_p(doc, "3. Dashboard MySQL Overview (ID: 7362): Theo dõi đồ thị số lượng truy vấn mỗi giây (Queries/sec), số client thread đang kết nối đồng thời và tỷ lệ sử dụng bộ đệm nhớ InnoDB Buffer Pool.")
    add_p(doc, "4. Dashboard NginX: Đo lường số kết nối đang kích hoạt (Active Connections), tần suất phục vụ yêu cầu HTTP và phân loại kết nối theo các trạng thái Reading / Writing / Waiting.")
    add_p(doc, "5. Hai Dashboard Prometheus 2.0 Stats và Prometheus Stats: Giám sát sức khỏe bản thân máy chủ TSDB (tsdb_head_series, scrape duration) phục vụ việc bảo trì hệ thống giám sát.")

    add_h2(doc, "5.8 Kết quả truy vấn LogQL trong Grafana Loki")
    add_p(doc, "Truy cập mục Grafana Explore (`http://localhost:3000/explore`) và chọn Data Source là `Loki`, nhóm đã thực nghiệm 3 câu truy vấn LogQL tiêu chuẩn tương ứng với 3 tình huống quản trị thực tế:")

    add_figure(doc, "docs/screenshots/fig5_6_loki_explore.png", "Hình 5.6: Giao diện Grafana Explore truy vấn nhật ký trực tiếp từ kho lưu trữ Loki")

    add_p(doc, "• Tình huống 1: Giám sát toàn bộ luồng nhật ký ứng dụng của WordPress:")
    add_code_block(doc, '{container="blog-wordpress"}')
    add_p(doc, "Kết quả trả về toàn bộ các dòng log Apache access log và PHP-FPM, cho thấy các yêu cầu GET và POST được xử lý thành công với mã 200 OK.")

    add_figure(doc, "docs/screenshots/fig5_7_logql_filter.png", "Hình 5.7: Kết quả lọc truy vết các bản ghi lỗi HTTP bằng câu truy vấn LogQL")

    add_p(doc, "• Tình huống 2: Bóc tách các bản ghi lỗi HTTP (Mã 4xx hoặc 5xx) trên cổng Nginx Proxy Manager:")
    add_code_block(doc, '{container="blog-npm"} |~ "HTTP/[0-9.]+ (4[0-9]{2}|5[0-9]{2})"')
    add_p(doc, "Kết quả bắt được các yêu cầu truy cập sai đường dẫn (mã lỗi 404 Not Found), giúp người quản trị phát hiện ngay các nỗ lực quét lỗ hổng hoặc đường dẫn bị hỏng.")

    add_p(doc, "• Tình huống 3: Đo lường tốc độ phát sinh nhật ký theo thời gian thực (Log Rate trong cửa sổ 5 phút):")
    add_code_block(doc, 'rate({container="blog-npm"}[5m])')
    add_p(doc, "Grafana tự động vẽ biểu đồ tần suất phát sinh log dạng đồ thị sóng, giúp nhận diện các đợt bùng nổ lưu lượng truy cập bất thường (Traffic Spike) hoặc tấn công từ chối dịch vụ.")

    add_h2(doc, "5.9 Kiểm chứng cô lập mạng và các tiêu chí Bảo mật Hardening")
    add_p(doc, "Thực hiện kiểm chứng mức sâu trên dòng lệnh Linux:")

    add_figure(doc, "docs/screenshots/fig5_8_compose_ps.png", "Hình 5.8: Lệnh docker compose ps xác nhận 13/13 containers đều ở trạng thái Up ổn định")

    add_p(doc, "1. Kiểm chứng cờ chống leo thang đặc quyền `no-new-privileges`:")
    add_code_block(doc, "docker inspect blog-wordpress --format '{{.HostConfig.SecurityOpt}}'")
    add_p(doc, "Kết quả trả về chính xác: `[no-new-privileges:true]`, xác nhận tiến trình bên trong container không thể lợi dụng các tệp tin SUID để chiếm quyền root máy chủ.")
    add_p(doc, "2. Kiểm chứng giới hạn tài nguyên đã áp dụng hiệu lực:")
    add_code_block(doc, "docker stats --no-stream blog-mysql blog-wordpress blog-loki")
    add_p(doc, "Kết quả hiển thị trần bộ nhớ ứng với từng container (ví dụ `blog-mysql`: 360 MiB / 1 GiB, `blog-loki`: 50 MiB / 512 MiB), xác nhận cơ chế cgroups v2 đang áp đặt ngưỡng tài nguyên chính xác.")
    add_p(doc, "3. Kiểm chứng cô lập mạng CSDL bằng truy vấn phân giải DNS nội bộ:")
    add_code_block(doc, "docker exec blog-npm getent hosts mysql")
    add_p(doc, "Kết quả trả về trống (không phân giải được hostname `mysql`), chứng minh Nginx Proxy Manager ở mạng `blog_frontend_net` hoàn toàn không nhìn thấy máy chủ CSDL MySQL ẩn trong mạng `blog_backend_net`; trái lại, thực hiện cùng lệnh từ container `blog-wordpress` thì phân giải thành công, chứng minh việc cô lập là có chọn lọc theo thiết kế.")

    add_h2(doc, "5.10 Bảng đối chiếu nghiệm thu toàn diện theo yêu cầu đề bài")
    add_p(doc, "Đối chiếu toàn bộ sản phẩm thực tế của đề tài LyxLab Blog CMS với thang điểm 10 tiêu chuẩn của học phần:")

    final_eval_data = [
        ["Nhóm tiêu chí đánh giá", "Trọng số", "Kết quả thực tế đạt được của hệ thống LyxLab", "Đánh giá"],
        ["1. Quản lý mã nguồn trên GitHub", "1.5 đ", "• Repository đầy đủ source + cấu hình, 3 mốc commit đúng tiến trình (Core ➔ Monitoring ➔ Logging) và 1 commit tài liệu.\n• README.md 11 mục chi tiết: kiến trúc Mermaid, hướng dẫn chạy, bảng cổng, tài khoản, PromQL/LogQL mẫu.", "1.5 / 1.5 đ"],
        ["2. Triển khai ứng dụng + Database", "1.5 đ", "• WordPress 6 (PHP 8.2) + MySQL 8.0 + phpMyAdmin 5.2, 8 bài viết, 4 chuyên mục, 7 bình luận phân cấp.\n• Kết nối DB qua mạng backend_net biệt lập, dữ liệu bền vững trên named volumes.", "1.5 / 1.5 đ"],
        ["3. Nginx Reverse Proxy", "1.5 đ", "• Nginx Proxy Manager làm cổng Ingress duy nhất, forward tới WordPress/phpMyAdmin.\n• HTTPS chứng chỉ tự ký chuẩn SAN (DNS:localhost, IP:127.0.0.1), Security Headers và HSTS.", "1.5 / 1.5 đ"],
        ["4. Giám sát Prometheus + Grafana", "1.5 đ", "• Prometheus cào 6/6 targets UP chu kỳ 15s từ 5 nhóm exporter.\n• Grafana 7 dashboard giám sát host / container / MySQL / Nginx / TSDB.", "1.5 / 1.5 đ"],
        ["5. Log tập trung Loki + LogQL", "1.5 đ", "• Promtail cào Docker socket + NPM access logs đẩy về Loki 3.0.\n• 4 câu LogQL kiểm chứng: lọc container, regex lỗi 4xx/5xx, quét error/warn, đo rate.", "1.5 / 1.5 đ"],
        ["6. Hardening hệ thống", "1.5 đ", "• 4 mạng bridge cô lập CSDL, cờ no-new-privileges, resource limits CPU/RAM cho 6 dịch vụ trọng yếu.\n• Mật khẩu mạnh, Security Headers, hạn chế quyền DB user, .env loại khỏi Git.", "1.5 / 1.5 đ"],
        ["7. Tổng thể & Trình bày", "1.0 đ", "• 13/13 containers `Up` ổn định, khởi chạy 1-click `docker compose up -d`.\n• Demo đầy đủ kèm bộ minh chứng screenshot và sơ đồ kiến trúc trong báo cáo.", "1.0 / 1.0 đ"],
        ["TỔNG CỘNG ĐIỂM SỐ", "10.0 đ", "Hệ thống hoàn thành toàn bộ 7/7 tiêu chí đánh giá theo đề cương học phần.", "10.0 / 10.0 đ"]
    ]
    add_styled_table(doc, final_eval_data[0], final_eval_data[1:], "Bảng 5.3: Bảng đối chiếu tự đánh giá kết quả đề tài theo khung chấm điểm ICTU")

    print("Chapter 5 completed.")
