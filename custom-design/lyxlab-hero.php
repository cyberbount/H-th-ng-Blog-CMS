<?php
/**
 * Plugin Name: LyxLab Hero & Design Enhancement
 * Description: Renders the modern tech hero banner on LyxLab blog.
 */

add_action('astra_content_before', function() {
    if (is_home() || is_front_page()) {
        ?>
        <div class="lyx-hero-wrapper">
            <div class="lyx-hero-card">
                <div class="lyx-hero-badge">
                    <span class="lyx-pulse-dot"></span>
                    <span>HỆ THỐNG PHÒNG LAB ĐANG HOẠT ĐỘNG (13/13 CONTAINERS LIVE)</span>
                </div>
                <h1 class="lyx-hero-title">LyxLab — Cổng thông tin Triển khai &amp; Quản trị Hệ thống</h1>
                <p class="lyx-hero-desc">
                    Không gian nghiên cứu thực nghiệm chuyên sâu về kiến trúc Containerization, tự động hóa DevOps, 
                    giám sát chuỗi thời gian Prometheus &amp; Grafana, quản lý nhật ký tập trung Grafana Loki và Hardening an toàn thông tin.
                </p>
                <div class="lyx-hero-stats">
                    <div class="lyx-stat-chip">
                        <span class="lyx-stat-icon">🐳</span>
                        <div><strong>13 Containers</strong><span>Docker Compose v2</span></div>
                    </div>
                    <div class="lyx-stat-chip">
                        <span class="lyx-stat-icon">🛡️</span>
                        <div><strong>Nginx Gateway</strong><span>SSL Termination &amp; SAN</span></div>
                    </div>
                    <div class="lyx-stat-chip">
                        <span class="lyx-stat-icon">📈</span>
                        <div><strong>Prometheus &amp; Exporters</strong><span>Scrape Rate 15s</span></div>
                    </div>
                    <div class="lyx-stat-chip">
                        <span class="lyx-stat-icon">🔍</span>
                        <div><strong>Grafana Loki</strong><span>LogQL Realtime Query</span></div>
                    </div>
                </div>
            </div>
        </div>
        <style>
        .lyx-hero-wrapper {
            max-width: 1200px;
            margin: 28px auto 8px auto;
            padding: 0 20px;
        }
        .lyx-hero-card {
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 60%, #0f2b48 100%);
            border-radius: 16px;
            padding: 40px 36px;
            color: #ffffff;
            box-shadow: 0 20px 25px -5px rgba(15, 23, 42, 0.15), 0 8px 10px -6px rgba(15, 23, 42, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.1);
            position: relative;
            overflow: hidden;
        }
        .lyx-hero-card::after {
            content: "";
            position: absolute;
            top: -50%;
            right: -20%;
            width: 400px;
            height: 400px;
            background: radial-gradient(circle, rgba(59, 130, 246, 0.25) 0%, rgba(0,0,0,0) 70%);
            pointer-events: none;
        }
        .lyx-hero-badge {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(34, 197, 94, 0.15);
            border: 1px solid rgba(34, 197, 94, 0.35);
            color: #4ade80;
            padding: 6px 14px;
            border-radius: 9999px;
            font-size: 0.75rem;
            font-weight: 700;
            letter-spacing: 0.06em;
            margin-bottom: 18px;
        }
        .lyx-pulse-dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background-color: #22c55e;
            box-shadow: 0 0 8px #22c55e;
            animation: lyxPulse 2s infinite;
        }
        @keyframes lyxPulse {
            0% { transform: scale(0.95); opacity: 0.8; }
            50% { transform: scale(1.3); opacity: 1; }
            100% { transform: scale(0.95); opacity: 0.8; }
        }
        .lyx-hero-title {
            font-size: clamp(1.75rem, 3vw, 2.35rem);
            font-weight: 800;
            line-height: 1.25;
            letter-spacing: -0.02em;
            margin-bottom: 14px;
            color: #ffffff !important;
        }
        .lyx-hero-desc {
            font-size: 1.025rem;
            line-height: 1.65;
            color: #cbd5e1;
            max-width: 850px;
            margin-bottom: 26px;
        }
        .lyx-hero-stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 16px;
            margin-top: 10px;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            padding-top: 22px;
        }
        .lyx-stat-chip {
            display: flex;
            align-items: center;
            gap: 12px;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.08);
            padding: 10px 14px;
            border-radius: 10px;
            transition: background 0.2s;
        }
        .lyx-stat-chip:hover {
            background: rgba(255, 255, 255, 0.1);
        }
        .lyx-stat-icon {
            font-size: 1.5rem;
        }
        .lyx-stat-chip strong {
            display: block;
            font-size: 0.9rem;
            color: #f8fafc;
        }
        .lyx-stat-chip span {
            font-size: 0.75rem;
            color: #94a3b8;
        }
        </style>
        <?php
    }
});
