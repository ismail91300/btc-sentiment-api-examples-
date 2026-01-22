"""
BTC Sentiment API - Basic Example
Get current Bitcoin market sentiment in seconds.
"""

import requests

# Configuration
API_KEY = "YOUR_RAPIDAPI_KEY"  # Get yours at: https://rapidapi.com/ismail91300/api/btc-real-time-sentiment-news-analysis
BASE_URL = "https://btc-real-time-sentiment-news-analysis.p.rapidapi.com"

HEADERS = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "btc-real-time-sentiment-news-analysis.p.rapidapi.com"
}


def get_current_sentiment():
    """Get the current BTC sentiment score and market state."""
    response = requests.get(f"{BASE_URL}/current", headers=HEADERS)
    response.raise_for_status()
    return response.json()


def get_breakdown():
    """Get detailed sentiment breakdown by source (Pro plan required)."""
    response = requests.get(f"{BASE_URL}/breakdown", headers=HEADERS)
    response.raise_for_status()
    return response.json()


def get_headlines(limit=5, sentiment_filter="all"):
    """Get latest crypto headlines with sentiment (Pro plan required)."""
    params = {"limit": limit, "sentiment": sentiment_filter}
    response = requests.get(f"{BASE_URL}/headlines", headers=HEADERS, params=params)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    # Get current sentiment
    print("=" * 50)
    print("BTC SENTIMENT - CURRENT")
    print("=" * 50)
    
    data = get_current_sentiment()
    
    if data["success"]:
        sentiment = data["data"]
        print(f"Score:      {sentiment['score']}/100")
        print(f"State:      {sentiment['state']} {sentiment['emoji']}")
        print(f"Trend:      {sentiment['trend']}")
        print(f"Sources:    {sentiment['sources_count']}")
        print(f"Confidence: {sentiment['confidence']:.0%}")
        print(f"Updated:    {sentiment['updated_at']}")
    else:
        print(f"Error: {data['error']['message']}")
    
    print()
    
    # Get breakdown (Pro plan)
    print("=" * 50)
    print("BTC SENTIMENT - BREAKDOWN BY SOURCE")
    print("=" * 50)
    
    try:
        breakdown = get_breakdown()
        if breakdown["success"]:
            for source, info in breakdown["data"]["sources"].items():
                print(f"{source:20} Score: {info['score']:3} ({info['sentiment']})")
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 403:
            print("Upgrade to Pro plan to access breakdown endpoint")
        else:
            print(f"Error: {e}")
