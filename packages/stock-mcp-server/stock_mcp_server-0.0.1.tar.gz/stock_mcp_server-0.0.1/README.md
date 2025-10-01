# Stock MCP Server

[![Version](https://img.shields.io/badge/version-0.0.1-blue.svg)](https://pypi.org/project/stock-mcp-server/)
[![Python](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

**为AI助手提供全面的中国A股市场数据和分析能力的MCP服务器**

Stock MCP Server 是一个基于 [Model Context Protocol (MCP)](https://modelcontextprotocol.io) 的服务器，让 Claude Desktop 等AI助手能够访问实时股票数据、技术指标、市场情绪、新闻分析等功能。通过 10 个核心工具和 10 个资源端点，提供50+技术指标计算、全方位市场分析和投资建议生成。

[English Documentation](README_EN.md) | [API文档](docs/api.md)

## ✨ 核心特性

### 📊 10个强大的MCP工具

1. **`get_market_data`** - 市场数据查询
   - 实时行情（OHLC、成交量、涨跌幅）
   - 历史K线数据
   - 市场宽度统计（涨跌家数、涨跌停）
   - 估值指标（PE、PB、市值）

2. **`calculate_indicators`** - 技术指标计算（50+指标）
   - 趋势类：MA、EMA、MACD、DMI、ADX、TRIX、Aroon、CCI、SAR、Ichimoku
   - 动量类：RSI、KDJ、Stochastic、Williams %R、ROC
   - 波动类：BOLL、ATR、Keltner、Donchian
   - 成交量：OBV、MFI、CMF、VWAP、AD Line

3. **`get_money_flow`** - 资金流向追踪
   - 北向资金（沪深港通）
   - 融资融券数据
   - 主力资金流向（超大单、大单、中单、小单）

4. **`get_sentiment_analysis`** - 市场情绪分析
   - 多维度情绪指数（0-100分）
   - 成交量、价格、波动率、资金、新闻五大维度
   - 情绪趋势分析
   - 风险等级评估

5. **`get_news`** - 财经新闻抓取与分析
   - 4大新闻源：东方财富、新浪财经、证券时报、21财经
   - 智能重要性评分
   - 中文情绪分析（SnowNLP）
   - 热点话题聚合

6. **`get_sector_data`** - 板块行情分析
   - 400+ 板块分类（行业、概念、地域、风格）
   - 板块资金流向
   - 板块轮动分析
   - 领涨领跌个股

7. **`get_macro_data`** - 宏观经济数据
   - 国内宏观指标（GDP、CPI、PPI、PMI、M0/M1/M2）
   - 国际市场（美股、商品、外汇）
   - 对A股影响分析

8. **`get_special_data`** - 特色数据
   - 龙虎榜（机构/游资席位）
   - 大宗交易
   - 限售解禁
   - 新股发行
   - 期货期权（可选）

9. **`generate_advice`** - 投资建议生成
   - 多维度综合分析（技术面、基本面、情绪面、资金面、消息面）
   - 市场观点（看多/看空/震荡）
   - 操作建议（激进/谨慎/观望）
   - 仓位建议（重仓/半仓/轻仓/空仓 + 百分比）
   - 风险评估与预警
   - 具体操作策略

10. **`get_market_overview`** - 市场全景概览
    - 指数行情汇总
    - 市场宽度统计
    - 资金流向总览
    - 情绪指数
    - 热门板块
    - 重要新闻TOP5
    - 核心市场观点

### 🎯 10个资源端点

快速访问预生成的分析报告（通过URI直接获取）：

1. **`market://summary/{date}`** - 市场摘要
2. **`market://analysis/technical/{date}`** - 技术分析报告
3. **`market://sentiment/{date}`** - 情绪分析报告
4. **`market://briefing/{date}`** - 每日简报
5. **`market://news/{date}`** - 新闻摘要
6. **`market://moneyflow/{date}`** - 资金流向报告
7. **`market://sectors/heatmap/{date}`** - 板块热力图
8. **`market://indicators/all/{date}`** - 市场指标汇总
9. **`market://risk/{date}`** - 风险评估报告
10. **`market://macro/calendar`** - 宏观经济日历

## 🚀 快速开始

### 安装

#### 方式1：使用 uvx 运行（推荐）

无需安装，直接运行：

```bash
uvx stock-mcp-server
```

#### 方式2：使用 pip 安装

```bash
pip install stock-mcp-server
stock-mcp-server
```

#### 方式3：开发模式

```bash
git clone https://github.com/yourusername/stock-mcp-server.git
cd stock-mcp-server
uv sync
uv run stock-mcp-server
```

### 配置 Claude Desktop

在 Claude Desktop 配置文件中添加：

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`  
**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "stock-mcp": {
      "command": "uvx",
      "args": ["stock-mcp-server"]
    }
  }
}
```

**开发模式配置**：

```json
{
  "mcpServers": {
    "stock-mcp": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/stock-mcp-server",
        "run",
        "stock-mcp-server"
      ]
    }
  }
}
```

配置后**重启 Claude Desktop**即可使用。

### 验证安装

在 Claude Desktop 中询问：

```
今天上证指数表现如何？
```

预期响应包含：
- ✅ 实时价格和涨跌幅
- ✅ OHLC数据
- ✅ 成交量和金额
- ✅ 市场宽度统计
- ✅ 数据时间戳

## 📖 使用示例

### 示例1：查询实时行情

**提问**：
```
上证指数现在多少点？
```

**AI响应**：
```
上证指数 (000001)
当前：3,245.67 (+0.33% ↑)
开盘：3,230.50 | 最高：3,250.00 | 最低：3,228.00
成交量：2.85亿手 | 成交额：3,450亿元

市场宽度：
- 上涨：2,800只 (56%)
- 下跌：2,100只 (42%)
- 涨停：45只 | 跌停：12只

交易状态：已收盘（15:00）
数据时间：2025-10-01 15:00:00
```

### 示例2：技术指标分析

**提问**：
```
给我看一下上证指数的技术指标
```

**AI响应**：
```
上证指数技术指标分析

趋势指标：
- MA5: 3,240.50 | MA10: 3,235.00 | MA20: 3,230.00 | MA60: 3,220.00
  信号：买入 (短期均线上穿中期均线，呈多头排列)

- MACD: DIF=5.23 | DEA=3.45 | MACD=1.78
  信号：买入 (金叉，DIF上穿DEA)

动量指标：
- RSI(6): 65.5 | RSI(12): 62.3 | RSI(24): 58.7
  信号：中性 (处于正常区间，无超买超卖)

- KDJ: K=75.3 | D=68.2 | J=89.5
  信号：中性 (J值偏高，注意回调风险)

波动指标：
- 布林带: 上轨=3,260 | 中轨=3,230 | 下轨=3,200
  信号：中性 (价格接近中轨)

综合信号：买入 (7/10指标看多)
```

### 示例3：市场情绪分析

**提问**：
```
现在市场情绪怎么样？
```

**AI响应**：
```
市场情绪分析 - 2025-10-01

整体情绪：乐观 (62.5/100)

分维度得分：
- 成交量情绪：70.0/100 (成交活跃，量能充足)
- 价格情绪：68.0/100 (涨多跌少，市场偏强)
- 波动率情绪：55.0/100 (波动正常)
- 资金情绪：58.0/100 (资金观望，流入一般)
- 新闻情绪：65.0/100 (消息面偏正面)

情绪趋势：改善中 (+4.0 较昨日)

解读：
市场情绪偏乐观，成交活跃，资金流入积极。
技术面呈多头排列，短期可适当参与。
但需注意情绪是否过热，建议控制仓位。

风险等级：中等
```

### 示例4：获取财经新闻

**提问**：
```
今天有什么重要的股市新闻？
```

**AI响应**：
```
今日重要财经新闻 - 2025-10-01

1. [9.5/10] 央行宣布降准0.5个百分点 释放流动性约1.2万亿
   来源：东方财富 | 发布：16:30
   情绪：正面 (0.85)
   影响：全市场 | 时效：中期
   相关：银行、房地产

2. [8.5/10] 北向资金大幅净流入160亿 创近期新高
   来源：新浪财经 | 发布：15:45
   情绪：正面 (0.78)
   影响：全市场 | 时效：短期

3. [7.0/10] 多家券商上调A股年底目标位
   来源：证券时报 | 发布：14:20
   情绪：正面 (0.72)
   影响：全市场 | 时效：中期

整体新闻情绪：正面 (75%正面，20%中性，5%负面)

热点话题：
- 货币政策 (5篇)
- 北向资金 (3篇)
- 年底行情 (4篇)
```

### 示例5：投资建议

**提问**：
```
给我一个投资建议
```

**AI响应**：
```
投资建议 - 上证指数
生成时间：2025-10-01 16:00:00 | 有效至：2025-10-02 09:30:00

═══════════════════════════════════════════════

市场观点：看多
操作策略：谨慎
建议仓位：半仓 (40-70%)

═══════════════════════════════════════════════

多维度分析

技术分析：
短期均线多头排列，MACD金叉，RSI处于正常区间。
技术面偏多，但需注意短期涨幅较大，可能面临回调。

基本面分析：
涨跌家数比2:1，市场宽度良好。
成交量放大，市场参与度较高。
估值水平合理，PE约15倍。

情绪分析：
市场情绪指数62.5，处于偏乐观区间。
需注意情绪是否过热，警惕追高风险。

资金流向：
北向资金净流入16亿，外资态度积极。
主力资金小幅流出12亿，观望情绪浓厚。
融资余额上升，杠杆资金活跃。

消息面：
央行降准利好，释放流动性1.2万亿。
短期提振市场信心，中期有利于估值修复。

═══════════════════════════════════════════════

风险评估：中等风险

关键风险因素：
1. 市场情绪偏高，需警惕回调风险
2. 主力资金流出，缺乏持续性支撑
3. 外部环境仍有不确定性

风险提示：
市场短期波动可能加大，建议控制仓位，设置止损。

═══════════════════════════════════════════════

操作策略

关注要点：
- 关注北向资金动向，持续流入则多头延续
- 留意主力资金是否回流，资金面是关键
- 关注量能是否持续放大，缩量上涨不可持续

具体建议：
建议半仓操作（40-70%），可逢低适当加仓。
重点关注政策受益板块：银行、地产、基建。
短线关注强势板块，波段操作控制风险。
严格止损，破3200点减仓观望。

信心指数：72.5/100

═══════════════════════════════════════════════

免责声明：
本建议仅供参考，不构成投资建议。
投资有风险，入市需谨慎。
```

### 示例6：板块表现

**提问**：
```
哪些板块今天涨得最好？
```

**AI响应**：
```
今日板块涨幅榜 - 2025-10-01

涨幅前三：
1. 银行 (+2.35%) | 个股：42只 | 主力净流入：12亿
   领涨：工商银行 (+2.8%), 建设银行 (+2.5%)

2. 房地产 (+2.10%) | 个股：138只 | 主力净流入：8.5亿
   领涨：万科A (+3.2%), 保利发展 (+2.9%)

3. 保险 (+1.85%) | 个股：28只 | 主力净流入：4.2亿
   领涨：中国平安 (+2.1%), 中国人寿 (+1.9%)

跌幅前三：
1. 医疗器械 (-1.80%) | 主力净流出：-6.5亿
2. 半导体 (-1.25%) | 主力净流出：-8.2亿
3. 新能源 (-0.95%) | 主力净流出：-11亿

板块轮动：
从科技股向金融股轮动，政策利好推动低估值板块反弹。
```

### 示例7：市场全景

**提问**：
```
给我看一下今天的市场全景
```

**AI响应**：
```
市场全景 - 2025-10-01

📊 指数行情
上证指数: 3,245.67 (+0.33%)
深证成指: 10,850.23 (+0.45%)
创业板指: 2,234.56 (+0.28%)

📈 市场宽度
上涨：2,800只 (56%) | 下跌：2,100只 (42%)
涨停：45只 | 跌停：12只
创60日新高：250只 | 创60日新低：120只

💰 资金流向
北向资金：+160亿（净流入）
主力资金：-120亿（净流出）
融资余额：18,500亿（+300亿）

😊 市场情绪
情绪指数：62.5/100（乐观，+4.0）
趋势：改善中
风险等级：中等

🔥 热门板块
涨幅榜：银行 (+2.35%), 房地产 (+2.10%)
跌幅榜：医疗器械 (-1.80%), 半导体 (-1.25%)

📰 重要新闻
1. [9.5] 央行宣布降准0.5个百分点（正面）
2. [8.5] 北向资金大幅净流入160亿（正面）
3. [7.0] 多家券商上调A股年底目标位（正面）

💡 核心观点
市场情绪偏乐观，政策利好提振信心。
建议半仓操作，关注银行、地产板块。
控制风险，逢低参与。
```

## 🛠️ 高级用法

### 自定义技术指标参数

```
计算上证指数的20日RSI和MACD（快线12，慢线26）
```

### 过滤重要新闻

```
给我看重要性8分以上的政策类新闻
```

### 详细投资分析

```
给我一份详细的投资分析报告，包括回测结果
```

### 特定板块查询

```
显示医疗器械板块的资金流向和龙头股
```

### 宏观数据查询

```
显示最新的GDP、CPI和PMI数据
```

## 📊 性能指标

| 工具 | 目标响应时间 | 典型响应时间 |
|------|-------------|------------|
| get_market_data | <2s | ~500ms |
| calculate_indicators | <5s | ~2s |
| get_money_flow | <2s | ~500ms |
| get_sentiment_analysis | <3s | ~1.5s |
| get_news | <10s | ~5s |
| get_sector_data | <3s | ~1s |
| get_macro_data | <3s | ~1s |
| get_special_data | <3s | ~1s |
| generate_advice | <5s | ~3s |
| get_market_overview | <3s | ~2s |

### 缓存策略

- **实时数据**：交易时段5分钟缓存，收盘后24小时缓存
- **历史数据**：24小时缓存
- **新闻数据**：30分钟缓存
- **技术指标**：30分钟缓存
- **情绪分析**：1小时缓存

### 并发支持

- 支持 **10+ 并发请求**
- 智能请求队列管理
- 多数据源自动切换（东方财富 → 腾讯财经 → 新浪财经）

## 🔧 配置选项

### 环境变量

```bash
# 日志级别
STOCK_MCP_LOG_LEVEL=INFO  # DEBUG | INFO | WARNING | ERROR

# 缓存路径
STOCK_MCP_CACHE_DIR=~/.stock-mcp-server/

# 数据刷新间隔（秒）
STOCK_MCP_REALTIME_REFRESH=300  # 5分钟
STOCK_MCP_NEWS_REFRESH=1800     # 30分钟
```

### 配置文件

创建 `config.yaml`：

```yaml
logging:
  level: INFO
  dir: ~/.stock-mcp-server/logs

cache:
  db_path: ~/.stock-mcp-server/cache.db
  ttl:
    realtime: 300      # 5分钟
    historical: 86400  # 24小时
    news: 1800         # 30分钟
    indicators: 1800   # 30分钟

data_sources:
  news:
    - eastmoney
    - sina
    - stcn
    - 21finance
  
sentiment:
  method: snownlp  # snownlp | llm
  weights:
    volume: 0.25
    price: 0.25
    volatility: 0.15
    capital: 0.20
    news: 0.15
```

## 🐛 故障排查

### 服务器无法连接

1. **检查 Claude Desktop 配置**
   - 验证 JSON 语法正确
   - 检查文件路径正确
   - 修改配置后重启 Claude Desktop

2. **验证服务器安装**
   ```bash
   uvx stock-mcp-server --version
   ```

3. **查看日志**
   - macOS: `~/Library/Logs/Claude/mcp-server-stock-mcp.log`
   - Windows: `%APPDATA%\Claude\Logs\mcp-server-stock-mcp.log`
   - 本地: `~/.stock-mcp-server/logs/`

### 响应速度慢

1. **清理缓存**（如果响应>10秒）
   ```bash
   rm ~/.stock-mcp-server/cache.db
   ```

2. **检查网络连接**（数据获取需要互联网）

3. **减少查询范围**
   - 一次请求较少的指标
   - 限制新闻结果数量
   - 使用简单分析深度

### 数据不是最新的

1. **检查交易时间**：数据仅在交易时段更新（09:30-15:00 CST）
2. **缓存TTL**：实时数据缓存5分钟，不是绝对实时
3. **强制刷新**：查询不同时间段后再重新查询

### 代理问题

如遇到连接问题，服务器会自动绕过代理直连国内数据源。如需手动配置：

```bash
# 禁用代理
unset HTTP_PROXY HTTPS_PROXY http_proxy https_proxy
```

## 📚 术语表

| 中文术语 | 英文 | 说明 |
|---------|------|------|
| 上证指数 | Shanghai Composite Index | 代码：000001 |
| 深证成指 | Shenzhen Component Index | 代码：399001 |
| 创业板指 | ChiNext Index | 代码：399006 |
| 北向资金 | Northbound Capital | 通过沪深港通流入A股的资金 |
| 融资融券 | Margin Trading | 融资买入、融券卖出 |
| 主力资金 | Main Capital | 大单和超大单资金流向 |
| 涨跌停 | Limit Up/Down | A股单日涨跌幅限制通常为±10% |
| 龙虎榜 | Dragon-Tiger List | 异动股票的席位交易明细 |

### 技术指标缩写

- **MA**: Moving Average（移动平均线）
- **EMA**: Exponential Moving Average（指数移动平均线）
- **MACD**: Moving Average Convergence Divergence（指数平滑异同移动平均线）
- **RSI**: Relative Strength Index（相对强弱指标）
- **KDJ**: Stochastic Oscillator（随机指标）
- **BOLL**: Bollinger Bands（布林带）
- **ATR**: Average True Range（真实波动幅度均值）
- **OBV**: On-Balance Volume（能量潮）
- **MFI**: Money Flow Index（资金流量指标）

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 开启 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

## ⚠️ 免责声明

**重要提示**：

1. 本工具提供的所有数据、分析和建议**仅供参考**，不构成任何投资建议
2. 投资有风险，入市需谨慎。使用本工具进行投资决策的风险由用户自行承担
3. 数据来源于第三方（AKShare等），准确性和及时性无法保证
4. 技术指标和情绪分析基于历史数据，不代表未来表现
5. 作者不对使用本工具造成的任何损失负责

请务必在充分了解风险的前提下，谨慎做出投资决策。

## 🔗 相关链接

- [MCP 协议官网](https://modelcontextprotocol.io)
- [Claude Desktop](https://claude.ai/desktop)
- [AKShare 文档](https://akshare.akfamily.xyz/)
- [API 文档](docs/api.md)

## 📞 支持

- 问题反馈：[GitHub Issues](https://github.com/yourusername/stock-mcp-server/issues)
- 讨论：[GitHub Discussions](https://github.com/yourusername/stock-mcp-server/discussions)

---

**祝您投资顺利！** 📈✨
