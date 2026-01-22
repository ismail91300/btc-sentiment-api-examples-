/**
 * BTC Sentiment API - Trading Bot Integration
 * Example of integrating sentiment into your trading bot.
 */

const axios = require('axios');

// Configuration
const API_KEY = 'YOUR_RAPIDAPI_KEY';
const BASE_URL = 'https://btc-real-time-sentiment-news-analysis.p.rapidapi.com';

const headers = {
  'X-RapidAPI-Key': API_KEY,
  'X-RapidAPI-Host': 'btc-real-time-sentiment-news-analysis.p.rapidapi.com'
};

/**
 * Sentiment-based position sizing
 */
function getPositionMultiplier(score, state) {
  // Extreme Fear - increase position (contrarian)
  if (score <= 24) return 1.5;
  
  // Fear - slightly increase
  if (score <= 39) return 1.25;
  
  // Neutral - normal size
  if (score <= 59) return 1.0;
  
  // Greed - reduce position
  if (score <= 74) return 0.75;
  
  // Extreme Greed - minimize exposure
  return 0.5;
}

/**
 * Check if trading conditions are favorable
 */
function shouldTrade(sentiment) {
  const score = sentiment.score;
  const confidence = sentiment.confidence;
  
  // Don't trade if confidence is too low
  if (confidence < 0.5) {
    return { trade: false, reason: 'Low confidence: ' + confidence };
  }
  
  // Don't trade in extreme greed unless shorting
  if (score >= 80) {
    return { trade: false, reason: 'Extreme greed - high risk zone' };
  }
  
  return { trade: true, reason: 'Conditions favorable' };
}

/**
 * Example trading decision
 */
async function makeDecision(basePositionSize) {
  try {
    // Fetch sentiment
    const response = await axios.get(BASE_URL + '/current', { headers });
    const sentiment = response.data.data;
    
    console.log('\n--- Sentiment Analysis ---');
    console.log('Score:', sentiment.score);
    console.log('State:', sentiment.state);
    console.log('Trend:', sentiment.trend);
    console.log('Confidence:', sentiment.confidence);
    
    // Check if we should trade
    const tradeCheck = shouldTrade(sentiment);
    
    if (!tradeCheck.trade) {
      console.log('\n>>> SKIP TRADE:', tradeCheck.reason);
      return null;
    }
    
    // Calculate position size
    const multiplier = getPositionMultiplier(sentiment.score, sentiment.state);
    const adjustedPosition = basePositionSize * multiplier;
    
    console.log('\n--- Trading Decision ---');
    console.log('Base Position:', basePositionSize);
    console.log('Multiplier:', multiplier + 'x');
    console.log('Adjusted Position:', adjustedPosition);
    
    return {
      sentiment: sentiment,
      position: adjustedPosition,
      multiplier: multiplier
    };
    
  } catch (error) {
    console.error('Error fetching sentiment:', error.message);
    return null;
  }
}

// Example usage
makeDecision(10000); // Base position of $10,000
