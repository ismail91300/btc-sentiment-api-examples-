# BTC Real-Time Sentiment API

[![RapidAPI](https://img.shields.io/badge/RapidAPI-Available-blue?style=for-the-badge&logo=rapidapi)](https://rapidapi.com/ismail91300/api/btc-real-time-sentiment-news-analysis)
[![Python](https://img.shields.io/badge/Python-3.7+-green?style=for-the-badge&logo=python)](https://python.org)
[![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-yellow?style=for-the-badge&logo=javascript)](https://nodejs.org)
[![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)](LICENSE)

Real-time Bitcoin market sentiment analysis powered by **FinBERT NLP**, aggregating data from 5+ professional crypto news sources. Updated every 5 minutes.

## Why This API?

| Feature | BTC Sentiment Pro | Competitors |
|---------|-------------------|-------------|
| Update Frequency | **5 minutes** | 1-6 hours |
| News Sources | **5+ specialized sites** | Twitter bots |
| NLP Model | **FinBERT (finance-specific)** | Basic dictionary |
| Macro Events | **Yes (Fed, Halving, etc.)** | No |
| Transparency | **Per-source breakdown** | Single score |

## Quick Start

### Get Your API Key

1. Visit [RapidAPI - BTC Sentiment](https://rapidapi.com/ismail91300/api/btc-real-time-sentiment-news-analysis)
2. Subscribe to a plan (Free tier available)
3. Copy your API key

### Installation

```bash
# Python
pip install requests

# Node.js
npm install axios
```

### Basic Usage

```python
import requests

response = requests.get(
    "https://btc-real-time-sentiment-news-analysis.p.rapidapi.com/current",
    headers={
        "X-RapidAPI-Key": "YOUR_API_KEY",
        "X-RapidAPI-Host": "btc-real-time-sentiment-news-analysis.p.rapidapi.com"
    }
)

data = response.json()
print(f"Score: {data['data']['score']}/100")
print(f"State: {data['data']['state']}")  # extreme_fear, fear, neutral, greed, extreme_greed
print(f"Trend: {data['data']['trend']}")  # rising, falling, stable
```

## Endpoints

| Endpoint | Description | Plans |
|----------|-------------|-------|
| `GET /current` | Current sentiment score & market state | Free, Pro, Ultra |
| `GET /breakdown` | Detailed score per news source | Pro, Ultra |
| `GET /headlines` | Latest headlines with sentiment | Pro, Ultra |
| `GET /impact` | Macro economic events calendar | Pro, Ultra |
| `GET /history` | Historical data for backtesting | Pro (7d), Ultra (90d) |

## Response Example

### GET /current

```json
{
  "success": true,
  "data": {
    "score": 62,
    "state": "greed",
    "label": "Greed",
    "emoji": "🤑",
    "trend": "rising",
    "sources_count": 5,
    "confidence": 0.87,
    "updated_at": "2026-01-22T15:30:00Z"
  }
}
```

### Sentiment States

| Score | State | Label | Emoji | Trading Signal |
|-------|-------|-------|-------|----------------|
| 0-24 | `extreme_fear` | Extreme Fear | 😱 | Strong Buy Zone |
| 25-39 | `fear` | Fear | 😧 | Accumulation Zone |
| 40-59 | `neutral` | Neutral | 😐 | Hold / Wait |
| 60-74 | `greed` | Greed | 🤑 | Take Profits |
| 75-100 | `extreme_greed` | Extreme Greed | 🚀 | Strong Sell Zone |

## Code Examples

### Python

- [basic_example.py](python/basic_example.py) - Simple API usage
- [trading_signals.py](python/trading_signals.py) - Generate trading signals
- [sentiment_monitor.py](python/sentiment_monitor.py) - Live monitoring with alerts

### JavaScript

- [basic_example.js](javascript/basic_example.js) - Node.js example
- [trading_bot.js](javascript/trading_bot.js) - Integration with trading bot

### PHP

- [basic_example.php](php/basic_example.php) - PHP integration

### cURL

- [examples.sh](curl/examples.sh) - Command-line examples

## Pricing

| Plan | Price | Requests/Month | Features |
|------|-------|----------------|----------|
| **Free** | $0 | 100 | `/current` only |
| **Pro** | $29 | 10,000 | All endpoints + 7 days history |
| **Ultra** | $99 | Unlimited | All + 90 days history + webhooks |

## Use Cases

### Trading Bots
Use sentiment as a filter for your trading strategy:
```python
if sentiment['score'] < 25:  # Extreme Fear
    # Increase position size - historically good buy zone
    position_multiplier = 1.5
elif sentiment['score'] > 75:  # Extreme Greed
    # Reduce exposure - take profits
    position_multiplier = 0.5
```

### Alerts & Notifications
Monitor sentiment changes and get notified:
```python
if sentiment['state'] != previous_state:
    send_alert(f"Sentiment changed: {previous_state} → {sentiment['state']}")
```

### Dashboards
Build real-time sentiment widgets for your dashboard with the `/current` endpoint.

### Backtesting
Use `/history` endpoint to backtest sentiment-based strategies on historical data.

## Rate Limits

| Plan | Requests/Minute | Requests/Month |
|------|-----------------|----------------|
| Free | 5 | 100 |
| Pro | 60 | 10,000 |
| Ultra | 300 | Unlimited |

## Support

- **Documentation**: [API Reference](https://rapidapi.com/ismail91300/api/btc-real-time-sentiment-news-analysis)
- **Issues**: [GitHub Issues](https://github.com/ismail91300/btc-sentiment-api-examples-/issues)
- **Email**: support@sahbi-systems.tech

## License

MIT License - see [LICENSE](LICENSE) for details.

---

Built with ❤️ by [SAHBI Systems](https://sahbi-systems.tech)
