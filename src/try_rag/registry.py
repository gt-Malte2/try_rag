TASKS = {}


def task(name: str):
    def decorator(func):
        TASKS[name] = func
        return func

    return decorator


def run_task(name: str):
    if name not in TASKS:
        raise ValueError(f"Task '{name}' not registered")
    return TASKS[name]()
