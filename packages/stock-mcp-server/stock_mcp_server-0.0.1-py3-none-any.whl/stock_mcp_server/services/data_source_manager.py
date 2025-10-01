"""数据源管理器 - 支持多数据源自动切换"""

from datetime import datetime
from decimal import Decimal
from typing import Any, Callable

import akshare as ak
import pandas as pd
from loguru import logger

from stock_mcp_server.models.market import MarketIndex, MarketBreadth, CapitalFlow


class DataSourceManager:
    """
    数据源管理器 - 自动在多个数据源之间切换
    
    优先级: 东方财富(快) > 腾讯(稳定) > 新浪(备用)
    """
    
    def __init__(self):
        self.sources = {
            'eastmoney': {'priority': 1, 'failures': 0, 'name': '东方财富'},
            'tencent': {'priority': 2, 'failures': 0, 'name': '腾讯财经'},
            'sina': {'priority': 3, 'failures': 0, 'name': '新浪财经'},
        }
        self.max_failures = 3  # 连续失败3次后降低优先级
        
    def get_index_spot(self, index_code: str = "000001") -> MarketIndex | None:
        """
        获取指数实时数据 - 多数据源自动切换
        
        Args:
            index_code: 指数代码 (000001=上证, 399001=深证, 399006=创业板)
            
        Returns:
            MarketIndex对象或None
        """
        # 方法列表（按优先级）
        methods = [
            ('eastmoney', self._get_index_from_eastmoney),
            ('tencent', self._get_index_from_tencent),
        ]
        
        # 按当前失败次数排序
        methods.sort(key=lambda x: self.sources[x[0]]['failures'])
        
        for source_name, method in methods:
            try:
                logger.info(f"尝试从 {self.sources[source_name]['name']} 获取指数数据...")
                result = method(index_code)
                if result:
                    # 成功 - 重置失败计数
                    self.sources[source_name]['failures'] = 0
                    logger.info(f"✓ 成功从 {self.sources[source_name]['name']} 获取数据")
                    return result
            except Exception as e:
                # 失败 - 增加失败计数
                self.sources[source_name]['failures'] += 1
                logger.warning(
                    f"✗ {self.sources[source_name]['name']} 失败 "
                    f"({self.sources[source_name]['failures']}/{self.max_failures}): {str(e)[:100]}"
                )
                continue
        
        logger.error("所有数据源均失败")
        return None
    
    def _get_index_from_eastmoney(self, index_code: str) -> MarketIndex | None:
        """从东方财富获取指数数据"""
        df = ak.stock_zh_index_spot_em()
        if df is None or df.empty:
            return None
        
        row = df[df["代码"] == index_code]
        if row.empty:
            return None
        
        row = row.iloc[0]
        return self._parse_index_data_eastmoney(row, index_code)
    
    def _get_index_from_tencent(self, index_code: str) -> MarketIndex | None:
        """从腾讯财经获取指数数据"""
        # 腾讯代码映射
        symbol_map = {
            "000001": "sh000001",  # 上证指数
            "399001": "sz399001",  # 深证成指
            "399006": "sz399006",  # 创业板指
        }
        
        symbol = symbol_map.get(index_code, f"sh{index_code}")
        
        # 获取历史数据（包含最新一天）
        df = ak.stock_zh_index_daily_tx(symbol=symbol)
        if df is None or df.empty:
            return None
        
        # 取最新一天的数据
        latest = df.iloc[-1]
        
        # 计算涨跌额和涨跌幅
        current = Decimal(str(latest['close']))
        pre_close = Decimal(str(df.iloc[-2]['close'])) if len(df) > 1 else current
        change = current - pre_close
        change_pct = (change / pre_close * Decimal("100")) if pre_close > 0 else Decimal("0")
        
        return MarketIndex(
            code=index_code,
            name=self._get_index_name(index_code),
            current=current,
            open=Decimal(str(latest['open'])),
            high=Decimal(str(latest['high'])),
            low=Decimal(str(latest['low'])),
            close=current,
            pre_close=pre_close,
            change=change,
            change_pct=change_pct,
            amplitude=((Decimal(str(latest['high'])) - Decimal(str(latest['low']))) / pre_close * Decimal("100")) if pre_close > 0 else Decimal("0"),
            volume=int(latest.get('amount', 0)),
            amount=Decimal(str(latest.get('amount', 0))),
            turnover_rate=None,
            timestamp=datetime.now(),
            trading_date=str(latest['date']) if pd.notna(latest['date']) else datetime.now().strftime("%Y-%m-%d"),
            market_status="closed",  # 腾讯接口只有日线，标记为已收盘
        )
    
    def _get_index_name(self, index_code: str) -> str:
        """获取指数名称"""
        name_map = {
            "000001": "上证指数",
            "399001": "深证成指",
            "399006": "创业板指",
        }
        return name_map.get(index_code, f"指数{index_code}")
    
    def _parse_index_data_eastmoney(self, row: pd.Series, index_code: str) -> MarketIndex:
        """解析东方财富的指数数据"""
        return MarketIndex(
            code=index_code,
            name=str(row["名称"]),
            current=Decimal(str(row["最新价"])),
            open=Decimal(str(row["今开"])),
            high=Decimal(str(row["最高"])),
            low=Decimal(str(row["最低"])),
            close=Decimal(str(row["最新价"])),
            pre_close=Decimal(str(row["昨收"])),
            change=Decimal(str(row["涨跌额"])),
            change_pct=Decimal(str(row["涨跌幅"])),
            amplitude=Decimal(str(row.get("振幅", 0))),
            volume=int(row.get("成交量", 0)),
            amount=Decimal(str(row.get("成交额", 0))),
            turnover_rate=Decimal(str(row.get("换手率", 0))) if "换手率" in row else None,
            timestamp=datetime.now(),
            trading_date=datetime.now().strftime("%Y-%m-%d"),
            market_status="open",
        )
    
    def get_market_breadth(self, date: str | None = None) -> MarketBreadth | None:
        """
        获取市场宽度数据 - 多数据源自动切换
        
        Args:
            date: 交易日期
            
        Returns:
            MarketBreadth对象或None
        """
        methods = [
            ('eastmoney', self._get_breadth_from_eastmoney),
            ('sina', self._get_breadth_from_sina),
        ]
        
        # 按失败次数排序
        methods.sort(key=lambda x: self.sources.get(x[0], {}).get('failures', 0))
        
        for source_name, method in methods:
            try:
                logger.info(f"尝试从 {self.sources.get(source_name, {}).get('name', source_name)} 获取市场宽度数据...")
                result = method(date)
                if result:
                    self.sources[source_name]['failures'] = 0
                    logger.info(f"✓ 成功从 {self.sources.get(source_name, {}).get('name', source_name)} 获取数据")
                    return result
            except Exception as e:
                self.sources[source_name]['failures'] += 1
                logger.warning(
                    f"✗ {self.sources.get(source_name, {}).get('name', source_name)} 失败: {str(e)[:100]}"
                )
                continue
        
        logger.error("所有数据源均失败")
        return None
    
    def _get_breadth_from_eastmoney(self, date: str | None) -> MarketBreadth | None:
        """从东方财富获取市场宽度"""
        df = ak.stock_zh_a_spot_em()
        if df is None or df.empty:
            return None
        
        total = len(df)
        advancing = len(df[df["涨跌幅"] > 0])
        declining = len(df[df["涨跌幅"] < 0])
        unchanged = len(df[df["涨跌幅"] == 0])
        limit_up = len(df[df["涨跌幅"] >= 9.9])
        limit_down = len(df[df["涨跌幅"] <= -9.9])
        
        return MarketBreadth(
            total_stocks=total,
            advancing=advancing,
            declining=declining,
            unchanged=unchanged,
            limit_up=limit_up,
            limit_down=limit_down,
            gain_over_5pct=len(df[df["涨跌幅"] > 5]),
            loss_over_5pct=len(df[df["涨跌幅"] < -5]),
            gain_over_7pct=len(df[df["涨跌幅"] > 7]),
            loss_over_7pct=len(df[df["涨跌幅"] < -7]),
            advance_decline_ratio=Decimal(str(advancing / max(declining, 1))),
            advance_pct=Decimal(str(advancing / total * 100)),
            decline_pct=Decimal(str(declining / total * 100)),
            date=date or datetime.now().strftime("%Y-%m-%d"),
            timestamp=datetime.now(),
        )
    
    def _get_breadth_from_sina(self, date: str | None) -> MarketBreadth | None:
        """从新浪财经获取市场宽度"""
        # 使用新浪的申万行业分类接口，会返回所有A股的实时数据
        df = ak.stock_classify_sina(symbol='申万行业')
        if df is None or df.empty:
            return None
        
        # 新浪返回的涨跌幅字段是 changepercent
        total = len(df)
        advancing = len(df[df["changepercent"] > 0])
        declining = len(df[df["changepercent"] < 0])
        unchanged = len(df[df["changepercent"] == 0])
        
        # 涨停/跌停 (A股一般是±10%)
        limit_up = len(df[df["changepercent"] >= 9.9])
        limit_down = len(df[df["changepercent"] <= -9.9])
        
        return MarketBreadth(
            total_stocks=total,
            advancing=advancing,
            declining=declining,
            unchanged=unchanged,
            limit_up=limit_up,
            limit_down=limit_down,
            gain_over_5pct=len(df[df["changepercent"] > 5]),
            loss_over_5pct=len(df[df["changepercent"] < -5]),
            gain_over_7pct=len(df[df["changepercent"] > 7]),
            loss_over_7pct=len(df[df["changepercent"] < -7]),
            advance_decline_ratio=Decimal(str(advancing / max(declining, 1))),
            advance_pct=Decimal(str(advancing / total * 100)),
            decline_pct=Decimal(str(declining / total * 100)),
            date=date or datetime.now().strftime("%Y-%m-%d"),
            timestamp=datetime.now(),
        )
    
    def get_capital_flow(self, date: str | None = None) -> CapitalFlow | None:
        """
        获取资金流向数据
        
        Args:
            date: 交易日期
            
        Returns:
            CapitalFlow对象或None
        """
        methods = [
            ('eastmoney', self._get_capital_from_eastmoney),
        ]
        
        for source_name, method in methods:
            try:
                logger.info(f"尝试从 {self.sources[source_name]['name']} 获取资金流向数据...")
                result = method(date)
                if result:
                    self.sources[source_name]['failures'] = 0
                    logger.info(f"✓ 成功从 {self.sources[source_name]['name']} 获取数据")
                    return result
            except Exception as e:
                self.sources[source_name]['failures'] += 1
                logger.warning(
                    f"✗ {self.sources[source_name]['name']} 失败: {str(e)[:100]}"
                )
                continue
        
        return None
    
    def _get_capital_from_eastmoney(self, date: str | None) -> CapitalFlow | None:
        """从东方财富获取资金流向"""
        df = ak.stock_hsgt_fund_flow_summary_em()
        if df is None or df.empty:
            return None
        
        latest = df.iloc[-1]
        
        return CapitalFlow(
            north_net=Decimal(str(latest.get("北向资金", 0))),
            north_inflow=Decimal(str(abs(latest.get("北向资金", 0)))) if latest.get("北向资金", 0) > 0 else Decimal("0"),
            north_outflow=Decimal(str(abs(latest.get("北向资金", 0)))) if latest.get("北向资金", 0) < 0 else Decimal("0"),
            date=date or datetime.now().strftime("%Y-%m-%d"),
            timestamp=datetime.now(),
        )


# 单例
_data_source_manager = None


def get_data_source_manager() -> DataSourceManager:
    """获取数据源管理器单例"""
    global _data_source_manager
    if _data_source_manager is None:
        _data_source_manager = DataSourceManager()
    return _data_source_manager

