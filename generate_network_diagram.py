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

net_puml = r"""@startuml
!theme plain
skinparam defaultFontName "Segoe UI"
skinparam defaultFontSize 11
skinparam roundcorner 8
skinparam shadowing true
skinparam packageStyle rectangle
skinparam componentStyle rectangle

title **HÌNH 4.2: MÔ HÌNH PHÂN VÙNG MẠNG 4 DOCKER BRIDGE NETWORK ĐỘC LẬP**

actor "Internet / Client\n(Độc giả & Quản trị viên)" as Client #E0F2FE

node "Hạ tầng Docker Host OS (Ubuntu 24.04 / WSL2)" {

    package "1. blog_frontend_net [Subnet: 172.30.0.0/16] — Vùng đệm Tiếp nhận Ingress" as NetFrontend #F0F9FF {
        component "blog-npm\n<<Ingress Gateway>>\nPorts: 80, 443, 81" as NPM #BAE6FD
        component "blog-wordpress\n<<Application Core>>\nPort nội bộ: 80" as WP_Front #DBEAFE
        component "blog-phpmyadmin\n<<DB Web Admin>>\nPort nội bộ: 80" as PMA_Front #FEF3C7
        component "blog-nginx-exporter\n<<Metrics Exporter>>\nPort: 9113" as NGX_Front #E0F2FE
    }

    package "2. blog_backend_net [Subnet: 172.29.0.0/16] — Vùng CSDL Cô Lập Tuyệt Đối" as NetBackend #FFF7ED {
        component "blog-wordpress\n<<Database Client>>" as WP_Back #DBEAFE
        component "blog-phpmyadmin\n<<Database Client>>" as PMA_Back #FEF3C7
        database "blog-mysql\n<<MySQL 8.0 Server>>\nPort nội bộ: 3306\n🛡️ CẤM TRUY CẬP TỪ NPM" as DB #FED7AA
        component "blog-mysqld-exporter\n<<Metrics Exporter>>\nPort: 9104" as DB_EXP_Back #FFEDD5
    }

    package "3. blog_monitor_net [Subnet: 172.31.0.0/16] — Kênh Giám Sát Metrics (PULL 15s)" as NetMonitor #FAF5FF {
        component "blog-prometheus\n<<TSDB Server>>\nPort: 9090" as PROM #EDE9FE
        component "blog-grafana\n<<Dashboards UI>>\nPort: 3000" as GRAF #FCE7F3
        component "blog-node-exporter\n<<Host Metrics>>\nPort: 9100" as NODE_EXP #F3E8FF
        component "blog-cadvisor\n<<Container Metrics>>\nPort: 8080" as CADV #F3E8FF
        component "blog-docker-stats-exporter\n<<Docker Engine>>\nPort: 9487" as DOCK_EXP #F3E8FF
        component "blog-mysqld-exporter" as DB_EXP_Mon #FFEDD5
        component "blog-nginx-exporter" as NGX_Mon #E0F2FE
        component "blog-loki\n<<Datasource Provider>>" as LOKI_Mon #A7F3D0
    }

    package "4. blog_logging_net [Subnet: 192.168.0.0/20] — Kênh Thu Thập Nhật Ký (PUSH)" as NetLogging #ECFDF5 {
        component "blog-promtail\n<<Log Shipper Agent>>\nMount: /var/run/docker.sock\nMount: /data/logs/*_*.log" as PROMTAIL #D1FAE5
        component "blog-loki\n<<Log Index & Chunk Engine>>\nPort: 3100" as LOKI #A7F3D0
    }
}

Client --> NPM : HTTPS :443 (TLS 1.3 SAN)

NPM --> WP_Front : Reverse Proxy HTTP:80
NPM --> PMA_Front : Proxy Host :8081

WP_Back --> DB : TCP:3306 (Prepared Statements)
PMA_Back --> DB : TCP:3306 (Quản trị CSDL)
DB_EXP_Back --> DB : TCP:3306 (Cào metrics .my.cnf)

PROM --> NODE_EXP : PULL :9100 (15s)
PROM --> CADV : PULL :8080 (15s)
PROM --> DOCK_EXP : PULL :9487 (15s)
PROM --> NGX_Mon : PULL :9113 (15s)
PROM --> DB_EXP_Mon : PULL :9104 (15s)
GRAF --> PROM : PromQL :9090
GRAF --> LOKI_Mon : LogQL :3100

PROMTAIL --> LOKI : PUSH Batch HTTP:3100\n(log stream qua logging_net)

legend right
  |<#0284c7>| **1. blog_frontend_net (172.30.0.0/16)**: Vùng đệm tiếp nhận lưu lượng Web công cộng |
  |<#c2410c>| **2. blog_backend_net (172.29.0.0/16)**: Vùng cô lập CSDL MySQL, chặn đứng NPM truy cập |
  |<#7c3aed>| **3. blog_monitor_net (172.31.0.0/16)**: Kênh PULL metrics định kỳ 15s phục vụ Grafana |
  |<#059669>| **4. blog_logging_net (192.168.0.0/20)**: Kênh truyền tải log an toàn từ Promtail về Loki |
  |<#ef4444>| **Nguyên lý An ninh Zero-Trust**: Không chia sẻ mạng chung giữa Ingress và Database |
endlegend
@enduml"""

def main():
    output_dir = "docs/architecture"
    os.makedirs(output_dir, exist_ok=True)
    artifact_dir = "/home/cyberbount/.gemini/antigravity/brain/de78f41e-e732-4572-9c45-484dc7900b08"
    
    p = os.path.join(output_dir, "fig4_2_network_diagram.puml")
    with open(p, "w", encoding="utf-8") as f:
        f.write(net_puml.strip())
        
    png = os.path.join(output_dir, "fig4_2_network_diagram.png")
    render_plantuml(net_puml.strip(), png)
    
    if os.path.exists(artifact_dir):
        os.system(f"cp {png} {artifact_dir}/")
        print("✅ Copied network diagram to artifact directory!")

if __name__ == "__main__":
    main()

