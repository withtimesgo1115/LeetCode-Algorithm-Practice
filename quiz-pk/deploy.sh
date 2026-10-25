#!/bin/bash
set -e

echo "=========================================="
echo "  Quiz PK 一键部署脚本"
echo "=========================================="

# ── 1. 拉取代码 ──────────────────────────────
echo ""
echo "[1/6] 拉取代码..."
cd /var/www || (sudo mkdir -p /var/www && sudo chown $(whoami):$(whoami) /var/www && cd /var/www)

if [ -d "quiz-pk" ]; then
  echo "  quiz-pk 目录已存在，拉取最新代码..."
  cd quiz-pk
  git pull origin main
else
  git clone https://github.com/withtimesgo1115/quiz-pk.git
  cd quiz-pk
fi

# ── 2. 安装依赖 ──────────────────────────────
echo ""
echo "[2/6] 安装依赖..."
npm install --production

# ── 3. 初始化题库 ─────────────────────────────
echo ""
echo "[3/6] 初始化题库..."
node initQuestions.js

# ── 4. PM2 启动 ──────────────────────────────
echo ""
echo "[4/6] 启动服务..."
pm2 delete quiz-pk 2>/dev/null || true
pm2 start server.js --name quiz-pk
pm2 save
pm2 startup 2>/dev/null || true

# ── 5. 配置 Nginx ────────────────────────────
echo ""
echo "[5/6] 配置 Nginx..."

NGINX_CONF="server {
    listen 80;
    server_name _;

    location / {
        proxy_pass http://127.0.0.1:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade \$http_upgrade;
        proxy_set_header Connection \"upgrade\";
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_read_timeout 86400s;
    }
}"

# 找到 nginx 配置目录
if [ -d "/etc/nginx/conf.d" ]; then
  echo "$NGINX_CONF" | sudo tee /etc/nginx/conf.d/quiz-pk.conf > /dev/null
elif [ -d "/etc/nginx/sites-available" ]; then
  echo "$NGINX_CONF" | sudo tee /etc/nginx/sites-available/quiz-pk > /dev/null
  sudo ln -sf /etc/nginx/sites-available/quiz-pk /etc/nginx/sites-enabled/quiz-pk
else
  echo "  未找到 nginx 配置目录，使用默认路径"
  echo "$NGINX_CONF" | sudo tee /etc/nginx/conf.d/quiz-pk.conf > /dev/null
fi

sudo nginx -t
sudo systemctl enable nginx
sudo systemctl restart nginx

# ── 6. 防火墙 ────────────────────────────────
echo ""
echo "[6/6] 配置防火墙..."
if command -v firewall-cmd &> /dev/null; then
  sudo firewall-cmd --permanent --add-port=80/tcp 2>/dev/null || true
  sudo firewall-cmd --reload 2>/dev/null || true
  echo "  firewalld 已开放 80 端口"
elif command -v iptables &> /dev/null; then
  sudo iptables -I INPUT -p tcp --dport 80 -j ACCEPT 2>/dev/null || true
  echo "  iptables 已开放 80 端口"
fi

# ── 获取公网 IP ──────────────────────────────
PUBLIC_IP=$(curl -s ifconfig.me 2>/dev/null || curl -s ip.sb 2>/dev/null || echo "你的公网IP")

echo ""
echo "=========================================="
echo "  ✅ 部署完成！"
echo "=========================================="
echo ""
echo "  手机访问: http://$PUBLIC_IP"
echo ""
echo "  ⚠️  记得去阿里云控制台:"
echo "  轻量应用服务器 → 防火墙 → 添加 TCP 80 端口规则"
echo ""
echo "  常用命令:"
echo "  pm2 status          # 查看服务状态"
echo "  pm2 logs quiz-pk    # 查看日志"
echo "  pm2 restart quiz-pk # 重启服务"
echo "=========================================="
