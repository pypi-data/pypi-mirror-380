"""Pydantic models for structured output."""

from typing import Dict, List, Optional, Any
from datetime import datetime
from pydantic import BaseModel, Field


class StockQuote(BaseModel):
    """Real-time stock quote data."""
    symbol: str = Field(description="Stock symbol")
    price: float = Field(description="Current price")
    change: float = Field(description="Price change")
    change_percent: float = Field(description="Price change percentage")
    volume: int = Field(description="Trading volume")
    market_cap: Optional[float] = Field(None, description="Market capitalization")
    open: Optional[float] = Field(None, description="Opening price")
    high: Optional[float] = Field(None, description="Daily high")
    low: Optional[float] = Field(None, description="Daily low")
    previous_close: Optional[float] = Field(None, description="Previous closing price")
    timestamp: datetime = Field(description="Quote timestamp")


class StockHistory(BaseModel):
    """Historical stock data."""
    symbol: str = Field(description="Stock symbol")
    period: str = Field(description="Time period (e.g., 1d, 1wk, 1mo, 1y)")
    data: List[Dict[str, Any]] = Field(description="Historical price data")


class TechnicalIndicators(BaseModel):
    """Technical analysis indicators."""
    rsi: Optional[float] = Field(None, description="Relative Strength Index")
    sma_20: Optional[float] = Field(None, description="20-day Simple Moving Average")
    sma_50: Optional[float] = Field(None, description="50-day Simple Moving Average")
    sma_200: Optional[float] = Field(None, description="200-day Simple Moving Average")
    ema_12: Optional[float] = Field(None, description="12-day Exponential Moving Average")
    ema_26: Optional[float] = Field(None, description="26-day Exponential Moving Average")
    macd: Optional[float] = Field(None, description="MACD indicator")
    bollinger_upper: Optional[float] = Field(None, description="Bollinger Band upper")
    bollinger_lower: Optional[float] = Field(None, description="Bollinger Band lower")
    volume_avg: Optional[float] = Field(None, description="Average volume")


class StockFundamentals(BaseModel):
    """Company fundamental data."""
    pe_ratio: Optional[float] = Field(None, description="Price-to-Earnings ratio")
    eps: Optional[float] = Field(None, description="Earnings per share")
    dividend_yield: Optional[float] = Field(None, description="Dividend yield percentage")
    beta: Optional[float] = Field(None, description="Beta coefficient")
    profit_margin: Optional[float] = Field(None, description="Profit margin")
    revenue: Optional[float] = Field(None, description="Total revenue")
    debt_to_equity: Optional[float] = Field(None, description="Debt-to-equity ratio")


class StockAnalysis(BaseModel):
    """Comprehensive stock analysis."""
    symbol: str = Field(description="Stock symbol")
    quote: StockQuote = Field(description="Current quote data")
    indicators: TechnicalIndicators = Field(description="Technical indicators")
    fundamentals: Optional[StockFundamentals] = Field(None, description="Fundamental data")
    recommendation: Optional[str] = Field(None, description="Analysis recommendation")
    sentiment: Optional[str] = Field(None, description="Market sentiment")


class MarketOverview(BaseModel):
    """Market overview data."""
    indices: Dict[str, float] = Field(description="Major market indices")
    gainers: List[str] = Field(description="Top gaining stocks")
    losers: List[str] = Field(description="Top losing stocks")
    most_active: List[str] = Field(description="Most actively traded stocks")
    timestamp: datetime = Field(description="Overview timestamp")


class PortfolioAnalysis(BaseModel):
    """Portfolio analysis results."""
    total_value: float = Field(description="Total portfolio value")
    total_return: float = Field(description="Total return amount")
    return_percentage: float = Field(description="Return percentage")
    holdings: List[Dict[str, Any]] = Field(description="Individual holdings analysis")
    allocation: Dict[str, float] = Field(description="Asset allocation percentages")
    risk_metrics: Dict[str, Any] = Field(description="Risk metrics")