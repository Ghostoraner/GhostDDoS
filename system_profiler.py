import psutil


def get_system_specs():
    """Собирает информацию о системе."""
    cpu_count = psutil.cpu_count(logical=False)
    cpu_threads = psutil.cpu_count(logical=True)
    ram_gb = psutil.virtual_memory().total / (1024 ** 3)

    return {
        "cpu_cores": cpu_count,
        "cpu_threads": cpu_threads,
        "ram_gb": round(ram_gb, 2)
    }


def get_attack_recommendations():
    """Выдает рекомендации на основе характеристик системы."""
    specs = get_system_specs()

    recommended_rps = min(specs['cpu_threads'] * 500, 5000)
    recommended_connections = specs['cpu_threads'] * 15
    recommended_duration = 120 if specs['ram_gb'] > 8 else 60

    return {
        "rps": recommended_rps,
        "connections": recommended_connections,
        "duration": recommended_duration
    }