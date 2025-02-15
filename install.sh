#!/bin/bash


detect_package_manager() {
    if command -v apt &> /dev/null; then
        echo "apt"  # Debian/Ubuntu
    elif command -v dnf &> /dev/null; then
        echo "dnf"  # Fedora
    elif command -v yum &> /dev/null; then
        echo "yum"  # RHEL/CentOS
    elif command -v pacman &> /dev/null; then
        echo "pacman"  # Arch Linux
    else
        echo "unknown"
    fi
}


install_tkinter() {
    local package_manager=$1
    case $package_manager in
        apt)
            sudo apt update
            sudo apt install -y python3-tk
            ;;
        dnf|yum)
            sudo $package_manager install -y python3-tkinter
            ;;
        pacman)
            sudo pacman -S tk
            ;;
        *)
            echo "Gerenciador de pacotes não suportado ou não detectado."
            echo "Por favor, instale manualmente o tkinter para o seu sistema."
            exit 1
            ;;
    esac
}


VENV_DIR="/tmp/pdf-split-pro-venv"
if [ ! -d "$VENV_DIR" ]; then
    echo "Criando ambiente virtual em $VENV_DIR..."
    python3 -m venv "$VENV_DIR"
fi


echo "Ativando ambiente virtual..."
source "$VENV_DIR/bin/activate"


package_manager=$(detect_package_manager)


echo "Detectado gerenciador de pacotes: $package_manager"
install_tkinter "$package_manager"


echo "Instalando dependências do Python..."
pip install -r requirements.txt


echo "Verificando se o tkinter está instalado corretamente..."
python3 -c "import tkinter; print('Tkinter está instalado corretamente!')"


echo "Desativando ambiente virtual..."
deactivate

echo "Instalação concluída com sucesso!"
