"""
BTC Sentiment API - Live Monitor
Monitor sentiment changes and get alerts when state changes.
"""

import requests
import time
from datetime import datetime

# Configuration
API_KEY = "YOUR_RAPIDAPI_KEY"
BASE_URL = "https://btc-real-time-sentiment-news-analysis.p.rapidapi.com"
CHECK_INTERVAL = 300  # 5 minutes (matches API update frequency)

HEADERS = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "btc-real-time-sentiment-news-analysis.p.rapidapi.com"
}

# State emojis for display
STATE_DISPLAY = {
    "extreme_fear": ("😱", "\033[91m"),   # Red
    "fear": ("😧", "\033[93m"),            # Yellow
    "neutral": ("😐", "\033[0m"),          # Default
    "greed": ("🤑", "\033[92m"),           # Green
    "extreme_greed": ("🚀", "\033[95m"),   # Magenta
}


def get_sentiment():
    """Fetch current sentiment."""
    response = requests.get(f"{BASE_URL}/current", headers=HEADERS)
    response.raise_for_status()
    return response.json()["data"]


def on_state_change(old_state: str, new_state: str, sentiment: dict):
    """
    Called when sentiment state changes.
    Customize this to send notifications (Telegram, Discord, Email, etc.)
    """
    print("\n" + "!" * 60)
    print(f"ALERT: Sentiment state changed!")
    print(f"  From: {old_state} → To: {new_state}")
    print(f"  Score: {sentiment['score']}")
    print("!" * 60 + "\n")
    
    # Example: Send to Telegram (uncomment and configure)
    # import requests
    # telegram_token = "YOUR_BOT_TOKEN"
    # chat_id = "YOUR_CHAT_ID"
    # message = f"🚨 BTC Sentiment Changed!\n{old_state} → {new_state}\nScore: {sentiment['score']}"
    # requests.post(f"https://api.telegram.org/bot{telegram_token}/sendMessage", 
    #               json={"chat_id": chat_id, "text": message})


def display_sentiment(sentiment: dict):
    """Display current sentiment in terminal."""
    state = sentiment["state"]
    emoji, color = STATE_DISPLAY.get(state, ("?", "\033[0m"))
    reset = "\033[0m"
    
    timestamp = datetime.now().strftime("%H:%M:%S")
    
    print(f"[{timestamp}] {color}Score: {sentiment['score']:3}/100 | "
          f"State: {state:15} {emoji} | "
          f"Trend: {sentiment['trend']}{reset}")


def monitor():
    """Main monitoring loop."""
    print("=" * 60)
    print("BTC SENTIMENT MONITOR")
    print(f"Checking every {CHECK_INTERVAL} seconds")
    print("Press Ctrl+C to stop")
    print("=" * 60 + "\n")
    
    previous_state = None
    
    while True:
        try:
            sentiment = get_sentiment()
            current_state = sentiment["state"]
            
            # Display current state
            display_sentiment(sentiment)
            
            # Check for state change
            if previous_state and current_state != previous_state:
                on_state_change(previous_state, current_state, sentiment)
            
            previous_state = current_state
            
            # Wait for next check
            time.sleep(CHECK_INTERVAL)
            
        except requests.exceptions.RequestException as e:
            print(f"[ERROR] API request failed: {e}")
            time.sleep(60)  # Wait 1 minute before retry
            
        except KeyboardInterrupt:
            print("\n\nMonitor stopped.")
            break


if __name__ == "__main__":
    monitor()
