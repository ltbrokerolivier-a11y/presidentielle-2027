"""Vérifie data/candidats.json et construit docs/index.html (aperçu hors ligne) à partir de index.html."""
import json, pathlib, sys

root = pathlib.Path(__file__).resolve().parent.parent
data = json.loads((root / "data" / "candidats.json").read_text(encoding="utf-8"))

# Contrôles minimaux : chaque candidat a les champs requis et chaque proposition une source.
erreurs = []
for c in data["candidats"]:
    for champ in ("id", "prenom", "nom", "parti", "statut", "declaration", "parcours", "propositions", "sources"):
        if champ not in c:
            erreurs.append(f"{c.get('id')}: champ manquant {champ}")
    for p in c.get("propositions", []):
        if not p.get("source", "").startswith("https://"):
            erreurs.append(f"{c['id']}: proposition sans source")
if len({c["id"] for c in data["candidats"]}) != len(data["candidats"]):
    erreurs.append("identifiants en double")
if erreurs:
    print("\n".join(erreurs)); sys.exit(1)

payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
html = (root / "index.html").read_text(encoding="utf-8").replace("/*__DATA__*/", payload)
(root / "docs").mkdir(exist_ok=True)
(root / "docs" / "index.html").write_text(html, encoding="utf-8")
print(f"OK : {len(data['candidats'])} candidats, docs/index.html écrit ({len(html)//1024} Ko)")
