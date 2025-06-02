tasks = {Add commentMore actions
    "Завдання 1": "виконано",
    "Завдання 2": "очікує",
    "Завдання 3": "в процесі"
}

def add_task(name, status):
    tasks[name] = status

def delete_task(name):
    tasks.pop(name, None)

def update_status(name, status):
    if name in tasks:
        tasks[name] = status

add_task("Завдання 4", "очікує")
update_status("Завдання 3", "виконано")
delete_task("Завдання 1")

print("Задачі:", tasks)

pending_tasks = [name for name, status in tasks.items() if status == "очікує"]
print("Задачі зі статусом 'очікує':", pending_tasks)