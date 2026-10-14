def run_menu_choice(choice, tasks):
    if choice == "add":
        tasks.append("new task")
        return f"{len(tasks)} task(s)"
    elif choice == "clear":
        tasks.clear()
        return "0 task(s)"
    elif choice == "count":
        return f"{len(tasks)} task(s)"
    else:
        return "Unknown choice"


def safe_int(text):
    return int(text)


def set_age(person, age):
    person["age"] = age
    return person


def ask_for_number(prompt):
    return int(input(prompt))
