import os
import zlib
import urllib.request

def render_plantuml(puml_code, output_png_path):
    zlibbed_str = zlib.compress(puml_code.encode("utf-8"))
    compressed_string = zlibbed_str[2:-4]
    mapping = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_"
    def _encode6bit(b):
        return mapping[b & 0x3f]
    def _append3bytes(b1, b2, b3):
        c1 = b1 >> 2
        c2 = ((b1 & 0x3) << 4) | (b2 >> 4)
        c3 = ((b2 & 0xF) << 2) | (b3 >> 6)
        c4 = b3 & 0x3F
        return _encode6bit(c1) + _encode6bit(c2) + _encode6bit(c3) + _encode6bit(c4)
    res = ""
    i = 0
    while i < len(compressed_string):
        b1 = compressed_string[i]
        b2 = compressed_string[i+1] if i+1 < len(compressed_string) else 0
        b3 = compressed_string[i+2] if i+2 < len(compressed_string) else 0
        res += _append3bytes(b1, b2, b3)
        i += 3
        
    url = f"http://www.plantuml.com/plantuml/png/{res}"
    print(f"Fetching from PlantUML ({len(puml_code)} chars)...")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
    except urllib.error.HTTPError as e:
        print(f"❌ Error {e.code}: {e.read().decode('utf-8', errors='ignore')[:400]}")
        raise e
        
    with open(output_png_path, "wb") as f:
        f.write(data)
    print(f"✅ Generated: {output_png_path} ({len(data):,} bytes)")

fig4_5_puml = r"""@startuml
!theme plain
left to right direction
skinparam defaultFontName "Segoe UI"
skinparam defaultFontSize 11
skinparam roundcorner 8
skinparam shadowing true
skinparam packageStyle rectangle
skinparam componentStyle rectangle

title **HÌNH 4.5: KIẾN TRÚC THU THẬP METRICS ĐA TẦNG VỚI PROMETHEUS TSDB VÀ 5 EXPORTERS**

package "TẦNG 1: CỤM 5 EXPORTERS (DATA PRODUCERS)\n[Mạng blog_monitor_net :172.31.0.0/16]" as Tier1 #FFF7ED {
    component "blog-node-exporter\n<<Port 9100/metrics>>\n--\n• CPU, RAM, Disk I/O Host\n• Băng thông mạng Vật lý" as EXP_Node #FED7AA
    component "blog-cadvisor\n<<Port 8080/metrics>>\n--\n• CPU/RAM từng Container\n• Giới hạn tài nguyên Quotas" as EXP_Cadv #FED7AA
    component "blog-mysqld-exporter\n<<Port 9104/metrics>>\n--\n• Queries/s, Slow queries\n• InnoDB Buffer Pool Hit Ratio" as EXP_Mysql #FED7AA
    component "blog-nginx-exporter\n<<Port 9113/metrics>>\n--\n• Active Connections Nginx\n• Requests/sec, Handled/Dropped" as EXP_Nginx #FED7AA
    component "blog-docker-stats-exporter\n<<Port 9487/metrics>>\n--\n• Trạng thái Sống còn Container\n• Block I/O & Network I/O" as EXP_Docker #FED7AA
}

package "TẦNG 2: MÁY CHỦ PROMETHEUS TSDB (CORE ENGINE)\n[Port 9090:9090 | Volume: prometheus_data]" as Tier2 #EFF6FF {
    component "Pull Engine (Scraper)\n--\n• Scrape Interval: 15s\n• Scrape Timeout: 10s\n• Target State: 6/6 UP" as Prom_Scraper #DBEAFE
    database "TSDB Storage Engine\n--\n• Nén Gorilla Compression\n• Khối dữ liệu thời gian 2h\n• Retention: 15 ngày" as Prom_TSDB #BFDBFE
    component "PromQL Query Engine\n--\n• Hàm: rate(), irate(), sum()\n• Đánh giá Alerting: 15s\n• HTTP API v1 Endpoint" as Prom_Query #93C5FD
}

package "TẦNG 3: TRỰC QUAN HÓA GRAFANA (VISUALIZATION)\n[Port 3000:3000 | Tự động Provisioning]" as Tier3 #FAF5FF {
    component "Dashboard: Node Exporter Full\n(Giám sát phần cứng máy chủ Host)" as Dash_Node #F3E8FF
    component "Dashboard: Docker Containers\n(Giám sát tải 13 Containers cAdvisor)" as Dash_Cont #F3E8FF
    component "Dashboard: MySQL Overview\n(QPS, Threads, InnoDB Buffer Pool)" as Dash_Mysql #F3E8FF
    component "Dashboard: Nginx Proxy Manager\n(Lưu lượng Web, Tỷ lệ phản hồi HTTP)" as Dash_Nginx #F3E8FF
    component "Dashboard: Prometheus Stats\n(Hiệu năng TSDB & Tốc độ cào)" as Dash_Prom #F3E8FF
}

actor "Kỹ sư DevOps / SRE\n(Vận hành & Giám sát)" as SRE #E0F2FE

' Connections: Pull engine scrapes 5 exporters
Prom_Scraper --> EXP_Node : PULL HTTP GET :9100\n(chu kỳ 15s)
Prom_Scraper --> EXP_Cadv : PULL HTTP GET :8080\n(chu kỳ 15s)
Prom_Scraper --> EXP_Mysql : PULL HTTP GET :9104\n(chu kỳ 15s)
Prom_Scraper --> EXP_Nginx : PULL HTTP GET :9113\n(chu kỳ 15s)
Prom_Scraper --> EXP_Docker : PULL HTTP GET :9487\n(chu kỳ 15s)

' Scraper stores into TSDB
Prom_Scraper --> Prom_TSDB : Ghi chuỗi thời gian nén\n(Gorilla chunks)
Prom_Query --> Prom_TSDB : Đọc dữ liệu lịch sử

' Grafana queries PromQL
Dash_Node --> Prom_Query : PromQL Query :9090
Dash_Cont --> Prom_Query : PromQL Query :9090
Dash_Mysql --> Prom_Query : PromQL Query :9090
Dash_Nginx --> Prom_Query : PromQL Query :9090
Dash_Prom --> Prom_Query : PromQL Query :9090

' SRE views Grafana
SRE --> Tier3 : Truy cập HTTP :3000\n(Đăng nhập Admin)

legend right
  |<#FED7AA>| **Tầng 1 (5 Exporters)**: Đo lường phần cứng, container, CSDL, web proxy |
  |<#BFDBFE>| **Tầng 2 (Prometheus TSDB)**: Kéo số liệu (PULL 15s), nén dữ liệu và cung cấp PromQL |
  |<#F3E8FF>| **Tầng 3 (Grafana)**: Nạp tự động Datasource & 7 Dashboard hiển thị trực quan |
  |<#0284c7>| **Kênh truyền tải**: Toàn bộ luồng PULL diễn ra trên mạng cô lập `blog_monitor_net` |
endlegend
@enduml"""

def main():
    output_dir = "docs/architecture"
    os.makedirs(output_dir, exist_ok=True)
    artifact_dir = "/home/cyberbount/.gemini/antigravity/brain/de78f41e-e732-4572-9c45-484dc7900b08"
    
    p = os.path.join(output_dir, "fig4_5_monitoring_diagram.puml")
    with open(p, "w", encoding="utf-8") as f:
        f.write(fig4_5_puml.strip())
        
    png = os.path.join(output_dir, "fig4_5_monitoring_diagram.png")
    render_plantuml(fig4_5_puml.strip(), png)
    
    if os.path.exists(artifact_dir):
        os.system(f"cp {png} {artifact_dir}/")
        print("✅ Copied fig4_5 monitoring diagram to artifact directory!")

if __name__ == "__main__":
    main()

