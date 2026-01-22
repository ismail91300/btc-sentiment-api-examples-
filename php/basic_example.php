<?php
/**
 * BTC Sentiment API - Basic Example (PHP)
 * Get current Bitcoin market sentiment.
 */

// Configuration
$API_KEY = 'YOUR_RAPIDAPI_KEY'; // Get yours at: https://rapidapi.com/ismail91300/api/btc-real-time-sentiment-news-analysis
$BASE_URL = 'https://btc-real-time-sentiment-news-analysis.p.rapidapi.com';

/**
 * Make API request
 */
function apiRequest($endpoint, $params = []) {
    global $API_KEY, $BASE_URL;
    
    $url = $BASE_URL . $endpoint;
    if (!empty($params)) {
        $url .= '?' . http_build_query($params);
    }
    
    $ch = curl_init();
    curl_setopt_array($ch, [
        CURLOPT_URL => $url,
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_HTTPHEADER => [
            'X-RapidAPI-Key: ' . $API_KEY,
            'X-RapidAPI-Host: btc-real-time-sentiment-news-analysis.p.rapidapi.com'
        ]
    ]);
    
    $response = curl_exec($ch);
    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);
    
    if ($httpCode !== 200) {
        throw new Exception("API request failed with status: $httpCode");
    }
    
    return json_decode($response, true);
}

/**
 * Get current sentiment
 */
function getCurrentSentiment() {
    return apiRequest('/current');
}

/**
 * Get breakdown by source (Pro plan)
 */
function getBreakdown() {
    return apiRequest('/breakdown');
}

/**
 * Get headlines (Pro plan)
 */
function getHeadlines($limit = 5) {
    return apiRequest('/headlines', ['limit' => $limit]);
}

// Main execution
echo str_repeat('=', 50) . "\n";
echo "BTC SENTIMENT - CURRENT\n";
echo str_repeat('=', 50) . "\n";

try {
    $data = getCurrentSentiment();
    
    if ($data['success']) {
        $s = $data['data'];
        echo "Score:      {$s['score']}/100\n";
        echo "State:      {$s['state']} {$s['emoji']}\n";
        echo "Trend:      {$s['trend']}\n";
        echo "Sources:    {$s['sources_count']}\n";
        echo "Confidence: " . round($s['confidence'] * 100) . "%\n";
        echo "Updated:    {$s['updated_at']}\n";
    } else {
        echo "Error: {$data['error']['message']}\n";
    }
} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . "\n";
}

// Laravel integration example
/*
// In your Controller:
use Illuminate\Support\Facades\Http;

public function getSentiment()
{
    $response = Http::withHeaders([
        'X-RapidAPI-Key' => config('services.btc_sentiment.key'),
        'X-RapidAPI-Host' => 'btc-real-time-sentiment-news-analysis.p.rapidapi.com'
    ])->get('https://btc-real-time-sentiment-news-analysis.p.rapidapi.com/current');
    
    return $response->json();
}
*/
