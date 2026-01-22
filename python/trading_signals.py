"""
BTC Sentiment API - Trading Signals Example
Generate buy/sell signals based on market sentiment.
"""

import requests
from dataclasses import dataclass
from typing import Optional

# Configuration
API_KEY = "YOUR_RAPIDAPI_KEY"
BASE_URL = "https://btc-real-time-sentiment-news-analysis.p.rapidapi.com"

HEADERS = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "btc-real-time-sentiment-news-analysis.p.rapidapi.com"
}


@dataclass
class TradingSignal:
    action: str          # "BUY", "SELL", "HOLD"
    strength: str        # "strong", "moderate", "weak"
    score: int           # 0-100
    state: str           # Market state
    position_size: float # Suggested position multiplier
    reason: str          # Explanation


def get_sentiment():
    """Fetch current sentiment from API."""
    response = requests.get(f"{BASE_URL}/current", headers=HEADERS)
    response.raise_for_status()
    return response.json()["data"]


def generate_signal(sentiment: dict) -> TradingSignal:
    """
    Generate trading signal based on sentiment.
    
    Strategy:
    - Extreme Fear (0-24): Strong BUY signal (contrarian)
    - Fear (25-39): Moderate BUY signal
    - Neutral (40-59): HOLD
    - Greed (60-74): Moderate SELL signal
    - Extreme Greed (75-100): Strong SELL signal (contrarian)
    """
    score = sentiment["score"]
    state = sentiment["state"]
    trend = sentiment["trend"]
    
    # Extreme Fear - Strong Buy Zone
    if score <= 24:
        return TradingSignal(
            action="BUY",
            strength="strong",
            score=score,
            state=state,
            position_size=1.5,
            reason=f"Extreme fear detected (score: {score}). Historically a strong buy zone."
        )
    
    # Fear - Accumulation Zone
    elif score <= 39:
        multiplier = 1.25 if trend == "falling" else 1.1
        return TradingSignal(
            action="BUY",
            strength="moderate",
            score=score,
            state=state,
            position_size=multiplier,
            reason=f"Fear in market (score: {score}). Good accumulation opportunity."
        )
    
    # Neutral - Hold
    elif score <= 59:
        return TradingSignal(
            action="HOLD",
            strength="weak",
            score=score,
            state=state,
            position_size=1.0,
            reason=f"Neutral sentiment (score: {score}). Wait for clearer signal."
        )
    
    # Greed - Take Profits Zone
    elif score <= 74:
        multiplier = 0.75 if trend == "rising" else 0.9
        return TradingSignal(
            action="SELL",
            strength="moderate",
            score=score,
            state=state,
            position_size=multiplier,
            reason=f"Greed detected (score: {score}). Consider taking partial profits."
        )
    
    # Extreme Greed - Strong Sell Zone
    else:
        return TradingSignal(
            action="SELL",
            strength="strong",
            score=score,
            state=state,
            position_size=0.5,
            reason=f"Extreme greed (score: {score}). High risk of correction."
        )


def main():
    print("=" * 60)
    print("BTC SENTIMENT TRADING SIGNAL GENERATOR")
    print("=" * 60)
    
    # Fetch sentiment
    sentiment = get_sentiment()
    
    print(f"\nCurrent Sentiment:")
    print(f"  Score: {sentiment['score']}/100")
    print(f"  State: {sentiment['state']} {sentiment['emoji']}")
    print(f"  Trend: {sentiment['trend']}")
    
    # Generate signal
    signal = generate_signal(sentiment)
    
    print(f"\n{'=' * 60}")
    print(f"SIGNAL: {signal.action} ({signal.strength.upper()})")
    print(f"{'=' * 60}")
    print(f"  Position Size Multiplier: {signal.position_size}x")
    print(f"  Reason: {signal.reason}")
    
    # Action colors for terminal
    colors = {"BUY": "\033[92m", "SELL": "\033[91m", "HOLD": "\033[93m"}
    reset = "\033[0m"
    
    print(f"\n{colors[signal.action]}>>> {signal.action} <<<{reset}")


if __name__ == "__main__":
    main()
