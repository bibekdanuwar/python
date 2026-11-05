# Python Practice

Exercises and exam solutions from my programming course (専門学校).

## Structure
| Folder | Contents |
|--------|----------|
| `ch3/` | Chapter 3 exercises |
| `ch4/` | Chapter 4: web API requests |
| `ch5/` | Chapter 5: reading JSON, CSV and text files |
| `ch6/` | Chapter 6 exercises |
| `exams/` | Exam solutions |
| `misc/` | Extra practice: algorithms, images, small scripts |

## Setup
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

## Running
Run scripts from inside their own folder, since they read data files by name:

    cd ch5
    python3 5-2-3.py