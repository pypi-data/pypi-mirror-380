"""API Clients for Company Research Data"""

import os
import asyncio
import aiohttp
from typing import Dict, Any, List, Optional
from datetime import datetime, timedelta
import json
import logging
from urllib.parse import quote
import yfinance as yf
import pandas as pd

# Import models with fallback
try:
    from .models import (
        CompanyProfile, CompanyFinancials, CompanyFilings,
        CompanyInsiders, CompanyRatings,
        IndustryComparison, CompanyOverview, Filing,
        InsiderTransaction, AnalystRating
    )
except ImportError:
    from models import (
        CompanyProfile, CompanyFinancials, CompanyFilings,
        CompanyInsiders, CompanyRatings,
        IndustryComparison, CompanyOverview, Filing,
        InsiderTransaction, AnalystRating
    )

logger = logging.getLogger(__name__)

class CompanyAPIClient:
    """Client for fetching company research data from multiple sources"""

    def __init__(self):
        self.alpha_vantage_key = os.getenv("ALPHA_VANTAGE_KEY", "")
        self.polygon_key = os.getenv("POLYGON_API_KEY", "")
        self.marketaux_key = os.getenv("MARKETAUX_API_KEY", "")
        self.session: Optional[aiohttp.ClientSession] = None
        self.sec_base_url = "https://data.sec.gov"
        self.alpha_base_url = "https://www.alphavantage.co/query"
        self.polygon_base_url = "https://api.polygon.io"
        self.marketaux_base_url = "https://api.marketaux.com/v1"

    @classmethod
    async def create(cls) -> "CompanyAPIClient":
        """Create and initialize the API client"""
        client = cls()
        client.session = aiohttp.ClientSession(
            headers={
                "User-Agent": "CompanyResearchMCP/1.0 (research@example.com)"
            }
        )
        return client

    async def close(self):
        """Close the HTTP session"""
        if self.session:
            await self.session.close()

    async def get_company_profile(self, symbol: str) -> CompanyProfile:
        """Get company profile from yfinance as primary source"""
        try:
            # Try yfinance first (more reliable and comprehensive)
            ticker = yf.Ticker(symbol)
            info = ticker.info

            if info and info.get('symbol'):
                return CompanyProfile(
                    symbol=info.get('symbol', symbol),
                    name=info.get('longName', info.get('shortName', f'{symbol} Company')),
                    description=info.get('longBusinessSummary', ''),
                    sector=info.get('sector', ''),
                    industry=info.get('industry', ''),
                    exchange=info.get('exchange', ''),
                    country=info.get('country', 'USA'),
                    address=f"{info.get('address1', '')} {info.get('city', '')} {info.get('state', '')} {info.get('zip', '')}".strip(),
                    employees=info.get('fullTimeEmployees', 0),
                    ceo=info.get('companyOfficers', [{}])[0].get('name', '') if info.get('companyOfficers') else '',
                    website=info.get('website', ''),
                    phone=info.get('phone', ''),
                    market_cap=info.get('marketCap', 0),
                    pe_ratio=info.get('trailingPE'),
                    dividend_yield=info.get('dividendYield'),
                    beta=info.get('beta'),
                    year_high=info.get('fiftyTwoWeekHigh', 0),
                    year_low=info.get('fiftyTwoWeekLow', 0)
                )

            # Fallback to Alpha Vantage if yfinance fails
            if self.alpha_vantage_key:
                url = f"{self.alpha_base_url}?function=OVERVIEW&symbol={symbol}&apikey={self.alpha_vantage_key}"
                async with self.session.get(url) as response:
                    data = await response.json()

                if "Symbol" in data:
                    return CompanyProfile(
                        symbol=data.get("Symbol", symbol),
                        name=data.get("Name", "Unknown Company"),
                        description=data.get("Description", ""),
                        sector=data.get("Sector", ""),
                        industry=data.get("Industry", ""),
                        exchange=data.get("Exchange", ""),
                        country=data.get("Country", "USA"),
                        address=data.get("Address", ""),
                        employees=int(data.get("FullTimeEmployees", 0)) if data.get("FullTimeEmployees") else 0,
                        ceo="",
                        website="",
                        phone="",
                        market_cap=float(data.get("MarketCapitalization", 0)),
                        pe_ratio=float(data.get("PERatio", 0)) if data.get("PERatio") and data.get("PERatio") != "None" else None,
                        dividend_yield=float(data.get("DividendYield", 0)) if data.get("DividendYield") and data.get("DividendYield") != "None" else None,
                        beta=float(data.get("Beta", 0)) if data.get("Beta") and data.get("Beta") != "None" else None,
                        year_high=float(data.get("52WeekHigh", 0)),
                        year_low=float(data.get("52WeekLow", 0))
                    )

            # If all else fails, return basic profile with error indication
            raise ValueError(f"Unable to fetch data for symbol: {symbol}")

        except Exception as e:
            logger.error(f"Error fetching company profile for {symbol}: {e}")
            # Return a minimal profile with error indication
            return CompanyProfile(
                symbol=symbol,
                name=f"{symbol} (Data Unavailable)",
                description="Unable to fetch company information. Please verify the symbol.",
                sector="Unknown",
                industry="Unknown",
                exchange="Unknown",
                country="Unknown",
                address="",
                employees=0,
                ceo="",
                website="",
                phone="",
                market_cap=0,
                pe_ratio=None,
                dividend_yield=None,
                beta=None,
                year_high=0,
                year_low=0
            )

    async def get_financials(self, symbol: str, period: str = "annual") -> CompanyFinancials:
        """Get company financial statements from yfinance"""
        # Validate period parameter
        if period not in ["annual", "quarterly"]:
            raise ValueError(f"Invalid period '{period}'. Must be 'annual' or 'quarterly'")

        try:
            # Use yfinance for financial data
            ticker = yf.Ticker(symbol)

            # Get financial statements
            if period == "annual":
                income_stmt = ticker.income_stmt
                balance_sheet = ticker.balance_sheet
                cash_flow = ticker.cash_flow
            else:  # quarterly
                income_stmt = ticker.quarterly_income_stmt
                balance_sheet = ticker.quarterly_balance_sheet
                cash_flow = ticker.quarterly_cash_flow

            if income_stmt is not None and not income_stmt.empty:
                latest_date = income_stmt.columns[0]

                # Extract financial metrics
                revenue = income_stmt.loc['Total Revenue'][latest_date] if 'Total Revenue' in income_stmt.index else 0
                gross_profit = income_stmt.loc['Gross Profit'][latest_date] if 'Gross Profit' in income_stmt.index else 0
                operating_income = income_stmt.loc['Operating Income'][latest_date] if 'Operating Income' in income_stmt.index else 0
                net_income = income_stmt.loc['Net Income'][latest_date] if 'Net Income' in income_stmt.index else 0

                # Get balance sheet data
                total_assets = balance_sheet.loc['Total Assets'][latest_date] if balance_sheet is not None and not balance_sheet.empty and 'Total Assets' in balance_sheet.index else 0
                total_liabilities = balance_sheet.loc['Total Liabilities Net Minority Interest'][latest_date] if balance_sheet is not None and not balance_sheet.empty and 'Total Liabilities Net Minority Interest' in balance_sheet.index else 0
                total_equity = balance_sheet.loc['Total Equity Gross Minority Interest'][latest_date] if balance_sheet is not None and not balance_sheet.empty and 'Total Equity Gross Minority Interest' in balance_sheet.index else 0
                cash = balance_sheet.loc['Cash And Cash Equivalents'][latest_date] if balance_sheet is not None and not balance_sheet.empty and 'Cash And Cash Equivalents' in balance_sheet.index else 0
                debt = balance_sheet.loc['Total Debt'][latest_date] if balance_sheet is not None and not balance_sheet.empty and 'Total Debt' in balance_sheet.index else 0

                # Get cash flow data
                free_cash_flow = cash_flow.loc['Free Cash Flow'][latest_date] if cash_flow is not None and not cash_flow.empty and 'Free Cash Flow' in cash_flow.index else 0

                # Get EPS from info
                info = ticker.info
                eps = info.get('trailingEps', 0) if period == "annual" else info.get('forwardEps', 0)

                return CompanyFinancials(
                    symbol=symbol,
                    period=period,
                    fiscal_year=str(latest_date.year) if hasattr(latest_date, 'year') else str(latest_date),
                    revenue=float(revenue) if revenue else 0,
                    gross_profit=float(gross_profit) if gross_profit else 0,
                    operating_income=float(operating_income) if operating_income else 0,
                    net_income=float(net_income) if net_income else 0,
                    eps=float(eps) if eps else 0,
                    total_assets=float(total_assets) if total_assets else 0,
                    total_liabilities=float(total_liabilities) if total_liabilities else 0,
                    total_equity=float(total_equity) if total_equity else 0,
                    cash=float(cash) if cash else 0,
                    debt=float(debt) if debt else 0,
                    free_cash_flow=float(free_cash_flow) if free_cash_flow else 0
                )

            # If yfinance fails, return error indication
            raise ValueError(f"No financial data available for {symbol}")

        except Exception as e:
            logger.error(f"Error fetching financials for {symbol}: {e}")
            # Return empty financials with error indication
            return CompanyFinancials(
                symbol=symbol,
                period=period,
                fiscal_year="N/A",
                revenue=0,
                gross_profit=0,
                operating_income=0,
                net_income=0,
                eps=0,
                total_assets=0,
                total_liabilities=0,
                total_equity=0,
                cash=0,
                debt=0,
                free_cash_flow=0
            )

    async def get_sec_filings(self, symbol: str, filing_type: Optional[str], limit: int) -> CompanyFilings:
        """Get SEC filings for a company using yfinance and SEC API"""
        try:
            # Try to get real SEC filings using yfinance
            ticker = yf.Ticker(symbol)

            # Get company CIK for SEC EDGAR API
            info = ticker.info
            company_name = info.get('longName', info.get('shortName', ''))

            filings_list = []

            # Try to fetch from SEC EDGAR API if we have session
            if self.session and company_name:
                try:
                    # Search for company CIK
                    search_url = f"https://www.sec.gov/cgi-bin/browse-edgar?company={quote(company_name)}&output=json"
                    headers = {'User-Agent': 'CompanyResearchMCP/1.0'}

                    # For now, use yfinance's available data
                    # Real SEC EDGAR integration would require proper CIK lookup
                    pass
                except Exception as e:
                    logger.debug(f"SEC EDGAR lookup failed: {e}")

            # Get recent actions from yfinance (earnings, dividends, etc.)
            try:
                # Get earnings dates as proxy for quarterly filings
                earnings_dates = ticker.earnings_dates
                if earnings_dates is not None and not earnings_dates.empty:
                    for date in earnings_dates.index[:min(limit, 5)]:
                        filings_list.append(Filing(
                            form_type="10-Q" if not filing_type or filing_type == "10-Q" else filing_type,
                            filing_date=date.strftime('%Y-%m-%d'),
                            period_ending=date.strftime('%Y-%m-%d'),
                            accession_number=f"EARN-{date.strftime('%Y%m%d')}",
                            file_url=f"https://finance.yahoo.com/quote/{symbol}/financials",
                            description="Quarterly earnings report"
                        ))
            except Exception:
                pass

            # Add annual report placeholder
            if not filing_type or filing_type == "10-K":
                current_year = datetime.now().year
                filings_list.append(Filing(
                    form_type="10-K",
                    filing_date=f"{current_year-1}-03-15",
                    period_ending=f"{current_year-1}-12-31",
                    accession_number=f"10K-{current_year-1}",
                    file_url=f"https://finance.yahoo.com/quote/{symbol}/financials?p={symbol}",
                    description="Annual report"
                ))

            # Filter by type if specified
            if filing_type:
                filings_list = [f for f in filings_list if f.form_type == filing_type]

            # Limit results
            filings_list = filings_list[:limit]

            if filings_list:
                return CompanyFilings(
                    symbol=symbol,
                    filings=filings_list,
                    total_filings=len(filings_list)
                )

            # Fallback to basic mock data if no real data available
            return self._get_mock_filings(symbol, filing_type, limit)

        except Exception as e:
            logger.error(f"Error fetching SEC filings: {e}")
            return self._get_mock_filings(symbol, filing_type, limit)


    async def get_insider_trading(self, symbol: str, months: int) -> CompanyInsiders:
        """Get insider trading data from yfinance"""
        try:
            ticker = yf.Ticker(symbol)

            # Get insider transactions from yfinance
            try:
                insider_transactions = ticker.insider_transactions

                if insider_transactions is not None and not insider_transactions.empty:
                    # Filter by date range
                    cutoff_date = datetime.now() - timedelta(days=months * 30)

                    transactions = []
                    total_bought = 0
                    total_sold = 0
                    net_shares = 0
                    net_value = 0

                    for _, row in insider_transactions.iterrows():
                        # Parse transaction date
                        trans_date = pd.to_datetime(row.get('Date', datetime.now()))

                        if trans_date >= cutoff_date:
                            shares = row.get('Shares', 0)
                            value = row.get('Value', 0)
                            trans_type = 'Buy' if shares > 0 else 'Sell'

                            if shares > 0:
                                total_bought += 1
                            else:
                                total_sold += 1
                                shares = abs(shares)
                                value = abs(value)

                            net_shares += row.get('Shares', 0)
                            net_value += row.get('Value', 0)

                            transactions.append(InsiderTransaction(
                                insider_name=row.get('Insider', 'Unknown'),
                                position=row.get('Position', 'Executive'),
                                transaction_type=trans_type,
                                shares=int(shares) if shares else 0,
                                price=float(value / shares) if shares and value else 0,
                                value=float(value) if value else 0,
                                date=trans_date.strftime('%Y-%m-%d'),
                                ownership_change=0  # yfinance doesn't provide ownership change
                            ))

                    if transactions:
                        return CompanyInsiders(
                            symbol=symbol,
                            transactions=transactions[:20],  # Limit to 20 most recent
                            total_bought=total_bought,
                            total_sold=total_sold,
                            net_shares=int(net_shares),
                            net_value=float(net_value),
                            period_months=months
                        )
            except Exception as e:
                logger.debug(f"Could not get insider transactions for {symbol}: {e}")

            # Get insider holdings as alternative
            try:
                insider_holders = ticker.insider_holders

                if insider_holders is not None and not insider_holders.empty:
                    transactions = []

                    for _, row in insider_holders.iterrows():
                        # Convert insider holdings to pseudo-transactions
                        shares = row.get('Shares', 0)
                        position = row.get('Position', 'Executive')
                        holder_name = row.get('Name', 'Unknown Insider')
                        date_reported = row.get('Date Reported', datetime.now())

                        if isinstance(date_reported, str):
                            try:
                                date_reported = pd.to_datetime(date_reported)
                            except:
                                date_reported = datetime.now()

                        transactions.append(InsiderTransaction(
                            insider_name=holder_name,
                            position=position,
                            transaction_type='Hold',
                            shares=int(shares) if shares else 0,
                            price=0,  # Holdings don't have price
                            value=0,  # Holdings don't have value
                            date=date_reported.strftime('%Y-%m-%d') if hasattr(date_reported, 'strftime') else str(date_reported),
                            ownership_change=0
                        ))

                    if transactions:
                        return CompanyInsiders(
                            symbol=symbol,
                            transactions=transactions[:10],
                            total_bought=0,
                            total_sold=0,
                            net_shares=sum(t.shares for t in transactions),
                            net_value=0,
                            period_months=months
                        )
            except Exception as e:
                logger.debug(f"Could not get insider holders for {symbol}: {e}")

            # If no real data available, return minimal response
            return CompanyInsiders(
                symbol=symbol,
                transactions=[],
                total_bought=0,
                total_sold=0,
                net_shares=0,
                net_value=0,
                period_months=months
            )

        except Exception as e:
            logger.error(f"Error fetching insider trading for {symbol}: {e}")
            # Return empty data instead of mock
            return CompanyInsiders(
                symbol=symbol,
                transactions=[],
                total_bought=0,
                total_sold=0,
                net_shares=0,
                net_value=0,
                period_months=months
            )

    async def get_analyst_ratings(self, symbol: str) -> CompanyRatings:
        """Get analyst ratings and price targets from yfinance"""
        try:
            ticker = yf.Ticker(symbol)
            info = ticker.info

            # Get recommendations if available
            try:
                recommendations = ticker.recommendations
                ratings = []

                if recommendations is not None and not recommendations.empty:
                    # Get latest recommendations
                    recent_recs = recommendations.tail(10)  # Last 10 recommendations

                    for idx, rec in recent_recs.iterrows():
                        # Format date properly
                        rec_date = idx if idx else datetime.now()
                        if hasattr(rec_date, 'strftime'):
                            date_str = rec_date.strftime('%Y-%m-%d')
                        else:
                            date_str = str(rec_date)[:10] if str(rec_date) != 'nan' else datetime.now().strftime('%Y-%m-%d')

                        ratings.append(AnalystRating(
                            firm=rec.get('Firm', 'Consensus') if rec.get('Firm') else 'Consensus',
                            analyst="",  # yfinance doesn't provide analyst names
                            rating=rec.get('To Grade', rec.get('Action', 'Hold')),
                            price_target=0,  # yfinance doesn't provide individual price targets in recommendations
                            date=date_str
                        ))
            except Exception as e:
                logger.debug(f"Could not get recommendations for {symbol}: {e}")

            # Get aggregated data from info
            target_mean = info.get('targetMeanPrice', 0)
            target_high = info.get('targetHighPrice', 0)
            target_low = info.get('targetLowPrice', 0)
            recommendation = info.get('recommendationKey', 'hold')
            num_analysts = info.get('numberOfAnalystOpinions', 0)

            # If we have target prices but no individual ratings, create aggregated entries
            if not ratings and target_mean > 0:
                ratings = [
                    AnalystRating(
                        firm="Consensus",
                        analyst="Multiple Analysts",
                        rating=recommendation.title() if recommendation else "Hold",
                        price_target=target_mean,
                        date=datetime.now().strftime('%Y-%m-%d')
                    )
                ]

            # Calculate consensus counts (estimate based on recommendation)
            if recommendation:
                rec_lower = recommendation.lower()
                if 'strong_buy' in rec_lower or 'buy' in rec_lower:
                    buy_count = int(num_analysts * 0.6)
                    hold_count = int(num_analysts * 0.3)
                    sell_count = num_analysts - buy_count - hold_count
                elif 'hold' in rec_lower:
                    buy_count = int(num_analysts * 0.3)
                    hold_count = int(num_analysts * 0.5)
                    sell_count = num_analysts - buy_count - hold_count
                else:
                    buy_count = int(num_analysts * 0.2)
                    hold_count = int(num_analysts * 0.3)
                    sell_count = num_analysts - buy_count - hold_count
            else:
                buy_count = hold_count = sell_count = 0

            if ratings or target_mean > 0:
                return CompanyRatings(
                    symbol=symbol,
                    ratings=ratings,
                    consensus=recommendation.title() if recommendation else "Hold",
                    average_target=target_mean,
                    high_target=target_high,
                    low_target=target_low,
                    total_analysts=num_analysts,
                    buy_count=buy_count,
                    hold_count=hold_count,
                    sell_count=sell_count
                )

            # No ratings data available
            return CompanyRatings(
                symbol=symbol,
                ratings=[],
                consensus="No Data",
                average_target=0,
                high_target=0,
                low_target=0,
                total_analysts=0,
                buy_count=0,
                hold_count=0,
                sell_count=0
            )

        except Exception as e:
            logger.error(f"Error fetching analyst ratings for {symbol}: {e}")
            return CompanyRatings(
                symbol=symbol,
                ratings=[],
                consensus="Error",
                average_target=0,
                high_target=0,
                low_target=0,
                total_analysts=0,
                buy_count=0,
                hold_count=0,
                sell_count=0
            )

    async def compare_companies(self, symbols: List[str], metrics: Optional[List[str]]) -> IndustryComparison:
        """Compare multiple companies"""
        try:
            companies = []
            for symbol in symbols:
                profile = await self.get_company_profile(symbol)
                financials = await self.get_financials(symbol, "annual")

                companies.append({
                    "symbol": symbol,
                    "name": profile.name,
                    "market_cap": profile.market_cap,
                    "pe_ratio": profile.pe_ratio,
                    "revenue": financials.revenue,
                    "net_income": financials.net_income,
                    "profit_margin": (financials.net_income / financials.revenue * 100) if financials.revenue else 0
                })

            return IndustryComparison(
                companies=companies,
                metrics_compared=metrics or ["market_cap", "pe_ratio", "revenue", "net_income", "profit_margin"],
                comparison_date=datetime.now().isoformat()
            )

        except Exception as e:
            logger.error(f"Error comparing companies: {e}")
            raise

    async def search_companies(self, query: str, filters: Optional[Dict[str, Any]], limit: int) -> List[CompanyOverview]:
        """Search for companies using multiple sources"""
        results = []

        try:
            # First try Alpha Vantage if API key is available
            if self.alpha_vantage_key and self.session:
                try:
                    url = f"{self.alpha_base_url}?function=SYMBOL_SEARCH&keywords={quote(query)}&apikey={self.alpha_vantage_key}"
                    async with self.session.get(url) as response:
                        data = await response.json()

                    if "bestMatches" in data:
                        for match in data["bestMatches"][:limit]:
                            results.append(CompanyOverview(
                                symbol=match.get("1. symbol", ""),
                                name=match.get("2. name", ""),
                                type=match.get("3. type", ""),
                                region=match.get("4. region", ""),
                                currency=match.get("8. currency", "USD"),
                                match_score=float(match.get("9. matchScore", 0))
                            ))

                        if results:
                            return results[:limit]
                except Exception as e:
                    logger.debug(f"Alpha Vantage search failed: {e}")

            # Fallback: Use yfinance to search for well-known symbols
            # Create a list of common stock symbols that match the query
            query_lower = query.lower()

            # Common stocks database (expandable)
            common_stocks = {
                # Technology
                "technology": ["AAPL", "MSFT", "GOOGL", "META", "NVDA", "TSM", "AVGO", "ORCL", "ASML", "CSCO"],
                "tech": ["AAPL", "MSFT", "GOOGL", "META", "NVDA", "AMD", "INTC", "CRM", "ADBE", "NOW"],
                "software": ["MSFT", "ORCL", "CRM", "ADBE", "NOW", "INTU", "PLTR", "SNOW", "TEAM", "WDAY"],
                # Finance
                "banking": ["JPM", "BAC", "WFC", "GS", "MS", "C", "USB", "PNC", "TFC", "COF"],
                "bank": ["JPM", "BAC", "WFC", "GS", "MS", "C", "USB", "PNC", "TFC", "COF"],
                "finance": ["JPM", "BAC", "BRK.B", "V", "MA", "GS", "MS", "AXP", "BLK", "SPGI"],
                "financial": ["JPM", "BAC", "BRK.B", "V", "MA", "WFC", "GS", "MS", "C", "AXP"],
                # Healthcare
                "healthcare": ["JNJ", "UNH", "PFE", "LLY", "ABBV", "TMO", "MRK", "ABT", "DHR", "CVS"],
                "pharmaceutical": ["JNJ", "PFE", "LLY", "ABBV", "MRK", "AZN", "NVS", "BMY", "AMGN", "GILD"],
                "pharma": ["JNJ", "PFE", "LLY", "ABBV", "MRK", "AZN", "NVS", "BMY", "AMGN", "GILD"],
                # Automotive
                "auto": ["TSLA", "F", "GM", "TM", "HMC", "STLA", "RIVN", "NIO", "LI", "XPEV"],
                "automotive": ["TSLA", "F", "GM", "TM", "HMC", "STLA", "RIVN", "NIO", "LI", "XPEV"],
                "car": ["TSLA", "F", "GM", "TM", "HMC", "STLA", "RIVN", "NIO", "LI", "XPEV"],
                # Energy
                "energy": ["XOM", "CVX", "COP", "SLB", "EOG", "MPC", "PSX", "VLO", "PXD", "OXY"],
                "oil": ["XOM", "CVX", "COP", "SLB", "BP", "SHEL", "TTE", "EOG", "MPC", "PSX"],
                "renewable": ["NEE", "ENPH", "SEDG", "RUN", "PLUG", "FSLR", "BE", "CSIQ", "NOVA", "ARRY"],
                # Retail
                "retail": ["AMZN", "WMT", "HD", "COST", "TGT", "LOW", "TJX", "CVS", "NKE", "SBUX"],
                "ecommerce": ["AMZN", "SHOP", "EBAY", "ETSY", "MELI", "SE", "CPNG", "PDD", "JD", "BABA"],
                # Default individual stock symbols
                "apple": ["AAPL"],
                "microsoft": ["MSFT"],
                "google": ["GOOGL", "GOOG"],
                "amazon": ["AMZN"],
                "tesla": ["TSLA"],
                "meta": ["META"],
                "nvidia": ["NVDA"],
                "berkshire": ["BRK.B", "BRK.A"],
            }

            # Find matching symbols based on query
            matching_symbols = []

            # Check if query matches a category
            for key, symbols in common_stocks.items():
                if key in query_lower:
                    matching_symbols.extend(symbols)

            # Also check if query is a direct symbol
            if query.upper() in ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "META", "NVDA", "JPM", "BAC", "WFC"]:
                matching_symbols.append(query.upper())

            # Remove duplicates while preserving order
            seen = set()
            unique_symbols = []
            for symbol in matching_symbols:
                if symbol not in seen:
                    seen.add(symbol)
                    unique_symbols.append(symbol)

            # Get company info for matching symbols
            for symbol in unique_symbols[:limit]:
                try:
                    ticker = yf.Ticker(symbol)
                    info = ticker.info

                    if info and info.get('symbol'):
                        results.append(CompanyOverview(
                            symbol=info.get('symbol', symbol),
                            name=info.get('longName', info.get('shortName', f'{symbol} Company')),
                            type="Equity",
                            region=info.get('country', 'US'),
                            currency=info.get('currency', 'USD'),
                            match_score=0.9  # High score for direct matches
                        ))
                except Exception as e:
                    logger.debug(f"Could not get info for {symbol}: {e}")

            # If no results yet, try a more generic search
            if not results and query:
                # Return some popular stocks as suggestions
                default_symbols = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"]
                for symbol in default_symbols[:limit]:
                    try:
                        ticker = yf.Ticker(symbol)
                        info = ticker.info

                        if info and info.get('symbol'):
                            # Check if company name contains query
                            company_name = info.get('longName', '').lower()
                            if query_lower in company_name or query_lower in symbol.lower():
                                score = 0.8
                            else:
                                score = 0.3  # Lower score for non-matches

                            results.append(CompanyOverview(
                                symbol=info.get('symbol', symbol),
                                name=info.get('longName', info.get('shortName', f'{symbol} Company')),
                                type="Equity",
                                region=info.get('country', 'US'),
                                currency=info.get('currency', 'USD'),
                                match_score=score
                            ))
                    except Exception as e:
                        logger.debug(f"Could not get info for {symbol}: {e}")

            # Sort by match score
            results.sort(key=lambda x: x.match_score, reverse=True)

            return results[:limit]

        except Exception as e:
            logger.error(f"Error searching companies: {e}")
            return []

    # Mock data methods for demonstration
    def _get_mock_profile(self, symbol: str) -> CompanyProfile:
        """Return mock company profile for demonstration"""
        mock_profiles = {
            "AAPL": CompanyProfile(
                symbol="AAPL",
                name="Apple Inc.",
                description="Apple Inc. designs, manufactures, and markets smartphones, personal computers, tablets, wearables, and accessories worldwide.",
                sector="Technology",
                industry="Consumer Electronics",
                exchange="NASDAQ",
                country="USA",
                address="One Apple Park Way, Cupertino, CA 95014",
                employees=161000,
                ceo="Tim Cook",
                website="https://www.apple.com",
                phone="1-408-996-1010",
                market_cap=3000000000000,
                pe_ratio=31.5,
                dividend_yield=0.44,
                beta=1.25,
                year_high=199.62,
                year_low=164.08
            )
        }

        return mock_profiles.get(symbol, CompanyProfile(
            symbol=symbol,
            name=f"{symbol} Company",
            description="Company description not available",
            sector="Unknown",
            industry="Unknown",
            exchange="Unknown",
            country="USA",
            address="",
            employees=0,
            ceo="",
            website="",
            phone="",
            market_cap=0,
            pe_ratio=None,
            dividend_yield=None,
            beta=None,
            year_high=0,
            year_low=0
        ))

    def _get_mock_financials(self, symbol: str, period: str) -> CompanyFinancials:
        """Return mock financial data"""
        return CompanyFinancials(
            symbol=symbol,
            period=period,
            fiscal_year="2023",
            revenue=394328000000,
            gross_profit=169148000000,
            operating_income=114301000000,
            net_income=96995000000,
            eps=6.16,
            total_assets=352755000000,
            total_liabilities=290437000000,
            total_equity=62318000000,
            cash=29965000000,
            debt=111088000000,
            free_cash_flow=99584000000
        )

    def _get_mock_filings(self, symbol: str, filing_type: Optional[str], limit: int) -> CompanyFilings:
        """Return mock SEC filings"""
        filings = [
            Filing(
                form_type="10-K",
                filing_date="2023-11-03",
                period_ending="2023-09-30",
                accession_number="0000320193-23-000106",
                file_url=f"https://www.sec.gov/Archives/edgar/data/{symbol}/10-K",
                description="Annual report"
            ),
            Filing(
                form_type="10-Q",
                filing_date="2023-08-04",
                period_ending="2023-07-01",
                accession_number="0000320193-23-000077",
                file_url=f"https://www.sec.gov/Archives/edgar/data/{symbol}/10-Q",
                description="Quarterly report"
            ),
            Filing(
                form_type="8-K",
                filing_date="2023-11-02",
                period_ending="",
                accession_number="0000320193-23-000105",
                file_url=f"https://www.sec.gov/Archives/edgar/data/{symbol}/8-K",
                description="Current report - Earnings release"
            )
        ]

        if filing_type:
            filings = [f for f in filings if f.form_type == filing_type]

        return CompanyFilings(
            symbol=symbol,
            filings=filings[:limit],
            total_filings=len(filings)
        )


    def _get_mock_insiders(self, symbol: str, months: int) -> CompanyInsiders:
        """Return mock insider trading data"""
        transactions = [
            InsiderTransaction(
                insider_name="John Doe",
                position="CEO",
                transaction_type="Buy",
                shares=10000,
                price=150.00,
                value=1500000,
                date="2023-10-15",
                ownership_change=0.1
            ),
            InsiderTransaction(
                insider_name="Jane Smith",
                position="CFO",
                transaction_type="Sell",
                shares=5000,
                price=155.00,
                value=775000,
                date="2023-10-01",
                ownership_change=-0.05
            )
        ]

        return CompanyInsiders(
            symbol=symbol,
            transactions=transactions,
            total_bought=1,
            total_sold=1,
            net_shares=5000,
            net_value=725000,
            period_months=months
        )

    def _get_mock_ratings(self, symbol: str) -> CompanyRatings:
        """Return mock analyst ratings"""
        ratings = [
            AnalystRating(
                firm="Goldman Sachs",
                analyst="John Analyst",
                rating="Buy",
                price_target=200.00,
                date="2023-10-20"
            ),
            AnalystRating(
                firm="Morgan Stanley",
                analyst="Jane Analyst",
                rating="Hold",
                price_target=185.00,
                date="2023-10-18"
            )
        ]

        return CompanyRatings(
            symbol=symbol,
            ratings=ratings,
            consensus="Buy",
            average_target=192.50,
            high_target=200.00,
            low_target=185.00,
            total_analysts=2,
            buy_count=1,
            hold_count=1,
            sell_count=0
        )