#!/bin/bash

sudo apt update
sudo apt install -y xfce4-notifyd dbus-x11 libnotify-bin

shell=$(basename "$SHELL")

if [ "$shell" = "bash" ]; then
    shellrc="$HOME/.bashrc"
elif [ "$shell" = "zsh" ]; then
    shellrc="$HOME/.zshrc"
else
    echo "Unsupported shell: $shell"
    exit 1
fi

cat << 'EOF' >> "$shellrc"

# Start D-Bus if not running
if ! pgrep -x "dbus-daemon" > /dev/null
then
    sudo service dbus start
fi

# Set the D-Bus session address
export $(dbus-launch)

# Set DISPLAY for X server
export DISPLAY=:0

EOF

source "$shellrc"
echo "Setup complete. Please restart your terminal or source your $shellrc file."
