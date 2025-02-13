read -p "What shell are you using? (zsh, fish, bash): " shellinuse

if [ "$shellinuse" == "zsh" ]; then
  export file="$HOME/.zshrc"
elif [ "$shellinuse" == "bash" ]; then
  export file="$HOME/.bashrc"
else
  export file="$HOME/.config/fish/config.fish"
fi

echo "alias harmony='python3 $PWD/menu.py'" >> "$file"
