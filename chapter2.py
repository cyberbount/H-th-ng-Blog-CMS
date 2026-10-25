from report_core import add_p, add_h1, add_h2, add_h3, add_callout, add_code_block, add_figure, add_styled_table

def render_chapter2(doc):
    add_h1(doc, "CHƯƠNG 2. CƠ SỞ LÝ THUYẾT VÀ CÔNG NGHỆ ÁP DỤNG")
    
    add_h2(doc, "2.1 Mô hình Client - Server và kiến trúc phân tầng Ingress - App - Data")
    add_p(doc, "Mô hình Client-Server (Khách - Chủ) là mô hình kiến trúc điện toán phân tán nền tảng của Internet, trong đó khối lượng công việc được phân chia rõ ràng giữa các bên cung cấp tài nguyên hoặc dịch vụ (gọi là Server - Máy chủ) và các bên yêu cầu dịch vụ (gọi là Client - Máy khách). Trong hệ thống Blog CMS LyxLab, máy khách là trình duyệt web của người dùng hoặc các công cụ dòng lệnh (như curl), gửi các yêu cầu HTTP/HTTPS qua mạng tới máy chủ.")
    add_p(doc, "Tuy nhiên, đối với một hệ thống phần mềm doanh nghiệp hiện đại, phía Server không thể là một khối nguyên khối (monolithic) đơn giản mà được tổ chức thành kiến trúc phân tầng (Multi-tier Architecture) nhằm đảm bảo tính mở rộng, bảo mật và khả năng bảo trì. Hệ thống LyxLab phân rã thành 5 tầng trách nhiệm độc lập:")
    add_p(doc, "1. Tầng Cổng biên & Định tuyến (Ingress Tier): Đại diện bởi Nginx Proxy Manager, đóng vai trò là điểm tiếp xúc duy nhất với mạng bên ngoài. Tầng này chịu trách nhiệm chấm dứt kết nối mã hóa SSL/TLS (SSL Termination), xác thực tiêu đề bảo mật HTTP, ngăn chặn truy cập trái phép và định tuyến yêu cầu tới đúng dịch vụ backend nội bộ.")
    add_p(doc, "2. Tầng Nghiệp vụ ứng dụng (Application Tier): Đại diện bởi container WordPress CMS (chạy trên PHP 8.2 và Apache Web Server). Tầng này tiếp nhận yêu cầu từ Nginx, thực thi logic nghiệp vụ (xác thực phiên người dùng, kiểm tra ma trận phân quyền, truy vấn dữ liệu bài viết) và sinh mã HTML trả về cho người dùng.")
    add_p(doc, "3. Tầng Dữ liệu quan hệ (Data Tier): Đại diện bởi máy chủ MySQL 8.0, chịu trách nhiệm lưu trữ có cấu trúc toàn bộ bài viết, chuyên mục, bình luận, người dùng và metadata. Tầng này được cô lập hoàn toàn ở mạng riêng (backend_net), chỉ cho phép các container ứng dụng được cấp phép kết nối qua cổng 3306.")
    add_p(doc, "4. Tầng Giám sát đo lường (Monitoring Tier): Đại diện bởi Prometheus TSDB, Grafana Dashboard và cụm 5 Exporters. Tầng này hoạt động theo mô hình kéo (Pull Model), liên tục thu thập số liệu phần cứng máy chủ, container và ứng dụng theo chu kỳ 15 giây.")
    add_p(doc, "5. Tầng Nhật ký tập trung (Logging Tier): Đại diện bởi Promtail Agent và Grafana Loki 3.0. Tầng này giám sát liên tục luồng nhật ký sự kiện phát sinh từ Docker socket và Nginx để phân tích lỗi thời gian thực.")

    add_callout(doc, "Việc phân chia hệ thống thành 5 tầng độc lập mang lại ưu thế vượt trội về mặt an toàn thông tin: Nếu kẻ tấn công xâm nhập được vào container web application ở tầng 2, chúng vẫn bị cô lập trong mạng con và không thể truy cập trực tiếp vào hệ điều hành máy chủ hay tầng giám sát/log.", "ƯU THẾ KIẾN TRÚC PHÂN TẦNG")

    add_h2(doc, "2.2 Công nghệ WordPress CMS, PHP 8.2 và Web Server Apache")
    add_h3(doc, "2.2.1 Kiến trúc lõi của WordPress")
    add_p(doc, "WordPress là hệ quản trị nội dung mã nguồn mở phổ biến nhất hành tinh, hiện đang vận hành hơn 43% tổng số website trên Internet. Kiến trúc của WordPress được xây dựng theo mô hình Module hóa cao độ với 3 thành phần chính:")
    add_p(doc, "• WordPress Core: Cung cấp bộ máy xử lý yêu cầu cốt lõi, hệ thống định tuyến truy vấn (WP_Query), cơ chế phân quyền người dùng (Roles & Capabilities) và bộ quản lý vòng đời bài viết.")
    add_p(doc, "• Theme System: Quản lý toàn bộ giao diện trình bày HTML/CSS/JS. Hệ thống LyxLab sử dụng theme Astra kết hợp cùng hệ thống thiết kế hiện đại (Design System tokens) nhằm tối ưu hóa trải nghiệm đọc bài và tra cứu tài liệu.")
    add_p(doc, "• Plugin & Must-Use Plugin (mu-plugin): Cho phép mở rộng tính năng của hệ thống mà không cần sửa đổi mã nguồn gốc. Dự án triển khai plugin chuyên biệt `lyxlab-hero.php` trong thư mục `wp-content/mu-plugins/` để render khối Banner trạng thái hạ tầng thời gian thực.")

    add_h3(doc, "2.2.2 Quản lý phiên làm việc và bảo mật xác thực")
    add_p(doc, "Giao thức HTTP về bản chất là giao thức không lưu trạng thái (Stateless). Để duy trì trạng thái đăng nhập của người dùng qua các yêu cầu liên tiếp, WordPress sử dụng cơ chế Cookie xác thực có chữ ký điện tử mật mã (Cryptographic Nonce & Auth Cookie). Khi người dùng đăng nhập thành công:")
    add_p(doc, "• Máy chủ băm mật khẩu bằng thuật toán mật mã phpass (kết hợp HMAC-MD5 và muối ngẫu nhiên độ dài cao) để đối chiếu với trường `user_pass` trong bảng `wp_users`.")
    add_p(doc, "• Máy chủ sinh ra chuỗi cookie xác thực `wordpress_logged_in_[hash]` chứa thông tin định danh người dùng và thời hạn phiên, được ký bằng các khóa bảo mật bí mật (AUTH_KEY, SECURE_AUTH_KEY, LOGGED_IN_KEY) khai báo trong cấu hình.")
    add_p(doc, "• Trình duyệt tự động gửi cookie này trong mỗi yêu cầu tiếp theo, cho phép WordPress nhận diện chính xác vai trò (Administrator, Author hoặc Subscriber) để cấp quyền truy cập tài nguyên phù hợp.")

    add_h2(doc, "2.3 Cơ sở dữ liệu quan hệ MySQL 8.0 và công cụ quản trị phpMyAdmin")
    add_h3(doc, "2.3.1 Kiến trúc lưu trữ InnoDB và tính toàn vẹn dữ liệu")
    add_p(doc, "MySQL 8.0 là một trong những hệ quản trị cơ sở dữ liệu quan hệ (RDBMS) mạnh mẽ và ổn định nhất thế giới. Trong đề tài Blog CMS, cơ sở dữ liệu được cấu hình sử dụng công cụ lưu trữ (Storage Engine) mặc định là InnoDB. InnoDB sở hữu các tính năng kỹ thuật quan trọng:")
    add_p(doc, "• Tuân thủ nghiêm ngặt 4 thuộc tính ACID (Atomicity, Consistency, Isolation, Durability), bảo đảm mọi thao tác ghi dữ liệu bài viết và bình luận diễn ra trọn vẹn hoặc bị hủy bỏ hoàn toàn (Rollback) nếu xảy ra lỗi.")
    add_p(doc, "• Khóa mức bản ghi (Row-level Locking): Cho phép nhiều độc giả gửi bình luận đồng thời trên các bài viết khác nhau mà không làm nghẽn toàn bộ bảng dữ liệu.")
    add_p(doc, "• Bộ đệm nhớ InnoDB Buffer Pool: Cơ chế cache các trang dữ liệu (data pages) và cây chỉ mục (index pages) trực tiếp trên RAM, giảm thiểu tối đa các thao tác I/O đọc ghi đĩa vật lý chậm chạp.")
    add_p(doc, "• Hỗ trợ toàn diện bộ ký tự `utf8mb4` với collation `utf8mb4_unicode_520_ci`: Bảo đảm hiển thị tiếng Việt có dấu hoàn hảo và lưu trữ đầy đủ các ký tự đặc biệt, biểu tượng cảm xúc (emoji) trong nội dung bài viết kỹ thuật.")

    add_h3(doc, "2.3.2 Vai trò của phpMyAdmin và Phân định quyền tài khoản")
    add_p(doc, "phpMyAdmin cung cấp giao diện quản trị đồ họa trực quan trên nền web, giúp người quản trị dễ dàng duyệt cấu trúc bảng, kiểm tra khóa chính (Primary Key), khóa ngoại (Foreign Key), xuất/nhập file SQL sao lưu và thực thi các câu lệnh truy vấn kiểm tra mà không cần gõ lệnh dòng lệnh phức tạp.")
    add_p(doc, "Hệ thống áp dụng nguyên tắc đặc quyền tối thiểu (Principle of Least Privilege) trong quản trị cơ sở dữ liệu:")
    add_p(doc, "• Tài khoản ứng dụng (`wp_user`): Chỉ được cấp quyền DDL/DML trên phạm vi duy nhất cơ sở dữ liệu `wordpress_db`. Container WordPress bắt buộc phải sử dụng tài khoản này, hoàn toàn không được biết mật khẩu `root`.")
    add_p(doc, "• Tài khoản quản trị tối cao (`root`): Chỉ dùng nội bộ khi khởi tạo container hoặc khi kỹ sư vận hành đăng nhập phpMyAdmin để thực hiện các bảo trì cấp cao của máy chủ MySQL.")

    add_h2(doc, "2.4 Ảo hóa Container với Docker Engine và Docker Compose v2")
    add_h3(doc, "2.4.1 Cơ chế cách ly tiến trình và quản lý tài nguyên")
    add_p(doc, "Khác với công nghệ máy ảo truyền thống (Virtual Machine) vốn yêu cầu một hệ điều hành khách (Guest OS) riêng biệt chạy trên tầng Hypervisor gây lãng phí lớn tài nguyên, công nghệ Container của Docker chia sẻ trực tiếp nhân hệ điều hành Linux (Linux Kernel Sharing). Sự cô lập giữa các container được thực hiện dựa trên hai tính năng cốt lõi của nhân Linux:")
    add_p(doc, "1. Linux Namespaces (Không gian tên): Tạo ra ảo giác cho tiến trình bên trong container rằng nó đang làm việc trên một hệ điều hành riêng biệt:")
    add_p(doc, "  - PID Namespace: Cô lập cây tiến trình, tiến trình chính trong container luôn có PID = 1.")
    add_p(doc, "  - NET Namespace: Cung cấp giao diện mạng ảo (veth), bảng định tuyến và địa chỉ IP riêng biệt.")
    add_p(doc, "  - MNT Namespace: Cô lập điểm gắn kết hệ thống tệp tin (Mount Points).")
    add_p(doc, "  - IPC & UTS Namespace: Cô lập hàng đợi thông điệp bộ nhớ dùng chung và tên máy chủ (Hostname).")
    add_p(doc, "2. Control Groups (cgroups v2): Giám sát và áp đặt giới hạn tài nguyên phần cứng mà mỗi container được phép sử dụng. Trong đề tài, cgroups được cấu hình chặt chẽ để giới hạn dung lượng RAM và tỷ lệ sử dụng CPU cho từng container, ngăn ngừa nguy cơ một dịch vụ bị tấn công gây cạn kiệt tài nguyên toàn máy chủ.")

    add_h3(doc, "2.4.2 Mạng Bridge và Lưu trữ bền vững (Volumes)")
    add_p(doc, "Mặc định khi khởi động, Docker tạo ra mạng bridge tiêu chuẩn `docker0`. Tuy nhiên, để đảm bảo an ninh mạng theo mô hình Zero Trust, dự án LyxLab tự định nghĩa 4 mạng bridge tùy chỉnh (Custom Bridge Networks). Các mạng này hoạt động như các phân đoạn mạng vật lý độc lập (VLAN), chỉ cho phép các container cùng nằm trong một mạng nhìn thấy và liên lạc được với nhau qua cơ chế phân giải tên miền nội bộ (Docker Embedded DNS).")
    add_p(doc, "Do hệ thống tệp của container mang tính chất tạm thời (Ephemeral - dữ liệu sẽ biến mất khi container bị xóa bỏ), Docker Volume được sử dụng để gắn kết thư mục từ máy chủ host vào container. Toàn bộ cơ sở dữ liệu MySQL (`mysql_data`), mã nguồn WordPress (`wordpress_data`), cấu hình và chứng chỉ SSL của Nginx Proxy Manager (`npm_data`, `npm_letsencrypt`) và dữ liệu chuỗi thời gian Prometheus (`prometheus_data`) đều được lưu trữ trên Named Volumes, bảo đảm dữ liệu tồn tại vĩnh viễn qua mọi chu kỳ khởi động lại container.")

    add_h2(doc, "2.5 Cổng Nginx Reverse Proxy, SSL SAN và Quản lý lưu lượng")
    add_p(doc, "Trong kiến trúc micro-services đa container, việc để các dịch vụ backend mở cổng trực tiếp ra Internet là một sai lầm bảo mật nghiêm trọng. Cổng Reverse Proxy (Máy chủ ủy quyền ngược) là giải pháp tiêu chuẩn công nghiệp:")
    add_p(doc, "• Ẩn giấu cấu trúc mạng nội bộ: Người dùng bên ngoài chỉ nhìn thấy duy nhất cổng 80 (HTTP) và 443 (HTTPS) của Nginx. Toàn bộ địa chỉ IP nội bộ và cổng thực tế của WordPress (8080) hay phpMyAdmin (8081) được ẩn giấu hoàn toàn.")
    add_p(doc, "• Chấm dứt kết nối mã hóa (SSL/TLS Termination): Nginx chịu trách nhiệm xử lý thuật toán bắt tay mã hóa khóa công khai (TLS Handshake) và giải mã lưu lượng HTTPS. Lưu lượng chuyển tiếp tới container WordPress trong mạng nội bộ là HTTP thuần, giúp giải phóng tải tính toán CPU rất lớn cho máy chủ ứng dụng.")
    add_p(doc, "• Tích hợp chứng chỉ số tự ký Subject Alternative Name (SAN): Trong môi trường thực hành nội bộ (localhost), việc sử dụng chứng chỉ thông thường sẽ bị trình duyệt cảnh báo lỗi tên miền. Nhóm đã sử dụng OpenSSL để tạo chứng chỉ SSL x509 hỗ trợ trường mở rộng SAN cho cả `DNS:localhost`, `DNS:lyxlab.local` và `IP:127.0.0.1`, cho phép mã hóa đường truyền an toàn tuyệt đối.")
    add_p(doc, "• Cấu hình HTTP Security Headers: Bổ sung các tiêu đề bảo vệ vào phản hồi HTTP bao gồm `X-Frame-Options: SAMEORIGIN` (chống tấn công Clickjacking), `X-Content-Type-Options: nosniff` (chống tấn công MIME sniffing) và `Strict-Transport-Security` (cưỡng chế HTTPS).")

    add_h2(doc, "2.6 Hệ thống Giám sát chuỗi thời gian Prometheus TSDB và 5 Exporters")
    add_h3(doc, "2.6.1 Cơ chế hoạt động của Prometheus TSDB")
    add_p(doc, "Prometheus là dự án mã nguồn mở hàng đầu thuộc quỹ điện toán đám mây CNCF (Cloud Native Computing Foundation), được thiết kế chuyên biệt để giám sát và tạo cảnh báo cho các hệ thống container phân tán. Khác với mô hình truyền thống (Push Model - ứng dụng tự gửi dữ liệu về máy chủ), Prometheus hoạt động theo mô hình kéo (Pull-based Model):")
    add_p(doc, "• Prometheus Server định kỳ (mặc định 15 giây trong dự án) gửi các yêu cầu HTTP GET tới endpoint `/metrics` của các tác nhân thu thập số liệu (Exporters).")
    add_p(doc, "• Dữ liệu thu thập được lưu trữ vào Cơ sở dữ liệu chuỗi thời gian nội bộ (Time-Series Database - TSDB) với hiệu năng nén cực cao (trung bình chỉ tốn 1-2 bytes cho mỗi điểm đo).")
    add_p(doc, "• Ngôn ngữ PromQL: Cung cấp bộ toán tử mạnh mẽ cho phép tính toán tức thời độ dốc (rate), giá trị trung bình (avg), phần trăm sử dụng (histogram_quantile) và tổng hợp số liệu theo các nhãn (labels).")

    add_h3(doc, "2.6.2 Cụm 5 Exporters thu thập số liệu đa chiều")
    add_p(doc, "Để giám sát toàn diện mọi ngóc ngách của hệ thống Blog CMS, đề tài đã cấu hình 5 nhóm Exporter chuyên trách:")
    
    exp_data = [
        ["Tên Exporter", "Cổng dịch vụ", "Chỉ số đo lường trọng tâm", "Ý nghĩa trong vận hành"],
        ["Node Exporter", "9100", "node_cpu_seconds_total,\nnode_memory_MemAvailable_bytes,\nnode_disk_read_bytes_total", "Đo lường tải phần cứng CPU, tỷ lệ RAM trống, băng thông đọc ghi đĩa và lưu lượng mạng của máy chủ host."],
        ["cAdvisor\n(Container Advisor)", "8080", "container_cpu_usage_seconds_total,\ncontainer_memory_usage_bytes,\ncontainer_network_receive_bytes_total", "Đọc trực tiếp từ cgroups của Linux kernel, thống kê chi tiết phần trăm CPU và RAM tiêu thụ của từng container riêng biệt."],
        ["MySQL Exporter", "9104", "mysql_up,\nmysql_global_status_queries,\nmysql_global_status_threads_connected,\nmysql_global_status_innodb_buffer_pool_pages_data", "Theo dõi trạng thái sống còn của MySQL, tần suất truy vấn/giây, số lượng kết nối đang mở và hiệu năng sử dụng vùng nhớ đệm Buffer Pool."],
        ["Nginx Exporter", "9113", "nginx_up,\nnginx_connections_active,\nnginx_connections_accepted,\nnginx_http_requests_total", "Đọc số liệu từ module `ngx_http_stub_status_module` của Nginx, đo lường số kết nối đang kích hoạt, số request/giây và trạng thái chờ/đọc/ghi."],
        ["Docker Stats Exporter", "9487", "docker_stats_cpu_percentage,\ndocker_stats_memory_percentage", "Thu thập số liệu thời gian thực từ Docker Engine Socket (`docker.sock`), bổ trợ số liệu trực quan cho cAdvisor."]
    ]
    add_styled_table(doc, exp_data[0], exp_data[1:], "Bảng 2.1: Danh mục các thành phần trong cụm 5 Exporters giám sát")

    add_h2(doc, "2.7 Thu thập và Phân tích Nhật ký tập trung với Loki 3.0 và Promtail")
    add_p(doc, "Trong môi trường microservices gồm 13 containers, việc điều tra nguyên nhân gốc rễ (Root Cause Analysis - RCA) của một lỗi hệ thống trở nên bất khả thi nếu người quản trị phải dùng lệnh `docker logs` trên từng container riêng lẻ. Các giải pháp truyền thống như ELK Stack (Elasticsearch, Logstash, Kibana) tuy mạnh mẽ nhưng tiêu tốn quá nhiều tài nguyên RAM (thường yêu cầu tối thiểu 4GB - 8GB RAM chỉ để chạy Elasticsearch) do cơ chế đánh chỉ mục toàn văn (Full-text indexing).")
    add_p(doc, "Grafana Loki được mệnh danh là 'Prometheus for logs' với tư duy thiết kế tối giản mang tính cách mạng:")
    add_p(doc, "• Không đánh chỉ mục nội dung text của log: Thay vào đó, Loki chỉ đánh chỉ mục các cặp nhãn siêu dữ liệu (Metadata Labels) tương tự như Prometheus (ví dụ: `container='blog-wordpress'`, `job='nginx'`).")
    add_p(doc, "• Nén dữ liệu theo khối (Chunks): Nội dung log thực tế được nén chặt bằng thuật toán gzip/snappy và lưu thành các chunks dạng luồng (streams), giúp giảm dung lượng lưu trữ tới hơn 80% so với dữ liệu thô.")
    add_p(doc, "• Promtail Agent: Đóng vai trò là tác nhân thu thập log cực kỳ nhẹ nhàng (lightweight shipper), gắn kết trực tiếp vào Docker socket (`/var/run/docker.sock`) để tự động bắt luồng `stdout` và `stderr` của toàn bộ các container, đồng thời theo dõi (tail) các tệp tin log truy cập của Nginx Proxy Manager.")
    add_p(doc, "• Ngôn ngữ truy vấn LogQL: Cho phép người quản trị tìm kiếm nhanh các thông báo lỗi bằng biểu thức chính quy (Regex Filter) và tổng hợp tần suất sinh log thành đồ thị trực quan.")

    add_h2(doc, "2.8 Các nguyên lý Gia cố Bảo mật Hệ thống (System Hardening)")
    add_p(doc, "Nhằm đáp ứng yêu cầu khắt khe của một hệ thống chuẩn sản xuất và tiêu chí đánh giá an toàn thông tin của học phần, hệ thống LyxLab áp dụng nguyên lý Phòng thủ theo chiều sâu (Defense-in-Depth) với 4 trụ cột:")
    add_p(doc, "1. Ngăn chặn leo thang đặc quyền (no-new-privileges): Mặc định, nếu một ứng dụng web bị tin tặc chèn mã độc (RCE), chúng có thể tìm kiếm các tệp tin nhị phân mang cờ SUID (như sudo, passwd) bên trong container để chiếm quyền root máy chủ host (Container Escape). Bằng cách khai báo thuộc tính `security_opt: - no-new-privileges:true` trong Docker Compose, Linux kernel sẽ cấm hoàn toàn các tiến trình con nâng quyền cao hơn tiến trình cha.")
    add_p(doc, "2. Giới hạn tài nguyên phần cứng (Resource Limits): Thiết lập trần CPU và bộ nhớ RAM cho từng container, loại bỏ hoàn toàn nguy cơ một tiến trình bị lỗi rò rỉ bộ nhớ hoặc bị tấn công từ chối dịch vụ (DoS) làm cạn kiệt tài nguyên máy chủ vật lý.")
    add_p(doc, "3. Phân vùng mạng độc lập (Network Segmentation): Tách biệt mạng ngoài (Frontend) và mạng trong (Backend). Cơ sở dữ liệu MySQL hoàn toàn không mở cổng ra Internet mà chỉ chấp nhận kết nối từ các container hợp lệ trong cùng mạng `backend_net`.")
    add_p(doc, "4. Bảo mật cấu hình nhạy cảm: Toàn bộ mật khẩu root, mật khẩu cơ sở dữ liệu và token truy cập được quản lý tập trung qua biến môi trường `.env`, được loại trừ khỏi kho lưu trữ Git thông qua `.gitignore` để tránh rò rỉ thông tin lên không gian mạng.")

    print("Chapter 2 completed.")
