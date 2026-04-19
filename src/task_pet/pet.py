import random

COMMON_PLANTS = ["🌷", "🌸", "🌼", "🌻", "🪴"]
RARE_PLANTS = ["🌺", "🌹", "🌵", "🍀", "🪷"]


def create_task(name):
    return {
        "name": name,
        "done": False,
    }


def complete_task(tasks, index):
    if tasks[index]["done"]:
        return False

    tasks[index]["done"] = True
    return True


def reset_tasks(tasks):
    for task in tasks:
        task["done"] = False


def all_tasks_completed(tasks):
    return all(task["done"] for task in tasks)


def get_final_plant():
    roll = random.randint(1, 100)

    if roll <= 75:
        rarity = "common"
        emoji = random.choice(COMMON_PLANTS)
    else:
        rarity = "rare"
        emoji = random.choice(RARE_PLANTS)

    return emoji, rarity
