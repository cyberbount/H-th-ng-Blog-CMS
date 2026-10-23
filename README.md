# Đồ án Triển khai và Quản trị Hệ thống Phần mềm (ICTU)
**Đề tài:** Hệ thống Blog / CMS (WordPress + MySQL + phpMyAdmin + Nginx + Prometheus + Grafana + Loki)

---

## 1. Cấu trúc Dự án
Dự án được phân tách module hóa chuyên nghiệp theo chuẩn Docker Compose:
```text
.
├── compose/
│   ├── docker-compose.app.yml          # Core Stack (WordPress, MySQL, phpMyAdmin, NPM)
│   ├── docker-compose.monitoring.yml   # Monitoring Stack (Prometheus, Grafana, Exporters)
│   └── docker-compose.logging.yml      # Centralized Logging Stack (Loki, Promtail)
├── docker-compose.yml                  # Root Compose kết hợp toàn bộ stacks qua include
├── monitoring/                         # Cấu hình Prometheus, Exporters, Grafana Provisioning
├── logging/                            # Cấu hình Loki & Promtail
├── nginx/                              # SSL Certs tự ký SAN & cấu hình Nginx
└── README.md
```

---

## 2. Danh sách Dịch vụ & Cổng Truy cập

| Dịch vụ | Địa chỉ truy cập | Tài khoản / Mật khẩu |
| :--- | :--- | :--- |
| **WordPress Blog** | `http://localhost:8080` hoặc `https://localhost` | Tài khoản Admin thiết lập lần đầu |
| **phpMyAdmin** | `http://localhost:8081` | User: `wp_user`<br>Pass: `WP_SecurePassword2026!` |
| **Nginx Proxy Manager** | `http://localhost:81` | User: `admin@example.com`<br>Pass: `changeme` |
| **Prometheus Server** | `http://localhost:9090` | Không yêu cầu đăng nhập |
| **Grafana Dashboard** | `http://localhost:3000` | User: `admin`<br>Pass: `GrafanaAdminSecurePass2026!` |
| **Loki Log Server** | `http://localhost:3100` | API endpoint nhận log từ Promtail |

---

## 3. Hướng dẫn Khởi chạy Hệ thống
```bash
# 1. Tạo file môi trường nếu chưa có
cp .env.example .env

# 2. Khởi chạy toàn bộ 13 containers của hệ thống
docker compose up -d

# 3. Kiểm tra trạng thái hoạt động
docker compose ps
```

---

## 4. Hệ thống Giám sát (Monitoring) - Commit 2
- **Prometheus Targets** (`http://localhost:9090/targets`): Cào đầy đủ metrics từ Node Exporter, cAdvisor, MySQL Exporter, Nginx Exporter, Docker Stats Exporter.
- **Danh sách Dashboards chuẩn trên Grafana**:
  1. **Node Exporter (CPU, RAM, Disk, Mạng máy chủ):** Dashboard ID `1860`
  2. **MySQL Database (Queries, Buffer Pool, Connections):** Dashboard ID `7362`
  3. **Nginx Reverse Proxy (Req/s, Connections, Status):** Dashboard ID `12740`
  4. **Docker Containers (Container CPU/RAM/Traffic):** Dashboard ID `14282`

---

## 5. Hệ thống Log tập trung (Loki + Promtail) - Commit 3
Promtail tự động thu thập toàn bộ log từ stdout/stderr của Docker socket và các file log của Nginx Proxy Manager gửi về Loki.

### Các câu truy vấn LogQL mẫu phục vụ Báo cáo & Demo:
Truy cập **Grafana** -> Menu **Explore** -> Chọn data source **Loki**:

1. **Xem toàn bộ log của Web WordPress:**
   ```logql
   {container="blog-wordpress"}
   ```

2. **Lọc log truy cập (Access Log) của Nginx:**
   ```logql
   {job="nginx"} |= "GET"
   ```

3. **Lọc các log cảnh báo hoặc lỗi của hệ thống:**
   ```logql
   {container=~".+"} |= "error" or "warn"
   ```

4. **Đếm tần suất yêu cầu HTTP theo thời gian thực:**
   ```logql
   rate({job="nginx"}[1m])
   ```

---

## 6. Các Biện pháp Bảo mật & Tối ưu (Hardening)
1. **Network Isolation (Phân vùng mạng cô lập):**
   - `blog_frontend_net`: Chỉ cho phép Nginx, WordPress, phpMyAdmin giao tiếp.
   - `blog_backend_net`: Cô lập database MySQL, chỉ cho WordPress, phpMyAdmin và mysqld-exporter kết nối.
   - `blog_monitor_net`: Dành riêng cho Prometheus, Grafana và các Exporter.
   - `blog_logging_net`: Dành riêng cho Loki và Promtail chuyển vận log an toàn.
2. **Resource Limits (Giới hạn tài nguyên CPU/RAM):**
   - Giới hạn CPU và Memory (RAM) trên từng container ngăn chặn tấn công DoS/OOM làm treo máy chủ.
3. **Container Privilege Limitation:**
   - Kích hoạt `security_opt: no-new-privileges:true` ngăn chặn leo thang đặc quyền trong container.
4. **Mật khẩu & Mã hóa:**
   - Sử dụng mật khẩu phức tạp với độ dài cao cho root MySQL và người dùng WordPress.
   - Hỗ trợ SSL tự ký SAN (`Local-SSL`) trên Reverse Proxy.
