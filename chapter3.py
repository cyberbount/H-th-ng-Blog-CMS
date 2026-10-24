from report_core import add_p, add_h1, add_h2, add_h3, add_callout, add_code_block, add_figure, add_styled_table

def render_chapter3(doc):
    add_h1(doc, "CHƯƠNG 3. PHÂN TÍCH VÀ THIẾT KẾ HỆ THỐNG")
    
    add_h2(doc, "3.1 Yêu cầu chức năng và phi chức năng của hệ thống Blog CMS")
    add_p(doc, "Giai đoạn phân tích và thiết kế hệ thống đóng vai trò định hình toàn bộ cấu trúc dữ liệu, các luồng tương tác nghiệp vụ và kiến trúc mạng kỹ thuật. Một thiết kế đúng đắn ngay từ đầu sẽ giúp hệ thống vận hành ổn định, dễ dàng mở rộng và giảm thiểu tối đa các lỗi tiềm ẩn trong quá trình triển khai thực tế.")

    add_h3(doc, "3.1.1 Danh mục yêu cầu chức năng (Functional Requirements)")
    fr_data = [
        ["Mã YC", "Tên chức năng nghiệp vụ", "Mô tả chi tiết yêu cầu", "Đối tượng sử dụng"],
        ["FR01", "Xem & Tìm kiếm bài viết", "Cho phép người dùng xem danh sách bài viết mới nhất, phân trang và tìm kiếm bài viết theo từ khóa tiêu đề hoặc nội dung.", "Khách, Độc giả, Tác giả, Admin"],
        ["FR02", "Lọc theo Chuyên mục", "Phân loại bài viết theo 4 chuyên mục công nghệ (DevOps, Hệ thống, An toàn thông tin, Dự án Lab).", "Khách, Độc giả, Tác giả, Admin"],
        ["FR03", "Đăng ký & Xác thực", "Hỗ trợ người dùng đăng nhập bằng tài khoản mật khẩu, quản lý phiên qua cookie và bảo vệ mật khẩu bằng hàm băm an toàn.", "Tất cả các tài khoản"],
        ["FR04", "Biên soạn bài viết", "Cung cấp trình soạn thảo trực quan (Block Editor), cho phép thêm tiêu đề, định dạng khối lệnh, trích dẫn và tải lên ảnh bìa.", "Tác giả, Quản trị viên"],
        ["FR05", "Quản lý vòng đời bài viết", "Hỗ trợ lưu nháp (Draft), hẹn giờ xuất bản hoặc công khai bài viết ngay lập tức (Publish), chỉnh sửa hoặc xóa bài viết.", "Tác giả (bài của mình), Admin"],
        ["FR06", "Bình luận & Phản hồi", "Cho phép độc giả gửi bình luận thảo luận kỹ thuật dưới mỗi bài viết và phản hồi lồng nhau dạng cây phân cấp.", "Độc giả, Tác giả, Admin"],
        ["FR07", "Kiểm duyệt nội dung", "Cung cấp giao diện duyệt bình luận chờ (Pending), đánh dấu spam hoặc xóa các bình luận vi phạm tiêu chuẩn cộng đồng.", "Quản trị viên"],
        ["FR08", "Quản lý Người dùng & RBAC", "Tạo mới tài khoản, phân bổ vai trò (Admin, Author, Subscriber) và quản lý trạng thái kích hoạt của người dùng.", "Quản trị viên"],
        ["FR09", "Giám sát & Quản trị nhật ký", "Thu thập số liệu tài nguyên máy chủ/container và tra cứu vết vết sự cố qua nhật ký tập trung LogQL.", "Kỹ sư vận hành (DevOps/SRE)"]
    ]
    add_styled_table(doc, fr_data[0], fr_data[1:], "Bảng 3.1: Danh mục các yêu cầu chức năng cốt lõi của hệ thống Blog CMS")

    add_h3(doc, "3.1.2 Danh mục yêu cầu phi chức năng (Non-Functional Requirements)")
    nfr_data = [
        ["Mã YC", "Nhóm yêu cầu", "Chỉ số mục tiêu kỹ thuật", "Giải pháp đáp ứng"],
        ["NFR01", "Bảo mật đường truyền", "100% lưu lượng web đi qua cổng HTTPS cổng 443 mã hóa TLS.", "Nginx Proxy Manager với SSL tự ký chuẩn SAN."],
        ["NFR02", "Bảo mật ứng dụng", "Ngăn chặn tấn công Clickjacking, MIME-sniffing, XSS và leo thang đặc quyền.", "HTTP Security Headers, cờ `no-new-privileges`."],
        ["NFR03", "Cách ly CSDL", "Cơ sở dữ liệu MySQL không được mở cổng trực tiếp ra mạng công cộng.", "Cô lập trong mạng bridge `blog_backend_net`."],
        ["NFR04", "Hiệu năng phản hồi", "Thời gian phản hồi trang chủ (Response Time) < 300ms với 20 kết nối đồng thời.", "Bộ nhớ đệm InnoDB Buffer Pool và Apache FastCGI."],
        ["NFR05", "Độ sẵn sàng & Giám sát", "Thời gian phát hiện sự cố (MTTD) < 30 giây khi có container gặp lỗi.", "Prometheus cào metrics chu kỳ 15s và cAdvisor."],
        ["NFR06", "Khả năng lưu trữ", "Dữ liệu bài viết, tệp tin và log không bị mất khi container restart.", "7 Docker Named Volumes lưu trữ bền vững trên host."]
    ]
    add_styled_table(doc, nfr_data[0], nfr_data[1:], "Bảng 3.2: Danh mục yêu cầu phi chức năng của hệ thống")

    add_h2(doc, "3.2 Xác định Actor và Ma trận phân quyền (RBAC Matrix)")
    add_p(doc, "Hệ thống xác định 4 tác nhân (Actors) tham gia tương tác:")
    add_p(doc, "1. Khách vãng lai (Guest): Người dùng chưa đăng nhập, chỉ có quyền xem nội dung công khai, tìm kiếm và xem các bình luận đã duyệt.")
    add_p(doc, "2. Độc giả (Subscriber / Reader): Người dùng đã đăng nhập tài khoản độc giả, được quyền quản lý thông tin cá nhân và tham gia gửi bình luận trao đổi kỹ thuật.")
    add_p(doc, "3. Tác giả (Author / Biên tập viên): Kỹ sư hoặc nghiên cứu viên phòng lab, có quyền soạn thảo bài viết mới, tải lên ảnh bìa, chỉnh sửa/xóa bài viết của chính mình và phản hồi bình luận của độc giả.")
    add_p(doc, "4. Quản trị viên (Administrator): Trưởng phòng lab, nắm toàn quyền kiểm soát website, duyệt bài viết của mọi tác giả, quản lý chuyên mục, phân quyền tài khoản và cấu hình hệ thống.")

    rbac_data = [
        ["Hành động / Quyền hạn trên hệ thống", "Khách (Guest)", "Độc giả (Reader)", "Tác giả (Author)", "Quản trị viên (Admin)"],
        ["Đọc bài viết & Tìm kiếm theo chuyên mục", "Cho phép", "Cho phép", "Cho phép", "Cho phép"],
        ["Gửi bình luận thảo luận kỹ thuật", "Bị cấm", "Cho phép", "Cho phép", "Cho phép"],
        ["Tải lên hình ảnh, tệp đính kèm (Media)", "Bị cấm", "Bị cấm", "Cho phép", "Cho phép"],
        ["Viết bài mới & Lưu nháp (Save Draft)", "Bị cấm", "Bị cấm", "Cho phép", "Cho phép"],
        ["Xuất bản bài viết của chính mình (Publish)", "Bị cấm", "Bị cấm", "Cho phép", "Cho phép"],
        ["Chỉnh sửa / Xóa bài viết của người khác", "Bị cấm", "Bị cấm", "Bị cấm", "Cho phép"],
        ["Kiểm duyệt, ẩn, xóa bình luận người khác", "Bị cấm", "Bị cấm", "Bị cấm", "Cho phép"],
        ["Tạo chuyên mục mới, đổi tên chuyên mục", "Bị cấm", "Bị cấm", "Bị cấm", "Cho phép"],
        ["Quản lý người dùng, gán vai trò Role", "Bị cấm", "Bị cấm", "Bị cấm", "Cho phép"],
        ["Cài đặt Theme, Plugin và Tùy biến CSS", "Bị cấm", "Bị cấm", "Bị cấm", "Cho phép"]
    ]
    add_styled_table(doc, rbac_data[0], rbac_data[1:], "Bảng 3.3: Ma trận phân quyền kiểm soát truy cập (RBAC Matrix)")

    add_callout(doc, "Ma trận phân quyền RBAC nêu trên thể hiện sự khác biệt ranh giới rõ rệt giữa Tác giả (chỉ có quyền trên tài nguyên nội dung do mình tạo ra) và Độc giả (chỉ có quyền tương tác bình luận). Khi chụp ảnh minh chứng thực nghiệm, giao diện Dashboard của hai vai trò này sẽ hoàn toàn khác biệt, chứng minh hệ thống phân quyền chính xác 100%.", "Ý NGHĨA NGHIỆP VỤ PHÂN QUYỀN")

    add_h2(doc, "3.3 Biểu đồ Use Case tổng quát và Đặc tả các ca sử dụng tiêu biểu")
    add_p(doc, "Biểu đồ Use Case tổng quát gom nhóm các tương tác của hệ thống Blog CMS thành 4 phân hệ chính: Phân hệ Nội dung công khai, Phân hệ Tương tác người dùng, Phân hệ Biên tập nội dung, và Phân hệ Quản trị & Vận hành:")

    add_figure(doc, "docs/figures/fig3_1_usecase.png", "Hình 3.1: Sơ đồ Use Case tổng quát hệ thống Blog CMS LyxLab")

    add_h3(doc, "3.3.1 Luồng xác thực đăng nhập và quản lý phiên làm việc")
    add_p(doc, "Quy trình xác thực người dùng được bảo vệ chặt chẽ thông qua giao thức HTTPS cổng 443 do Nginx Proxy Manager tiếp nhận, chuyển tiếp vào WordPress Core để đối chiếu hash mật khẩu phpass lưu trữ trong bảng wp_users của MySQL:")

    add_figure(doc, "docs/figures/fig3_2_seq_login.png", "Hình 3.2: Biểu đồ tuần tự (Sequence Diagram) luồng đăng nhập và xác thực phiên")

    add_h3(doc, "3.3.2 Đặc tả Use Case UC01: Biên soạn và Xuất bản bài viết kỹ thuật")
    add_p(doc, "• Actor: Tác giả (Author), Quản trị viên (Admin).")
    add_p(doc, "• Điều kiện tiên quyết: Người dùng đã đăng nhập thành công với tài khoản có vai trò tối thiểu là Author.")
    add_p(doc, "• Luồng sự kiện chính:")
    add_p(doc, "  1. Người dùng truy cập menu `Bài viết` (Posts) ➔ Chọn `Thêm bài mới` (Add New Post).")
    add_p(doc, "  2. Hệ thống hiển thị giao diện soạn thảo khối (Block Editor Gutenberg).")
    add_p(doc, "  3. Tác giả nhập tiêu đề bài viết, nội dung phân đoạn, chèn khối mã nguồn code block và trích dẫn.")
    add_p(doc, "  4. Tác giả chọn chuyên mục công nghệ phù hợp tại thanh công cụ bên phải (ví dụ: DevOps & Cloud).")
    add_p(doc, "  5. Tác giả tải lên ảnh đại diện bài viết (Featured Image) vào Thư viện Media cá nhân.")
    add_p(doc, "  6. Tác giả nhấn nút `Lưu nháp` (Save Draft) để lưu trữ tạm thời hoặc nhấn `Đăng` (Publish) để công khai.")
    add_p(doc, "  7. Hệ thống mở một MySQL Transaction, lưu trữ bài viết vào bảng `wp_posts` với `post_status = 'publish'`, liên kết chuyên mục trong bảng `wp_term_relationships` và ghi nhận thời điểm xuất bản `post_date`.")
    add_p(doc, "• Ngoại lệ: Nếu mất kết nối mạng hoặc lỗi cơ sở dữ liệu, hệ thống tự động lưu bản sao phục hồi (Autosave) vào LocalStorage của trình duyệt.")

    add_figure(doc, "docs/figures/fig3_3_seq_post.png", "Hình 3.3: Biểu đồ tuần tự luồng biên soạn, xuất bản bài viết kỹ thuật")

    add_h3(doc, "3.3.3 Đặc tả Use Case UC02: Gửi và Phản hồi bình luận lồng nhau đa cấp")
    add_p(doc, "• Actor: Độc giả (Reader), Tác giả (Author), Quản trị viên (Admin).")
    add_p(doc, "• Điều kiện tiên quyết: Bài viết đã ở trạng thái xuất bản và cho phép bình luận.")
    add_p(doc, "• Luồng sự kiện chính:")
    add_p(doc, "  1. Độc giả xem chi tiết bài viết, cuộn xuống khu vực bình luận bên dưới bài viết.")
    add_p(doc, "  2. Độc giả nhập nội dung câu hỏi thảo luận kỹ thuật vào ô phản hồi và nhấn `Gửi bình luận`.")
    add_p(doc, "  3. Hệ thống kiểm tra tính hợp lệ của nội dung, lưu bản ghi vào bảng `wp_comments` với `comment_parent = 0` (bình luận gốc cấp 1).")
    add_p(doc, "  4. Tác giả của bài viết nhận được thông báo, truy cập bài viết và nhấn nút `Trả lời` (Reply) ngay bên dưới bình luận của độc giả.")
    add_p(doc, "  5. Tác giả nhập nội dung giải đáp và nhấn gửi.")
    add_p(doc, "  6. Hệ thống lưu bản ghi mới với trường `comment_parent` chứa ID của bình luận gốc, thiết lập cây thảo luận lồng nhau (Threaded Discussion).")

    add_figure(doc, "docs/figures/fig3_4_seq_comment.png", "Hình 3.4: Biểu đồ tuần tự luồng gửi và phản hồi bình luận phân cấp")

    add_h2(doc, "3.4 Thiết kế Cơ sở dữ liệu quan hệ (Database Schema)")
    add_p(doc, "Cơ sở dữ liệu của WordPress (`wordpress_db`) được thiết kế cực kỳ chuẩn mực theo mô hình quan hệ Codd, sử dụng khóa chính tự tăng (BIGINT Auto-Increment) và các chỉ mục (Indexes) tối ưu hóa truy vấn. Bốn bảng dữ liệu nghiệp vụ quan trọng nhất bao gồm:")

    posts_schema = [
        ["Tên cột", "Kiểu dữ liệu", "Ràng buộc & Khóa", "Ý nghĩa nghiệp vụ"],
        ["ID", "bigint unsigned", "PRIMARY KEY, AUTO_INC", "Mã định danh duy nhất của mỗi bài viết."],
        ["post_author", "bigint unsigned", "INDEX, FK -> wp_users(ID)", "Mã người dùng của tác giả tạo ra bài viết."],
        ["post_date", "datetime", "NOT NULL", "Thời điểm tạo bài viết (tính theo giờ địa phương)."],
        ["post_title", "text", "NOT NULL", "Tiêu đề của bài viết kỹ thuật."],
        ["post_content", "longtext", "NOT NULL", "Nội dung chi tiết của bài viết định dạng HTML."],
        ["post_status", "varchar(20)", "INDEX, NOT NULL", "Trạng thái bài viết: 'publish', 'draft', 'trash'."],
        ["post_name", "varchar(200)", "INDEX, NOT NULL", "Chuỗi slug URL thân thiện (ví dụ: quan-ly-log-loki)."],
        ["post_type", "varchar(20)", "INDEX, NOT NULL", "Loại đối tượng: 'post', 'page', 'attachment'."]
    ]
    add_styled_table(doc, posts_schema[0], posts_schema[1:], "Bảng 3.4: Thiết kế cấu trúc bảng wp_posts lưu trữ bài viết")

    comments_schema = [
        ["Tên cột", "Kiểu dữ liệu", "Ràng buộc & Khóa", "Ý nghĩa nghiệp vụ"],
        ["comment_ID", "bigint unsigned", "PRIMARY KEY, AUTO_INC", "Mã định danh duy nhất của mỗi bình luận."],
        ["comment_post_ID", "bigint unsigned", "INDEX, FK -> wp_posts(ID)", "Mã bài viết mà bình luận này thuộc về."],
        ["comment_author", "tinytext", "NOT NULL", "Tên hiển thị của người bình luận."],
        ["comment_author_email", "varchar(100)", "INDEX, NOT NULL", "Địa chỉ email của người bình luận."],
        ["comment_content", "text", "NOT NULL", "Nội dung thảo luận trao đổi của người dùng."],
        ["comment_approved", "varchar(20)", "INDEX, DEFAULT '1'", "Trạng thái kiểm duyệt: '1' (đã duyệt), '0' (chờ duyệt)."],
        ["comment_parent", "bigint unsigned", "INDEX, DEFAULT '0'", "Mã ID của bình luận cha (phục vụ cây phân cấp đệ quy)."]
    ]
    add_styled_table(doc, comments_schema[0], comments_schema[1:], "Bảng 3.5: Thiết kế cấu trúc bảng wp_comments và trường phân cấp comment_parent")

    add_figure(doc, "docs/figures/fig3_5_erd.png", "Hình 3.5: Mô hình quan hệ thực thể (ERD) các bảng nghiệp vụ cốt lõi của WordPress")

    add_callout(doc, "Trường `comment_parent` trong bảng `wp_comments` là điểm mấu chốt để hiện thực hóa luồng bình luận phân cấp đa tầng (Nested Comments): Khi một bình luận là gốc, giá trị `comment_parent = 0`. Khi Tác giả hoặc Admin trả lời bình luận đó, bản ghi mới sẽ có `comment_parent = [ID của bình luận gốc]`. Giao diện web dựa vào trường này để thụt lề hiển thị cuộc đối thoại theo cấu trúc phân cấp trực quan.", "QUAN HỆ ĐỆ QUY TRONG CSDL")

    add_h2(doc, "3.5 Thiết kế Phân vùng Mạng và Lưu trữ Bền vững")
    add_p(doc, "Nhằm triệt tiêu nguy cơ tấn công bắc cầu (Lateral Movement) trong cụm máy chủ, hệ thống quy hoạch 4 phân vùng mạng riêng biệt:")
    
    net_data = [
        ["Tên phân vùng mạng", "Trình điều khiển", "Dải mạng nội bộ (Subnet)", "Danh sách các container tham gia", "Mục đích an ninh"],
        ["blog_frontend_net", "bridge", "172.28.10.0/24", "blog-npm, blog-wordpress, blog-phpmyadmin", "Vùng đệm tiếp nhận lưu lượng HTTP/HTTPS từ người dùng, ngăn cách với cơ sở dữ liệu."],
        ["blog_backend_net", "bridge", "172.28.20.0/24", "blog-wordpress, blog-phpmyadmin, blog-mysql, blog-mysqld-exporter", "Vùng cô lập cơ sở dữ liệu tuyệt mật, chỉ các dịch vụ có xác thực mới được tham gia."],
        ["blog_monitor_net", "bridge", "172.28.30.0/24", "blog-prometheus, blog-grafana, cụm 5 exporters, blog-loki", "Kênh riêng thu thập số liệu metrics và liên kết trực quan hóa giữa Grafana và TSDB."],
        ["blog_logging_net", "bridge", "172.28.40.0/24", "blog-promtail, blog-loki", "Kênh truyền tải luồng dữ liệu nhật ký sự kiện mã hóa giữa Promtail và Loki Engine."]
    ]
    add_styled_table(doc, net_data[0], net_data[1:], "Bảng 3.6: Thiết kế 4 phân vùng mạng độc lập trong Docker Compose")

    add_p(doc, "Để đảm bảo dữ liệu không bị thất thoát khi cập nhật container, 7 Docker Named Volumes được quy hoạch phân bổ rõ ràng:")
    add_p(doc, "1. `mysql_data`: Lưu trữ toàn bộ bảng dữ liệu InnoDB, file nhị phân redo log và undo log của MySQL.")
    add_p(doc, "2. `wp_data`: Lưu trữ mã nguồn PHP của WordPress, các tệp ảnh tải lên trong `wp-content/uploads/` và theme Astra.")
    add_p(doc, "3. `npm_data` & `npm_ssl`: Lưu trữ cơ sở dữ liệu SQLite của Nginx Proxy Manager và các tệp chứng chỉ SSL x509.")
    add_p(doc, "4. `prometheus_data`: Lưu trữ các khối dữ liệu chuỗi thời gian nén (TSDB blocks) của Prometheus.")
    add_p(doc, "5. `grafana_data`: Lưu trữ thông tin tài khoản người dùng, cấu hình plugin và cache của Grafana.")
    add_p(doc, "6. `loki_data`: Lưu trữ các tệp index và khối chunks nén của hệ thống nhật ký Loki.")

    print("Chapter 3 completed.")
