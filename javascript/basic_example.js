/**
 * BTC Sentiment API - Basic Example (Node.js)
 * Get current Bitcoin market sentiment.
 */

const axios = require('axios');

// Configuration
const API_KEY = 'YOUR_RAPIDAPI_KEY'; // Get yours at: https://rapidapi.com/ismail91300/api/btc-real-time-sentiment-news-analysis
const BASE_URL = 'https://btc-real-time-sentiment-news-analysis.p.rapidapi.com';

const headers = {
  'X-RapidAPI-Key': API_KEY,
  'X-RapidAPI-Host': 'btc-real-time-sentiment-news-analysis.p.rapidapi.com'
};

/**
 * Get current sentiment score and market state
 */
async function getCurrentSentiment() {
  const response = await axios.get(BASE_URL + '/current', { headers });
  return response.data;
}

/**
 * Get detailed breakdown by source (Pro plan)
 */
async function getBreakdown() {
  const response = await axios.get(BASE_URL + '/breakdown', { headers });
  return response.data;
}

/**
 * Get latest headlines with sentiment (Pro plan)
 */
async function getHeadlines(limit = 5) {
  const response = await axios.get(BASE_URL + '/headlines', {
    headers,
    params: { limit }
  });
  return response.data;
}

// Main execution
async function main() {
  console.log('==================================================');
  console.log('BTC SENTIMENT - CURRENT');
  console.log('==================================================');

  try {
    const data = await getCurrentSentiment();

    if (data.success) {
      const s = data.data;
      console.log('Score:      ' + s.score + '/100');
      console.log('State:      ' + s.state + ' ' + s.emoji);
      console.log('Trend:      ' + s.trend);
      console.log('Sources:    ' + s.sources_count);
      console.log('Confidence: ' + (s.confidence * 100).toFixed(0) + '%');
      console.log('Updated:    ' + s.updated_at);
    } else {
      console.log('Error: ' + data.error.message);
    }
  } catch (error) {
    console.error('Error:', error.message);
  }
}

main();
