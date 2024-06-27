#!/usr/bin/zsh

pip install -r requirements.txt

for file in ui/*; do
  pyuic5 -o "src/gui/$(basename "$file" .ui)_ui.py" "$file"
done