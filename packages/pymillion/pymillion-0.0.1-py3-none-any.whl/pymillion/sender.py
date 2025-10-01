import urllib.request
import json
from time import sleep

def send_batches(url, method, data_gen, batch_size=5000, delay=0.1):
    """Envía datos por lotes desde un generador"""
    method = method.upper()
    batch = []
    batch_count = 0

    for record in data_gen:
        batch.append(record)
        if len(batch) >= batch_size:
            batch_count += 1
            _send_batch(url, method, batch, batch_count)
            batch = []
            sleep(delay)
    
    if batch:  # enviar el último batch
        batch_count += 1
        _send_batch(url, method, batch, batch_count)

def _send_batch(url, method, batch, count):
    req = urllib.request.Request(
        url,
        data=json.dumps(batch).encode("utf-8"),
        method=method,
        headers={"Content-Type": "application/json"}
    )
    try:
        with urllib.request.urlopen(req) as resp:
            print(f"Batch {count} enviado, status {resp.status}")
    except Exception as e:
        print(f"Error en batch {count}: {e}")
