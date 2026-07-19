"""Main Streamlit entry point - Trading Bot Dashboard."""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
import numpy as np
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

st.set_page_config(
    page_title="Trading Bot Dashboard",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 5px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Title & Header
st.title("📊 Trading Bot Dashboard")
st.markdown("""
**Real-time Monitoring for NSE Futures, Options & Multi-Timeframe Trading**

🚀 Powered by: Backtrader | Zerodha Kite | Black-Scholes Greeks Calculator
""")

st.divider()

# Sidebar Configuration
with st.sidebar:
    st.header("⚙️ Settings")
    
    mode = st.radio(
        "Select Trading Mode",
        ["📊 Backtest", "📈 Paper Trading", "🚀 Live Trading"],
        help="Choose the trading mode"
    )
    
    symbol = st.selectbox(
        "Select Symbol",
        ["NIFTY", "BANKNIFTY", "FINNIFTY", "SENSEX"],
        help="Choose trading instrument"
    )
    
    timeframe = st.selectbox(
        "Select Timeframe",
        ["5m", "15m", "1h", "4h", "daily"],
        help="Candlestick timeframe"
    )
    
    st.markdown("---")
    st.subheader("🔄 Auto-Refresh")
    auto_refresh = st.checkbox("Enable Auto-Refresh", value=True)
    if auto_refresh:
        refresh_interval = st.slider("Refresh Interval (seconds)", 5, 60, 10)
    
    st.markdown("---")
    st.info(
        "📌 **Status:** Trading Bot v1.0\n"
        f"🕐 **Last Updated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"📍 **Mode:** {mode.split()[0]}"
    )

st.markdown("---")

# Main Metrics
st.subheader("💰 Portfolio Metrics")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Account Balance",
        value="₹10,00,000",
        delta="+5.2%",
        delta_color="off"
    )

with col2:
    st.metric(
        label="Active Positions",
        value="2",
        delta="+1 Today",
        delta_color="off"
    )

with col3:
    st.metric(
        label="Today's P&L",
        value="₹8,500",
        delta="+0.85%",
        delta_color="off"
    )

with col4:
    st.metric(
        label="Win Rate",
        value="62.5%",
        delta="+2.5%",
        delta_color="off"
    )

st.divider()

# Tab Interface
tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["📈 Price Chart", "📊 Positions", "🎯 Greeks", "📋 Trade History", "⚠️ Risk Management"]
)

with tab1:
    st.subheader(f"📊 {symbol} - {timeframe} Candlestick Chart")
    
    # Generate sample price data
    dates = pd.date_range('2024-07-01', periods=100, freq='D')
    np.random.seed(42)
    prices = np.cumsum(np.random.randn(100) * 10) + 17400
    
    price_data = pd.DataFrame({
        'date': dates,
        'open': prices + np.random.randn(100) * 5,
        'high': prices + np.abs(np.random.randn(100) * 15),
        'low': prices - np.abs(np.random.randn(100) * 15),
        'close': prices,
        'ema_20': pd.Series(prices).ewm(span=20).mean().values,
        'ema_50': pd.Series(prices).ewm(span=50).mean().values,
    })
    
    # Create interactive chart
    fig = go.Figure()
    
    # Candlestick
    fig.add_trace(go.Candlestick(
        x=price_data['date'],
        open=price_data['open'],
        high=price_data['high'],
        low=price_data['low'],
        close=price_data['close'],
        name="OHLC"
    ))
    
    # EMAs
    fig.add_trace(go.Scatter(
        x=price_data['date'],
        y=price_data['ema_20'],
        mode='lines',
        name='EMA 20',
        line=dict(color='blue', width=2)
    ))
    
    fig.add_trace(go.Scatter(
        x=price_data['date'],
        y=price_data['ema_50'],
        mode='lines',
        name='EMA 50',
        line=dict(color='red', width=2)
    ))
    
    fig.layout.update(
        xaxis_rangeslider_visible=False,
        height=500,
        hovermode='x unified',
        template='plotly_white'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Technical Indicators
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("RSI(14)", "52.3", "Neutral", delta_color="off")
    with col2:
        st.metric("MACD", "Positive", "+2.5", delta_color="off")
    with col3:
        st.metric("ATR(14)", "125.50", "Vol: Moderate")

with tab2:
    st.subheader("📊 Active Positions")
    
    positions_data = pd.DataFrame({
        'Symbol': ['NIFTYAUG24FUT', 'NIFTY17400CE', 'BANKNIFTYAUG24FUT'],
        'Side': ['LONG', 'SHORT', 'LONG'],
        'Qty': [1, 2, 1],
        'Entry Price': [17380, 185, 44250],
        'Current Price': [17420, 175, 44300],
        'P&L (₹)': [2000, 1000, 500],
        'P&L %': ['+0.24%', '+2.70%', '+0.11%'],
        'Greeks': ['N/A', '0.45 Δ', 'N/A'],
    })
    
    st.dataframe(
        positions_data,
        use_container_width=True,
        hide_index=True,
        column_config={
            'P&L (₹)': st.column_config.NumberColumn(format="₹%d"),
            'Current Price': st.column_config.NumberColumn(format="%.2f"),
        }
    )
    
    st.markdown("---")
    st.subheader("💡 Position Management")
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Close Position**")
        position_to_close = st.selectbox("Select Position", positions_data['Symbol'])
        if st.button("Close Selected Position", key="close_pos"):
            st.success(f"✅ Position {position_to_close} closed successfully!")
    
    with col2:
        st.write("**Modify Position**")
        new_sl = st.number_input("New Stop Loss", min_value=0, value=17380)
        new_tp = st.number_input("New Take Profit", min_value=0, value=17500)
        if st.button("Update Levels", key="update_levels"):
            st.success("✅ Position levels updated!")

with tab3:
    st.subheader("🎯 Portfolio Greeks (Iron Condor Example)")
    
    # Greeks metrics
    greeks_metrics = {
        'Delta': {'value': 0.45, 'description': 'Directional exposure (Bullish)'},
        'Gamma': {'value': 0.002, 'description': 'Delta acceleration (Low)'},
        'Theta': {'value': -50, 'description': 'Daily decay (Good for seller)'},
        'Vega': {'value': 125, 'description': 'IV sensitivity (Long vol)'},
        'Rho': {'value': 45, 'description': 'Interest rate sensitivity'},
    }
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    cols = [col1, col2, col3, col4, col5]
    greek_names = ['Delta', 'Gamma', 'Theta', 'Vega', 'Rho']
    
    for idx, (col, greek_name) in enumerate(zip(cols, greek_names)):
        with col:
            metric = greeks_metrics[greek_name]
            st.metric(
                label=greek_name,
                value=f"{metric['value']:.2f}",
                help=metric['description']
            )
    
    st.markdown("---")
    
    st.subheader("📊 Greeks Evolution Over Time")
    
    # Generate Greeks time series
    dates = pd.date_range('2024-07-01', periods=20, freq='D')
    greeks_evolution = pd.DataFrame({
        'Date': dates,
        'Delta': np.random.uniform(0.3, 0.6, 20),
        'Gamma': np.random.uniform(0.001, 0.005, 20),
        'Theta': np.random.uniform(-100, -20, 20),
        'Vega': np.random.uniform(100, 200, 20),
    })
    
    st.line_chart(
        greeks_evolution.set_index('Date'),
        height=400,
        use_container_width=True
    )
    
    st.markdown("---")
    
    st.subheader("🎯 Options Strategies")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Iron Condor Setup**")
        ic_data = pd.DataFrame({
            'Leg': ['Short Call', 'Long Call', 'Short Put', 'Long Put'],
            'Strike': [17600, 17700, 17200, 17100],
            'Type': ['Sell', 'Buy', 'Sell', 'Buy'],
            'Premium': [120, 30, 115, 25],
        })
        st.table(ic_data)
        st.metric("Max Profit", "₹300", "At 17400")
        st.metric("Max Loss", "₹100", "Beyond boundaries")
    
    with col2:
        st.write("**Bull Call Spread Setup**")
        bcs_data = pd.DataFrame({
            'Position': ['Long 17400 CE', 'Short 17500 CE'],
            'Premium': [185, -85],
            'Net Cost': ['₹100 (credit)'],
        })
        st.table(bcs_data)
        st.metric("Probability of Profit", "65%", "At expiry")
        st.metric("Risk/Reward Ratio", "1:2", "Favorable")

with tab4:
    st.subheader("📋 Trade History & Performance")
    
    trades_data = pd.DataFrame({
        'Entry Date': ['2024-07-19', '2024-07-19', '2024-07-18', '2024-07-18', '2024-07-17'],
        'Symbol': ['NIFTYAUG24FUT', 'NIFTY17400CE', 'BANKNIFTYAUG24FUT', 'NIFTY17300PE', 'FINNIFTYAUG24FUT'],
        'Strategy': ['MTF', 'Iron Condor', 'MTF', 'Bull Call', 'MTF'],
        'Side': ['BUY', 'SELL', 'BUY', 'BUY', 'SELL'],
        'Entry': [17380, 185, 44250, 165, 21850],
        'Exit': [17420, 175, 44300, 175, 21820],
        'Qty': [1, 2, 1, 3, 1],
        'P&L (₹)': [2000, 1000, 500, 3000, -300],
        'P&L %': ['+0.24%', '+2.70%', '+0.11%', '+6.06%', '-0.14%'],
        'Duration': ['45m', '2h 15m', '1h 30m', '50m', '1h 20m'],
        'Status': ['✅ Closed', '✅ Closed', '✅ Closed', '✅ Closed', '✅ Closed'],
    })
    
    st.dataframe(
        trades_data,
        use_container_width=True,
        hide_index=True,
        height=400
    )
    
    st.markdown("---")
    
    st.subheader("📈 Performance Summary")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Trades", "5", "+2 Today")
    with col2:
        st.metric("Win Rate", "80%", "+10%")
    with col3:
        st.metric("Profit Factor", "3.2", "+0.5")
    with col4:
        st.metric("Avg Win/Loss", "₹1,500", "-₹300")
    
    # Trade distribution chart
    st.subheader("Trade Distribution")
    
    trade_by_strategy = pd.DataFrame({
        'Strategy': ['MTF', 'Iron Condor', 'Bull Call'],
        'Win Count': [3, 1, 1],
        'Loss Count': [0, 0, 0],
        'Total P&L': [2200, 1000, 3000]
    })
    
    fig = go.Figure(data=[
        go.Bar(name='Wins', x=trade_by_strategy['Strategy'], y=trade_by_strategy['Win Count']),
        go.Bar(name='Losses', x=trade_by_strategy['Strategy'], y=trade_by_strategy['Loss Count'])
    ])
    
    fig.update_layout(barmode='stack', height=400, hovermode='x')
    st.plotly_chart(fig, use_container_width=True)

with tab5:
    st.subheader("⚠️ Risk Dashboard")
    
    # Risk metrics
    risk_data = pd.DataFrame({
        'Risk Metric': [
            'Max Drawdown',
            'Daily Loss Limit',
            'Margin Usage',
            'Position Exposure',
            'Leverage Used',
            'Account Heat'
        ],
        'Current': ['8.5%', '2.1%', '42%', '₹15,00,000', '1.5x', '2 trades'],
        'Limit': ['15%', '5%', '80%', '₹20,00,000', '10x', '5 trades'],
        'Status': ['✅ Safe', '✅ Safe', '✅ Safe', '✅ Safe', '✅ Safe', '✅ Safe'],
    })
    
    st.dataframe(
        risk_data,
        use_container_width=True,
        hide_index=True,
        column_config={
            'Status': st.column_config.TextColumn(width='small'),
        }
    )
    
    st.markdown("---")
    
    # Risk gauge
    st.subheader("📊 Risk Gauge")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Account Heat", "40%", "2 out of 5 positions active")
    with col2:
        st.metric("Margin Buffer", "38%", "Can add ₹8,00,000 exposure")
    with col3:
        st.metric("Max Loss Today", "₹2,900", "Before 5% limit triggers")
    
    st.markdown("---")
    
    # Risk Controls
    st.subheader("🎛️ Risk Controls")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Position Risk Limits**")
        max_pos_size = st.slider("Max Position Size (%)", 1, 20, 10)
        risk_per_trade = st.slider("Risk Per Trade (%)", 0.5, 5.0, 2.0)
        max_positions = st.slider("Max Concurrent Positions", 1, 10, 5)
    
    with col2:
        st.write("**Account Risk Limits**")
        max_drawdown = st.slider("Max Drawdown (%)", 5, 30, 15)
        daily_loss_limit = st.slider("Daily Loss Limit (%)", 1, 10, 5)
        max_leverage = st.slider("Max Leverage", 1, 20, 10)
    
    if st.button("💾 Save Risk Settings", key="save_risk"):
        st.success("✅ Risk settings updated successfully!")

st.divider()

# Footer
st.markdown(f"""
---

### 📌 About This Dashboard

**Trading Bot India v1.0** - Complete Algorithmic Trading System
- 🔄 Multi-Timeframe Analysis (5m, 15m, 1h, 4h, daily)
- 📊 Options Greeks Calculator (Delta, Gamma, Theta, Vega)
- 🎯 Multiple Trading Strategies (MTF, Iron Condor, Bull Call)
- 📈 Live Backtesting Engine
- ⚠️ Built-in Risk Management

**Powered by:**
- Backtrader (Backtesting)
- Zerodha Kite Connect (Live Trading)
- Black-Scholes Model (Options Pricing)
- Streamlit (Dashboard)

**Last Updated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

**Repository:** https://github.com/vishsid/trading-bot-india

⚠️ **DISCLAIMER:** This is for educational purposes only. Trading involves substantial risk of loss.
""")
