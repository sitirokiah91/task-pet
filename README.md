# Task Pet 🌱

A gamified focus app where completed tasks grow plant companions over time.

Finish all tasks before the timer ends to help your plant thrive.  
Miss the round, and it returns to seed. Try again, grow again.

Built for people who need progress to feel visible, gentle, and alive.

---

## Core Idea

Many tasks disappear the moment they are done.

Task Pet turns completed focus rounds into something you can keep:
a growing garden filled with proof that you showed up.

Open the app and think:

> Oh hey. I did that.

---

## Why I Built This

Traditional productivity systems stopped working for me.

I wanted something with:
- urgency
- emotional connection
- visible progress
- playful stakes
- short focus rounds
- evidence of growth over time

So I’m building Task Pet.

---

## Gameplay Loop

1. Add one or more tasks  
2. Choose a timer:
   - 5 minutes
   - 10 minutes
   - 25 minutes
   - Custom
3. Start the round  
4. Complete **all** tasks before time runs out  
5. Win: your plant grows  
6. Lose: your plant returns to seed 🌰  
7. Mature plants move into your garden 🌿

---

## The Garden

Each completed plant becomes part of your long-term garden.

Every plant remembers:
- what tasks helped grow it
- planted date
- your progress over time

The garden exists to remind you:

You are not starting from nothing.

---

## Current Status

### MVP In Progress
- [x] Initial desktop GUI window
- [x] Working Python environment
- [x] First clickable prototype
- [x] Add task input
- [x] Task list
- [x] Timer presets
- [x] Start round logic
- [x] Countdown timer
- [ ] Growth states (seed → sprout → adult)
- [ ] Garden view
- [ ] Save/load data

---

## Tech Stack

- Python
- CustomTkinter
- Local JSON storage
- Git + GitHub

---

## Project Structure


src/task_pet/
├── main.py
├── ui.py
├── pet.py
└── storage.py

---

## Run locally

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/task_pet/main.py

---

## Future Ideas
	•	Rare seed types
	•	Plant personalities
	•	Seasonal garden themes
	•	Tap a plant to view the tasks that grew it
	•	Plant encounters where they boast about their trainers

---

## Author

Built by Siti Rokiah (Rora)
QA → Developer → AI Engineer journey in progress.
