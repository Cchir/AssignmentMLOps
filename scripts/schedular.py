import time
import datetime
import subprocess

def log(msg):
    print(f"[{datetime.datetime.now()}] {msg}")

if __name__ == "__main__":
    log("Penguin Prediction Scheduler Started")
    while True:
        try:
            # Run predict script
            log("Running prediction...")
            subprocess.run(["python", "scripts/predict.py"], check=True)
            log("Prediction complete.")
        except Exception as e:
            log(f"Error running prediction: {e}")

        # Sleep for 24 hours (or 10s for testing)
        time.sleep(86400)  # 86400 seconds = 24 hours
