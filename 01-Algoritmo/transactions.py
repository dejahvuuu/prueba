import json
from datetime import datetime
import heapq
from concurrent.futures import ThreadPoolExecutor, as_completed

start_time = datetime(2025, 3, 1, 0, 0)  
end_time = datetime(2025, 3, 31, 23, 59)  
file_path = "transactions.json"  

batch_size = 1000 

client_count = {}

def process_batch(batch):
    local_count = {}
    for record in batch:
        try:
            data = json.loads(record.strip())
            timestamp = datetime.fromisoformat(data["timestamp"])

            if start_time <= timestamp <= end_time:
                client_id = data["client_id"]

                if client_id not in local_count:
                    local_count[client_id] = 0
                local_count[client_id] += 1

        except Exception as e:
            print(f"Error al procesar transacción: {e}")
    return local_count

def merge_counts(local_count):
    for client_id, count in local_count.items():
        if client_id not in client_count:
            client_count[client_id] = 0
        client_count[client_id] += count

def process_transactions(file_path, batch_size):
    with open(file_path, 'r') as file:
        batch = []
        futures = []

        # Aca implemento concurrencia
        with ThreadPoolExecutor(max_workers=4) as executor: 
            for line in file:
                batch.append(line.strip())
                
                if len(batch) >= batch_size:
                    futures.append(executor.submit(process_batch, batch))
                    batch = []

            if batch:
                futures.append(executor.submit(process_batch, batch))

        for future in as_completed(futures):
            local_count = future.result()
            merge_counts(local_count)

process_transactions(file_path, batch_size)

top_clients = heapq.nlargest(10, client_count.items(), key=lambda x: x[1])

print("Top 10 clientes más frecuentes:")
for client_id, transactions in top_clients:
    print(f"Cliente {client_id}: {transactions} transacciones")
