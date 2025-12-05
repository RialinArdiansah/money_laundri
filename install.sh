#!/bin/bash

# Warna untuk output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}============================================${NC}"
echo -e "${BLUE}  Instalasi Sistem Manajemen Laundry${NC}"
echo -e "${BLUE}  Platform: Linux/macOS${NC}"
echo -e "${BLUE}============================================${NC}"
echo ""

# Detect OS
detect_os() {
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        if [ -f /etc/debian_version ]; then
            OS="debian"
        elif [ -f /etc/fedora-release ]; then
            OS="fedora"
        elif [ -f /etc/arch-release ]; then
            OS="arch"
        else
            OS="linux"
        fi
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        OS="macos"
    else
        OS="unknown"
    fi
    echo -e "${YELLOW}[INFO]${NC} Sistem operasi terdeteksi: $OS"
}

# Check Python
check_python() {
    echo -e "\n${BLUE}[1/7]${NC} Memeriksa Python..."
    
    if command -v python3 &> /dev/null; then
        PYTHON_CMD="python3"
        PIP_CMD="pip3"
    elif command -v python &> /dev/null; then
        PYTHON_CMD="python"
        PIP_CMD="pip"
    else
        echo -e "${RED}[ERROR]${NC} Python tidak ditemukan!"
        echo ""
        echo "Silakan install Python terlebih dahulu:"
        case $OS in
            debian)
                echo "  sudo apt install python3 python3-pip python3-venv"
                ;;
            fedora)
                echo "  sudo dnf install python3 python3-pip"
                ;;
            arch)
                echo "  sudo pacman -S python python-pip"
                ;;
            macos)
                echo "  brew install python3"
                ;;
            *)
                echo "  Install Python 3.10+ dari https://www.python.org"
                ;;
        esac
        exit 1
    fi
    
    $PYTHON_CMD --version
    echo -e "${GREEN}[OK]${NC} Python ditemukan."
}

# Install system dependencies
install_system_deps() {
    echo -e "\n${BLUE}[2/7]${NC} Memeriksa dependencies sistem..."
    
    case $OS in
        debian)
            echo -e "${YELLOW}[INFO]${NC} Menginstall dependencies untuk Ubuntu/Debian..."
            sudo apt update
            sudo apt install -y libjpeg-dev zlib1g-dev libpng-dev libpq-dev python3-venv
            ;;
        fedora)
            echo -e "${YELLOW}[INFO]${NC} Menginstall dependencies untuk Fedora..."
            sudo dnf install -y libjpeg-devel zlib-devel libpng-devel postgresql-devel gcc python3-devel
            ;;
        arch)
            echo -e "${YELLOW}[INFO]${NC} Menginstall dependencies untuk Arch Linux..."
            sudo pacman -S --noconfirm libjpeg-turbo zlib libpng postgresql-libs base-devel
            ;;
        macos)
            if command -v brew &> /dev/null; then
                echo -e "${YELLOW}[INFO]${NC} Menginstall dependencies untuk macOS..."
                brew install libjpeg zlib libpng
            else
                echo -e "${YELLOW}[WARNING]${NC} Homebrew tidak ditemukan. Dependencies mungkin perlu diinstall manual."
            fi
            ;;
        *)
            echo -e "${YELLOW}[WARNING]${NC} OS tidak dikenali. Pastikan dependencies Pillow dan psycopg2 terinstall."
            ;;
    esac
    
    echo -e "${GREEN}[OK]${NC} Dependencies sistem siap."
}

# Create virtual environment
create_venv() {
    echo -e "\n${BLUE}[3/7]${NC} Membuat Virtual Environment..."
    
    if [ -d "venv" ]; then
        echo -e "${YELLOW}[INFO]${NC} Virtual environment sudah ada, melewati..."
    else
        $PYTHON_CMD -m venv venv
        if [ $? -ne 0 ]; then
            echo -e "${RED}[ERROR]${NC} Gagal membuat virtual environment!"
            exit 1
        fi
    fi
    
    echo -e "${GREEN}[OK]${NC} Virtual environment siap."
}

# Activate virtual environment
activate_venv() {
    echo -e "\n${BLUE}[4/7]${NC} Mengaktifkan Virtual Environment..."
    
    source venv/bin/activate
    if [ $? -ne 0 ]; then
        echo -e "${RED}[ERROR]${NC} Gagal mengaktifkan virtual environment!"
        exit 1
    fi
    
    echo -e "${GREEN}[OK]${NC} Virtual environment aktif."
}

# Install Python dependencies
install_python_deps() {
    echo -e "\n${BLUE}[5/7]${NC} Menginstall dependencies Python..."
    
    # Upgrade pip
    pip install --upgrade pip
    
    # Install requirements
    pip install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo -e "${RED}[ERROR]${NC} Gagal menginstall dependencies Python!"
        exit 1
    fi
    
    echo -e "${GREEN}[OK]${NC} Dependencies Python terinstall."
}

# Setup environment file
setup_env() {
    echo -e "\n${BLUE}[6/7]${NC} Memeriksa file konfigurasi..."
    
    if [ ! -f ".env" ]; then
        if [ -f ".env.example" ]; then
            cp .env.example .env
            echo -e "${YELLOW}[INFO]${NC} File .env dibuat dari .env.example"
            echo -e "${YELLOW}[PENTING]${NC} Edit file .env dan sesuaikan konfigurasi database!"
        else
            echo -e "${YELLOW}[WARNING]${NC} File .env.example tidak ditemukan!"
        fi
    else
        echo -e "${GREEN}[OK]${NC} File .env sudah ada."
    fi
}

# Run migrations
run_migrations() {
    echo -e "\n${BLUE}[7/7]${NC} Menjalankan migrasi database..."
    
    python manage.py migrate
    if [ $? -ne 0 ]; then
        echo -e "${YELLOW}[WARNING]${NC} Migrasi gagal. Pastikan konfigurasi database benar di file .env"
    else
        echo -e "${GREEN}[OK]${NC} Migrasi database selesai."
    fi
}

# Main installation
main() {
    detect_os
    check_python
    install_system_deps
    create_venv
    activate_venv
    install_python_deps
    setup_env
    run_migrations
    
    echo ""
    echo -e "${BLUE}============================================${NC}"
    echo -e "${GREEN}  Instalasi Selesai!${NC}"
    echo -e "${BLUE}============================================${NC}"
    echo ""
    echo "Langkah selanjutnya:"
    echo "1. Edit file .env dan sesuaikan konfigurasi database"
    echo "2. Jalankan: python manage.py createsuperuser"
    echo "3. Jalankan: python manage.py runserver"
    echo "4. Buka browser: http://127.0.0.1:8000/"
    echo ""
    echo "Untuk mengaktifkan virtual environment di sesi baru:"
    echo "   source venv/bin/activate"
    echo ""
}

# Run main function
main
