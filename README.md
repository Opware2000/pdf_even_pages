# pdf_even_pages

Utilitaire Python pour ajouter une page blanche aux fichiers PDF ayant un nombre impair de pages.

## Description

**pdf_even_pages** traite automatiquement les PDF en ajoutant une page blanche au dernier si nécessaire. Utile pour les documents destinés à l'impression double-face ou à la reliure.

## Installation

### Prérequis
- Python 3.8+
- `uv` (gestionnaire de paquets Python) — [Installer](https://docs.astral.sh/uv/)

### Méthode rapide (macOS/Linux)

```bash
./install.sh
```

Cela va :
1. Vérifier que `uv` est installé
2. Installer les dépendances (`pypdf`)
3. Installer le projet en mode développement
4. Rendre la commande `pdf_even_pages` accessible globalement

### Installation manuelle

```bash
uv pip install -e .
```

## Utilisation

### Mode simple
```bash
pdf_even_pages document.pdf
```
Crée `document_even.pdf` avec une page blanche si nécessaire.

### Traiter plusieurs fichiers
```bash
pdf_even_pages *.pdf
```
Traite tous les PDF du répertoire courant.

### Options

| Option             | Description                                                           |
| ------------------ | --------------------------------------------------------------------- |
| `--inplace`        | Remplace les fichiers originaux (une sauvegarde `.bak.pdf` est créée) |
| `--outdir DOSSIER` | Sauvegarde les résultats dans le dossier spécifié (créé si absent)    |

### Exemples

**Remplacer les originaux :**
```bash
pdf_even_pages rapport.pdf facture.pdf --inplace
```
Crée `rapport.bak.pdf` et `facture.bak.pdf`, puis modifie les originaux.

**Sauvegarder dans un dossier :**
```bash
pdf_even_pages *.pdf --outdir ./pdf_processed/
```
Traite tous les PDF et sauvegarde les résultats dans `./pdf_processed/`.

## Comportement

- **Nombre pair de pages** → copie inchangée (ou sauvegardée selon l'option)
- **Nombre impair de pages** → page blanche ajoutée à la fin, au même format que la dernière page

## Aide

```bash
pdf_even_pages --help
```

## Licence

MIT
