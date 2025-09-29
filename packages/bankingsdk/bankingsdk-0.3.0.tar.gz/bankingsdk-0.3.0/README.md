# BANQUE SDK - `bankingsdk`

Un SDK Python simple pour interagir avec l’API REST de données d'un portefeuille client demandeur de ligne de crédit bancaire. Il est conçu pour les **Data Analysts** et **Data Scientists**, avec une prise en charge native de **Pydantic**, **dictionnaires** et **DataFrames Pandas**.

[![PyPI version](https://badge.fury.io/py/bankingsdk.svg)](https://badge.fury.io/py/bankingsdk)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

---

## Installation

```bash
pip install bankingsdk
```

---

## Configuration

```python
from bankingsdk import DemandeClient, BankConfig

# Configuration avec l’URL de votre API (Render ou locale)
config = BankConfig(movie_base_url="https://api-risk-credit.onrender.com")
client = DemandeClient(config=config)
```

---

## Tester le SDK

### 1. Health check

```python
client.health_check()
# Retourne : {"status": "ok"}
```

### 2. Récupérer une demande

```python
demande = client.get_demande(1)
print(demande.agence)
```

### 3. Liste des demandes au format DataFrame

```python
df = client.list_demandes(limit=5, output_format="pandas")
print(df.head())
```

---

## Modes de sortie disponibles

Toutes les méthodes de liste (`list_demandes`, `list_agences`, etc.) peuvent retourner :

- des objets **Pydantic** (défaut)
- des **dictionnaires**
- des **DataFrames Pandas**

Exemple :

```python
client.list_demandes(limit=10, output_format="dict")
client.list_agences(limit=10, output_format="pandas")
```

---

## Tester en local

Vous pouvez aussi utiliser une API locale :

```python
config = BankConfig(bank_base_url="http://localhost:8000")
client = DemandeClient(config=config)
```

---

## Public cible

- Data Analysts
- Data Scientists
- Étudiants et curieux en Data
- Développeurs Python

---

## Licence

MIT License

---

## Liens utiles

- API Render : [https://api-risk-credit.onrender.com/](https://api-risk-credit.onrender.com/)
- PyPI : [https://pypi.org/project/bankingsdk](https://pypi.org/project/bankingsdk)