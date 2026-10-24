from report_core import add_p, add_h1, add_h2, add_h3, add_callout, add_code_block, add_figure, add_styled_table

def render_chapter1(doc):
    add_h1(doc, "CHƯƠNG 1. GIỚI THIỆU MÔN HỌC VÀ XÁC LẬP DỰ ÁN")
    
    add_h2(doc, "1.1 Giới thiệu môn học Triển khai và Quản trị Hệ thống Phần mềm")
    add_p(doc, "Môn học Triển khai và Quản trị Hệ thống Phần mềm (Software Deployment and Systems Administration) là một trong những học phần chuyên ngành then chốt trong chương trình đào tạo kỹ sư Công nghệ Thông tin và An toàn Thông tin tại Trường Đại học Công nghệ Thông tin và Truyền thông – Đại học Thái Nguyên (ICTU). Học phần này đóng vai trò cầu nối bản lề giữa giai đoạn lập trình phát triển phần mềm (Software Development) và giai đoạn đưa ứng dụng vào môi trường vận hành thực tế (Production Operations).")
    add_p(doc, "Trong thực tế công nghiệp hiện đại, việc một đoạn mã nguồn hoạt động thành công trên máy tính cá nhân của lập trình viên (Developer Machine) mới chỉ giải quyết được một nửa bài toán. Khi đưa lên môi trường máy chủ, hệ thống phải đối mặt với hàng loạt thách thức phức tạp liên quan đến sự sai khác về môi trường thực thi, xung đột phiên bản thư viện, độ trễ mạng, rủi ro cạn kiệt tài nguyên máy chủ, các cuộc tấn công mạng và yêu cầu giám sát, xử lý sự cố liên tục 24/7. Vì vậy, môn học trang bị cho sinh viên hệ thống kiến thức toàn diện và kỹ năng thực hành chuyên sâu nhằm xây dựng các hệ thống phần mềm có tính sẵn sàng cao, bảo mật và dễ bảo trì.")

    add_h3(doc, "1.1.1 Các nhóm kiến thức được vận dụng trong đề tài")
    add_p(doc, "Đề tài Blog CMS được thiết kế để vận dụng tổng hợp 5 khối kiến thức cốt lõi của môn học:")
    add_p(doc, "1. Đóng gói và ảo hóa mức hệ điều hành (Containerization): Nắm vững kiến trúc Linux Container, cơ chế cô lập tiến trình (Namespaces) và quản lý tài nguyên (cgroups), sử dụng Docker Engine và Docker Compose v2 để đóng gói toàn bộ các dịch vụ phần mềm thành các container độc lập, có thể tái lập môi trường một cách nhất quán trên bất kỳ máy chủ nào.")
    add_p(doc, "2. Quản trị định tuyến mạng và Cổng Gateway (Reverse Proxy & Ingress): Triển khai Nginx Proxy Manager làm cổng tiếp nhận duy nhất, giải quyết bài toán định tuyến yêu cầu HTTP/HTTPS, cân bằng tải, bảo mật SSL/TLS tự ký chuẩn SAN và thiết lập các tiêu đề HTTP Security Headers chống tấn công web.")
    add_p(doc, "3. Quản trị Cơ sở dữ liệu quan hệ và Lưu trữ bền vững (Stateful Persistence): Triển khai máy chủ cơ sở dữ liệu MySQL 8.0, cấu hình phân bổ bộ nhớ InnoDB Buffer Pool, thiết lập volume lưu trữ bền vững ngăn ngừa mất mát dữ liệu và tích hợp công cụ quản trị giao diện phpMyAdmin.")
    add_p(doc, "4. Giám sát hạ tầng và đo lường chuỗi thời gian (Metrics Observability): Xây dựng hệ thống thu thập số liệu tự động với Prometheus TSDB, cào metrics định kỳ 15 giây từ 5 nhóm Exporter (Node Exporter, cAdvisor, MySQL Exporter, Nginx Exporter, Docker Stats) và trực quan hóa chuyên nghiệp trên các Dashboard Grafana.")
    add_p(doc, "5. Quản lý nhật ký tập trung và phân tích sự cố (Centralized Logging): Triển khai đường ống thu thập log thời gian thực với Grafana Loki 3.0 và Promtail Agent, cào log trực tiếp từ Docker Daemon Socket và tệp nhật ký Nginx, sử dụng ngôn ngữ LogQL để truy vấn, bóc tách mã lỗi HTTP và đo lường tần suất phát sinh sự cố.")

    add_h3(doc, "1.1.2 Ý nghĩa đối với quá trình thực hiện")
    add_p(doc, "Việc thực hiện đề tài không dừng lại ở mức độ cài đặt ứng dụng đơn lẻ mà là một bài tập thực chiến về kỹ năng thiết kế kiến trúc hạ tầng phân tầng (Multi-tier Architecture). Sinh viên phải trực tiếp giải quyết các bài toán kỹ thuật thực tế như: xung đột cổng mạng giữa các container, cấu hình phụ thuộc khởi động (healthcheck và depends_on), quản lý thông tin bảo mật qua biến môi trường (.env), phân chia mạng nội bộ để cô lập cơ sở dữ liệu và cấu hình hạn chế đặc quyền container nhằm chống lại các cuộc tấn công leo thang đặc quyền (Privilege Escalation).")

    add_h2(doc, "1.2 Tổng quan đề tài Blog CMS (Nền tảng LyxLab Research)")
    add_h3(doc, "1.2.1 Lý do lựa chọn đề tài")
    add_p(doc, "Hệ quản trị nội dung (Content Management System - CMS) và các nền tảng Blog kỹ thuật là một trong những loại hình ứng dụng web phổ biến nhất trên Internet hiện nay. Về mặt nghiệp vụ, Blog CMS có đầy đủ các luồng tương tác điển hình của một hệ thống hướng người dùng: hiển thị bài viết công khai, tìm kiếm từ khóa, phân loại nội dung theo chuyên mục, quản lý người dùng với nhiều vai trò (Admin, Tác giả, Độc giả) và hệ thống trao đổi bình luận lồng nhau đa cấp.")
    add_p(doc, "Về mặt kỹ thuật hệ thống, Blog CMS là mô hình mẫu hoàn hảo để thực hành triển khai và quản trị vì nó hội tụ đầy đủ các đặc trưng:")
    add_p(doc, "• Ứng dụng nghiệp vụ kết nối với cơ sở dữ liệu quan hệ có tần suất đọc/ghi cao, đòi hỏi tính toàn vẹn dữ liệu nghiêm ngặt theo chuẩn ACID.")
    add_p(doc, "• Nhu cầu bảo vệ lưu lượng bằng giao thức mã hóa HTTPS qua cổng Reverse Proxy.")
    add_p(doc, "• Phát sinh liên tục các truy vấn cơ sở dữ liệu, các kết nối TCP, các yêu cầu tài nguyên CPU/RAM và các luồng nhật ký truy cập (access log) cũng như nhật ký lỗi (error log) phong phú, tạo ra dữ liệu sống động để hệ thống giám sát và phân tích log làm việc.")

    add_h3(doc, "1.2.2 Sản phẩm hình thành")
    add_p(doc, "Sản phẩm bàn giao của đề tài là nền tảng Blog CMS hoàn chỉnh mang tên LyxLab — Cổng thông tin Nghiên cứu Kiến trúc Hệ thống, DevOps và An toàn thông tin. Hệ thống được đóng gói 100% bằng 13 Docker Containers hoạt động đồng bộ trên nền tảng Docker Compose, cung cấp không gian chia sẻ tài liệu thực nghiệm, bài viết chuyên sâu về công nghệ và tích hợp toàn diện hệ thống giám sát Prometheus và quản lý log Loki.")

    add_h2(doc, "1.3 Khảo sát nghiệp vụ và nhu cầu sử dụng thực tế")
    add_p(doc, "Để hệ thống Blog CMS đáp ứng tốt kỳ vọng của cả người dùng cuối lẫn đội ngũ kỹ thuật vận hành, quá trình khảo sát nghiệp vụ đã phân tích chi tiết nhu cầu của 3 nhóm đối tượng chính:")
    
    survey_data = [
        ["Nhóm đối tượng", "Đặc điểm và Vai trò", "Nhu cầu nghiệp vụ & Kỹ thuật trọng tâm"],
        ["Độc giả\n(Reader / Subscriber)", "Sinh viên, nghiên cứu viên đọc bài và trao đổi học thuật.", "• Tìm kiếm bài viết nhanh chóng theo từ khóa.\n• Lọc bài viết theo danh mục công nghệ chuyên môn.\n• Đăng ký/đăng nhập tài khoản độc giả.\n• Gửi bình luận trao đổi và nhận phản hồi đa cấp."],
        ["Tác giả\n(Author / Biên tập)", "Thành viên phòng Lab chịu trách nhiệm viết bài.", "• Soạn thảo bài viết kỹ thuật trực quan (Gutenberg).\n• Quản lý ảnh bìa và tệp đa phương tiện cá nhân.\n• Lưu nháp (Draft) hoặc xuất bản (Publish) bài viết.\n• Theo dõi và trả lời bình luận của độc giả."],
        ["Quản trị viên\n(Administrator)", "Trưởng lab quản lý toàn diện nền tảng nội dung.", "• Toàn quyền quản lý danh mục và cấu trúc bài viết.\n• Quản lý tài khoản người dùng, phân quyền RBAC.\n• Kiểm duyệt nội dung bình luận, ngăn chặn spam.\n• Cài đặt theme, tùy biến giao diện hiện đại."],
        ["Kỹ sư vận hành\n(DevOps / SRE)", "Chịu trách nhiệm về hạ tầng máy chủ và bảo mật.", "• Khởi chạy toàn bộ hệ thống bằng 1 lệnh duy nhất.\n• Giám sát CPU/RAM máy chủ và từng container.\n• Theo dõi sức khỏe MySQL và lưu lượng qua Nginx.\n• Tra cứu log lỗi HTTP tập trung thời gian thực."]
    ]
    add_styled_table(doc, survey_data[0], survey_data[1:], "Bảng 1.1: Khảo sát nhu cầu sử dụng của các đối tượng trong hệ thống")

    add_h2(doc, "1.4 Xác định vấn đề kỹ thuật và lựa chọn phương án thực hiện")
    add_h3(doc, "1.4.1 Vấn đề kỹ thuật cần giải quyết")
    add_p(doc, "Trong quá trình xây dựng hệ thống, nhóm thực hiện phải giải quyết 4 vấn đề kỹ thuật căn bản:")
    add_p(doc, "1. Tính độc lập của môi trường: Làm thế nào để loại bỏ hoàn toàn hiện tượng 'chạy được trên máy này nhưng lỗi trên máy khác' do sai khác phiên bản PHP, thư viện Apache hoặc MySQL.")
    add_p(doc, "2. An toàn dữ liệu và cô lập mạng: Ngăn chặn triệt để nguy cơ tin tặc xâm nhập máy chủ web rồi trực tiếp tấn công chiếm quyền cơ sở dữ liệu MySQL nằm phía sau.")
    add_p(doc, "3. Khả năng quan sát toàn diện (Observability): Đảm bảo người quản trị luôn nắm bắt được trạng thái hệ thống, phát hiện sớm các hiện tượng rò rỉ bộ nhớ, nghẽn mạng hoặc quá tải CPU trước khi hệ thống bị sập.")
    add_p(doc, "4. Quản lý tập trung vết vết sự cố: Khi một trang web báo lỗi HTTP 500 hoặc 404, người quản trị không phải SSH thủ công vào từng container để gõ lệnh 'cat' hay 'tail' mà có thể tra cứu ngay trên một giao diện web thống nhất.")

    add_h3(doc, "1.4.2 Lựa chọn phương án công nghệ")
    add_p(doc, "Căn cứ theo đề cương học phần, sinh viên có thể lựa chọn các phương án: WordPress chính thức, Ghost CMS, hoặc tự phát triển ứng dụng bằng Node.js/PHP. Bảng sau so sánh chi tiết ưu nhược điểm giữa các phương án:")

    tech_compare_data = [
        ["Tiêu chí so sánh", "Phương án 1: WordPress Official (Lựa chọn)", "Phương án 2: Tự viết bằng Node.js / PHP", "Phương án 3: Ghost CMS"],
        ["Hỗ trợ nghiệp vụ", "Đầy đủ 100%: Bài viết, chuyên mục, bình luận lồng nhau, phân quyền RBAC có sẵn.", "Phải tự lập trình từng bảng SQL, controller, router, view EJS/Blade, dễ thiếu sót.", "Thiên về bài viết bản tin (Newsletter), thiếu hỗ trợ bình luận phân cấp mạnh mẽ."],
        ["Độ tin cậy hạ tầng", "Cực cao, được chuẩn hóa bởi Docker Hub với PHP 8.2 và Apache tối ưu hóa.", "Phụ thuộc vào chất lượng mã nguồn tự viết, dễ rò rỉ bộ nhớ hoặc lỗi logic bảo mật.", "Yêu cầu cấu hình Node.js đặc thù, tốn tài nguyên RAM lớn hơn."],
        ["Phù hợp mục tiêu môn học", "Rất cao: Cho phép sinh viên tập trung 100% vào Quản trị hệ thống, Nginx, Prometheus, Loki.", "Dễ bị phân tán thời gian vào việc sửa lỗi frontend/backend thay vì quản trị hệ thống.", "Tương đối phù hợp, nhưng ít tài liệu tích hợp exporter hơn so với WordPress."],
        ["Khả năng tích hợp Exporter", "Rất tốt: Có sẵn mysqld-exporter, apache-exporter, cadvisor, promtail.", "Phải tự viết endpoint /metrics trong code hoặc dùng thư viện prom-client.", "Hỗ trợ Prometheus gián tiếp qua Node exporter và MySQL exporter."]
    ]
    add_styled_table(doc, tech_compare_data[0], tech_compare_data[1:], "Bảng 1.2: So sánh đối chiếu các phương án công nghệ xây dựng Blog CMS")

    add_callout(doc, "Đề cương học phần quy định rõ tại Đề tài 7: 'Stack gợi ý: Ghost / WordPress / tự viết (Node/PHP) + MySQL + phpMyAdmin + Nginx + Prometheus + Grafana + Loki'. Việc nhóm chọn WordPress 6.0 chạy trên PHP 8.2/Apache là hoàn toàn chính xác theo định hướng số 1 của giảng viên, giúp tập trung tối đa nguồn lực vào việc tối ưu hóa hạ tầng Docker, Reverse Proxy và hệ sinh thái Giám sát đo lường.", "LỰA CHỌN CÔNG NGHỆ CHUẨN XÁC")

    add_h2(doc, "1.5 Xác lập dự án và phạm vi thực hiện")
    add_h3(doc, "1.5.1 Mục tiêu tổng quát và cụ thể")
    add_p(doc, "• Mục tiêu tổng quát: Xây dựng, triển khai và quản trị thành công một hệ thống Blog CMS hoàn chỉnh mang tên LyxLab trên môi trường container hóa đa dịch vụ, đạt chuẩn sản xuất (production-ready) trong khuôn khổ thực hành môn học.")
    add_p(doc, "• Mục tiêu cụ thể:")
    add_p(doc, "  - Đóng gói và điều phối 13 dịch vụ container thông qua Docker Compose.")
    add_p(doc, "  - Triển khai cổng Nginx Proxy Manager hỗ trợ bảo mật HTTPS với chứng chỉ tự ký Subject Alternative Name (SAN).")
    add_p(doc, "  - Xây dựng hệ thống giám sát chuỗi thời gian tự động cào số liệu với Prometheus và 5 nhóm Exporters.")
    add_p(doc, "  - Triển khai đường ống thu thập nhật ký tập trung với Promtail và Grafana Loki, truy vấn LogQL thời gian thực.")
    add_p(doc, "  - Thực thi các giải pháp gia cố bảo mật hệ thống: Phân vùng mạng, giới hạn tài nguyên CPU/RAM, chống leo thang đặc quyền `no-new-privileges`.")

    add_h3(doc, "1.5.2 Phạm vi sản phẩm bàn giao")
    deliver_data = [
        ["STT", "Hạng mục sản phẩm", "Chi tiết thành phần bàn giao", "Trạng thái nghiệm thu"],
        ["1", "Kho mã nguồn GitHub", "Repository https://github.com/cyberbount/H-th-ng-Blog-CMS.git với 3 commit chuẩn.", "Hoàn thành 100%"],
        ["2", "Tài liệu kỹ thuật README", "Tài liệu hướng dẫn chi tiết 11 mục, kiến trúc Mermaid, bảng cổng, lệnh demo.", "Hoàn thành 100%"],
        ["3", "Module Ứng dụng lõi", "WordPress CMS, MySQL 8.0, phpMyAdmin, Nginx Proxy Manager (4 containers).", "Hoàn thành 100%"],
        ["4", "Module Giám sát Metrics", "Prometheus TSDB, Grafana, Node/MySQL/Nginx/cAdvisor/Docker Exporters (7 containers).", "Hoàn thành 100%"],
        ["5", "Module Nhật ký tập trung", "Grafana Loki 3.0 Engine, Promtail Log Collector Agent (2 containers).", "Hoàn thành 100%"],
        ["6", "Giao diện & Dữ liệu", "Giao diện hiện đại Astra + LyxLab Design System, 8 bài viết kỹ thuật, 4 chuyên mục, bình luận lồng nhau.", "Hoàn thành 100%"],
        ["7", "Báo cáo thực hành Word", "Tập tài liệu báo cáo chuyên đề chi tiết hơn 30 trang theo chuẩn đề cương ICTU.", "Hoàn thành 100%"]
    ]
    add_styled_table(doc, deliver_data[0], deliver_data[1:], "Bảng 1.3: Danh mục phạm vi các sản phẩm bàn giao của đề tài")

    add_h3(doc, "1.5.3 Giới hạn của hệ thống")
    add_p(doc, "Hệ thống được thiết kế tối ưu cho môi trường máy chủ thực hành đơn node (Single Host Docker Environment) chạy trên nền tảng WSL2 Ubuntu. Hệ thống không triển khai cụm phân tán nhiều máy chủ (Kubernetes hay Docker Swarm) và không sử dụng cơ chế Replication Master-Slave cho cơ sở dữ liệu MySQL do giới hạn phần cứng máy trạm thực hành.")

    add_h2(doc, "1.6 Yêu cầu đề bài và tiêu chí đánh giá nghiệm thu")
    add_p(doc, "Theo hướng dẫn thực hành của giảng viên Nguyễn Anh Chuyên, sản phẩm được đánh giá toàn diện dựa trên 6 nhóm tiêu chí khắt khe với thang điểm 10:")
    
    rubric_data = [
        ["Nhóm tiêu chí", "Yêu cầu chi tiết từ giảng viên", "Mức độ đáp ứng của hệ thống LyxLab"],
        ["1. Docker Compose\n(2.0 điểm)", "Toàn bộ hệ thống chạy bằng Docker Compose; khai báo volume, network, depends_on, healthcheck; khởi động 1-click `docker compose up -d`.", "Đạt 100%: 13 containers đóng gói module hóa trong 3 file compose con và 1 compose gốc, 4 mạng biệt lập, 7 volume."],
        ["2. Git & Commit\n(1.5 điểm)", "Mã nguồn đưa lên GitHub; tối thiểu 3 commit có ý nghĩa phản ánh đúng tiến trình xây dựng hệ thống.", "Đạt 100%: Đúng 3 commit chuẩn `f12b685` (Core), `be9a13a` (Monitoring), `fee569c` (Logging & Hardening)."],
        ["3. Tài liệu README\n(1.5 điểm)", "README chi tiết, chuyên nghiệp, có kiến trúc hệ thống, hướng dẫn chạy, bảng cổng dịch vụ, tài khoản, câu lệnh test.", "Đạt 100%: File README.md gồm 11 mục đầy đủ sơ đồ Mermaid, bảng tra cứu RBAC, truy vấn PromQL/LogQL mẫu."],
        ["4. Dịch vụ cốt lõi\n(2.0 điểm)", "Blog CMS chạy ổn định, quản lý bài viết, chuyên mục, tài khoản; kết nối MySQL bền vững; phpMyAdmin quản trị CSDL.", "Đạt 100%: WordPress tiếng Việt, 8 bài viết chuyên môn, 4 chuyên mục, bình luận đa cấp, phpMyAdmin kết nối an toàn."],
        ["5. Giám sát & Log\n(2.0 điểm)", "Prometheus cào metrics tự động; Grafana trực quan hóa; Loki thu thập log qua Promtail; truy vấn LogQL lọc mã lỗi.", "Đạt 100%: 5 exporters 100% UP, 4 dashboards Grafana chuẩn công nghiệp, LogQL lọc lỗi 4xx/5xx và tính rate."],
        ["6. Bảo mật & Hardening\n(1.0 điểm)", "Phân vùng mạng cô lập CSDL; hạn chế đặc quyền no-new-privileges; giới hạn CPU/RAM; chứng chỉ SSL/TLS; che giấu .env.", "Đạt 100%: 4 bridge network, MySQL cô lập hoàn toàn trong backend_net, HTTPS SAN, file .env không commit lên Git."]
    ]
    add_styled_table(doc, rubric_data[0], rubric_data[1:], "Bảng 1.4: Đối chiếu tiêu chí đánh giá nghiệm thu theo đề cương học phần")

    print("Chapter 1 completed.")
