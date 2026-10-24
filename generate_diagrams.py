import os
import cairosvg

def create_svg_and_png(filename_base, svg_content):
    svg_path = f"docs/figures/{filename_base}.svg"
    png_path = f"docs/figures/{filename_base}.png"
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    cairosvg.svg2png(url=svg_path, write_to=png_path, dpi=200)
    print(f"Generated: {png_path} ({os.path.getsize(png_path)} bytes)")

# 1. Use Case Diagram
svg_usecase = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 680" width="1000" height="680">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#2563eb" />
    </marker>

    <style type="text/css"><![CDATA[
      .actor-box { fill: #f8fafc; stroke: #3b82f6; stroke-width: 2; rx: 12; }
      .actor-title { font-family: 'Segoe UI', Arial, sans-serif; font-size: 14px; font-weight: bold; fill: #1e3a8a; text-anchor: middle; }
      .actor-desc { font-family: 'Segoe UI', Arial, sans-serif; font-size: 11px; fill: #64748b; text-anchor: middle; }
      .sys-box { fill: #ffffff; stroke: #cbd5e1; stroke-width: 2; stroke-dasharray: 6 6; rx: 16; }
      .sys-title { font-family: 'Segoe UI', Arial, sans-serif; font-size: 16px; font-weight: bold; fill: #0f172a; text-anchor: middle; }
      .uc-box { fill: #eff6ff; stroke: #2563eb; stroke-width: 1.5; rx: 20; }
      .uc-text { font-family: 'Segoe UI', Arial, sans-serif; font-size: 12px; font-weight: 600; fill: #1e40af; text-anchor: middle; }
      .line { stroke: #94a3b8; stroke-width: 1.5; }
      .line-auth { stroke: #10b981; stroke-width: 1.5; }
      .line-admin { stroke: #ef4444; stroke-width: 1.5; }
    ]]></style>
  </defs>

  <!-- Background -->
  <rect width="1000" height="680" fill="#f8fafc" />

  <!-- Header -->
  <rect x="30" y="20" width="940" height="45" rx="8" fill="#1e3a8a" />
  <text x="500" y="48" font-family="'Segoe UI', Arial" font-size="16" font-weight="bold" fill="#ffffff" text-anchor="middle">
    HÌNH 3.1: SƠ ĐỒ USE CASE TỔNG QUÁT HỆ THỐNG BLOG CMS LYXLAB
  </text>

  <!-- System Boundary -->
  <rect x="240" y="85" width="520" height="570" class="sys-box" />
  <text x="500" y="115" class="sys-title">Phạm vi Hệ thống Blog CMS (WordPress &amp; Infra)</text>

  <!-- Left Actors: Guest, Reader -->
  <!-- Guest -->
  <rect x="40" y="140" width="160" height="90" class="actor-box" />
  <circle cx="120" cy="170" r="14" fill="#3b82f6" />
  <text x="120" y="202" class="actor-title">Khách vãng lai</text>
  <text x="120" y="218" class="actor-desc">(Chưa đăng nhập)</text>

  <!-- Reader -->
  <rect x="40" y="320" width="160" height="90" class="actor-box" />
  <circle cx="120" cy="350" r="14" fill="#10b981" />
  <text x="120" y="382" class="actor-title">Độc giả (Reader)</text>
  <text x="120" y="398" class="actor-desc">(Vai trò Subscriber)</text>

  <!-- Right Actors: Author, Administrator -->
  <!-- Author -->
  <rect x="800" y="170" width="160" height="90" class="actor-box" style="stroke: #f59e0b;" />
  <circle cx="880" cy="200" r="14" fill="#f59e0b" />
  <text x="880" y="232" class="actor-title">Tác giả (Author)</text>
  <text x="880" y="248" class="actor-desc">(Kỹ sư / Biên tập)</text>

  <!-- Administrator -->
  <rect x="800" y="420" width="160" height="90" class="actor-box" style="stroke: #ef4444;" />
  <circle cx="880" cy="450" r="14" fill="#ef4444" />
  <text x="880" y="482" class="actor-title">Quản trị viên (Admin)</text>
  <text x="880" y="498" class="actor-desc">(Trưởng Lab / DevOps)</text>

  <!-- Use Cases in System Boundary -->
  <!-- UC1: Xem &amp; Tìm kiếm bài viết -->
  <rect x="280" y="140" width="200" height="36" class="uc-box" />
  <text x="380" y="163" class="uc-text">Xem &amp; Tìm kiếm bài viết</text>

  <!-- UC2: Lọc theo chuyên mục -->
  <rect x="280" y="190" width="200" height="36" class="uc-box" />
  <text x="380" y="213" class="uc-text">Lọc theo chuyên mục</text>

  <!-- UC3: Đăng nhập &amp; Xác thực -->
  <rect x="280" y="245" width="200" height="36" class="uc-box" style="fill: #fef3c7; stroke: #d97706;" />
  <text x="380" y="268" class="uc-text" style="fill: #92400e;">Đăng nhập &amp; Xác thực phiên</text>

  <!-- UC4: Gửi bình luận thảo luận -->
  <rect x="280" y="300" width="200" height="36" class="uc-box" />
  <text x="380" y="323" class="uc-text">Gửi bình luận thảo luận</text>

  <!-- UC5: Phản hồi bình luận phân cấp -->
  <rect x="280" y="355" width="200" height="36" class="uc-box" />
  <text x="380" y="378" class="uc-text">Phản hồi bình luận lồng nhau</text>

  <!-- UC6: Soạn thảo bài viết Gutenberg -->
  <rect x="520" y="140" width="210" height="36" class="uc-box" style="fill: #fef3c7; stroke: #d97706;" />
  <text x="625" y="163" class="uc-text" style="fill: #92400e;">Soạn thảo bài viết mới</text>

  <!-- UC7: Upload hình ảnh Media -->
  <rect x="520" y="195" width="210" height="36" class="uc-box" style="fill: #fef3c7; stroke: #d97706;" />
  <text x="625" y="218" class="uc-text" style="fill: #92400e;">Upload ảnh Media &amp; Featured</text>

  <!-- UC8: Xuất bản &amp; Quản lý bài mình -->
  <rect x="520" y="250" width="210" height="36" class="uc-box" style="fill: #fef3c7; stroke: #d97706;" />
  <text x="625" y="273" class="uc-text" style="fill: #92400e;">Xuất bản &amp; Quản lý bài cá nhân</text>

  <!-- UC9: Quản lý người dùng &amp; RBAC -->
  <rect x="520" y="360" width="210" height="36" class="uc-box" style="fill: #fee2e2; stroke: #dc2626;" />
  <text x="625" y="383" class="uc-text" style="fill: #991b1b;">Quản lý Người dùng &amp; RBAC</text>

  <!-- UC10: Duyệt / Xóa bình luận &amp; bài -->
  <rect x="520" y="415" width="210" height="36" class="uc-box" style="fill: #fee2e2; stroke: #dc2626;" />
  <text x="625" y="438" class="uc-text" style="fill: #991b1b;">Kiểm duyệt toàn bộ bài viết &amp; comment</text>

  <!-- UC11: Cấu hình Nginx &amp; SSL -->
  <rect x="520" y="470" width="210" height="36" class="uc-box" style="fill: #fee2e2; stroke: #dc2626;" />
  <text x="625" y="493" class="uc-text" style="fill: #991b1b;">Cấu hình Nginx SSL &amp; Proxy Host</text>

  <!-- UC12: Giám sát Prometheus &amp; Loki -->
  <rect x="520" y="525" width="210" height="36" class="uc-box" style="fill: #fee2e2; stroke: #dc2626;" />
  <text x="625" y="548" class="uc-text" style="fill: #991b1b;">Giám sát Metrics &amp; LogQL Explore</text>

  <!-- Association Lines -->
  <!-- Guest to UC1, UC2 -->
  <line x1="200" y1="170" x2="280" y2="158" class="line" />
  <line x1="200" y1="185" x2="280" y2="208" class="line" />

  <!-- Reader to UC1, UC2, UC3, UC4, UC5 -->
  <line x1="200" y1="350" x2="280" y2="168" class="line" />
  <line x1="200" y1="360" x2="280" y2="218" class="line" />
  <line x1="200" y1="370" x2="280" y2="263" class="line" />
  <line x1="200" y1="380" x2="280" y2="318" class="line" />
  <line x1="200" y1="390" x2="280" y2="373" class="line" />

  <!-- Author to UC3, UC5, UC6, UC7, UC8 -->
  <line x1="800" y1="200" x2="480" y2="263" class="line-auth" />
  <line x1="800" y1="210" x2="480" y2="373" class="line-auth" />
  <line x1="800" y1="215" x2="730" y2="158" class="line-auth" />
  <line x1="800" y1="225" x2="730" y2="213" class="line-auth" />
  <line x1="800" y1="235" x2="730" y2="268" class="line-auth" />

  <!-- Admin to All -->
  <line x1="800" y1="440" x2="730" y2="268" class="line-admin" />
  <line x1="800" y1="450" x2="730" y2="378" class="line-admin" />
  <line x1="800" y1="460" x2="730" y2="433" class="line-admin" />
  <line x1="800" y1="470" x2="730" y2="488" class="line-admin" />
  <line x1="800" y1="480" x2="730" y2="543" class="line-admin" />

  <!-- Legend -->
  <rect x="250" y="605" width="500" height="40" rx="8" fill="#f1f5f9" stroke="#cbd5e1" />
  <line x1="270" y1="625" x2="310" y2="625" class="line" />
  <text x="320" y="629" font-family="'Segoe UI', Arial" font-size="11" fill="#475569">Khách &amp; Độc giả</text>
  <line x1="420" y1="625" x2="460" y2="625" class="line-auth" />
  <text x="470" y="629" font-family="'Segoe UI', Arial" font-size="11" fill="#475569">Tác giả (Biên tập)</text>
  <line x1="580" y1="625" x2="620" y2="625" class="line-admin" />
  <text x="630" y="629" font-family="'Segoe UI', Arial" font-size="11" fill="#475569">Quản trị viên (Toàn quyền)</text>
</svg>"""

create_svg_and_png("fig3_1_usecase", svg_usecase)

# 2. Sequence Diagram: Login Flow
svg_seq_login = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 560" width="950" height="560">
  <defs>
    <style type="text/css"><![CDATA[
      .actor-bar { fill: #1e3a8a; rx: 8; }
      .actor-txt { font-family: 'Segoe UI', Arial; font-size: 13px; font-weight: bold; fill: #ffffff; text-anchor: middle; }
      .life-line { stroke: #94a3b8; stroke-width: 1.5; stroke-dasharray: 4 4; }
      .msg-line { stroke: #2563eb; stroke-width: 1.5; marker-end: url(#arrow); }
      .ret-line { stroke: #10b981; stroke-width: 1.5; stroke-dasharray: 4 2; marker-end: url(#arrow-green); }
      .msg-txt { font-family: 'Segoe UI', Arial; font-size: 11.5px; font-weight: 600; fill: #1e293b; }
      .exec-box { fill: #dbeafe; stroke: #3b82f6; stroke-width: 1; rx: 4; }
    ]]></style>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#2563eb" />
    </marker>
    <marker id="arrow-green" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#10b981" />
    </marker>
  </defs>

  <rect width="950" height="560" fill="#f8fafc" />
  <rect x="25" y="15" width="900" height="40" rx="8" fill="#1e3a8a" />
  <text x="475" y="40" font-family="'Segoe UI', Arial" font-size="15" font-weight="bold" fill="#ffffff" text-anchor="middle">
    HÌNH 3.2: BIỂU ĐỒ TUẦN TỰ (SEQUENCE DIAGRAM) LUỒNG ĐĂNG NHẬP VÀ XÁC THỰC PHIÊN
  </text>

  <!-- Lifelines -->
  <!-- 1. Trình duyệt / Client -->
  <rect x="60" y="80" width="140" height="40" class="actor-bar" fill="#3b82f6" />
  <text x="130" y="105" class="actor-txt">Client Browser</text>
  <line x1="130" y1="120" x2="130" y2="510" class="life-line" />

  <!-- 2. Nginx Reverse Proxy -->
  <rect x="280" y="80" width="160" height="40" class="actor-bar" fill="#0f766e" />
  <text x="360" y="105" class="actor-txt">Nginx Proxy (Port 443)</text>
  <line x1="360" y1="120" x2="360" y2="510" class="life-line" />

  <!-- 3. WordPress Core (PHP 8.2) -->
  <rect x="520" y="80" width="160" height="40" class="actor-bar" fill="#2563eb" />
  <text x="600" y="105" class="actor-txt">WordPress (App Tier)</text>
  <line x1="600" y1="120" x2="600" y2="510" class="life-line" />

  <!-- 4. MySQL 8.0 Database -->
  <rect x="750" y="80" width="150" height="40" class="actor-bar" fill="#c2410c" />
  <text x="825" y="105" class="actor-txt">MySQL 8.0 (DB Tier)</text>
  <line x1="825" y1="120" x2="825" y2="510" class="life-line" />

  <!-- Steps -->
  <!-- Step 1: User submits login -->
  <line x1="130" y1="150" x2="355" y2="150" class="msg-line" />
  <text x="145" y="142" class="msg-txt">1. HTTPS POST /wp-login.php (log=tacgia_k23, pwd=***)</text>

  <!-- Step 2: Nginx terminates SSL &amp; forwards -->
  <line x1="360" y1="180" x2="595" y2="180" class="msg-line" />
  <text x="375" y="172" class="msg-txt">2. Proxy Pass (X-Forwarded-For, X-Forwarded-Proto=https)</text>

  <!-- Step 3: WP queries DB -->
  <line x1="600" y1="215" x2="820" y2="215" class="msg-line" />
  <text x="615" y="207" class="msg-txt">3. SELECT * FROM wp_users WHERE user_login = 'tacgia_k23'</text>

  <!-- Step 4: DB returns user row -->
  <line x1="825" y1="250" x2="605" y2="250" class="ret-line" />
  <text x="635" y="242" class="msg-txt" fill="#15803d">4. Trả về hash mật khẩu phpass ($P$B...)</text>

  <!-- Step 5: WP verifies hash -->
  <rect x="585" y="275" width="170" height="36" class="exec-box" />
  <text x="595" y="297" font-family="'Segoe UI', Arial" font-size="11" font-weight="600" fill="#1e3a8a">5. Kiểm tra HMAC-MD5 &amp; Salt</text>

  <!-- Step 6: WP generates Session Cookie -->
  <rect x="585" y="325" width="200" height="36" class="exec-box" />
  <text x="595" y="347" font-family="'Segoe UI', Arial" font-size="11" font-weight="600" fill="#1e3a8a">6. Tạo Cookie wordpress_logged_in_*</text>

  <!-- Step 7: WP responds 302 Found -->
  <line x1="600" y1="380" x2="365" y2="380" class="ret-line" />
  <text x="390" y="372" class="msg-txt" fill="#15803d">7. HTTP 302 Redirect + Set-Cookie (HttpOnly, Secure)</text>

  <!-- Step 8: Nginx forwards to browser -->
  <line x1="360" y1="410" x2="135" y2="410" class="ret-line" />
  <text x="145" y="402" class="msg-txt" fill="#15803d">8. Chuyển hướng trình duyệt tới /wp-admin/</text>

  <!-- Step 9: Browser loads /wp-admin/ with cookie -->
  <line x1="130" y1="450" x2="355" y2="450" class="msg-line" />
  <text x="145" y="442" class="msg-txt">9. GET /wp-admin/ (Kèm Cookie xác thực)</text>

  <!-- Step 10: Nginx &amp; WP return dashboard -->
  <line x1="360" y1="480" x2="135" y2="480" class="ret-line" />
  <text x="145" y="472" class="msg-txt" fill="#15803d">10. Trả về Giao diện Bảng tin tác giả (Author Dashboard)</text>
</svg>"""

create_svg_and_png("fig3_2_seq_login", svg_seq_login)

# 3. Sequence Diagram: Post Publishing
svg_seq_post = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 540" width="950" height="540">
  <defs>
    <style type="text/css"><![CDATA[
      .actor-bar { fill: #1e3a8a; rx: 8; }
      .actor-txt { font-family: 'Segoe UI', Arial; font-size: 13px; font-weight: bold; fill: #ffffff; text-anchor: middle; }
      .life-line { stroke: #94a3b8; stroke-width: 1.5; stroke-dasharray: 4 4; }
      .msg-line { stroke: #2563eb; stroke-width: 1.5; marker-end: url(#arrow); }
      .ret-line { stroke: #10b981; stroke-width: 1.5; stroke-dasharray: 4 2; marker-end: url(#arrow-green); }
      .msg-txt { font-family: 'Segoe UI', Arial; font-size: 11.5px; font-weight: 600; fill: #1e293b; }
      .exec-box { fill: #fef3c7; stroke: #d97706; stroke-width: 1; rx: 4; }
    ]]></style>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#2563eb" />
    </marker>
    <marker id="arrow-green" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#10b981" />
    </marker>
  </defs>

  <rect width="950" height="540" fill="#f8fafc" />
  <rect x="25" y="15" width="900" height="40" rx="8" fill="#1e3a8a" />
  <text x="475" y="40" font-family="'Segoe UI', Arial" font-size="15" font-weight="bold" fill="#ffffff" text-anchor="middle">
    HÌNH 3.3: BIỂU ĐỒ TUẦN TỰ LUỒNG BIÊN SOẠN VÀ XUẤT BẢN BÀI VIẾT KỸ THUẬT
  </text>

  <!-- Lifelines -->
  <rect x="50" y="80" width="130" height="40" class="actor-bar" fill="#f59e0b" />
  <text x="115" y="105" class="actor-txt">Tác giả (Author)</text>
  <line x1="115" y1="120" x2="115" y2="490" class="life-line" />

  <rect x="250" y="80" width="150" height="40" class="actor-bar" fill="#3b82f6" />
  <text x="325" y="105" class="actor-txt">Gutenberg Editor</text>
  <line x1="325" y1="120" x2="325" y2="490" class="life-line" />

  <rect x="470" y="80" width="150" height="40" class="actor-bar" fill="#2563eb" />
  <text x="545" y="105" class="actor-txt">WordPress Core API</text>
  <line x1="545" y1="120" x2="545" y2="490" class="life-line" />

  <rect x="680" y="80" width="130" height="40" class="actor-bar" fill="#059669" />
  <text x="745" y="105" class="actor-txt">Volume /wp_data</text>
  <line x1="745" y1="120" x2="745" y2="490" class="life-line" />

  <rect x="830" y="80" width="100" height="40" class="actor-bar" fill="#c2410c" />
  <text x="880" y="105" class="actor-txt">MySQL 8.0</text>
  <line x1="880" y1="120" x2="880" y2="490" class="life-line" />

  <!-- Flow -->
  <line x1="115" y1="150" x2="320" y2="150" class="msg-line" />
  <text x="130" y="142" class="msg-txt">1. Nhập tiêu đề, nội dung &amp; chọn ảnh đại diện</text>

  <line x1="325" y1="185" x2="540" y2="185" class="msg-line" />
  <text x="340" y="177" class="msg-txt">2. POST /wp-json/wp/v2/media (Tải ảnh lên)</text>

  <line x1="545" y1="215" x2="740" y2="215" class="msg-line" />
  <text x="560" y="207" class="msg-txt">3. Ghi tệp ảnh vào /uploads/2026/10/</text>

  <line x1="745" y1="245" x2="550" y2="245" class="ret-line" />
  <text x="580" y="237" class="msg-txt" fill="#15803d">4. Trả về attachment ID &amp; URL ảnh</text>

  <line x1="115" y1="285" x2="320" y2="285" class="msg-line" />
  <text x="130" y="277" class="msg-txt">5. Nhấn nút "Publish" (Đăng bài)</text>

  <line x1="325" y1="320" x2="540" y2="320" class="msg-line" />
  <text x="340" y="312" class="msg-txt">6. POST /wp-json/wp/v2/posts (status='publish', cat_id=2)</text>

  <!-- MySQL Transaction -->
  <line x1="545" y1="355" x2="875" y2="355" class="msg-line" />
  <text x="560" y="347" class="msg-txt">7. START TRANSACTION</text>

  <line x1="545" y1="385" x2="875" y2="385" class="msg-line" />
  <text x="560" y="377" class="msg-txt">8. INSERT INTO wp_posts (title, content, author, status='publish')</text>

  <line x1="545" y1="415" x2="875" y2="415" class="msg-line" />
  <text x="560" y="407" class="msg-txt">9. INSERT INTO wp_term_relationships (post_id, term_id)</text>

  <line x1="545" y1="445" x2="875" y2="445" class="msg-line" />
  <text x="560" y="437" class="msg-txt">10. COMMIT TRANSACTION</text>

  <line x1="545" y1="475" x2="120" y2="475" class="ret-line" />
  <text x="210" y="467" class="msg-txt" fill="#15803d">11. HTTP 201 Created — Bài viết hiển thị trực tiếp trên trang chủ LyxLab</text>
</svg>"""

create_svg_and_png("fig3_3_seq_post", svg_seq_post)

# 4. Sequence Diagram: Comment Flow
svg_seq_comment = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 520" width="950" height="520">
  <defs>
    <style type="text/css"><![CDATA[
      .actor-bar { fill: #1e3a8a; rx: 8; }
      .actor-txt { font-family: 'Segoe UI', Arial; font-size: 13px; font-weight: bold; fill: #ffffff; text-anchor: middle; }
      .life-line { stroke: #94a3b8; stroke-width: 1.5; stroke-dasharray: 4 4; }
      .msg-line { stroke: #2563eb; stroke-width: 1.5; marker-end: url(#arrow); }
      .ret-line { stroke: #10b981; stroke-width: 1.5; stroke-dasharray: 4 2; marker-end: url(#arrow-green); }
      .msg-txt { font-family: 'Segoe UI', Arial; font-size: 11.5px; font-weight: 600; fill: #1e293b; }
      .exec-box { fill: #eff6ff; stroke: #3b82f6; stroke-width: 1; rx: 4; }
    ]]></style>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#2563eb" />
    </marker>
    <marker id="arrow-green" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#10b981" />
    </marker>
  </defs>

  <rect width="950" height="520" fill="#f8fafc" />
  <rect x="25" y="15" width="900" height="40" rx="8" fill="#1e3a8a" />
  <text x="475" y="40" font-family="'Segoe UI', Arial" font-size="15" font-weight="bold" fill="#ffffff" text-anchor="middle">
    HÌNH 3.4: BIỂU ĐỒ TUẦN TỰ LUỒNG GỬI VÀ PHẢN HỒI BÌNH LUẬN PHÂN CẤP ĐA TẦNG
  </text>

  <!-- Lifelines -->
  <rect x="50" y="80" width="140" height="40" class="actor-bar" fill="#10b981" />
  <text x="120" y="105" class="actor-txt">Độc giả (docgia_k23)</text>
  <line x1="120" y1="120" x2="120" y2="470" class="life-line" />

  <rect x="300" y="80" width="160" height="40" class="actor-bar" fill="#2563eb" />
  <text x="380" y="105" class="actor-txt">WordPress Comments API</text>
  <line x1="380" y1="120" x2="380" y2="470" class="life-line" />

  <rect x="570" y="80" width="140" height="40" class="actor-bar" fill="#c2410c" />
  <text x="640" y="105" class="actor-txt">MySQL (wp_comments)</text>
  <line x1="640" y1="120" x2="640" y2="470" class="life-line" />

  <rect x="780" y="80" width="140" height="40" class="actor-bar" fill="#f59e0b" />
  <text x="850" y="105" class="actor-txt">Tác giả (tacgia_k23)</text>
  <line x1="850" y1="120" x2="850" y2="470" class="life-line" />

  <!-- Flow -->
  <line x1="120" y1="150" x2="375" y2="150" class="msg-line" />
  <text x="135" y="142" class="msg-txt">1. POST /wp-comments-post.php (comment_post_ID=9, comment_parent=0, "Hỏi về...")</text>

  <line x1="380" y1="185" x2="635" y2="185" class="msg-line" />
  <text x="395" y="177" class="msg-txt">2. INSERT INTO wp_comments (comment_parent=0, approved=1)</text>

  <line x1="640" y1="215" x2="385" y2="215" class="ret-line" />
  <text x="430" y="207" class="msg-txt" fill="#15803d">3. Trả về new comment_ID = 2</text>

  <line x1="380" y1="245" x2="125" y2="245" class="ret-line" />
  <text x="145" y="237" class="msg-txt" fill="#15803d">4. Hiển thị bình luận Cấp 1 (Root Comment)</text>

  <line x1="380" y1="275" x2="845" y2="275" class="ret-line" />
  <text x="430" y="267" class="msg-txt" fill="#15803d">5. Thông báo có bình luận mới dưới bài viết của Tác giả</text>

  <line x1="850" y1="320" x2="385" y2="320" class="msg-line" />
  <text x="410" y="312" class="msg-txt">6. Nhấn "Trả lời" (Reply) -> POST comment_parent=2 ("Giải đáp...")</text>

  <line x1="380" y1="355" x2="635" y2="355" class="msg-line" />
  <text x="395" y="347" class="msg-txt">7. INSERT INTO wp_comments (comment_parent=2, approved=1)</text>

  <line x1="640" y1="390" x2="385" y2="390" class="ret-line" />
  <text x="430" y="382" class="msg-txt" fill="#15803d">8. Trả về new comment_ID = 3</text>

  <line x1="380" y1="425" x2="125" y2="425" class="ret-line" />
  <text x="145" y="417" class="msg-txt" fill="#15803d">9. Cập nhật giao diện: Bình luận của Tác giả thụt lề dưới bình luận Độc giả (Threaded)</text>
</svg>"""

create_svg_and_png("fig3_4_seq_comment", svg_seq_comment)

# 5. ERD Diagram
svg_erd = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 980 580" width="980" height="580">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#2563eb" />
    </marker>

    <style type="text/css"><![CDATA[
      .tbl-hdr { fill: #1e3a8a; }
      .tbl-hdr-txt { font-family: 'Segoe UI', Arial; font-size: 13px; font-weight: bold; fill: #ffffff; }
      .tbl-bg { fill: #ffffff; stroke: #cbd5e1; stroke-width: 1.5; rx: 8; }
      .fld-txt { font-family: 'Consolas', monospace; font-size: 11px; fill: #0f172a; }
      .pk-txt { font-family: 'Segoe UI', Arial; font-size: 10px; font-weight: bold; fill: #dc2626; }
      .fk-txt { font-family: 'Segoe UI', Arial; font-size: 10px; font-weight: bold; fill: #2563eb; }
      .rel-line { stroke: #3b82f6; stroke-width: 2; fill: none; }
    ]]></style>
  </defs>

  <rect width="980" height="580" fill="#f8fafc" />
  <rect x="25" y="15" width="930" height="40" rx="8" fill="#1e3a8a" />
  <text x="490" y="40" font-family="'Segoe UI', Arial" font-size="15" font-weight="bold" fill="#ffffff" text-anchor="middle">
    HÌNH 3.5: MÔ HÌNH QUAN HỆ THỰC THỂ (ERD) CÁC BẢNG DỮ LIỆU NGHIỆP VỤ WORDPRESS
  </text>

  <!-- Table 1: wp_users -->
  <g transform="translate(40, 80)">
    <rect width="250" height="190" class="tbl-bg" />
    <rect width="250" height="32" class="tbl-hdr" rx="8" />
    <rect y="20" width="250" height="12" class="tbl-hdr" />
    <text x="12" y="21" class="tbl-hdr-txt">wp_users (Tài khoản người dùng)</text>
    <text x="12" y="52" class="pk-txt">PK</text><text x="35" y="52" class="fld-txt">ID: bigint unsigned (AI)</text>
    <text x="35" y="72" class="fld-txt">user_login: varchar(60)</text>
    <text x="35" y="92" class="fld-txt">user_pass: varchar(255)</text>
    <text x="35" y="112" class="fld-txt">user_nicename: varchar(50)</text>
    <text x="35" y="132" class="fld-txt">user_email: varchar(100)</text>
    <text x="35" y="152" class="fld-txt">user_registered: datetime</text>
    <text x="35" y="172" class="fld-txt">display_name: varchar(250)</text>
  </g>

  <!-- Table 2: wp_posts -->
  <g transform="translate(360, 80)">
    <rect width="270" height="230" class="tbl-bg" />
    <rect width="270" height="32" class="tbl-hdr" rx="8" />
    <rect y="20" width="270" height="12" class="tbl-hdr" />
    <text x="12" y="21" class="tbl-hdr-txt">wp_posts (Bài viết kỹ thuật)</text>
    <text x="12" y="52" class="pk-txt">PK</text><text x="35" y="52" class="fld-txt">ID: bigint unsigned (AI)</text>
    <text x="12" y="72" class="fk-txt">FK</text><text x="35" y="72" class="fld-txt">post_author: bigint unsigned</text>
    <text x="35" y="92" class="fld-txt">post_date: datetime</text>
    <text x="35" y="112" class="fld-txt">post_content: longtext</text>
    <text x="35" y="132" class="fld-txt">post_title: text</text>
    <text x="35" y="152" class="fld-txt">post_status: varchar(20)</text>
    <text x="35" y="172" class="fld-txt">comment_status: varchar(20)</text>
    <text x="35" y="192" class="fld-txt">post_name: varchar(200)</text>
    <text x="35" y="212" class="fld-txt">post_type: varchar(20)</text>
  </g>

  <!-- Table 3: wp_comments -->
  <g transform="translate(690, 80)">
    <rect width="250" height="210" class="tbl-bg" />
    <rect width="250" height="32" class="tbl-hdr" rx="8" />
    <rect y="20" width="250" height="12" class="tbl-hdr" />
    <text x="12" y="21" class="tbl-hdr-txt">wp_comments (Bình luận phân cấp)</text>
    <text x="12" y="52" class="pk-txt">PK</text><text x="35" y="52" class="fld-txt">comment_ID: bigint unsigned</text>
    <text x="12" y="72" class="fk-txt">FK</text><text x="35" y="72" class="fld-txt">comment_post_ID: bigint</text>
    <text x="35" y="92" class="fld-txt">comment_author: tinytext</text>
    <text x="35" y="112" class="fld-txt">comment_content: text</text>
    <text x="35" y="132" class="fld-txt">comment_approved: varchar(20)</text>
    <text x="12" y="152" class="fk-txt">FK</text><text x="35" y="152" class="fld-txt">comment_parent: bigint (Self)</text>
    <text x="12" y="172" class="fk-txt">FK</text><text x="35" y="172" class="fld-txt">user_id: bigint unsigned</text>
  </g>

  <!-- Table 4: wp_terms -->
  <g transform="translate(140, 360)">
    <rect width="220" height="150" class="tbl-bg" />
    <rect width="220" height="32" class="tbl-hdr" rx="8" />
    <rect y="20" width="220" height="12" class="tbl-hdr" />
    <text x="12" y="21" class="tbl-hdr-txt">wp_terms (Chuyên mục)</text>
    <text x="12" y="52" class="pk-txt">PK</text><text x="35" y="52" class="fld-txt">term_id: bigint unsigned</text>
    <text x="35" y="72" class="fld-txt">name: varchar(200)</text>
    <text x="35" y="92" class="fld-txt">slug: varchar(200)</text>
    <text x="35" y="112" class="fld-txt">term_group: bigint</text>
  </g>

  <!-- Table 5: wp_term_taxonomy -->
  <g transform="translate(420, 360)">
    <rect width="240" height="160" class="tbl-bg" />
    <rect width="240" height="32" class="tbl-hdr" rx="8" />
    <rect y="20" width="240" height="12" class="tbl-hdr" />
    <text x="12" y="21" class="tbl-hdr-txt">wp_term_taxonomy</text>
    <text x="12" y="52" class="pk-txt">PK</text><text x="35" y="52" class="fld-txt">term_taxonomy_id: bigint</text>
    <text x="12" y="72" class="fk-txt">FK</text><text x="35" y="72" class="fld-txt">term_id: bigint unsigned</text>
    <text x="35" y="92" class="fld-txt">taxonomy: varchar(32)</text>
    <text x="35" y="112" class="fld-txt">description: longtext</text>
    <text x="35" y="132" class="fld-txt">count: bigint</text>
  </g>

  <!-- Table 6: wp_term_relationships -->
  <g transform="translate(720, 360)">
    <rect width="230" height="130" class="tbl-bg" />
    <rect width="230" height="32" class="tbl-hdr" rx="8" />
    <rect y="20" width="230" height="12" class="tbl-hdr" />
    <text x="12" y="21" class="tbl-hdr-txt">wp_term_relationships</text>
    <text x="12" y="52" class="pk-txt">PK</text><text x="35" y="52" class="fk-txt">object_id (-> wp_posts)</text>
    <text x="12" y="72" class="pk-txt">PK</text><text x="35" y="72" class="fk-txt">term_taxonomy_id</text>
    <text x="35" y="92" class="fld-txt">term_order: int</text>
  </g>

  <!-- Relationship Lines -->
  <!-- wp_users to wp_posts (1 to N) -->
  <line x1="290" y1="130" x2="360" y2="150" class="rel-line" />
  <text x="300" y="135" font-family="'Segoe UI', Arial" font-size="11" font-weight="bold" fill="#2563eb">1:N</text>

  <!-- wp_posts to wp_comments (1 to N) -->
  <line x1="630" y1="150" x2="690" y2="150" class="rel-line" />
  <text x="645" y="142" font-family="'Segoe UI', Arial" font-size="11" font-weight="bold" fill="#2563eb">1:N</text>

  <!-- wp_terms to wp_term_taxonomy (1 to 1) -->
  <line x1="360" y1="430" x2="420" y2="430" class="rel-line" />
  <text x="380" y="422" font-family="'Segoe UI', Arial" font-size="11" font-weight="bold" fill="#2563eb">1:1</text>

  <!-- wp_term_taxonomy to wp_term_relationships (1 to N) -->
  <line x1="660" y1="430" x2="720" y2="430" class="rel-line" />
  <text x="680" y="422" font-family="'Segoe UI', Arial" font-size="11" font-weight="bold" fill="#2563eb">1:N</text>

  <!-- wp_posts to wp_term_relationships (1 to N) -->
  <path d="M 500 310 L 500 335 L 750 335 L 750 360" class="rel-line" stroke-dasharray="4 2" />
</svg>"""

create_svg_and_png("fig3_5_erd", svg_erd)

# 6. Docker 4 Bridge Network Topology
svg_network = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 620" width="1000" height="620">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#2563eb" />
    </marker>

    <style type="text/css"><![CDATA[
      .net-box { fill: #f8fafc; stroke-width: 2; rx: 14; }
      .net-title { font-family: 'Segoe UI', Arial; font-size: 14px; font-weight: bold; }
      .cont-box { fill: #ffffff; stroke-width: 1.5; rx: 8; }
      .cont-name { font-family: 'Consolas', monospace; font-size: 12px; font-weight: bold; fill: #0f172a; }
      .cont-role { font-family: 'Segoe UI', Arial; font-size: 10.5px; fill: #64748b; }
      .bridge-line { stroke-width: 2; fill: none; }
    ]]></style>
  </defs>

  <rect width="1000" height="620" fill="#f8fafc" />
  <rect x="30" y="15" width="940" height="40" rx="8" fill="#1e3a8a" />
  <text x="500" y="40" font-family="'Segoe UI', Arial" font-size="15" font-weight="bold" fill="#ffffff" text-anchor="middle">
    HÌNH 4.2: MÔ HÌNH PHÂN VÙNG MẠNG 4 DOCKER BRIDGE NETWORK ĐỘC LẬP
  </text>

  <!-- External User Traffic -->
  <rect x="50" y="80" width="140" height="45" rx="8" fill="#3b82f6" />
  <text x="120" y="107" font-family="'Segoe UI', Arial" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Internet / Client</text>

  <!-- Network 1: blog_frontend_net (172.28.10.0/24) -->
  <rect x="230" y="70" width="730" height="110" class="net-box" style="stroke: #0284c7; fill: #f0f9ff;" />
  <text x="250" y="95" class="net-title" fill="#0369a1">1. blog_frontend_net (Subnet: 172.28.10.0/24) — Vùng đệm Ingress</text>

  <g transform="translate(250, 110)">
    <rect width="180" height="50" class="cont-box" stroke="#0284c7" />
    <text x="10" y="24" class="cont-name">blog-npm</text>
    <text x="10" y="40" class="cont-role">Nginx Proxy (Ports 80, 443, 81)</text>
  </g>
  <g transform="translate(460, 110)">
    <rect width="180" height="50" class="cont-box" stroke="#0284c7" />
    <text x="10" y="24" class="cont-name">blog-wordpress</text>
    <text x="10" y="40" class="cont-role">App Tier (Port 80 nội bộ)</text>
  </g>
  <g transform="translate(670, 110)">
    <rect width="180" height="50" class="cont-box" stroke="#0284c7" />
    <text x="10" y="24" class="cont-name">blog-phpmyadmin</text>
    <text x="10" y="40" class="cont-role">DB Admin GUI (Port 8081)</text>
  </g>

  <!-- Network 2: blog_backend_net (172.28.20.0/24) -->
  <rect x="230" y="200" width="730" height="110" class="net-box" style="stroke: #c2410c; fill: #fff7ed;" />
  <text x="250" y="225" class="net-title" fill="#c2410c">2. blog_backend_net (Subnet: 172.28.20.0/24) — Vùng CSDL Tuyệt Mật</text>

  <g transform="translate(250, 240)">
    <rect width="180" height="50" class="cont-box" stroke="#c2410c" />
    <text x="10" y="24" class="cont-name">blog-wordpress</text>
    <text x="10" y="40" class="cont-role">Kết nối DB qua port 3306</text>
  </g>
  <g transform="translate(460, 240)">
    <rect width="180" height="50" class="cont-box" stroke="#c2410c" />
    <text x="10" y="24" class="cont-name">blog-mysql</text>
    <text x="10" y="40" class="cont-role">MySQL 8.0 Engine (Port 3306)</text>
  </g>
  <g transform="translate(670, 240)">
    <rect width="180" height="50" class="cont-box" stroke="#c2410c" />
    <text x="10" y="24" class="cont-name">blog-mysqld-exporter</text>
    <text x="10" y="40" class="cont-role">Cào metrics DB (Port 9104)</text>
  </g>

  <!-- Network 3: blog_monitor_net (172.28.30.0/24) -->
  <rect x="230" y="330" width="730" height="140" class="net-box" style="stroke: #7c3aed; fill: #faf5ff;" />
  <text x="250" y="355" class="net-title" fill="#6d28d9">3. blog_monitor_net (Subnet: 172.28.30.0/24) — Kênh Giám Sát Metrics</text>

  <g transform="translate(250, 370)">
    <rect width="170" height="45" class="cont-box" stroke="#7c3aed" />
    <text x="8" y="20" class="cont-name">blog-prometheus</text>
    <text x="8" y="36" class="cont-role">TSDB Server (Port 9090)</text>
  </g>
  <g transform="translate(435, 370)">
    <rect width="170" height="45" class="cont-box" stroke="#7c3aed" />
    <text x="8" y="20" class="cont-name">blog-grafana</text>
    <text x="8" y="36" class="cont-role">Dashboards (Port 3000)</text>
  </g>
  <g transform="translate(620, 370)">
    <rect width="150" height="45" class="cont-box" stroke="#7c3aed" />
    <text x="8" y="20" class="cont-name">blog-cadvisor</text>
    <text x="8" y="36" class="cont-role">Container Metrics (8080)</text>
  </g>
  <g transform="translate(785, 370)">
    <rect width="160" height="45" class="cont-box" stroke="#7c3aed" />
    <text x="8" y="20" class="cont-name">blog-node-exporter</text>
    <text x="8" y="36" class="cont-role">Host Hardware (9100)</text>
  </g>

  <g transform="translate(250, 420)">
    <rect width="210" height="40" class="cont-box" stroke="#7c3aed" />
    <text x="8" y="18" class="cont-name">blog-nginx-exporter</text>
    <text x="8" y="32" class="cont-role">Nginx Stub Status (9113)</text>
  </g>
  <g transform="translate(475, 420)">
    <rect width="240" height="40" class="cont-box" stroke="#7c3aed" />
    <text x="8" y="18" class="cont-name">blog-docker-stats-exporter</text>
    <text x="8" y="32" class="cont-role">Docker Engine Metrics (9487)</text>
  </g>

  <!-- Network 4: blog_logging_net (172.28.40.0/24) -->
  <rect x="230" y="490" width="730" height="110" class="net-box" style="stroke: #059669; fill: #ecfdf5;" />
  <text x="250" y="515" class="net-title" fill="#047857">4. blog_logging_net (Subnet: 172.28.40.0/24) — Kênh Thu Thập Log Tập Trung</text>

  <g transform="translate(250, 530)">
    <rect width="220" height="50" class="cont-box" stroke="#059669" />
    <text x="10" y="24" class="cont-name">blog-promtail</text>
    <text x="10" y="40" class="cont-role">Agent đọc socket /var/run/docker.sock</text>
  </g>
  <g transform="translate(500, 530)">
    <rect width="200" height="50" class="cont-box" stroke="#059669" />
    <text x="10" y="24" class="cont-name">blog-loki</text>
    <text x="10" y="40" class="cont-role">Loki Engine Server (Port 3100)</text>
  </g>

  <!-- Connection from Client to NPM -->
  <line x1="190" y1="105" x2="250" y2="125" stroke="#3b82f6" stroke-width="2.5" marker-end="url(#arrow)" />
</svg>"""

create_svg_and_png("fig4_2_network", svg_network)

# 7. Monitoring Architecture (Prometheus TSDB + 5 Exporters)
svg_monitoring = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 980 540" width="980" height="540">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#2563eb" />
    </marker>

    <style type="text/css"><![CDATA[
      .hdr-bar { fill: #1e3a8a; rx: 8; }
      .hdr-txt { font-family: 'Segoe UI', Arial; font-size: 15px; font-weight: bold; fill: #ffffff; text-anchor: middle; }
      .tier-box { fill: #ffffff; stroke-width: 1.5; rx: 12; }
      .box-title { font-family: 'Segoe UI', Arial; font-size: 13px; font-weight: bold; }
      .item-box { fill: #f8fafc; stroke-width: 1; rx: 6; }
      .item-name { font-family: 'Consolas', monospace; font-size: 11.5px; font-weight: bold; fill: #0f172a; }
      .item-desc { font-family: 'Segoe UI', Arial; font-size: 10px; fill: #64748b; }
      .scrape-arrow { stroke: #ea580c; stroke-width: 1.5; stroke-dasharray: 4 2; }
    ]]></style>
  </defs>

  <rect width="980" height="540" fill="#f8fafc" />
  <rect x="25" y="15" width="930" height="40" class="hdr-bar" />
  <text x="490" y="40" class="hdr-txt">HÌNH 4.5: KIẾN TRÚC GIÁM SÁT METRICS ĐA TẦNG VỚI PROMETHEUS VÀ 5 EXPORTERS</text>

  <!-- 1. Exporters Tier -->
  <rect x="35" y="75" width="280" height="440" class="tier-box" stroke="#ea580c" />
  <text x="50" y="105" class="box-title" fill="#c2410c">TẦNG 1: 5 EXPORTERS (DATA PRODUCERS)</text>

  <g transform="translate(50, 125)">
    <rect width="250" height="60" class="item-box" stroke="#fdba74" />
    <text x="12" y="25" class="item-name">Node Exporter (:9100)</text>
    <text x="12" y="45" class="item-desc">CPU, RAM, Disk I/O, Băng thông máy chủ</text>
  </g>

  <g transform="translate(50, 200)">
    <rect width="250" height="60" class="item-box" stroke="#fdba74" />
    <text x="12" y="25" class="item-name">cAdvisor (:8080)</text>
    <text x="12" y="45" class="item-desc">Mức tiêu thụ CPU/RAM từng Container</text>
  </g>

  <g transform="translate(50, 275)">
    <rect width="250" height="60" class="item-box" stroke="#fdba74" />
    <text x="12" y="25" class="item-name">MySQL Exporter (:9104)</text>
    <text x="12" y="45" class="item-desc">Queries/s, InnoDB Buffer Pool, Threads</text>
  </g>

  <g transform="translate(50, 350)">
    <rect width="250" height="60" class="item-box" stroke="#fdba74" />
    <text x="12" y="25" class="item-name">Nginx Exporter (:9113)</text>
    <text x="12" y="45" class="item-desc">Active Connections, Requests/s, Handled</text>
  </g>

  <g transform="translate(50, 425)">
    <rect width="250" height="60" class="item-box" stroke="#fdba74" />
    <text x="12" y="25" class="item-name">Docker Stats Exporter (:9487)</text>
    <text x="12" y="45" class="item-desc">Trạng thái sống còn, Network I/O Container</text>
  </g>

  <!-- 2. Storage Tier (Prometheus) -->
  <rect x="360" y="75" width="280" height="440" class="tier-box" stroke="#2563eb" />
  <text x="380" y="105" class="box-title" fill="#1e40af">TẦNG 2: PROMETHEUS TSDB (CORE)</text>

  <g transform="translate(375, 130)">
    <rect width="250" height="100" rx="8" fill="#eff6ff" stroke="#93c5fd" />
    <text x="15" y="30" class="item-name" fill="#1e3a8a">Pull Engine (Scraper)</text>
    <text x="15" y="55" class="item-desc">• Chu kỳ cào dữ liệu: scrape_interval = 15s</text>
    <text x="15" y="75" class="item-desc">• Timeout: scrape_timeout = 10s</text>
  </g>

  <g transform="translate(375, 250)">
    <rect width="250" height="110" rx="8" fill="#eff6ff" stroke="#93c5fd" />
    <text x="15" y="30" class="item-name" fill="#1e3a8a">TSDB Storage Engine</text>
    <text x="15" y="55" class="item-desc">• Định dạng khối thời gian: 2h block chunk</text>
    <text x="15" y="75" class="item-desc">• Nén dữ liệu: Gorilla float compression</text>
    <text x="15" y="95" class="item-desc">• Thời hạn lưu trữ: retention.time = 15d</text>
  </g>

  <g transform="translate(375, 380)">
    <rect width="250" height="110" rx="8" fill="#eff6ff" stroke="#93c5fd" />
    <text x="15" y="30" class="item-name" fill="#1e3a8a">PromQL Query Engine</text>
    <text x="15" y="55" class="item-desc">• Hỗ trợ tính toán rate(), irate(), sum()</text>
    <text x="15" y="75" class="item-desc">• Đánh giá rule cảnh báo: evaluation = 15s</text>
    <text x="15" y="95" class="item-desc">• Cung cấp REST API trên cổng 9090</text>
  </g>

  <!-- 3. Visualization Tier (Grafana) -->
  <rect x="680" y="75" width="265" height="440" class="tier-box" stroke="#7c3aed" />
  <text x="700" y="105" class="box-title" fill="#6d28d9">TẦNG 3: GRAFANA DASHBOARDS</text>

  <g transform="translate(695, 130)">
    <rect width="235" height="65" class="item-box" stroke="#d8b4fe" />
    <text x="10" y="25" class="item-name">Dashboard: Node Exporter Full</text>
    <text x="10" y="45" class="item-desc">Giám sát tải CPU, RAM &amp; Disk Host</text>
  </g>
  <g transform="translate(695, 210)">
    <rect width="235" height="65" class="item-box" stroke="#d8b4fe" />
    <text x="10" y="25" class="item-name">Dashboard: Docker cAdvisor</text>
    <text x="10" y="45" class="item-desc">Tài nguyên &amp; giới hạn 13 Containers</text>
  </g>
  <g transform="translate(695, 290)">
    <rect width="235" height="65" class="item-box" stroke="#d8b4fe" />
    <text x="10" y="25" class="item-name">Dashboard: MySQL Overview</text>
    <text x="10" y="45" class="item-desc">Hiệu năng truy vấn &amp; InnoDB Buffer Pool</text>
  </g>
  <g transform="translate(695, 370)">
    <rect width="235" height="65" class="item-box" stroke="#d8b4fe" />
    <text x="10" y="25" class="item-name">Dashboard: Nginx Proxy</text>
    <text x="10" y="45" class="item-desc">Lưu lượng truy cập &amp; tỷ lệ phản hồi HTTP</text>
  </g>

  <!-- Lines -->
  <!-- Scrape arrow from Prom to Exporters -->
  <line x1="375" y1="180" x2="315" y2="180" stroke="#ea580c" stroke-width="2" marker-end="url(#arrow)" />
  <text x="325" y="172" font-family="'Segoe UI', Arial" font-size="10" font-weight="bold" fill="#ea580c">PULL</text>

  <!-- Query arrow from Grafana to Prom -->
  <line x1="695" y1="280" x2="640" y2="280" stroke="#7c3aed" stroke-width="2" marker-end="url(#arrow)" />
  <text x="645" y="272" font-family="'Segoe UI', Arial" font-size="10" font-weight="bold" fill="#7c3aed">PromQL</text>
</svg>"""

create_svg_and_png("fig4_5_monitoring", svg_monitoring)

# 8. Logging Pipeline Architecture (Docker Socket -> Promtail -> Loki -> Grafana)
svg_logging = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 980 500" width="980" height="500">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#2563eb" />
    </marker>

    <style type="text/css"><![CDATA[
      .hdr-bar { fill: #1e3a8a; rx: 8; }
      .hdr-txt { font-family: 'Segoe UI', Arial; font-size: 15px; font-weight: bold; fill: #ffffff; text-anchor: middle; }
      .step-box { fill: #ffffff; stroke-width: 1.5; rx: 12; }
      .step-title { font-family: 'Segoe UI', Arial; font-size: 13px; font-weight: bold; }
      .item-name { font-family: 'Consolas', monospace; font-size: 11px; font-weight: bold; fill: #0f172a; }
      .item-desc { font-family: 'Segoe UI', Arial; font-size: 10px; fill: #64748b; }
      .flow-arrow { stroke: #059669; stroke-width: 2.5; fill: none; }
    ]]></style>
  </defs>

  <rect width="980" height="500" fill="#f8fafc" />
  <rect x="25" y="15" width="930" height="40" class="hdr-bar" />
  <text x="490" y="40" class="hdr-txt">HÌNH 4.6: ĐƯỜNG ỐNG THU THẬP VÀ TRUY VẤN NHẬT KÝ TẬP TRUNG PROMTAIL - LOKI - LOGQL</text>

  <!-- Step 1: Docker Containers Logs -->
  <rect x="35" y="80" width="200" height="380" class="step-box" stroke="#0284c7" />
  <text x="50" y="110" class="step-title" fill="#0369a1">1. DOCKER HOST LOGS</text>

  <g transform="translate(50, 130)">
    <rect width="170" height="50" rx="6" fill="#f0f9ff" stroke="#bae6fd" />
    <text x="10" y="22" class="item-name">stdout / stderr</text>
    <text x="10" y="40" class="item-desc">Mọi container xả log qua console</text>
  </g>
  <g transform="translate(50, 195)">
    <rect width="170" height="60" rx="6" fill="#f0f9ff" stroke="#bae6fd" />
    <text x="10" y="22" class="item-name">JSON-file Logging</text>
    <text x="10" y="40" class="item-desc">/var/lib/docker/containers/</text>
    <text x="10" y="52" class="item-desc">[id]/[id]-json.log</text>
  </g>
  <g transform="translate(50, 270)">
    <rect width="170" height="60" rx="6" fill="#f0f9ff" stroke="#bae6fd" />
    <text x="10" y="22" class="item-name">Docker Engine Socket</text>
    <text x="10" y="40" class="item-desc">/var/run/docker.sock</text>
    <text x="10" y="52" class="item-desc">(Gắn kết Read-Only :ro)</text>
  </g>

  <!-- Step 2: Promtail Agent -->
  <rect x="270" y="80" width="210" height="380" class="step-box" stroke="#059669" />
  <text x="285" y="110" class="step-title" fill="#047857">2. PROMTAIL AGENT</text>

  <g transform="translate(285, 130)">
    <rect width="180" height="65" rx="6" fill="#ecfdf5" stroke="#a7f3d0" />
    <text x="10" y="22" class="item-name">Service Discovery</text>
    <text x="10" y="40" class="item-desc">Tự động phát hiện 13 containers</text>
    <text x="10" y="54" class="item-desc">qua docker_sd_configs</text>
  </g>
  <g transform="translate(285, 210)">
    <rect width="180" height="75" rx="6" fill="#ecfdf5" stroke="#a7f3d0" />
    <text x="10" y="22" class="item-name">Relabeling Engine</text>
    <text x="10" y="40" class="item-desc">Gắn nhãn nhận diện tự động:</text>
    <text x="10" y="54" class="item-desc">• container = [tên container]</text>
    <text x="10" y="68" class="item-desc">• job = "container-logs"</text>
  </g>
  <g transform="translate(285, 300)">
    <rect width="180" height="65" rx="6" fill="#ecfdf5" stroke="#a7f3d0" />
    <text x="10" y="22" class="item-name">Buffer &amp; Push Batch</text>
    <text x="10" y="40" class="item-desc">Gom nhóm dòng log theo batch</text>
    <text x="10" y="54" class="item-desc">Đẩy về Loki qua HTTP/gRPC</text>
  </g>

  <!-- Step 3: Grafana Loki Engine -->
  <rect x="515" y="80" width="210" height="380" class="step-box" stroke="#ea580c" />
  <text x="530" y="110" class="step-title" fill="#c2410c">3. GRAFANA LOKI 3.0</text>

  <g transform="translate(530, 130)">
    <rect width="180" height="65" rx="6" fill="#fff7ed" stroke="#fed7aa" />
    <text x="10" y="22" class="item-name">Ingester &amp; Indexer</text>
    <text x="10" y="40" class="item-desc">Chỉ đánh chỉ mục nhãn (Labels)</text>
    <text x="10" y="54" class="item-desc">Tiết kiệm RAM tới 90% so với ELK</text>
  </g>
  <g transform="translate(530, 210)">
    <rect width="180" height="75" rx="6" fill="#fff7ed" stroke="#fed7aa" />
    <text x="10" y="22" class="item-name">Compressed Chunks</text>
    <text x="10" y="40" class="item-desc">Nén toàn bộ nội dung dòng log</text>
    <text x="10" y="54" class="item-desc">bằng giải thuật Snappy / gzip</text>
    <text x="10" y="68" class="item-desc">Lưu trong volume loki_data</text>
  </g>
  <g transform="translate(530, 300)">
    <rect width="180" height="65" rx="6" fill="#fff7ed" stroke="#fed7aa" />
    <text x="10" y="22" class="item-name">Querier API (:3100)</text>
    <text x="10" y="40" class="item-desc">Xử lý biểu thức lọc chuỗi LogQL</text>
    <text x="10" y="54" class="item-desc">Phục vụ truy vết thời gian thực</text>
  </g>

  <!-- Step 4: Grafana Explore -->
  <rect x="760" y="80" width="195" height="380" class="step-box" stroke="#7c3aed" />
  <text x="775" y="110" class="step-title" fill="#6d28d9">4. GRAFANA EXPLORE</text>

  <g transform="translate(775, 130)">
    <rect width="165" height="75" rx="6" fill="#faf5ff" stroke="#e9d5ff" />
    <text x="8" y="22" class="item-name">Log Stream Selector</text>
    <text x="8" y="40" class="item-desc">{container="blog-npm"}</text>
    <text x="8" y="54" class="item-desc">{container="blog-mysql"}</text>
    <text x="8" y="68" class="item-desc">Live tail dòng log tức thì</text>
  </g>
  <g transform="translate(775, 220)">
    <rect width="165" height="75" rx="6" fill="#faf5ff" stroke="#e9d5ff" />
    <text x="8" y="22" class="item-name">LogQL Filter Expressions</text>
    <text x="8" y="40" class="item-desc">|~ "HTTP/[0-9.]+ [45][0-9][0-9]"</text>
    <text x="8" y="54" class="item-desc">Lọc lỗi 4xx/5xx chính xác</text>
    <text x="8" y="68" class="item-desc">không cần regex phức tạp</text>
  </g>
  <g transform="translate(775, 310)">
    <rect width="165" height="75" rx="6" fill="#faf5ff" stroke="#e9d5ff" />
    <text x="8" y="22" class="item-name">Metric Queries (Rate)</text>
    <text x="8" y="40" class="item-desc">rate({container=...}[5m])</text>
    <text x="8" y="54" class="item-desc">Vẽ biểu đồ tần suất phát sinh</text>
    <text x="8" y="68" class="item-desc">nhật ký sự kiện theo thời gian</text>
  </g>

  <!-- Flow Arrows -->
  <line x1="235" y1="200" x2="265" y2="200" stroke="#059669" stroke-width="2.5" marker-end="url(#arrow)" />
  <line x1="480" y1="200" x2="510" y2="200" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrow)" />
  <line x1="725" y1="200" x2="755" y2="200" stroke="#7c3aed" stroke-width="2.5" marker-end="url(#arrow)" />
</svg>"""

create_svg_and_png("fig4_6_logging", svg_logging)

print("🎉 ALL 8 ARCHITECTURAL DIAGRAMS GENERATED SUCCESSFULLY!")
