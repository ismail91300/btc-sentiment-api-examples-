#!/bin/bash
#
# BTC Sentiment API - cURL Examples
# Quick command-line access to Bitcoin sentiment data.
#

API_KEY="YOUR_RAPIDAPI_KEY"
HOST="btc-real-time-sentiment-news-analysis.p.rapidapi.com"
BASE_URL="https://${HOST}"

echo "=============================================="
echo "BTC Sentiment API - cURL Examples"
echo "=============================================="

# 1. Get Current Sentiment (Free plan)
echo ""
echo ">>> GET /current (Free plan)"
echo ""
curl -s "${BASE_URL}/current" \
  -H "X-RapidAPI-Key: ${API_KEY}" \
  -H "X-RapidAPI-Host: ${HOST}" | jq .

# 2. Get Breakdown by Source (Pro plan)
echo ""
echo ">>> GET /breakdown (Pro plan)"
echo ""
curl -s "${BASE_URL}/breakdown" \
  -H "X-RapidAPI-Key: ${API_KEY}" \
  -H "X-RapidAPI-Host: ${HOST}" | jq .

# 3. Get Headlines (Pro plan)
echo ""
echo ">>> GET /headlines?limit=3 (Pro plan)"
echo ""
curl -s "${BASE_URL}/headlines?limit=3" \
  -H "X-RapidAPI-Key: ${API_KEY}" \
  -H "X-RapidAPI-Host: ${HOST}" | jq .

# 4. Get Macro Impact Events (Pro plan)
echo ""
echo ">>> GET /impact?days=7 (Pro plan)"
echo ""
curl -s "${BASE_URL}/impact?days=7" \
  -H "X-RapidAPI-Key: ${API_KEY}" \
  -H "X-RapidAPI-Host: ${HOST}" | jq .

# 5. Get Historical Data (Ultra plan)
echo ""
echo ">>> GET /history?days=7&interval=1h (Ultra plan)"
echo ""
curl -s "${BASE_URL}/history?days=7&interval=1h" \
  -H "X-RapidAPI-Key: ${API_KEY}" \
  -H "X-RapidAPI-Host: ${HOST}" | jq .
