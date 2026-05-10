#!/usr/bin/env python3
"""
pdf_even_pages.py – Ajoute une page blanche aux PDF ayant un nombre de pages impair.
Usage :
    python3 pdf_even_pages.py fichier.pdf [fichier2.pdf ...]
    python3 pdf_even_pages.py *.pdf
    python3 pdf_even_pages.py *.pdf --inplace      # écrase les originaux
    python3 pdf_even_pages.py *.pdf --outdir ./out  # dossier de sortie
"""

import argparse
import sys
from pathlib import Path
from pypdf import PdfReader, PdfWriter
from pypdf.generic import RectangleObject


def add_blank_if_odd(input_path: Path, output_path: Path) -> str:
    reader = PdfReader(str(input_path))
    n = len(reader.pages)

    if n % 2 == 0:
        # Nombre pair : copie simple
        if input_path != output_path:
            import shutil
            shutil.copy2(input_path, output_path)
        return f"  ✔  {input_path.name}  ({n} pages, pair – inchangé)"

    # Nombre impair : on ajoute une page blanche
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)

    # Page blanche au même format que la dernière page
    last = reader.pages[-1]
    w = float(last.mediabox.width)
    h = float(last.mediabox.height)
    blank = writer.add_blank_page(width=w, height=h)

    with open(output_path, "wb") as f:
        writer.write(f)

    return f"  ✚  {input_path.name}  ({n} → {n+1} pages, page blanche ajoutée)"


def main():
    parser = argparse.ArgumentParser(
        description="Ajoute une page blanche aux PDF avec un nombre de pages impair."
    )
    parser.add_argument("pdfs", nargs="+", help="Fichiers PDF à traiter")
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--inplace", action="store_true",
        help="Écrase les fichiers originaux (une sauvegarde .bak est créée)"
    )
    group.add_argument(
        "--outdir", metavar="DOSSIER",
        help="Dossier de sortie (créé si inexistant). Par défaut : suffixe _even."
    )
    args = parser.parse_args()

    files = [Path(p) for p in args.pdfs]
    missing = [f for f in files if not f.exists()]
    if missing:
        print("Fichiers introuvables :", *missing, sep="\n  ")
        sys.exit(1)

    results = []
    for f in files:
        if args.inplace:
            bak = f.with_suffix(".bak.pdf")
            import shutil
            shutil.copy2(f, bak)
            out = f
        elif args.outdir:
            outdir = Path(args.outdir)
            outdir.mkdir(parents=True, exist_ok=True)
            out = outdir / f.name
        else:
            out = f.with_stem(f.stem + "_even")

        try:
            msg = add_blank_if_odd(f, out)
            results.append(msg)
        except Exception as e:
            results.append(f"  ✖  {f.name} – ERREUR : {e}")

    print(f"\n{'─'*55}")
    print(f"  {len(files)} fichier(s) traité(s)")
    print(f"{'─'*55}")
    for r in results:
        print(r)
    print(f"{'─'*55}\n")


if __name__ == "__main__":
    main()
