# Đồ án Triển khai và Quản trị Hệ thống Phần mềm
**Đề tài 7:** Hệ thống Blog / CMS (WordPress + MySQL + phpMyAdmin + Nginx)

## 1. Cấu trúc hệ thống (Mốc 1 - Core Application)
Hệ thống được tách module rõ ràng trong thư mục `compose/`:
- `compose/docker-compose.app.yml`: Chứa các dịch vụ cốt lõi (WordPress, MySQL, phpMyAdmin, Nginx).
- `docker-compose.yml`: File gốc dùng cú pháp `include` để quản lý tập trung.

## 2. Hướng dẫn khởi chạy
1. Chuẩn bị file biến môi trường:
   cp .env.example .env
2. Khởi chạy toàn bộ hệ thống:
   docker compose up -d
3. Kiểm tra các container:
   docker compose ps

## 3. Đường dẫn truy cập
- **WordPress:** https://localhost/
- **phpMyAdmin:** https://localhost/pma/ (User: wp_user, Pass: WP_SecurePassword2026!)
