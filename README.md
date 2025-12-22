# DA_Task

🧑‍💻 Team Workflow – GitHub & VS Code (lokal)

Dieses Projekt nutzt GitHub + VS Code (lokal) mit einem geschützten main-Branch.
👉 Direktes Arbeiten auf main ist nicht erlaubt – Änderungen laufen immer über Branches + Pull Requests.

🔒 Wichtige Regeln (bitte lesen!)
❌ Nicht direkt auf main pushen
✅ Jede Aufgabe = eigener Branch
✅ Änderungen nur über Pull Requests (PR)
✅ Mindestens 1 Review vor dem Merge


🚀 Setup (einmalig pro Person)
1) Repository klonen
git clone <REPO_URL>
cd <REPO_ORDNER>

2) VS Code öffnen
 code .

3) (Optional, empfohlen) Python-Umgebung

python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt


🔁 Standard-Workflow (jedes Mal gleich)
1️⃣ main aktualisieren
git checkout main
git pull

2️⃣ Eigenen Branch erstellen

Namensschema:

feature/<thema> für neue Features

fix/<thema> für Bugfixes

git checkout -b feature/data-cleaning

3️⃣ Arbeiten & committen
git add .
git commit -m "Add data cleaning pipeline"


💡 Kleine, verständliche Commits machen!

4️⃣ Branch pushen
git push -u origin feature/data-cleaning


(-u nur beim ersten Push nötig)

5️⃣ Pull Request (PR) erstellen

Auf GitHub:

PR von feature/... → main

Kurz beschreiben, was geändert wurde

Mindestens 1 Review abwarten

Danach Merge

⚠️ Konflikte vermeiden (sehr wichtig!)

Nicht gleichzeitig an derselben Datei arbeiten

Besonders bei Jupyter Notebooks

Regelmäßig main in den eigenen Branch holen:

git checkout main
git pull
git checkout feature/dein-branch
git merge main


Lieber mehr kleine PRs als ein riesiger

📁 Empfohlene Projektstruktur
project/
│
├─ data/          # Daten (nur wenn klein / erlaubt)
├─ notebooks/     # EDA & Experimente
├─ src/           # Python-Code (cleaning, models, utils)
├─ reports/       # Ergebnisse / Plots
│
├─ requirements.txt
├─ README.md
├─ .gitignore

🧠 Merksatz

Wenn du unsicher bist:
👉 main updaten → Branch erstellen → arbeiten → PR
