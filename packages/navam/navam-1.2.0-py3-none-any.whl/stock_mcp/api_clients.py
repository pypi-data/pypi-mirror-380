"""API client implementations for various finance data sources."""

import os
import asyncio
from typing import Dict, Any, List, Optional
from datetime import datetime, timedelta
import yfinance as yf
import pandas as pd
import numpy as np
try:
    from .models import StockQuote, StockHistory, TechnicalIndicators, StockFundamentals
except ImportError:
    from models import StockQuote, StockHistory, TechnicalIndicators, StockFundamentals


class StockAPIClient:
    """Client for fetching stock data from various APIs."""

    def __init__(self):
        """Initialize the API client."""
        self.yf_cache = {}
        self.cache_duration = timedelta(minutes=5)

    async def get_quote(self, symbol: str) -> StockQuote:
        """Get real-time stock quote."""
        loop = asyncio.get_event_loop()
        ticker = await loop.run_in_executor(None, yf.Ticker, symbol)
        info = await loop.run_in_executor(None, lambda: ticker.info)

        current_price = info.get('currentPrice', info.get('regularMarketPrice', 0))
        previous_close = info.get('previousClose', info.get('regularMarketPreviousClose', 0))

        change = current_price - previous_close if previous_close else 0
        change_percent = (change / previous_close * 100) if previous_close else 0

        return StockQuote(
            symbol=symbol.upper(),
            price=current_price,
            change=change,
            change_percent=change_percent,
            volume=info.get('volume', 0),
            market_cap=info.get('marketCap'),
            open=info.get('open', info.get('regularMarketOpen')),
            high=info.get('dayHigh', info.get('regularMarketDayHigh')),
            low=info.get('dayLow', info.get('regularMarketDayLow')),
            previous_close=previous_close,
            timestamp=datetime.now()
        )

    async def get_history(self, symbol: str, period: str = "1mo") -> StockHistory:
        """Get historical stock data."""
        loop = asyncio.get_event_loop()
        ticker = await loop.run_in_executor(None, yf.Ticker, symbol)

        history = await loop.run_in_executor(
            None,
            lambda: ticker.history(period=period)
        )

        data = []
        for date, row in history.iterrows():
            data.append({
                "date": date.isoformat(),
                "open": float(row['Open']),
                "high": float(row['High']),
                "low": float(row['Low']),
                "close": float(row['Close']),
                "volume": int(row['Volume'])
            })

        return StockHistory(
            symbol=symbol.upper(),
            period=period,
            data=data
        )

    async def calculate_indicators(self, symbol: str) -> TechnicalIndicators:
        """Calculate technical indicators for a stock."""
        loop = asyncio.get_event_loop()
        ticker = await loop.run_in_executor(None, yf.Ticker, symbol)

        history = await loop.run_in_executor(
            None,
            lambda: ticker.history(period="6mo")
        )

        if history.empty:
            return TechnicalIndicators()

        close_prices = history['Close']
        volume = history['Volume']

        def calculate_rsi(prices, period=14):
            """Calculate RSI."""
            delta = prices.diff()
            gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
            loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
            rs = gain / loss
            rsi = 100 - (100 / (1 + rs))
            return rsi.iloc[-1] if not rsi.empty else None

        def calculate_bollinger_bands(prices, period=20, std_dev=2):
            """Calculate Bollinger Bands."""
            sma = prices.rolling(window=period).mean()
            std = prices.rolling(window=period).std()
            upper = sma + (std * std_dev)
            lower = sma - (std * std_dev)
            return upper.iloc[-1], lower.iloc[-1]

        sma_20 = close_prices.rolling(window=20).mean().iloc[-1] if len(close_prices) >= 20 else None
        sma_50 = close_prices.rolling(window=50).mean().iloc[-1] if len(close_prices) >= 50 else None
        sma_200 = close_prices.rolling(window=200).mean().iloc[-1] if len(close_prices) >= 200 else None

        ema_12 = close_prices.ewm(span=12, adjust=False).mean().iloc[-1] if len(close_prices) >= 12 else None
        ema_26 = close_prices.ewm(span=26, adjust=False).mean().iloc[-1] if len(close_prices) >= 26 else None

        macd = (ema_12 - ema_26) if ema_12 and ema_26 else None

        rsi = calculate_rsi(close_prices)

        upper_band, lower_band = calculate_bollinger_bands(close_prices) if len(close_prices) >= 20 else (None, None)

        volume_avg = volume.rolling(window=20).mean().iloc[-1] if len(volume) >= 20 else None

        return TechnicalIndicators(
            rsi=float(rsi) if rsi and not pd.isna(rsi) else None,
            sma_20=float(sma_20) if sma_20 and not pd.isna(sma_20) else None,
            sma_50=float(sma_50) if sma_50 and not pd.isna(sma_50) else None,
            sma_200=float(sma_200) if sma_200 and not pd.isna(sma_200) else None,
            ema_12=float(ema_12) if ema_12 and not pd.isna(ema_12) else None,
            ema_26=float(ema_26) if ema_26 and not pd.isna(ema_26) else None,
            macd=float(macd) if macd and not pd.isna(macd) else None,
            bollinger_upper=float(upper_band) if upper_band and not pd.isna(upper_band) else None,
            bollinger_lower=float(lower_band) if lower_band and not pd.isna(lower_band) else None,
            volume_avg=float(volume_avg) if volume_avg and not pd.isna(volume_avg) else None
        )

    async def get_fundamentals(self, symbol: str) -> StockFundamentals:
        """Get fundamental data for a stock."""
        loop = asyncio.get_event_loop()
        ticker = await loop.run_in_executor(None, yf.Ticker, symbol)
        info = await loop.run_in_executor(None, lambda: ticker.info)

        return StockFundamentals(
            pe_ratio=info.get('trailingPE'),
            eps=info.get('trailingEps'),
            dividend_yield=info.get('dividendYield'),
            beta=info.get('beta'),
            profit_margin=info.get('profitMargins'),
            revenue=info.get('totalRevenue'),
            debt_to_equity=info.get('debtToEquity')
        )

    async def get_market_overview(self) -> Dict[str, Any]:
        """Get market overview data."""
        indices = {
            "^DJI": "Dow Jones",
            "^GSPC": "S&P 500",
            "^IXIC": "NASDAQ",
            "^VIX": "VIX"
        }

        index_data = {}
        for symbol, name in indices.items():
            try:
                quote = await self.get_quote(symbol)
                index_data[name] = {
                    "price": quote.price,
                    "change": quote.change,
                    "change_percent": quote.change_percent
                }
            except:
                index_data[name] = {"price": 0, "change": 0, "change_percent": 0}

        return {
            "indices": index_data,
            "timestamp": datetime.now().isoformat()
        }

    async def search_stocks(self, query: str, sector: Optional[str] = None) -> List[Dict[str, Any]]:
        """Search for stocks by query or sector."""
        results = []

        if sector:
            sector_tickers = {
                "technology": ["AAPL", "MSFT", "GOOGL", "META", "NVDA"],
                "finance": ["JPM", "BAC", "WFC", "GS", "MS"],
                "healthcare": ["JNJ", "UNH", "PFE", "CVS", "ABBV"],
                "energy": ["XOM", "CVX", "COP", "SLB", "EOG"],
                "consumer": ["AMZN", "TSLA", "WMT", "HD", "NKE"]
            }

            tickers = sector_tickers.get(sector.lower(), [])
            for ticker in tickers:
                try:
                    quote = await self.get_quote(ticker)
                    results.append({
                        "symbol": ticker,
                        "price": quote.price,
                        "change_percent": quote.change_percent
                    })
                except:
                    pass

        return results