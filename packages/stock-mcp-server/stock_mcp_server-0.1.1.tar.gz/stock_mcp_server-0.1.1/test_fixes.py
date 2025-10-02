#!/usr/bin/env python3
"""Test script for the three fixed functions"""

import sys
sys.path.insert(0, 'src')

print("=" * 70)
print("Testing Fixed Functions")
print("=" * 70)
print()

# Test 1: calculate_indicators
print("Test 1: calculate_indicators")
print("-" * 70)
try:
    from stock_mcp_server.tools.indicators import calculate_indicators
    result = calculate_indicators(indicators=["MA", "RSI", "MACD"])
    if result.get("success"):
        print(f"✅ SUCCESS: Got {len(result.get('indicators', []))} indicators")
        for ind in result.get('indicators', [])[:2]:
            print(f"   - {ind['name']}: {ind['signal']}")
    else:
        print(f"✗ FAILED: {result.get('error', {}).get('message')}")
except Exception as e:
    print(f"✗ EXCEPTION: {e}")
print()

# Test 2: get_sentiment_analysis
print("Test 2: get_sentiment_analysis")
print("-" * 70)
try:
    from stock_mcp_server.tools.sentiment import get_sentiment_analysis
    result = get_sentiment_analysis()
    if result.get("success"):
        sentiment = result.get("sentiment", {})
        print(f"✅ SUCCESS: Sentiment Index: {sentiment.get('sentiment_index')}")
        print(f"   - Level: {sentiment.get('sentiment_level')}")
        print(f"   - Risk: {sentiment.get('risk_level')}")
    else:
        print(f"✗ FAILED: {result.get('error', {}).get('message')}")
except Exception as e:
    print(f"✗ EXCEPTION: {e}")
print()

# Test 3: get_news
print("Test 3: get_news")
print("-" * 70)
try:
    from stock_mcp_server.tools.news import get_news
    result = get_news(limit=5)
    if result.get("success"):
        news_list = result.get("news", [])
        print(f"✅ SUCCESS: Got {len(news_list)} news articles")
        print(f"   - Data source: {result.get('metadata', {}).get('data_source')}")
        print(f"   - Sources tried: {result.get('metadata', {}).get('sources_tried', [])}")
        if news_list:
            print(f"   - First article: {news_list[0].get('title', 'N/A')[:50]}...")
    else:
        print(f"✗ FAILED: {result.get('error', {}).get('message')}")
        print(f"   - Details: {result.get('error', {}).get('details')}")
except Exception as e:
    print(f"✗ EXCEPTION: {e}")
print()

print("=" * 70)
print("Testing Complete!")
print("=" * 70)


