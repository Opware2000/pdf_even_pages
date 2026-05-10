#!/bin/bash
set -e

echo "📦 Installation de pdf_even_pages avec uv..."

# Vérifier que uv est installé
if ! command -v uv &> /dev/null; then
    echo "❌ uv n'est pas installé. Installer : https://docs.astral.sh/uv/"
    exit 1
fi

# Installer le projet en mode développement
echo "📥 Installation des dépendances..."
uv pip install -e .

# Vérifier l'installation
echo "✅ Vérification..."
pdf_even_pages --help

echo "✨ Installation terminée ! Vous pouvez utiliser 'pdf_even_pages' de n'importe quel dossier."
