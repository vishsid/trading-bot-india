# 🚀 Trading Bot India

**Complete Algorithmic Trading System for Indian Markets (NSE Futures, Options & Index)**

## ✨ Features

✅ **Multi-Timeframe Analysis** - Combine signals from 5m, 15m, 1h, 4h, daily timeframes
✅ **Futures Trading** - NIFTY, BANKNIFTY, SENSEX futures strategies
✅ **Options Strategies** - Iron Condor, Bull/Bear Call Spreads, Straddles
✅ **Greeks Calculation** - Real-time Delta, Gamma, Theta, Vega for options
✅ **Backtesting Engine** - Backtrader integration with realistic slippage & commissions
✅ **Live Trading** - Zerodha Kite Connect API integration
✅ **Real-time Dashboard** - Streamlit-based monitoring & analytics
✅ **Risk Management** - Position limits, drawdown controls, margin tracking
✅ **Free Cloud Hosting** - Deploy on Streamlit Cloud in 2 minutes

---

## 📊 Dashboard Features

**5 Interactive Tabs:**

### 1️⃣ **📈 Price Chart**
- Live OHLC candlesticks
- EMA 20/50 indicators
- RSI, MACD, ATR readings
- Multi-timeframe support

### 2️⃣ **📊 Positions**
- Active positions tracking
- Real-time P&L monitoring
- Greeks display
- Close/modify controls

### 3️⃣ **🎯 Greeks Calculator**
- Delta (Directional exposure)
- Gamma (Delta acceleration)
- Theta (Time decay)
- Vega (Volatility exposure)
- Rho (Interest rate sensitivity)
- Iron Condor & Bull Call setups

### 4️⃣ **📋 Trade History**
- Complete trade log
- Performance metrics
- Win rate tracking
- Strategy breakdown
- P&L distribution

### 5️⃣ **⚠️ Risk Management**
- Drawdown tracking
- Margin monitoring
- Position limits
- Daily loss controls
- Risk gauge

---

## 🚀 Quick Start (2 Minutes)

### **Deploy to Streamlit Cloud (FREE)**

1. **Sign in with GitHub:**
   - Go to: https://streamlit.io/cloud
   - Click "Sign in with GitHub"

2. **Create New App:**
   - Click "New app"
   - Repository: `vishsid/trading-bot-india`
   - Branch: `main`
   - Main file: `streamlit_app.py`

3. **Deploy:**
   - Click "Deploy"
   - Wait 2 minutes
   - Your dashboard is live! 🎉

### **Your Dashboard URL:**
```
https://trading-bot-india.streamlit.app
```

---

## 💻 Run Locally

```bash
# Clone repository
git clone https://github.com/vishsid/trading-bot-india.git
cd trading-bot-india

# Install dependencies
pip install -r requirements.txt

# Run dashboard
streamlit run streamlit_app.py

# Opens at: http://localhost:8501
```

---

## 📦 Installation

### **From Source**

```bash
# Clone repo
git clone https://github.com/vishsid/trading-bot-india.git
cd trading-bot-india

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy and configure
cp .env.example .env
```

### **With Docker**

```bash
docker build -t trading-bot .
docker run -p 8501:8501 trading-bot
```

---

## 🎯 Trading Strategies

### **1. Multi-Timeframe Strategy** ⭐
- Uses 1h for trend confirmation
- Uses 5m for precise entry timing
- Exits based on profit targets or stops
- **Best for:** Intraday & swing trading

### **2. Iron Condor (Options)**
- Sell OTM call & put spreads
- Max profit at expiry
- **Best for:** Range-bound markets

### **3. Bull Call Spread**
- Buy ATM call, sell OTM call
- Limited risk/reward
- **Best for:** Directional bullish bias

### **4. Calendar Spread**
- Sell near-term, buy longer-term
- Theta decay strategy
- **Best for:** Benefits from time decay

---

## 📊 Greeks Explained

| Greek | Meaning | Use Case |
|-------|---------|----------|
| **Delta** | Change per ₹1 move | Directional exposure |
| **Gamma** | Delta acceleration | Volatility risk |
| **Theta** | Daily decay | Time-value strategies |
| **Vega** | IV sensitivity | Volatility trading |
| **Rho** | Interest rate sensitivity | Long-term options |

---

## 🔧 Configuration

### **`.env` File**

```env
# Zerodha Kite API
KITE_API_KEY=your_api_key
KITE_API_SECRET=your_api_secret
KITE_REQUEST_TOKEN=your_request_token

# Strategy Settings
INITIAL_CAPITAL=1000000
RISK_PER_TRADE=0.02  # 2%
MAX_POSITIONS=5
MAX_DRAWDOWN=0.15   # 15%

# Trading Mode
TRADING_MODE=backtest  # or live, paper
```

---

## 🌐 Free Cloud Deployment Options

### **1. Streamlit Cloud (RECOMMENDED) ⭐**
✅ 1-click deploy
✅ Auto-scaling
✅ Free tier
✅ 60-second setup

**Link:** https://streamlit.io/cloud

### **2. Render.com**
✅ Free tier
✅ 750 hours/month
✅ Docker support

**Link:** https://render.com

### **3. Railway.app**
✅ $5 monthly credits
✅ Easy deployment
✅ GitHub integration

**Link:** https://railway.app

---

## 📚 Project Structure

```
trading-bot-india/
├── README.md                    # Documentation
├── requirements.txt             # Dependencies
├── .env.example                 # Configuration template
├── streamlit_app.py             # Dashboard (Streamlit)
├── .gitignore
│
├── config/
│   ├── settings.py
│   ├── strategies.yaml
│   └── instruments.yaml
│
├── data/
│   └── data_fetcher.py
│
├── indicators/
│   ├── technical_indicators.py
│   └── options_greeks.py
│
├── strategies/
│   ├── base_strategy.py
│   ├── mtf_strategy.py
│   └── options_strategy.py
│
├── backtesting/
│   └── backtest_runner.py
│
├── execution/
│   └── kite_connector.py
│
└── monitoring/
    └── dashboard.py
```

---

## 🔗 API Integrations

### **Data Sources**
- **nsemine** - Real-time & historical NSE data ✅
- **Zerodha Kite** - Live futures/options data ✅
- **OpenChart** - Intraday OHLCV data (optional)

### **Brokers**
- **Zerodha** (fully integrated) ✅
- **Angel One** (adapter provided)
- **Upstox** (adapter provided)

### **Alerts**
- **Telegram** - Trade notifications
- **Email** - Daily reports
- **Webhook** - Custom integrations

---

## ⚠️ Risk Management

Built-in safeguards:
- ✅ Position size limits (per strategy config)
- ✅ Maximum daily loss limits (5%)
- ✅ Leverage caps (max 10x)
- ✅ Margin utilization tracking
- ✅ Volatility-adjusted position sizing
- ✅ Correlation-based portfolio limits

---

## 📖 Examples

### **Example 1: View Dashboard**
```bash
streamlit run streamlit_app.py
```
Then visit: http://localhost:8501

### **Example 2: Deploy to Streamlit Cloud**
1. Go to https://streamlit.io/cloud
2. Click "New app"
3. Select this repo
4. Set main file: `streamlit_app.py`
5. Deploy!

---

## 🤝 Contributing

Contributions welcome! Areas for enhancement:
- More strategy implementations
- Additional broker integrations
- Advanced ML models
- Mobile app
- Real-time alerts improvements

---

## 📞 Support & Community

- 📧 **Issues**: [GitHub Issues](https://github.com/vishsid/trading-bot-india/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/vishsid/trading-bot-india/discussions)
- 🐛 **Bug Reports**: [Report a Bug](https://github.com/vishsid/trading-bot-india/issues/new)

---

## 📜 License

MIT License - See LICENSE file for details

---

## ⚠️ DISCLAIMER

**This is for educational purposes only.**
- Trading involves substantial risk of loss
- Not financial advice. Do your own research.
- Backtest results don't guarantee live performance
- Always test on paper trading first
- Start with small capital when going live
- SEBI algo-trading regulations must be followed

---

**🚀 Happy Trading!**

*Last Updated: July 2024*
