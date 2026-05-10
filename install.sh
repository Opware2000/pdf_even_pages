#!/bin/bash
set -e

echo "📦 Installation de pdf_even_pages..."

# Vérifier que uv est installé
if ! command -v uv &> /dev/null; then
    echo "❌ uv n'est pas installé. Installer : https://docs.astral.sh/uv/"
    exit 1
fi

# Installer le projet comme outil global avec uv
echo "📥 Installation en tant qu'outil global..."
uv tool install -e .

# Vérifier l'installation
echo "✅ Vérification..."
pdf_even_pages --help

echo ""
echo "✨ Installation terminée !"
echo "Vous pouvez maintenant utiliser 'pdf_even_pages' de n'importe quel dossier !"
