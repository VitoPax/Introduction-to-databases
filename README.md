# Cycling Results Database — Flask Web App

A small Flask web application built for the Databases course at Politecnico di Torino (a.y. 2021/2022). It queries a MySQL database of cycling race results — cyclists, teams, stages, and individual standings.

## What it does

- **Search by stage**: look up which cyclists appear in the individual standings for a given stage code.
- **Full results view**: a combined table joining cyclists, their teams, and their stage results (edition, stage, team name).

## Schema

| Table | Description |
|---|---|
| `CICLISTA` | Cyclists — code, name, surname, nationality, team code, birth year |
| `SQUADRA` | Teams — code, name, founding year, city |
| `TAPPA` | Race stages — number, edition, start/end city, distance, and other stage details |
| `CLASSIFICA_INDIVIDUALE` | Individual standings — cyclist, stage, edition, finishing position |

## Stack

- Python / Flask
- SQLAlchemy (Core)
- MySQL

## Routes

| Route | Purpose |
|---|---|
| `/` | Form to search cyclists by stage code (`CodT`) |
| `/ciclista` | Full results table joining cyclists, teams, and standings |

## Setup

1. Install Flask (see the [official guide](https://flask.palletsprojects.com/en/2.1.x/installation/)), ideally inside a virtual environment in the project folder.
2. Running MySQL locally (e.g. via XAMPP)? Install the Python MySQL client:
   ```bash
   pip install mysqlclient
   ```
3. Create a `Ciclisti` database in MySQL with the four tables above.
4. Update the connection details in `app.py` (`username`, `password`, `host`, `dbname`) to match your local MySQL setup.
5. Run the app:
   ```bash
   python app.py
   ```
   It serves on `http://127.0.0.1:8080`.

## Known limitations

This was built as a coursework exercise, so a few things are on the to-do list rather than done:

- Query parameters (e.g. the stage code in `/`) aren't currently parameterized, which is a SQL-injection risk — safe to run locally for coursework, but would need fixing (e.g. with SQLAlchemy's `text()` + bound parameters) before exposing it beyond localhost.
- DB credentials are hardcoded in `app.py` rather than read from environment variables.
- The SQLAlchemy engine is created per-request instead of once at startup.
