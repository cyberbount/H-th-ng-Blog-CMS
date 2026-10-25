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

fig4_6_puml = r"""@startuml
!theme plain
left to right direction
skinparam defaultFontName "Segoe UI"
skinparam defaultFontSize 11
skinparam roundcorner 8
skinparam shadowing true
skinparam packageStyle rectangle
skinparam componentStyle rectangle

title **HÌNH 4.6: ĐƯỜNG ỐNG THU THẬP VÀ TRUY VẤN NHẬT KÝ TẬP TRUNG PROMTAIL - LOKI - LOGQL**

package "TẦNG 1: NGUỒN PHÁT SINH LOG\n(DOCKER HOST & 13 CONTAINERS)" as Tier1 #F0F9FF {
    component "13 Docker Containers\n<<stdout / stderr console>>\n--\n• blog-wordpress (PHP/Apache)\n• blog-mysql (InnoDB Query Logs)\n• blog-npm, exporters..." as Logs_Stdout #BAE6FD
    file "Nginx Access & Error Files\n<<Path: /data/logs/*_*.log>>\n--\n• proxy-host-1_access.log\n• default-host_error.log" as Logs_Nginx #BAE6FD
    interface "Docker Daemon Socket\n<<unix:///var/run/docker.sock:ro>>\n--\n• Lắng nghe sự kiện container\n• Trích xuất metadata thời gian thực" as Docker_Sock #93C5FD
}

package "TẦNG 2: ĐẠI LÝ THU THẬP & GẮN NHÃN\n(PROMTAIL AGENT :9080)" as Tier2 #ECFDF5 {
    component "Docker Service Discovery\n--\n• docker_sd_configs (mỗi 5s)\n• Tự động bắt 13 containers" as Promtail_SD #A7F3D0
    component "Relabeling Engine\n--\n• __meta_docker_container_name ➔ container\n• __meta_docker_log_stream ➔ stream\n• job: nginx, service: nginx-proxy" as Promtail_Relabel #A7F3D0
    component "Batching & Shipper Buffer\n--\n• File vị trí: /tmp/positions.yaml\n• Gom nhóm log thành các Batch" as Promtail_Push #6EE7B7
}

package "TẦNG 3: MÁY CHỦ CHỈ MỤC & NÉN NHẬT KÝ\n(GRAFANA LOKI 3.0 :3100)" as Tier3 #FFF7ED {
    component "Label Indexer (TSDB v13)\n--\n• CHỈ đánh chỉ mục Metadata / Nhãn\n• Tiết kiệm 90% RAM so với ELK Stack\n• Chu kỳ phân vùng Index: 24h" as Loki_Index #FED7AA
    database "Snappy Compressed Chunks\n--\n• Nén toàn bộ chuỗi nội dung log\n• Lưu trữ: /loki/chunks/\n• Volume bền vững: loki_data" as Loki_Chunks #FDBA74
    component "LogQL Query Engine\n--\n• HTTP API: /loki/api/v1/query_range\n• Lọc chuỗi, Regex, Rate calculations" as Loki_Querier #FED7AA
}

package "TẦNG 4: TRỰC QUAN HÓA & TRUY VẾT SỰ CỐ\n(GRAFANA EXPLORE UI :3000)" as Tier4 #FAF5FF {
    component "Stream Selector Filter\n--\n• {container='blog-wordpress'}\n• {job='nginx', service='nginx-proxy'}\n• Live Tail dòng log thời gian thực" as Graf_Stream #E9D5FF
    component "Line Filter & Regex Parser\n--\n• |= 'error' (Lọc từ khóa)\n• |~ 'HTTP/[0-9.]+ [45][0-9][0-9]'\n(Bóc tách mã lỗi HTTP 4xx và 5xx)" as Graf_Regex #E9D5FF
    component "Log Metric Queries\n--\n• rate({container=~'blog-.*'}[5m])\n(Vẽ biểu đồ tần suất phát sinh log)" as Graf_Metric #D8B4FE
}

actor "Kỹ sư DevOps / SRE\n(Điều tra sự cố)" as SRE #E0F2FE

' Flow 1: Sources to Promtail
Logs_Stdout --> Promtail_SD : Ghi nhận log streams
Docker_Sock --> Promtail_SD : Quét container events
Logs_Nginx --> Promtail_SD : Đọc file log từ host

Promtail_SD --> Promtail_Relabel : Gán metadata labels
Promtail_Relabel --> Promtail_Push : Gom batch dữ liệu

' Flow 2: Promtail PUSH to Loki (logging_net)
Promtail_Push --> Loki_Index : PUSH HTTP POST :3100\n[Endpoint: /loki/api/v1/push]\n(Mạng blog_logging_net)

Loki_Index --> Loki_Chunks : Đánh index nhãn & nén chunks Snappy
Loki_Querier --> Loki_Index : Tra cứu chỉ mục nhãn
Loki_Querier --> Loki_Chunks : Giải nén dòng log cần tìm

' Flow 3: Grafana Explore query LogQL
Graf_Stream --> Loki_Querier : Truy vấn LogQL qua cổng :3100
Graf_Regex --> Loki_Querier : Thực thi bộ lọc Regex
Graf_Metric --> Loki_Querier : Tính toán tốc độ dòng log

SRE --> Tier4 : Truy cập Grafana Explore :3000\n(Bóc tách và xử lý sự cố)

legend right
  |<#BAE6FD>| **Tầng 1 (Sources)**: Docker console stdout/stderr & tệp log access Nginx |
  |<#A7F3D0>| **Tầng 2 (Promtail)**: Tự động phát hiện container, relabel và PUSH batch |
  |<#FED7AA>| **Tầng 3 (Loki 3.0)**: Chỉ index nhãn, nén Snappy lưu volume loki_data |
  |<#E9D5FF>| **Tầng 4 (Grafana Explore)**: Truy vết LogQL lọc lỗi 4xx/5xx & Live Tail |
  |<#059669>| **Kênh truyền tải**: Luồng PUSH hoàn toàn nằm trong mạng `blog_logging_net` |
endlegend
@enduml"""

def main():
    output_dir = "docs/architecture"
    os.makedirs(output_dir, exist_ok=True)
    artifact_dir = "/home/cyberbount/.gemini/antigravity/brain/de78f41e-e732-4572-9c45-484dc7900b08"
    
    p = os.path.join(output_dir, "fig4_6_logging_diagram.puml")
    with open(p, "w", encoding="utf-8") as f:
        f.write(fig4_6_puml.strip())
        
    png = os.path.join(output_dir, "fig4_6_logging_diagram.png")
    render_plantuml(fig4_6_puml.strip(), png)
    
    if os.path.exists(artifact_dir):
        os.system(f"cp {png} {artifact_dir}/")
        print("✅ Copied fig4_6 logging diagram to artifact directory!")

if __name__ == "__main__":
    main()

