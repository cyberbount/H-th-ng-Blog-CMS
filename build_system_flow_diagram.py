import os
import cairosvg

def generate_flow_diagram():
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1360" width="1920" height="1360">
  <defs>
    <style type="text/css"><![CDATA[
      .title-main { font-family: 'Segoe UI', Arial, sans-serif; font-size: 24px; font-weight: 800; fill: #ffffff; letter-spacing: -0.5px; }
      .title-sub { font-family: 'Segoe UI', Arial, sans-serif; font-size: 13px; font-weight: 500; fill: #93c5fd; }
      .zone-box { rx: 14; stroke-width: 2; fill-opacity: 0.85; }
      .zone-title { font-family: 'Segoe UI', Arial, sans-serif; font-size: 14px; font-weight: 700; }
      .zone-sub { font-family: 'Consolas', monospace; font-size: 11px; font-weight: 600; fill: #64748b; }
      
      .card-cont { fill: #ffffff; rx: 10; stroke-width: 1.5; filter: drop-shadow(0 2px 4px rgba(0,0,0,0.04)); }
      .card-hdr { font-family: 'Consolas', monospace; font-size: 13px; font-weight: 800; }
      .card-tag { font-family: 'Segoe UI', Arial, sans-serif; font-size: 10.5px; font-weight: 700; fill: #ffffff; rx: 4; }
      .card-desc { font-family: 'Segoe UI', Arial, sans-serif; font-size: 11px; fill: #475569; }
      .card-port { font-family: 'Consolas', monospace; font-size: 10.5px; font-weight: 600; fill: #0284c7; }
      
      .actor-card { fill: #ffffff; rx: 10; stroke: #94a3b8; stroke-width: 1.5; }
      .actor-name { font-family: 'Segoe UI', Arial, sans-serif; font-size: 13px; font-weight: 700; fill: #0f172a; }
      .actor-role { font-family: 'Segoe UI', Arial, sans-serif; font-size: 10.5px; fill: #64748b; }
      
      .vol-box { fill: #ffffff; rx: 8; stroke: #d97706; stroke-width: 1.2; stroke-dasharray: 4 2; }
      .vol-text { font-family: 'Consolas', monospace; font-size: 10.5px; font-weight: 700; fill: #b45309; text-anchor: middle; }
      
      .badge-step { font-family: 'Segoe UI', Arial, sans-serif; font-size: 10px; font-weight: 800; fill: #ffffff; text-anchor: middle; }
      .flow-label { font-family: 'Segoe UI', Arial, sans-serif; font-size: 10.5px; font-weight: 600; }
    ]]></style>

    <!-- Markers -->
    <marker id="arr-blue" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#2563eb" />
    </marker>
    <marker id="arr-purple" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#7c3aed" />
    </marker>
    <marker id="arr-green" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#059669" />
    </marker>
    <marker id="arr-amber" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#d97706" />
    </marker>
    <marker id="arr-slate" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#475569" />
    </marker>
  </defs>

  <!-- Background Base -->
  <rect width="1920" height="1360" fill="#f8fafc" />

  <!-- ==================== HEADER BAR ==================== -->
  <rect x="25" y="20" width="1870" height="85" rx="12" fill="#1e3a8a" />
  <text x="50" y="55" class="title-main">SƠ ĐỒ LUỒNG ĐIỀU PHỐI VÀ DỮ LIỆU HỆ THỐNG TỔNG QUAN (END-TO-END SYSTEM FLOW)</text>
  <text x="50" y="82" class="title-sub">HỆ THỐNG BLOG CMS LYXLAB — KIẾN TRÚC 13 CONTAINERS | 4 DOCKER BRIDGE NETWORKS | 3 ĐƯỜNG DẪN DỮ LIỆU ĐỘC LẬP</text>
  
  <rect x="1560" y="38" width="310" height="38" rx="6" fill="#1e40af" stroke="#3b82f6" stroke-width="1" />
  <text x="1715" y="62" font-family="'Segoe UI', Arial" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">ICTU K23A — THỰC HÀNH CHUYÊN ĐỀ</text>

  <!-- ==================== FLOW LEGEND BAR ==================== -->
  <rect x="25" y="115" width="1870" height="42" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5" />
  
  <!-- Flow 1 Legend -->
  <line x1="45" y1="136" x2="80" y2="136" stroke="#2563eb" stroke-width="3" marker-end="url(#arr-blue)" />
  <text x="90" y="140" font-family="'Segoe UI', Arial" font-size="12" font-weight="bold" fill="#1e40af">Luồng 1: Nghiệp vụ Web &amp; CSDL (HTTP/HTTPS &amp; SQL Query)</text>

  <!-- Flow 2 Legend -->
  <line x1="560" y1="136" x2="595" y2="136" stroke="#7c3aed" stroke-width="3" stroke-dasharray="6 3" marker-end="url(#arr-purple)" />
  <text x="605" y="140" font-family="'Segoe UI', Arial" font-size="12" font-weight="bold" fill="#6d28d9">Luồng 2: Giám sát Chuỗi thời gian (Prometheus Metrics PULL 15s)</text>

  <!-- Flow 3 Legend -->
  <line x1="1100" y1="136" x2="1135" y2="136" stroke="#059669" stroke-width="3" stroke-dasharray="4 2" marker-end="url(#arr-green)" />
  <text x="1145" y="140" font-family="'Segoe UI', Arial" font-size="12" font-weight="bold" fill="#047857">Luồng 3: Thu thập Nhật ký Tập trung (Promtail Socket ➔ Loki PUSH)</text>

  <!-- Flow 4 Legend -->
  <line x1="1620" y1="136" x2="1655" y2="136" stroke="#d97706" stroke-width="2.5" stroke-dasharray="2 2" marker-end="url(#arr-amber)" />
  <text x="1665" y="140" font-family="'Segoe UI', Arial" font-size="12" font-weight="bold" fill="#b45309">Lưu trữ Bền vững (Named Volumes)</text>

  <!-- ==================== CỘT 1: CLIENTS & OPERATORS (BÊN TRÁI) ==================== -->
  <rect x="25" y="170" width="230" height="950" rx="12" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" />
  <rect x="25" y="170" width="230" height="40" rx="12" fill="#f1f5f9" />
  <text x="140" y="195" font-family="'Segoe UI', Arial" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">👤 TÁC NHÂN (ACTORS)</text>

  <!-- Actor 1: Admin -->
  <g transform="translate(40, 225)">
    <rect width="200" height="65" class="actor-card" stroke="#ef4444" />
    <circle cx="28" cy="32" r="14" fill="#fee2e2" stroke="#ef4444" stroke-width="1.5" />
    <text x="28" y="37" font-size="14" text-anchor="middle">👑</text>
    <text x="52" y="27" class="actor-name">Quản trị viên (Admin)</text>
    <text x="52" y="44" class="actor-role">User: bount</text>
    <text x="52" y="58" class="card-desc" font-size="9.5">Toàn quyền hệ thống &amp; NPM</text>
  </g>

  <!-- Actor 2: Author -->
  <g transform="translate(40, 305)">
    <rect width="200" height="65" class="actor-card" stroke="#f59e0b" />
    <circle cx="28" cy="32" r="14" fill="#fef3c7" stroke="#f59e0b" stroke-width="1.5" />
    <text x="28" y="37" font-size="14" text-anchor="middle">✍️</text>
    <text x="52" y="27" class="actor-name">Tác giả (Author)</text>
    <text x="52" y="44" class="actor-role">User: tacgia_k23</text>
    <text x="52" y="58" class="card-desc" font-size="9.5">Viết bài &amp; quản lý ảnh Media</text>
  </g>

  <!-- Actor 3: Reader -->
  <g transform="translate(40, 385)">
    <rect width="200" height="65" class="actor-card" stroke="#10b981" />
    <circle cx="28" cy="32" r="14" fill="#d1fae5" stroke="#10b981" stroke-width="1.5" />
    <text x="28" y="37" font-size="14" text-anchor="middle">📖</text>
    <text x="52" y="27" class="actor-name">Độc giả (Subscriber)</text>
    <text x="52" y="44" class="actor-role">User: docgia_k23</text>
    <text x="52" y="58" class="card-desc" font-size="9.5">Bình luận trao đổi kỹ thuật</text>
  </g>

  <!-- Actor 4: Guest -->
  <g transform="translate(40, 465)">
    <rect width="200" height="65" class="actor-card" stroke="#64748b" />
    <circle cx="28" cy="32" r="14" fill="#f1f5f9" stroke="#64748b" stroke-width="1.5" />
    <text x="28" y="37" font-size="14" text-anchor="middle">🌐</text>
    <text x="52" y="27" class="actor-name">Khách vãng lai</text>
    <text x="52" y="44" class="actor-role">Public Web Visitors</text>
    <text x="52" y="58" class="card-desc" font-size="9.5">Đọc bài &amp; tra cứu nghiên cứu</text>
  </g>

  <!-- Actor 5: DevOps Engineer / SRE -->
  <g transform="translate(40, 720)">
    <rect width="200" height="80" class="actor-card" stroke="#7c3aed" fill="#faf5ff" />
    <circle cx="28" cy="40" r="14" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5" />
    <text x="28" y="45" font-size="14" text-anchor="middle">🛠️</text>
    <text x="52" y="30" class="actor-name" fill="#6d28d9">Kỹ sư DevOps / SRE</text>
    <text x="52" y="48" class="actor-role">Giám sát &amp; Quản trị vận hành</text>
    <text x="52" y="65" class="card-desc" font-size="9.5">• Xem Dashboard Grafana (:3000)</text>
    <text x="52" y="76" class="card-desc" font-size="9.5">• Truy vấn PromQL &amp; LogQL</text>
  </g>

  <!-- Protocol Badges at Actor Output -->
  <rect x="60" y="555" width="160" height="26" rx="13" fill="#eff6ff" stroke="#3b82f6" />
  <text x="140" y="572" font-family="'Segoe UI', Arial" font-size="11" font-weight="bold" fill="#1e40af" text-anchor="middle">HTTPS :443 / HTTP :80</text>

  <rect x="60" y="820" width="160" height="26" rx="13" fill="#f5f3ff" stroke="#7c3aed" />
  <text x="140" y="837" font-family="'Segoe UI', Arial" font-size="11" font-weight="bold" fill="#6d28d9" text-anchor="middle">Grafana UI :3000</text>

  <!-- ==================== PHÂN VÙNG 1: blog_frontend_net ==================== -->
  <rect x="280" y="170" width="860" height="360" class="zone-box" fill="#f0f9ff" stroke="#0284c7" />
  <rect x="295" y="182" width="400" height="28" rx="6" fill="#e0f2fe" />
  <text x="310" y="201" class="zone-title" fill="#0369a1">MẠNG 1: blog_frontend_net (Subnet: 172.28.10.0/24)</text>

  <!-- Container 1: blog-npm -->
  <g transform="translate(305, 225)">
    <rect width="250" height="185" class="card-cont" stroke="#0284c7" />
    <rect x="12" y="12" width="70" height="20" rx="4" fill="#0284c7" />
    <text x="47" y="26" class="card-tag" text-anchor="middle">INGRESS</text>
    <text x="90" y="27" class="card-hdr" fill="#0369a1">blog-npm</text>
    <text x="12" y="52" class="card-desc" font-weight="bold">Nginx Proxy Manager Gateway</text>
    <text x="12" y="70" class="card-desc">• Giải mã SSL/TLS 1.3 (SAN tự ký)</text>
    <text x="12" y="88" class="card-desc">• WAF: Chặn SQLi, XSS (block-exploits)</text>
    <text x="12" y="106" class="card-desc">• Chuyển tiếp cổng HTTP Reverse Proxy</text>
    <text x="12" y="124" class="card-desc">• Bảo vệ Security Headers (HSTS, nosniff)</text>
    <line x1="12" y1="135" x2="238" y2="135" stroke="#e2e8f0" stroke-width="1" />
    <text x="12" y="152" class="card-port">Cổng Host: 80:80, 443:443, 81:81</text>
    <text x="12" y="170" class="card-desc" font-size="10">Volumes: npm_data, npm_ssl</text>
  </g>

  <!-- Container 2: blog-wordpress -->
  <g transform="translate(585, 225)">
    <rect width="265" height="185" class="card-cont" stroke="#2563eb" />
    <rect x="12" y="12" width="60" height="20" rx="4" fill="#2563eb" />
    <text x="42" y="26" class="card-tag" text-anchor="middle">APP TIER</text>
    <text x="80" y="27" class="card-hdr" fill="#1d4ed8">blog-wordpress</text>
    <text x="12" y="52" class="card-desc" font-weight="bold">WordPress 6.7.1 (PHP 8.2 + Apache)</text>
    <text x="12" y="70" class="card-desc">• Theme Astra + Modern Design Tokens</text>
    <text x="12" y="88" class="card-desc">• Plugin mu-plugin `lyxlab-hero.php`</text>
    <text x="12" y="106" class="card-desc">• Xác thực Nonce &amp; Cookie HMAC phpass</text>
    <text x="12" y="124" class="card-desc">• Prepared Statements chống SQLi</text>
    <line x1="12" y1="135" x2="253" y2="135" stroke="#e2e8f0" stroke-width="1" />
    <text x="12" y="152" class="card-port">Cổng Host: 8080:80 (Nội bộ :80)</text>
    <text x="12" y="170" class="card-desc" font-size="10">Tham gia: frontend_net, backend_net</text>
  </g>

  <!-- Container 3: blog-phpmyadmin -->
  <g transform="translate(875, 225)">
    <rect width="245" height="185" class="card-cont" stroke="#f59e0b" />
    <rect x="12" y="12" width="60" height="20" rx="4" fill="#d97706" />
    <text x="42" y="26" class="card-tag" text-anchor="middle">DB GUI</text>
    <text x="80" y="27" class="card-hdr" fill="#b45309">blog-phpmyadmin</text>
    <text x="12" y="52" class="card-desc" font-weight="bold">phpMyAdmin Web Database Tool</text>
    <text x="12" y="70" class="card-desc">• Quản trị đồ họa trực quan CSDL</text>
    <text x="12" y="88" class="card-desc">• Đăng nhập bằng `wp_user` an toàn</text>
    <text x="12" y="106" class="card-desc">• Kiểm tra bản ghi bài viết &amp; bình luận</text>
    <text x="12" y="124" class="card-desc">• Tra cứu bảng `wp_posts`, `wp_comments`</text>
    <line x1="12" y1="135" x2="233" y2="135" stroke="#e2e8f0" stroke-width="1" />
    <text x="12" y="152" class="card-port">Cổng Host: 8081:80 (Nội bộ :80)</text>
    <text x="12" y="170" class="card-desc" font-size="10">Tham gia: frontend_net, backend_net</text>
  </g>

  <!-- Nginx Exporter inside frontend_net -->
  <g transform="translate(305, 430)">
    <rect width="250" height="85" class="card-cont" stroke="#0ea5e9" />
    <text x="12" y="24" class="card-hdr" fill="#0369a1" font-size="12">blog-nginx-exporter</text>
    <text x="12" y="42" class="card-desc">Cào stub_status lưu lượng kết nối Web</text>
    <text x="12" y="60" class="card-port">Cổng: :9113 | Active, Handled, Requests</text>
    <text x="12" y="76" class="card-desc" font-size="9.5">Tham gia: frontend_net, monitor_net</text>
  </g>

  <!-- ==================== PHÂN VÙNG 2: blog_backend_net ==================== -->
  <rect x="1170" y="170" width="725" height="360" class="zone-box" fill="#fff7ed" stroke="#ea580c" />
  <rect x="1185" y="182" width="460" height="28" rx="6" fill="#ffedd5" />
  <text x="1200" y="201" class="zone-title" fill="#c2410c">MẠNG 2: blog_backend_net (Subnet: 172.28.20.0/24) — CSDL CÔ LẬP</text>

  <!-- Container 4: blog-mysql -->
  <g transform="translate(1190, 225)">
    <rect width="320" height="195" class="card-cont" stroke="#ea580c" />
    <rect x="12" y="12" width="70" height="20" rx="4" fill="#c2410c" />
    <text x="47" y="26" class="card-tag" text-anchor="middle">DATABASE</text>
    <text x="90" y="27" class="card-hdr" fill="#9a3412">blog-mysql</text>
    <text x="12" y="52" class="card-desc" font-weight="bold">MySQL 8.0 Relational Database Engine</text>
    <text x="12" y="70" class="card-desc">• Bộ đệm nhớ InnoDB Buffer Pool tối ưu</text>
    <text x="12" y="88" class="card-desc">• Collation: utf8mb4_unicode_520_ci</text>
    <text x="12" y="106" class="card-desc">• Tài khoản ứng dụng: `wp_user` (Least Priv)</text>
    <text x="12" y="124" class="card-desc">• Cơ sở dữ liệu nghiệp vụ: `wordpress_db`</text>
    <line x1="12" y1="135" x2="308" y2="135" stroke="#e2e8f0" stroke-width="1" />
    <text x="12" y="152" class="card-port">Cổng Host: 3308:3306 (Nội bộ :3306)</text>
    <text x="12" y="170" class="card-desc" font-size="10" fill="#dc2626" font-weight="bold">🛡️ CẤM TRUY CẬP TRỰC TIẾP TỪ FRONTEND/NPM</text>
    <text x="12" y="187" class="card-desc" font-size="9.5">Volume: mysql_data | Hardening: 1GB RAM limit</text>
  </g>

  <!-- Container 5: blog-mysqld-exporter -->
  <g transform="translate(1535, 225)">
    <rect width="335" height="195" class="card-cont" stroke="#f97316" />
    <rect x="12" y="12" width="80" height="20" rx="4" fill="#ea580c" />
    <text x="52" y="26" class="card-tag" text-anchor="middle">EXPORTER</text>
    <text x="100" y="27" class="card-hdr" fill="#9a3412">blog-mysqld-exporter</text>
    <text x="12" y="52" class="card-desc" font-weight="bold">MySQL Prometheus Exporter</text>
    <text x="12" y="70" class="card-desc">• Kết nối MySQL bằng tài khoản readonly riêng</text>
    <text x="12" y="88" class="card-desc">• Cấu hình file bí mật: `.my.cnf`</text>
    <text x="12" y="106" class="card-desc">• Cung cấp số liệu Queries/sec, Threads, Buffer</text>
    <text x="12" y="124" class="card-desc">• Đo lường tốc độ đọc ghi I/O bảng CSDL</text>
    <line x1="12" y1="135" x2="323" y2="135" stroke="#e2e8f0" stroke-width="1" />
    <text x="12" y="152" class="card-port">Cổng nội bộ: :9104/metrics</text>
    <text x="12" y="170" class="card-desc" font-size="10">Cầu nối 2 mạng: backend_net ➔ monitor_net</text>
  </g>

  <!-- ==================== PHÂN VÙNG 3: blog_monitor_net ==================== -->
  <rect x="280" y="550" width="860" height="420" class="zone-box" fill="#faf5ff" stroke="#7c3aed" />
  <rect x="295" y="562" width="460" height="28" rx="6" fill="#f3e8ff" />
  <text x="310" y="581" class="zone-title" fill="#6d28d9">MẠNG 3: blog_monitor_net (Subnet: 172.28.30.0/24) — GIÁM SÁT METRICS</text>

  <!-- 3 Exporters on the left -->
  <g transform="translate(305, 605)">
    <!-- Node Exporter -->
    <rect width="240" height="65" class="card-cont" stroke="#a855f7" />
    <text x="10" y="20" class="card-hdr" fill="#6b21a8" font-size="11.5">blog-node-exporter</text>
    <text x="10" y="38" class="card-desc">CPU, RAM, Ổ cứng, Mạng Host OS</text>
    <text x="10" y="54" class="card-port">Cổng :9100/metrics</text>
  </g>

  <g transform="translate(305, 680)">
    <!-- cAdvisor -->
    <rect width="240" height="65" class="card-cont" stroke="#a855f7" />
    <text x="10" y="20" class="card-hdr" fill="#6b21a8" font-size="11.5">blog-cadvisor</text>
    <text x="10" y="38" class="card-desc">Tài nguyên tiêu thụ 13 Containers</text>
    <text x="10" y="54" class="card-port">Cổng nội bộ :8080/metrics</text>
  </g>

  <g transform="translate(305, 755)">
    <!-- Docker Stats Exporter -->
    <rect width="240" height="65" class="card-cont" stroke="#a855f7" />
    <text x="10" y="20" class="card-hdr" fill="#6b21a8" font-size="11.5">blog-docker-stats-exporter</text>
    <text x="10" y="38" class="card-desc">Trạng thái sống/chết &amp; Net I/O container</text>
    <text x="10" y="54" class="card-port">Cổng nội bộ :9487/metrics</text>
  </g>

  <!-- Container 10: blog-prometheus (Core TSDB) -->
  <g transform="translate(575, 605)">
    <rect width="275" height="215" class="card-cont" stroke="#7c3aed" fill="#ffffff" />
    <rect x="12" y="12" width="95" height="20" rx="4" fill="#7c3aed" />
    <text x="59" y="26" class="card-tag" text-anchor="middle">METRICS TSDB</text>
    <text x="115" y="27" class="card-hdr" fill="#5b21b6">blog-prometheus</text>
    <text x="12" y="52" class="card-desc" font-weight="bold">Prometheus Server TSDB (v2.51)</text>
    <text x="12" y="70" class="card-desc">• Cơ chế PULL: Cào 5 Exporters chu kỳ 15s</text>
    <text x="12" y="88" class="card-desc">• 100% Targets UP (Healthy)</text>
    <text x="12" y="106" class="card-desc">• Lưu trữ chuỗi thời gian TSDB (15 ngày)</text>
    <text x="12" y="124" class="card-desc">• Cung cấp PromQL Engine cho Grafana</text>
    <line x1="12" y1="135" x2="263" y2="135" stroke="#e2e8f0" stroke-width="1" />
    <text x="12" y="152" class="card-port">Cổng Host: 9090:9090</text>
    <text x="12" y="170" class="card-desc" font-size="10">Volume: prometheus_data</text>
    <text x="12" y="188" class="card-desc" font-size="10">Cấu hình: monitoring/prometheus.yml</text>
  </g>

  <!-- Container 11: blog-grafana -->
  <g transform="translate(875, 605)">
    <rect width="245" height="215" class="card-cont" stroke="#d946ef" fill="#ffffff" />
    <rect x="12" y="12" width="75" height="20" rx="4" fill="#c026d3" />
    <text x="49" y="26" class="card-tag" text-anchor="middle">DASHBOARDS</text>
    <text x="95" y="27" class="card-hdr" fill="#86198f">blog-grafana</text>
    <text x="12" y="52" class="card-desc" font-weight="bold">Grafana Visual Analytics (v10.4)</text>
    <text x="12" y="70" class="card-desc">• Tự động nạp sẵn 4 Dashboards chuẩn</text>
    <text x="12" y="88" class="card-desc">• Provisioning Datasources (Prom + Loki)</text>
    <text x="12" y="106" class="card-desc">• Trực quan hóa CPU, RAM, MySQL, Web</text>
    <text x="12" y="124" class="card-desc">• Giao diện Explore truy vấn LogQL</text>
    <line x1="12" y1="135" x2="233" y2="135" stroke="#e2e8f0" stroke-width="1" />
    <text x="12" y="152" class="card-port">Cổng Host: 3000:3000</text>
    <text x="12" y="170" class="card-desc" font-size="10">User: admin / GrafanaAdminSecurePass2026!</text>
    <text x="12" y="188" class="card-desc" font-size="10">Volume: grafana_data</text>
  </g>

  <!-- Scrape Note in monitor_net -->
  <rect x="305" y="840" width="545" height="45" rx="8" fill="#f3e8ff" stroke="#c084fc" />
  <text x="320" y="860" font-family="'Segoe UI', Arial" font-size="11" font-weight="bold" fill="#6b21a8">Cơ chế PULL định kỳ 15s:</text>
  <text x="320" y="876" font-family="'Segoe UI', Arial" font-size="10.5" fill="#581c87">Prometheus gửi HTTP GET /metrics tới cả 5 Exporter (Node, cAdvisor, MySQL, Nginx, Docker Stats)</text>

  <!-- ==================== PHÂN VÙNG 4: blog_logging_net ==================== -->
  <rect x="1170" y="550" width="725" height="420" class="zone-box" fill="#ecfdf5" stroke="#059669" />
  <rect x="1185" y="562" width="460" height="28" rx="6" fill="#d1fae5" />
  <text x="1200" y="581" class="zone-title" fill="#047857">MẠNG 4: blog_logging_net (Subnet: 172.28.40.0/24) — NHẬT KÝ LOKI</text>

  <!-- Container 12: blog-promtail -->
  <g transform="translate(1190, 615)">
    <rect width="320" height="195" class="card-cont" stroke="#059669" />
    <rect x="12" y="12" width="75" height="20" rx="4" fill="#059669" />
    <text x="49" y="26" class="card-tag" text-anchor="middle">LOG AGENT</text>
    <text x="95" y="27" class="card-hdr" fill="#065f46">blog-promtail</text>
    <text x="12" y="52" class="card-desc" font-weight="bold">Promtail Log Shipper Agent (v3.0)</text>
    <text x="12" y="70" class="card-desc">• Đọc socket Host: `/var/run/docker.sock:ro`</text>
    <text x="12" y="88" class="card-desc">• Đọc log Nginx Proxy: `/data/logs/*_*.log`</text>
    <text x="12" y="106" class="card-desc">• Tự động trích xuất &amp; gắn nhãn (Relabeling):</text>
    <text x="25" y="122" class="card-desc" font-family="'Consolas', monospace" font-size="10">container="blog-wordpress", job="nginx"</text>
    <line x1="12" y1="135" x2="308" y2="135" stroke="#e2e8f0" stroke-width="1" />
    <text x="12" y="152" class="card-port">Cổng nội bộ: :9080</text>
    <text x="12" y="170" class="card-desc" font-size="10">Cơ chế PUSH lô bản ghi (Batching) về Loki</text>
  </g>

  <!-- Container 13: blog-loki -->
  <g transform="translate(1535, 615)">
    <rect width="335" height="195" class="card-cont" stroke="#10b981" />
    <rect x="12" y="12" width="80" height="20" rx="4" fill="#047857" />
    <text x="52" y="26" class="card-tag" text-anchor="middle">LOG ENGINE</text>
    <text x="100" y="27" class="card-hdr" fill="#065f46">blog-loki</text>
    <text x="12" y="52" class="card-desc" font-weight="bold">Grafana Loki Log Storage (v3.0)</text>
    <text x="12" y="70" class="card-desc">• "Prometheus dành cho Logs" — Siêu nhẹ</text>
    <text x="12" y="88" class="card-desc">• Chỉ đánh chỉ mục Nhãn (Labels), tiết kiệm RAM 90%</text>
    <text x="12" y="106" class="card-desc">• Nén toàn bộ dòng nhật ký (Snappy chunks)</text>
    <text x="12" y="124" class="card-desc">• Xử lý câu truy vấn lọc chuỗi LogQL</text>
    <line x1="12" y1="135" x2="323" y2="135" stroke="#e2e8f0" stroke-width="1" />
    <text x="12" y="152" class="card-port">Cổng Host: 3100:3100</text>
    <text x="12" y="170" class="card-desc" font-size="10">Volume: loki_data | Hardening: 512MB RAM</text>
  </g>

  <!-- LogQL Query Box in logging_net -->
  <rect x="1190" y="830" width="680" height="60" rx="8" fill="#d1fae5" stroke="#34d399" />
  <text x="1205" y="852" font-family="'Segoe UI', Arial" font-size="11" font-weight="bold" fill="#065f46">Truy vấn LogQL tiêu chuẩn tại Grafana Explore:</text>
  <text x="1205" y="872" font-family="'Consolas', monospace" font-size="10.5" fill="#047857">1. {container="blog-wordpress"}   2. {container="blog-npm"} |~ "HTTP/[0-9.]+ 404"   3. rate({container="blog-npm"}[5m])</text>

  <!-- ==================== TẦNG HẠ TẦNG VẬT LÝ & LƯU TRỮ HOST (BÊN DƯỚI) ==================== -->
  <rect x="25" y="1010" width="1870" height="320" rx="14" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" />
  <rect x="25" y="1010" width="1870" height="38" rx="14" fill="#f8fafc" />
  <text x="50" y="1035" class="zone-title" fill="#0f172a">💾 TẦNG LƯU TRỮ BỀN VỮNG TRÊN MÁY CHỦ VẬT LÝ HOST (7 DOCKER NAMED VOLUMES &amp; SECURITY HARDENING)</text>

  <!-- Volumes Grid -->
  <g transform="translate(50, 1070)">
    <rect width="230" height="70" class="vol-box" />
    <text x="115" y="30" class="vol-text">mysql_data</text>
    <text x="115" y="48" class="card-desc" text-anchor="middle" font-size="10">InnoDB Data &amp; Redo Logs</text>
    <text x="115" y="62" class="card-desc" text-anchor="middle" font-size="9.5" fill="#92400e">Mount: /var/lib/mysql</text>
  </g>

  <g transform="translate(310, 1070)">
    <rect width="230" height="70" class="vol-box" />
    <text x="115" y="30" class="vol-text">wp_data</text>
    <text x="115" y="48" class="card-desc" text-anchor="middle" font-size="10">WordPress PHP &amp; Uploads</text>
    <text x="115" y="62" class="card-desc" text-anchor="middle" font-size="9.5" fill="#92400e">Mount: /var/www/html</text>
  </g>

  <g transform="translate(570, 1070)">
    <rect width="230" height="70" class="vol-box" />
    <text x="115" y="30" class="vol-text">npm_data &amp; npm_ssl</text>
    <text x="115" y="48" class="card-desc" text-anchor="middle" font-size="10">SQLite Config &amp; SSL Certs</text>
    <text x="115" y="62" class="card-desc" text-anchor="middle" font-size="9.5" fill="#92400e">Mount: /data, /etc/letsencrypt</text>
  </g>

  <g transform="translate(830, 1070)">
    <rect width="230" height="70" class="vol-box" />
    <text x="115" y="30" class="vol-text">prometheus_data</text>
    <text x="115" y="48" class="card-desc" text-anchor="middle" font-size="10">Time-Series DB Chunks</text>
    <text x="115" y="62" class="card-desc" text-anchor="middle" font-size="9.5" fill="#92400e">Mount: /prometheus</text>
  </g>

  <g transform="translate(1090, 1070)">
    <rect width="230" height="70" class="vol-box" />
    <text x="115" y="30" class="vol-text">grafana_data</text>
    <text x="115" y="48" class="card-desc" text-anchor="middle" font-size="10">Users, Dashboards Cache</text>
    <text x="115" y="62" class="card-desc" text-anchor="middle" font-size="9.5" fill="#92400e">Mount: /var/lib/grafana</text>
  </g>

  <g transform="translate(1350, 1070)">
    <rect width="230" height="70" class="vol-box" />
    <text x="115" y="30" class="vol-text">loki_data</text>
    <text x="115" y="48" class="card-desc" text-anchor="middle" font-size="10">Compressed Snappy Chunks</text>
    <text x="115" y="62" class="card-desc" text-anchor="middle" font-size="9.5" fill="#92400e">Mount: /loki</text>
  </g>

  <g transform="translate(1610, 1070)">
    <rect width="260" height="70" rx="8" fill="#f8fafc" stroke="#3b82f6" stroke-width="1.2" />
    <text x="130" y="26" font-family="'Segoe UI', Arial" font-size="11" font-weight="bold" fill="#1e40af" text-anchor="middle">MÁY CHỦ VẬT LÝ HOST</text>
    <text x="130" y="44" class="card-desc" text-anchor="middle" font-size="10">Windows 11 WSL2 / Ubuntu 24.04</text>
    <text x="130" y="58" class="card-desc" text-anchor="middle" font-size="9.5">Docker Engine 27.0.3 / Compose v2</text>
  </g>

  <!-- Hardening Info Box -->
  <rect x="50" y="1165" width="1820" height="140" rx="8" fill="#f8fafc" stroke="#e2e8f0" />
  <text x="70" y="1190" font-family="'Segoe UI', Arial" font-size="12" font-weight="bold" fill="#0f172a">🛡️ 6 CƠ CHẾ GIA CỐ BẢO MẬT HẠ TẦNG (SYSTEM HARDENING) ĐƯỢC THI KẾ HOÀN HẢO:</text>

  <g transform="translate(70, 1205)">
    <text x="0" y="18" font-family="'Segoe UI', Arial" font-size="11" font-weight="bold" fill="#2563eb">1. Chống leo thang đặc quyền:</text>
    <text x="0" y="34" class="card-desc">Cờ `no-new-privileges: true` trên toàn bộ 13 containers ngăn chặn lợi dụng bit SUID để leo thang root máy chủ Host.</text>
    <text x="0" y="50" class="card-desc">Tài khoản MySQL `wp_user` bị cô lập quyền hạn chỉ trên `wordpress_db` (Least Privilege).</text>

    <text x="460" y="18" font-family="'Segoe UI', Arial" font-size="11" font-weight="bold" fill="#2563eb">2. Phân vùng mạng 4 tầng:</text>
    <text x="460" y="34" class="card-desc">MySQL cô lập trong `backend_net`. Cổng Nginx Ingress không thể gửi gói tin hoặc ping trực tiếp tới MySQL.</text>
    <text x="460" y="50" class="card-desc">Triệt tiêu nguy cơ tấn công bắc cầu (Lateral Movement) khi có container bị xâm nhập.</text>

    <text x="940" y="18" font-family="'Segoe UI', Arial" font-size="11" font-weight="bold" fill="#2563eb">3. Giới hạn trần tài nguyên (DoS Guard):</text>
    <text x="940" y="34" class="card-desc">Áp đặt CPU Limit (0.5 – 1.0 Core) và Memory Limit (256MB – 1024MB) trên từng dịch vụ trong compose.</text>
    <text x="940" y="50" class="card-desc">Ngăn chặn một container bị tấn công làm cạn kiệt tài nguyên (Resource Starvation) máy chủ.</text>

    <text x="1420" y="18" font-family="'Segoe UI', Arial" font-size="11" font-weight="bold" fill="#2563eb">4. Mã hóa SSL SAN &amp; WAF Ingress:</text>
    <text x="1420" y="34" class="card-desc">TLS 1.3 với Subject Alternative Name (localhost, 127.0.0.1) và tiêu đề HSTS.</text>
    <text x="1420" y="50" class="card-desc">Bộ lọc `block-exploits.conf` chặn các mẫu khai thác SQLi, XSS, File Injection.</text>
  </g>


  <!-- ==================== CÁC ĐƯỜNG DẪN DỮ LIỆU & MŨI TÊN ĐIỀU PHỐI (FLOW PATHS) ==================== -->

  <!-- LUỒNG 1: WEB TRAFFIC FLOW (MÀU XANH DƯƠNG) -->
  <!-- 1.1: Client to NPM -->
  <path d="M 240 380 L 270 380 L 270 320 L 305 320" fill="none" stroke="#2563eb" stroke-width="3" marker-end="url(#arr-blue)" />
  <circle cx="270" cy="350" r="11" fill="#2563eb" />
  <text x="270" y="354" class="badge-step">1</text>

  <!-- 1.2: NPM to WordPress -->
  <path d="M 555 315 L 585 315" fill="none" stroke="#2563eb" stroke-width="3" marker-end="url(#arr-blue)" />
  <circle cx="570" cy="305" r="11" fill="#2563eb" />
  <text x="570" y="309" class="badge-step">2</text>
  <text x="570" y="290" class="flow-label" fill="#1d4ed8" text-anchor="middle">HTTP:80 Proxy</text>

  <!-- 1.3: NPM to phpMyAdmin -->
  <path d="M 430 225 L 430 215 L 990 215 L 990 225" fill="none" stroke="#f59e0b" stroke-width="2" marker-end="url(#arr-amber)" />
  <text x="710" y="210" class="flow-label" fill="#b45309" text-anchor="middle">Port 8081 Proxy ➔ phpMyAdmin</text>

  <!-- 1.4: WordPress to MySQL -->
  <path d="M 850 315 L 1190 315" fill="none" stroke="#2563eb" stroke-width="3" marker-end="url(#arr-blue)" />
  <circle cx="1020" cy="315" r="11" fill="#2563eb" />
  <text x="1020" y="319" class="badge-step">3</text>
  <text x="1020" y="303" class="flow-label" fill="#1d4ed8" text-anchor="middle">TCP:3306 Prepared Statements</text>

  <!-- 1.5: phpMyAdmin to MySQL -->
  <path d="M 1120 350 L 1190 350" fill="none" stroke="#d97706" stroke-width="2" marker-end="url(#arr-amber)" />

  <!-- 1.6: MySQL to Volume mysql_data -->
  <path d="M 1350 420 L 1350 490 L 165 490 L 165 1070" fill="none" stroke="#d97706" stroke-width="2" stroke-dasharray="4 2" marker-end="url(#arr-amber)" />
  <text x="750" y="485" class="flow-label" fill="#b45309" text-anchor="middle">InnoDB Redo/Data Persistence ➔ named volume `mysql_data`</text>

  <!-- LUỒNG 2: PROMETHEUS METRICS PULL FLOW (MÀU TÍM) -->
  <!-- 2.1: Prometheus scrapes Node Exporter -->
  <path d="M 575 660 L 545 660" fill="none" stroke="#7c3aed" stroke-width="2.5" stroke-dasharray="6 3" marker-end="url(#arr-purple)" />

  <!-- 2.2: Prometheus scrapes cAdvisor -->
  <path d="M 575 710 L 545 710" fill="none" stroke="#7c3aed" stroke-width="2.5" stroke-dasharray="6 3" marker-end="url(#arr-purple)" />

  <!-- 2.3: Prometheus scrapes Docker Stats Exporter -->
  <path d="M 575 780 L 545 780" fill="none" stroke="#7c3aed" stroke-width="2.5" stroke-dasharray="6 3" marker-end="url(#arr-purple)" />

  <!-- 2.4: Prometheus scrapes Nginx Exporter -->
  <path d="M 640 605 L 640 540 L 430 540 L 430 515" fill="none" stroke="#7c3aed" stroke-width="2" stroke-dasharray="6 3" marker-end="url(#arr-purple)" />
  <text x="535" y="535" class="flow-label" fill="#7c3aed" text-anchor="middle">PULL :9113</text>

  <!-- 2.5: Prometheus scrapes MySQL Exporter -->
  <path d="M 850 660 L 1700 660 L 1700 420" fill="none" stroke="#7c3aed" stroke-width="2.5" stroke-dasharray="6 3" marker-end="url(#arr-purple)" />
  <circle cx="1275" cy="660" r="11" fill="#7c3aed" />
  <text x="1275" y="664" class="badge-step">4</text>
  <text x="1275" y="650" class="flow-label" fill="#6d28d9" text-anchor="middle">PULL :9104 MySQL Metrics (15s interval)</text>

  <!-- 2.6: Grafana queries Prometheus via PromQL -->
  <path d="M 875 710 L 850 710" fill="none" stroke="#d946ef" stroke-width="3" marker-end="url(#arr-purple)" />
  <circle cx="862" cy="710" r="11" fill="#c026d3" />
  <text x="862" y="714" class="badge-step">5</text>
  <text x="862" y="698" class="flow-label" fill="#86198f" text-anchor="middle">PromQL :9090</text>

  <!-- 2.7: DevOps Engineer connects to Grafana -->
  <path d="M 240 760 L 260 760 L 260 920 L 990 920 L 990 820" fill="none" stroke="#7c3aed" stroke-width="2.5" marker-end="url(#arr-purple)" />
  <text x="625" y="915" class="flow-label" fill="#6d28d9" text-anchor="middle">HTTP :3000 Truy cập 4 Dashboard Grafana &amp; Explore</text>

  <!-- LUỒNG 3: CENTRALIZED LOGGING FLOW (MÀU XANH LÁ) -->
  <!-- 3.1: Docker Daemon Socket to Promtail -->
  <path d="M 1350 1010 L 1350 920 L 1280 920 L 1280 810" fill="none" stroke="#059669" stroke-width="2.5" stroke-dasharray="5 2" marker-end="url(#arr-green)" />
  <circle cx="1315" cy="920" r="11" fill="#059669" />
  <text x="1315" y="924" class="badge-step">6</text>
  <text x="1315" y="905" class="flow-label" fill="#047857" text-anchor="middle">Cào socket /var/run/docker.sock</text>

  <!-- 3.2: Promtail pushes batches to Loki -->
  <path d="M 1510 710 L 1535 710" fill="none" stroke="#059669" stroke-width="3" marker-end="url(#arr-green)" />
  <circle cx="1522" cy="710" r="11" fill="#059669" />
  <text x="1522" y="714" class="badge-step">7</text>
  <text x="1522" y="698" class="flow-label" fill="#047857" text-anchor="middle">PUSH HTTP:3100</text>

  <!-- 3.3: Grafana Explore queries Loki via LogQL -->
  <path d="M 1120 750 L 1150 750 L 1150 760 L 1535 760" fill="none" stroke="#059669" stroke-width="2.5" stroke-dasharray="4 2" marker-end="url(#arr-green)" />
  <circle cx="1342" cy="760" r="11" fill="#059669" />
  <text x="1342" y="764" class="badge-step">8</text>
  <text x="1342" y="748" class="flow-label" fill="#047857" text-anchor="middle">LogQL Stream &amp; Rate Query</text>

  <!-- Footer Tag -->
  <text x="1870" y="1345" font-family="'Segoe UI', Arial" font-size="11" fill="#94a3b8" text-anchor="end">Kiến trúc thiết kế: LyxLab DevOps Engine | Đề tài 7 Blog CMS K23A</text>
</svg>"""

    output_dir = "docs/architecture"
    os.makedirs(output_dir, exist_ok=True)
    svg_path = os.path.join(output_dir, "so_do_luong_he_thong_tong_quan.svg")
    png_path = os.path.join(output_dir, "so_do_luong_he_thong_tong_quan.png")

    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"✅ Created SVG: {svg_path} ({os.path.getsize(svg_path)} bytes)")

    cairosvg.svg2png(url=svg_path, write_to=png_path, dpi=200)
    print(f"✅ Rendered High-Resolution PNG: {png_path} ({os.path.getsize(png_path)} bytes)")

if __name__ == "__main__":
    generate_flow_diagram()

