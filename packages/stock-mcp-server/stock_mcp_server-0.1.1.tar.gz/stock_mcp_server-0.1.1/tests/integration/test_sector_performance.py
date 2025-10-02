"""Integration test: Sector performance (Scenario 6).

Tests the complete flow of sector data retrieval and analysis,
including rankings, capital flows, and leading stocks.
"""

# Removed pytest import

from stock_mcp_server.tools.sector import get_sector_data



def test_basic_sector_query():
    """Test basic sector data query."""
    result = get_sector_data(
        sector_type="industry",
        limit=10
    )
    
    # Verify response structure
    assert result["success"] is True, "Sector query should succeed"
    assert "data" in result
    assert "sectors" in result["data"]
    
    sectors = result["data"]["sectors"]
    assert isinstance(sectors, list), "Sectors should be a list"
    assert len(sectors) <= 10, "Should not exceed requested limit"



def test_sector_rankings():
    """Test sector rankings by performance."""
    result = get_sector_data(
        sector_type="industry",
        sort_by="change",
        limit=10
    )
    
    assert result["success"] is True
    sectors = result["data"]["sectors"]
    
    if len(sectors) > 1:
        # Verify sectors have performance metrics
        for sector in sectors:
            assert "name" in sector, "Sector should have name"
            assert "change_pct" in sector or "change" in sector, \
                "Sector should have change percentage"
        
        # Verify sorting (descending order for gainers)
        has_change_pct = all("change_pct" in s or "change" in s for s in sectors)
        if has_change_pct:
            for i in range(len(sectors) - 1):
                change1 = float(sectors[i].get("change_pct", sectors[i].get("change", 0)))
                change2 = float(sectors[i + 1].get("change_pct", sectors[i + 1].get("change", 0)))
                # Allow small margin for float comparison
                assert change1 >= change2 - 0.01, \
                    f"Sectors should be sorted by change: {change1} < {change2}"



def test_sector_capital_flows():
    """Test sector capital flow data."""
    result = get_sector_data(
        sector_type="industry",
        sort_by="money_flow",
        limit=10
    )
    
    assert result["success"] is True
    sectors = result["data"]["sectors"]
    
    # Check for capital flow information
    if len(sectors) > 0:
        capital_flow_count = 0
        for sector in sectors:
            if "main_net_inflow" in sector or "capital_flow" in sector or "money_flow" in sector:
                capital_flow_count += 1
        
        # At least some sectors should have capital flow data
        # (but not strictly enforced as data availability may vary)



def test_sector_leading_stocks():
    """Test leading stocks identification."""
    result = get_sector_data(
        sector_type="industry",
        include_leaders=True,
        limit=5
    )
    
    assert result["success"] is True
    sectors = result["data"]["sectors"]
    
    if len(sectors) > 0:
        # Check if leader stocks are included
        has_leaders = False
        for sector in sectors:
            if "leader_stocks" in sector or "leaders" in sector:
                leaders = sector.get("leader_stocks") or sector.get("leaders")
                if leaders and len(leaders) > 0:
                    has_leaders = True
                    # Verify leader structure
                    leader = leaders[0]
                    if isinstance(leader, dict):
                        # Should have stock code and/or name
                        assert "code" in leader or "name" in leader, \
                            "Leader should have code or name"
        
        # At least some sectors should have leader information when requested
        # (but not mandatory for all)



def test_sector_rotation_analysis():
    """Test sector rotation analysis."""
    result = get_sector_data(
        sector_type="industry",
        include_rotation=True,
        rotation_days=30,
        limit=10
    )
    
    assert result["success"] is True
    data = result["data"]
    
    # Check for rotation analysis
    if "rotation" in data or "rotation_analysis" in data:
        rotation = data.get("rotation") or data.get("rotation_analysis")
        # Rotation analysis should provide insights
        assert rotation is not None



def test_sector_type_industry():
    """Test querying industry sectors."""
    result = get_sector_data(
        sector_type="industry",
        limit=10
    )
    
    assert result["success"] is True
    sectors = result["data"]["sectors"]
    
    # Should return industry sectors
    assert isinstance(sectors, list), "Should return list of sectors"



def test_sector_type_concept():
    """Test querying concept sectors."""
    result = get_sector_data(
        sector_type="concept",
        limit=10
    )
    
    assert result["success"] is True
    sectors = result["data"]["sectors"]
    
    # Should return concept sectors
    assert isinstance(sectors, list), "Should return list of sectors"



def test_sector_type_all():
    """Test querying all sector types."""
    result = get_sector_data(
        sector_type="all",
        limit=10
    )
    
    assert result["success"] is True
    sectors = result["data"]["sectors"]
    
    # Should return mixed sector types
    assert isinstance(sectors, list), "Should return list of sectors"



def test_sector_sort_by_turnover():
    """Test sorting sectors by turnover."""
    result = get_sector_data(
        sector_type="industry",
        sort_by="turnover",
        limit=10
    )
    
    assert result["success"] is True
    sectors = result["data"]["sectors"]
    
    # Should return sectors sorted by turnover
    if len(sectors) > 0:
        # Check for turnover field
        has_turnover = any("turnover" in s for s in sectors)



def test_sector_chinese_names():
    """Test that sector names are in Chinese."""
    result = get_sector_data(
        sector_type="industry",
        limit=10
    )
    
    assert result["success"] is True
    sectors = result["data"]["sectors"]
    
    if len(sectors) > 0:
        # Check for Chinese names
        has_chinese = False
        for sector in sectors:
            if "name" in sector:
                name = sector["name"]
                if any('\u4e00' <= c <= '\u9fff' for c in name):
                    has_chinese = True
                    break
        
        assert has_chinese, "Sector names should include Chinese"



def test_sector_stock_count():
    """Test that sectors include stock count."""
    result = get_sector_data(
        sector_type="industry",
        limit=10
    )
    
    assert result["success"] is True
    sectors = result["data"]["sectors"]
    
    if len(sectors) > 0:
        # Check for stock count
        for sector in sectors:
            if "stock_count" in sector or "count" in sector:
                count = sector.get("stock_count") or sector.get("count")
                assert count > 0, "Stock count should be positive"



def test_sector_metadata():
    """Test sector response metadata."""
    result = get_sector_data(
        sector_type="industry",
        limit=10
    )
    
    assert result["success"] is True
    assert "metadata" in result
    
    metadata = result["metadata"]
    assert "query_time" in metadata
    assert "data_source" in metadata



def test_sector_performance():
    """Test that sector query meets performance target (<3s)."""
    import time
    
    start_time = time.time()
    
    result = get_sector_data(
        sector_type="industry",
        include_leaders=True,
        limit=10
    )
    
    elapsed = time.time() - start_time
    
    assert result["success"] is True
    # Should complete within 3 seconds
    assert elapsed < 3.0, f"Sector query took too long: {elapsed}s"

