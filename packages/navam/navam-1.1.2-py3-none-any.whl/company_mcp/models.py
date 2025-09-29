"""Pydantic models for company research data"""

from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field
from datetime import datetime

class CompanyProfile(BaseModel):
    """Comprehensive company profile information"""
    symbol: str = Field(description="Stock ticker symbol")
    name: str = Field(description="Company name")
    description: str = Field(description="Business description")
    sector: str = Field(description="Business sector")
    industry: str = Field(description="Industry classification")
    exchange: str = Field(description="Stock exchange")
    country: str = Field(description="Country of incorporation")
    address: str = Field(description="Headquarters address")
    employees: int = Field(description="Number of full-time employees")
    ceo: str = Field(description="Chief Executive Officer name")
    website: str = Field(description="Company website")
    phone: str = Field(description="Contact phone number")
    market_cap: float = Field(description="Market capitalization")
    pe_ratio: Optional[float] = Field(description="Price-to-earnings ratio")
    dividend_yield: Optional[float] = Field(description="Dividend yield percentage")
    beta: Optional[float] = Field(description="Beta coefficient")
    year_high: float = Field(description="52-week high price")
    year_low: float = Field(description="52-week low price")

class CompanyFinancials(BaseModel):
    """Company financial statements data"""
    symbol: str = Field(description="Stock ticker symbol")
    period: str = Field(description="Reporting period (annual/quarterly)")
    fiscal_year: str = Field(description="Fiscal year")
    revenue: float = Field(description="Total revenue")
    gross_profit: float = Field(description="Gross profit")
    operating_income: float = Field(description="Operating income")
    net_income: float = Field(description="Net income")
    eps: float = Field(description="Earnings per share")
    total_assets: float = Field(description="Total assets")
    total_liabilities: float = Field(description="Total liabilities")
    total_equity: float = Field(description="Total shareholder equity")
    cash: float = Field(description="Cash and cash equivalents")
    debt: float = Field(description="Total debt")
    free_cash_flow: float = Field(description="Free cash flow")

class Filing(BaseModel):
    """SEC filing information"""
    form_type: str = Field(description="SEC form type (10-K, 10-Q, 8-K, etc.)")
    filing_date: str = Field(description="Filing date")
    period_ending: str = Field(description="Period ending date")
    accession_number: str = Field(description="SEC accession number")
    file_url: str = Field(description="URL to filing document")
    description: str = Field(description="Filing description")

class CompanyFilings(BaseModel):
    """Collection of SEC filings"""
    symbol: str = Field(description="Stock ticker symbol")
    filings: List[Filing] = Field(description="List of SEC filings")
    total_filings: int = Field(description="Total number of filings found")


class InsiderTransaction(BaseModel):
    """Individual insider trading transaction"""
    insider_name: str = Field(description="Insider's name")
    position: str = Field(description="Insider's position in company")
    transaction_type: str = Field(description="Buy/Sell/Option Exercise")
    shares: int = Field(description="Number of shares")
    price: float = Field(description="Transaction price per share")
    value: float = Field(description="Total transaction value")
    date: str = Field(description="Transaction date")
    ownership_change: float = Field(description="Percentage change in ownership")

class CompanyInsiders(BaseModel):
    """Insider trading summary"""
    symbol: str = Field(description="Stock ticker symbol")
    transactions: List[InsiderTransaction] = Field(description="List of insider transactions")
    total_bought: int = Field(description="Total buy transactions")
    total_sold: int = Field(description="Total sell transactions")
    net_shares: int = Field(description="Net shares bought/sold")
    net_value: float = Field(description="Net transaction value")
    period_months: int = Field(description="Period covered in months")

class AnalystRating(BaseModel):
    """Individual analyst rating"""
    firm: str = Field(description="Investment firm name")
    analyst: str = Field(description="Analyst name")
    rating: str = Field(description="Rating (Buy/Hold/Sell)")
    price_target: float = Field(description="Price target")
    date: str = Field(description="Rating date")

class CompanyRatings(BaseModel):
    """Analyst ratings consensus"""
    symbol: str = Field(description="Stock ticker symbol")
    ratings: List[AnalystRating] = Field(description="List of analyst ratings")
    consensus: str = Field(description="Consensus recommendation")
    average_target: float = Field(description="Average price target")
    high_target: float = Field(description="Highest price target")
    low_target: float = Field(description="Lowest price target")
    total_analysts: int = Field(description="Total number of analysts")
    buy_count: int = Field(description="Number of buy ratings")
    hold_count: int = Field(description="Number of hold ratings")
    sell_count: int = Field(description="Number of sell ratings")

class IndustryComparison(BaseModel):
    """Comparison of multiple companies"""
    companies: List[Dict[str, Any]] = Field(description="Company comparison data")
    metrics_compared: List[str] = Field(description="Metrics included in comparison")
    comparison_date: str = Field(description="Date of comparison")

class CompanyOverview(BaseModel):
    """Brief company overview for search results"""
    symbol: str = Field(description="Stock ticker symbol")
    name: str = Field(description="Company name")
    type: str = Field(description="Security type")
    region: str = Field(description="Geographic region")
    currency: str = Field(description="Trading currency")
    match_score: float = Field(description="Search relevance score")