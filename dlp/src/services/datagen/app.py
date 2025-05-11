import random
import time
import json
from datetime import datetime
import os

# Ensure data directory exists
os.makedirs("/data", exist_ok=True)

def generate_random_log():
    """Generate a random log entry"""
    log_levels = ["INFO", "DEBUG", "WARNING", "ERROR", "CRITICAL"]
    services = ["web-server", "database", "auth-service", "api-gateway", "frontend"]
    messages = [
        "User logged in",
        "Database query executed",
        "API request received",
        "Cache miss",
        "File uploaded",
        "Payment processed",
        "Email sent"
    ]
    
    return {
        "timestamp": datetime.now().isoformat(),
        "level": random.choice(log_levels),
        "service": random.choice(services),
        "message": random.choice(messages),
        "details": {
            "user_id": random.randint(1000, 9999),
            "duration_ms": random.randint(5, 500)
        }
    }

def main():
    """Generate random logs and write to shared volume"""
    print("Starting data generator service...")
    
    counter = 0
    while True:
        log_entry = generate_random_log()
        
        # Write to shared volume
        filename = f"/data/logs_{datetime.now().strftime('%Y%m%d')}.json"
        with open(filename, "a") as file:
            file.write(json.dumps(log_entry) + "\n")
        
        counter += 1
        print(f"Generated log entry #{counter}: {log_entry['level']} - {log_entry['message']}")
        
        # Sleep for a random interval (1-3 seconds)
        time.sleep(random.uniform(1, 3))

if __name__ == "__main__":
    main()
