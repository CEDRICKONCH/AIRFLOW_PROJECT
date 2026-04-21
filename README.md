# 🚀 Projet Airflow - Portfolio

Projet d'apprentissage et de démonstration des compétences en **Apache Airflow**, mettant en avant les concepts clés de l'orchestration de workflows.

## 📋 Contenu du Projet

Ce projet contient **11 DAGs progressifs** couvrant les concepts fondamentaux à avancés d'Airflow :

### 1️⃣ **DAGs Basiques**
- **`1_first_dag.py`** - Première DAG : définition basique, tâches Python et dépendances simples
- **`2_dag_versioning.py`** - Gestion des versions de DAGs

### 2️⃣ **Opérateurs & Types de Tâches**
- **`3_operators.py`** - Utilisation de différents opérateurs (Python, Bash, etc.)
- **`5_XCOMs_kwargs.py`** - Communication manuelle entre tâches avec XComs et kwargs

### 3️⃣ **Communication entre Tâches (XComs)**
- **`4_Xcoms_auto.py`** - XComs automatiques : passage de données implicite entre tâches
- **`7_branches.py`** - Branching conditionnel avec XComs pour contrôler le flux d'exécution
  - Extraction de données de multiples sources (API, BD, S3)
  - Transformation parallèle des données
  - Décision basée sur conditions (weekend/workday)

### 4️⃣ **Parallélisation & Dépendances**
- **`6_parallel_tasks.py`** - Exécution parallèle de tâches multiples
- **`7_branches.py`** - Tâches parallèles avec dépendances complexes

### 5️⃣ **Planification & Scheduling**
- **`8_schedules_preset.py`** - Scheduling avec présets prédéfinis
- **`9_schedule_cron.py`** - Scheduling avec expressions CRON
- **`10_schedule_delta.py`** - Scheduling avec delta time (délais relatifs)
- **`11_incremental load.py`** - Chargement incrémental de données avec date intervals et catchup

## 🎯 Compétences Démontrées

### ✅ Concepts Maîtrisés
- ✔️ **Déclaration et instantiation de DAGs**
- ✔️ **Opérateurs** : PythonOperator, BashOperator
- ✔️ **Task Decorators** : `@task.python`, `@task.bash`, `@task.branch`
- ✔️ **Dépendances entre tâches** : chaînage (`>>`, `<<`) et dépendances complexes
- ✔️ **Communication inter-tâches** : XComs automatiques et manuels (xcom_push/xcom_pull)
- ✔️ **Contrôle de flux** : branching conditionnel, décisions basées sur conditions
- ✔️ **Parallélisation** : exécution simultanée de tâches indépendantes
- ✔️ **Scheduling** : CRON, Delta Time, Presets prédéfinis
- ✔️ **Chargement incrémental** : Data Interval Start/End, Catchup
- ✔️ **Context & Kwargs** : accès aux métadonnées d'exécution (ti, data_interval_start, etc.)
- ✔️ **Templating Jinja2** : utilisation de variables template dans Bash

## 🏗️ Architecture & Pattern ETL

Les DAGs démontrent un pattern ETL classique :

```
Extract → Transform → Load
```

Exemple avancé avec branching :
```
Extract (multiples sources)
    ↓
Transform (parallèle)
    ↓
Decider (branchement conditionnel)
    ├→ Load (si workday)
    └→ No-Load (si weekend)
```

## 🛠️ Technologies & Stack

- **Apache Airflow** (SDK/Airflow 2.x+)
- **Python 3.x**
- **Pendulum** (gestion des timezones et dates)
- **Airflow Decorators** (syntaxe moderne)
- **CronTriggerTimetable & DeltaTriggerTimetable**

## 📂 Structure du Projet

```
.
├── dags/
│   ├── 1_first_dag.py
│   ├── 2_dag_versioning.py
│   ├── 3_operators.py
│   ├── 4_Xcoms_auto.py
│   ├── 5_XCOMs_kwargs.py
│   ├── 6_parallel_tasks.py
│   ├── 7_branches.py
│   ├── 8_schedules_preset.py
│   ├── 9_schedule_cron.py
│   ├── 10_schedule_delta.py
│   └── 11_incremental load.py
├── logs/
└── README.md
```

## 🚀 Guide de Démarrage

### Prérequis
```bash
pip install apache-airflow pendulum
```

### Initialiser Airflow
```bash
airflow standalone
```

### Accéder à l'interface Web
- URL : `http://localhost:8080`
- Login : `admin` / `admin` (par défaut)

### Déclencher une DAG
```bash
airflow dags trigger <dag_id>
```

## 📊 Points d'Apprentissage Clés

| Concept | Fichier | Niveau |
|---------|---------|--------|
| Bases Airflow | 1_first_dag.py | Débutant |
| XComs Automatiques | 4_Xcoms_auto.py | Débutant+ |
| XComs Manuels | 5_XCOMs_kwargs.py | Intermédiaire |
| Parallélisation | 6_parallel_tasks.py | Intermédiaire |
| Branching Conditionnel | 7_branches.py | Intermédiaire+ |
| CRON Scheduling | 9_schedule_cron.py | Avancé |
| Chargement Incrémental | 11_incremental load.py | Avancé |

## 💡 Cas d'Usage Réels

Ces DAGs sont directement applicables à des scenarios réels :

- 📊 **ETL Pipelines** : extraction, transformation et chargement de données
- 🔄 **Synchronisation Incrémentale** : chargement uniquement des deltas (changements)
- 🌍 **Multi-Source Integration** : intégration de données depuis API, BD, S3, etc.
- ⏰ **Scheduled Reports** : génération périodique de rapports
- 🔀 **Conditional Workflows** : workflows complexes avec décisions métier

## 📝 Notes Personnelles

Ce projet représente une progression pédagogique complète, du "Hello World" d'Airflow aux patterns avancés d'orchestration de données. Chaque DAG ajoute une couche de complexité, permettant une compréhension progressive des concepts.

## 🔗 Ressources Utiles

- [Documentation Apache Airflow](https://airflow.apache.org/docs/)
- [Airflow Community](https://airflow.apache.org/community/)
- [Pendulum Documentation](https://pendulum.eustace.io/)

---

**Auteur** : Cedric Konchie  
**Date** : 2026  
**Statut** : Complété ✅