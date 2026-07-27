#!/bin/bash

# ============================================================
# OMEGA-PROXY v11.0 - SETUP SCRIPT
# ============================================================
# هذا الملف يقوم بتثبيت جميع المتطلبات اللازمة للأداة
# ============================================================

echo ""
echo "╔══════════════════════════════════════════════════════════╗"
echo "║                                                          ║"
echo "║      🔧 OMEGA-PROXY v11.0 - SETUP SCRIPT 🔧             ║"
echo "║                                                          ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""

# ============================================================
# 1. تحديث النظام
# ============================================================
echo "[1/6] Updating system packages..."
sudo apt update -y
sudo apt upgrade -y

# ============================================================
# 2. تثبيت الأدوات الأساسية
# ============================================================
echo ""
echo "[2/6] Installing essential tools..."
sudo apt install -y python3 python3-pip python3-venv git curl wget

# ============================================================
# 3. تثبيت أدوات الشبكة
# ============================================================
echo ""
echo "[3/6] Installing network tools..."
sudo apt install -y nmap net-tools dnsutils
sudo apt install -y hping3 slowloris
sudo apt install -y aircrack-ng macchanger

# ============================================================
# 4. تثبيت أدوات Metasploit
# ============================================================
echo ""
echo "[4/6] Installing Metasploit framework..."
sudo apt install -y metasploit-framework
sudo msfdb init 2>/dev/null

# ============================================================
# 5. إعداد بيئة بايثون وتثبيت المكتبات
# ============================================================
echo ""
echo "[5/6] Setting up Python environment..."

# إنشاء بيئة افتراضية
python3 -m venv ~/Omega-Proxy/omega_env

# تفعيل البيئة وتثبيت المكتبات
source ~/Omega-Proxy/omega_env/bin/activate

pip install --upgrade pip
pip install groq scapy requests paramiko
pip install pycryptodome python-nmap

# ============================================================
# 6. تثبيت مكتبات بايثون في النظام
# ============================================================
echo ""
echo "[6/6] Installing system Python packages..."
sudo apt install -y python3-scapy python3-requests

# ============================================================
# الانتهاء
# ============================================================
echo ""
echo "╔══════════════════════════════════════════════════════════╗"
echo "║                                                          ║"
echo "║      ✅ OMEGA-PROXY v11.0 Setup Completed ✅             ║"
echo "║                                                          ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""
echo "How to run the tool:"
echo "  cd ~/Omega-Proxy"
echo "  source omega_env/bin/activate"
echo "  sudo -E env PATH=\$PATH python3 omega_proxy_ai.py"
echo ""
echo "Happy Hacking! 🔥"
