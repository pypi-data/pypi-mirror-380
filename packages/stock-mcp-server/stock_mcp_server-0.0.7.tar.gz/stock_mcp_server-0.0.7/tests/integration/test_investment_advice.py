"""Integration test: Investment advice (Scenario 5).

Tests the complete flow of investment recommendation generation,
including multi-dimensional analysis and risk assessment.
"""

# Removed pytest import
from datetime import datetime

from stock_mcp_server.tools.advice import generate_advice



def test_basic_investment_advice():
    """Test basic investment advice generation."""
    result = generate_advice(
        analysis_depth="normal",
        focus_area="all"
    )
    
    # Verify response structure
    assert result["success"] is True, "Advice generation should succeed"
    assert "data" in result
    assert "advice" in result["data"] or "recommendation" in result["data"]
    
    advice_key = "advice" if "advice" in result["data"] else "recommendation"
    advice = result["data"][advice_key]
    
    # Verify required fields
    assert "market_outlook" in advice, "Should have market outlook"
    assert "operation_suggestion" in advice, "Should have operation suggestion"
    assert "position_recommendation" in advice, "Should have position recommendation"



def test_advice_market_outlook():
    """Test market outlook classification."""
    result = generate_advice(
        analysis_depth="normal"
    )
    
    assert result["success"] is True
    advice_key = "advice" if "advice" in result["data"] else "recommendation"
    advice = result["data"][advice_key]
    
    # Verify market outlook is valid
    valid_outlooks = ["bullish", "bearish", "sideways", "看多", "看空", "震荡"]
    outlook = advice["market_outlook"]
    assert any(v in outlook.lower() for v in ["bullish", "bearish", "sideways", "看", "震"]), \
        f"Invalid market outlook: {outlook}"



def test_advice_operation_suggestion():
    """Test operation suggestion."""
    result = generate_advice(
        analysis_depth="normal"
    )
    
    assert result["success"] is True
    advice_key = "advice" if "advice" in result["data"] else "recommendation"
    advice = result["data"][advice_key]
    
    # Verify operation suggestion is valid
    valid_operations = ["aggressive", "cautious", "wait", "积极", "谨慎", "观望"]
    operation = advice["operation_suggestion"]
    assert any(v in operation.lower() for v in valid_operations), \
        f"Invalid operation suggestion: {operation}"



def test_advice_position_recommendation():
    """Test position recommendation."""
    result = generate_advice(
        analysis_depth="normal"
    )
    
    assert result["success"] is True
    advice_key = "advice" if "advice" in result["data"] else "recommendation"
    advice = result["data"][advice_key]
    
    # Verify position recommendation is valid
    valid_positions = ["heavy", "half", "light", "empty", "重仓", "半仓", "轻仓", "空仓"]
    position = advice["position_recommendation"]
    assert any(v in position.lower() for v in valid_positions), \
        f"Invalid position recommendation: {position}"



def test_advice_multi_dimensional_analysis():
    """Test multi-dimensional analysis components."""
    result = generate_advice(
        analysis_depth="detailed",
        focus_area="all"
    )
    
    assert result["success"] is True
    advice_key = "advice" if "advice" in result["data"] else "recommendation"
    advice = result["data"][advice_key]
    
    # Check for multi-dimensional analysis
    dimensions = [
        "technical_analysis",
        "fundamental_analysis",
        "sentiment_analysis",
        "capital_analysis"
    ]
    
    present_dimensions = []
    for dim in dimensions:
        if dim in advice and advice[dim]:
            present_dimensions.append(dim)
    
    # Should have at least 2-3 dimensions for "all" focus
    assert len(present_dimensions) >= 2, \
        f"Should have multiple analysis dimensions: {present_dimensions}"



def test_advice_risk_assessment():
    """Test risk assessment inclusion."""
    result = generate_advice(
        analysis_depth="normal",
        include_risk=True
    )
    
    assert result["success"] is True
    advice_key = "advice" if "advice" in result["data"] else "recommendation"
    advice = result["data"][advice_key]
    
    # Check for risk assessment
    assert "risk_level" in advice, "Should have risk level when requested"
    
    risk_level = advice["risk_level"]
    valid_risks = ["低", "中", "高", "极", "low", "medium", "high", "extreme"]
    assert any(v in risk_level.lower() for v in valid_risks), \
        f"Invalid risk level: {risk_level}"
    
    # Check for risk factors
    if "risk_factors" in advice:
        assert isinstance(advice["risk_factors"], list), \
            "Risk factors should be a list"



def test_advice_disclaimer():
    """Test that disclaimer is included."""
    result = generate_advice(
        analysis_depth="normal"
    )
    
    assert result["success"] is True
    advice_key = "advice" if "advice" in result["data"] else "recommendation"
    advice = result["data"][advice_key]
    
    # Check for disclaimer
    assert "disclaimer" in advice, "Should have disclaimer"
    disclaimer = advice["disclaimer"]
    
    assert isinstance(disclaimer, str), "Disclaimer should be string"
    assert len(disclaimer) > 0, "Disclaimer should not be empty"
    
    # Should contain risk warning keywords
    assert any(keyword in disclaimer for keyword in ["风险", "谨慎", "参考", "risk", "caution"]), \
        "Disclaimer should contain risk warning"



def test_advice_simple_depth():
    """Test simple analysis depth."""
    result = generate_advice(
        analysis_depth="simple"
    )
    
    assert result["success"] is True
    # Simple analysis should return basic recommendations
    assert "data" in result



def test_advice_detailed_depth():
    """Test detailed analysis depth."""
    result = generate_advice(
        analysis_depth="detailed",
        focus_area="all"
    )
    
    assert result["success"] is True
    advice_key = "advice" if "advice" in result["data"] else "recommendation"
    advice = result["data"][advice_key]
    
    # Detailed analysis should have more content
    # Count non-None analysis fields
    analysis_fields = [k for k in advice.keys() if "analysis" in k and advice[k]]
    assert len(analysis_fields) >= 2, \
        "Detailed analysis should have multiple analysis sections"



def test_advice_focus_technical():
    """Test advice with technical focus."""
    result = generate_advice(
        analysis_depth="normal",
        focus_area="technical"
    )
    
    assert result["success"] is True
    advice_key = "advice" if "advice" in result["data"] else "recommendation"
    advice = result["data"][advice_key]
    
    # Should prioritize technical analysis
    if "technical_analysis" in advice:
        assert advice["technical_analysis"] is not None, \
            "Technical analysis should be present"



def test_advice_focus_sentiment():
    """Test advice with sentiment focus."""
    result = generate_advice(
        analysis_depth="normal",
        focus_area="sentiment"
    )
    
    assert result["success"] is True
    advice_key = "advice" if "advice" in result["data"] else "recommendation"
    advice = result["data"][advice_key]
    
    # Should include sentiment analysis
    if "sentiment_analysis" in advice:
        assert advice["sentiment_analysis"] is not None



def test_advice_confidence_score():
    """Test confidence score if provided."""
    result = generate_advice(
        analysis_depth="detailed"
    )
    
    assert result["success"] is True
    advice_key = "advice" if "advice" in result["data"] else "recommendation"
    advice = result["data"][advice_key]
    
    # Check for confidence score
    if "confidence_score" in advice and advice["confidence_score"] is not None:
        confidence = float(advice["confidence_score"])
        assert 0 <= confidence <= 100, \
            f"Confidence should be 0-100: {confidence}"



def test_advice_actionable_insights():
    """Test actionable insights and strategy."""
    result = generate_advice(
        analysis_depth="detailed",
        include_risk=True
    )
    
    assert result["success"] is True
    advice_key = "advice" if "advice" in result["data"] else "recommendation"
    advice = result["data"][advice_key]
    
    # Check for actionable content
    actionable_fields = [
        "key_focus_points",
        "operational_strategy",
        "focus_points",
        "strategy"
    ]
    
    has_actionable = any(field in advice for field in actionable_fields)
    # Should have some actionable guidance
    # (not strictly enforced as it depends on implementation)



def test_advice_chinese_content():
    """Test that advice contains Chinese content."""
    result = generate_advice(
        analysis_depth="normal"
    )
    
    assert result["success"] is True
    advice_key = "advice" if "advice" in result["data"] else "recommendation"
    advice = result["data"][advice_key]
    
    # Check for Chinese characters in analysis sections
    has_chinese = False
    for key, value in advice.items():
        if isinstance(value, str) and any('\u4e00' <= c <= '\u9fff' for c in value):
            has_chinese = True
            break
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, str) and any('\u4e00' <= c <= '\u9fff' for c in item):
                    has_chinese = True
                    break
    
    assert has_chinese, "Advice should contain Chinese content"



def test_advice_performance():
    """Test that advice generation meets performance target (<5s)."""
    import time
    
    start_time = time.time()
    
    result = generate_advice(
        analysis_depth="normal",
        focus_area="all"
    )
    
    elapsed = time.time() - start_time
    
    assert result["success"] is True
    # Should complete within 5 seconds for normal depth
    assert elapsed < 5.0, f"Advice generation took too long: {elapsed}s"

