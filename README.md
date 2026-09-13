# VDA_1505 — runtime de table

Application Streamlit de table pour la chronique **Vampire V5 Dark Ages — Rennes 1505**.

## Autorité des données

- **Google Drive / CORPUS_ACTIF** reste la source de vérité du canon.
- **Supabase** stocke le runtime de table et des projections structurées dérivées.
- **GitHub** reste propriétaire du logiciel, du moteur, des migrations et des outils de synchronisation.

Une scène ouverte, un clic, une réponse affichée ou une chasse marquée « Jouée » dans l'application n'est **jamais** transformée automatiquement en événement canonique. Les faits joués doivent être revus par le MJ avant inscription dans `04A_DELTA_SESSION` puis consolidation dans leurs propriétaires.

`scenes_private/` signifie **scènes individuelles / solo** dans l'interface. Ce nom historique n'implique aucune confidentialité technique.

## Supabase runtime V1

La migration `supabase/migrations/0001_runtime_v1.sql` crée :

- `campaign_sessions`
- `runtime_events` (journal applicatif append-only par identifiants stables)
- `scene_runs`
- `hunt_runs`
- `published_scenes`
- `canon_entities` (projection Drive uniquement)
- `canon_sync_registry`

Les tables publiques ont RLS activé. V1 n'accorde aucun accès Data API à `anon` ou `authenticated`; seul le backend serveur utilisant la clé secrète peut lire/écrire.

## Configuration

Copier `.env.example` vers un mécanisme de secrets local/de déploiement. Ne jamais committer la clé secrète Supabase.

Variables :

- `SUPABASE_URL`
- `SUPABASE_SECRET_KEY` — serveur uniquement
- `VDA_SUPABASE_ENABLED=true|false`
- `VDA_SCENE_BACKEND=local|hybrid|supabase|snapshot`
- `VDA_1505_RUNTIME_DIR` — optionnel, défaut `~/.vda_1505`
- `VDA_RUNTIME_SNAPSHOT` — optionnel
- `VDA_APP_VERSION` — idéalement SHA Git déployé

Le backend de scènes reste `local` par défaut. `hybrid` charge le catalogue Python puis remplace les IDs disponibles dans Supabase. `supabase` privilégie Supabase, puis le snapshot local, puis les modules Python. Cette cascade maintient l'outil utilisable pendant une panne réseau.

L'état d'une scène ouverte est journalisé localement (`scene_runs.json`) avec la pile d'annulation. Après un redémarrage de Streamlit pendant une séance runtime encore ouverte, l'application restaure cette scène comme scène suspendue ainsi que les verrous irréversibles déjà déclenchés.

## Installation

Python 3.11 est la version de référence du CI. Pour une installation reproductible de table :

```bash
pip install -r requirements.lock.txt
pip check
streamlit run app.py
```

`requirements.txt` décrit les dépendances directes épinglées. `requirements.lock.txt` fige aussi leurs dépendances transitives à partir de l'environnement validé par CI. Après une mise à niveau volontaire, le lock doit être régénéré et revalidé avant une partie.

Sous Windows, `run.bat` crée le venv s'il manque puis resynchronise les dépendances à chaque lancement ; un venv déjà présent reçoit donc aussi les nouvelles dépendances.

## Mise en service Supabase

1. Appliquer `supabase/migrations/0001_runtime_v1.sql` au projet VDA dédié.
2. Configurer `SUPABASE_URL` et `SUPABASE_SECRET_KEY` dans les secrets du serveur.
3. Activer `VDA_SUPABASE_ENABLED=true` tout en gardant `VDA_SCENE_BACKEND=local`.
4. Publier les scènes et produire un snapshot hors ligne :

```bash
python -m scripts.publish_scenes --git-sha <SHA_DEPLOYE>
python -m scripts.build_runtime_snapshot --git-sha <SHA_DEPLOYE>
```

5. Tester `VDA_SCENE_BACKEND=hybrid` avant toute bascule vers `supabase`.

## Séances et pré-delta 04A

La barre latérale permet d'ouvrir/clore une séance runtime et de rejouer la file d'écritures hors ligne. Les mêmes opérations sont disponibles en CLI :

```bash
python -m scripts.runtime_session start --title "Séance Rennes"
python -m scripts.runtime_session status
python -m scripts.runtime_session sync
python -m scripts.runtime_session close
```

Pour produire un brouillon **non canonique** à relire :

```bash
python -m scripts.build_session_delta --session-id <UUID> --output pre_delta.md
```

Ce fichier est un aide-mémoire de consolidation. Il ne doit pas être injecté automatiquement dans Drive.

## Hors ligne

Le runtime écrit d'abord localement dans `~/.vda_1505` (ou `VDA_1505_RUNTIME_DIR`). Les écritures Supabase échouées sont mises en file puis rejouées. Les scènes peuvent également être lues depuis `runtime_snapshot.json`. Une indisponibilité Supabase ne doit donc pas interrompre une partie physique.
