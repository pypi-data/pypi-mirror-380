# Someday Backlog


[ ] Company Research MCP - Post-Evaluation Improvements (B+ 89% → A- 95%)
Data Quality Enhancements
- Fix search_companies tool returning individual JSON objects instead of proper list format
- Expand SEC filings data coverage (currently limited to 1 filing for AAPL, should show comprehensive filing history)
- Complete insider trading transaction data (some transactions missing price/value fields, showing null values)
- Clean up analyst ratings data structure (remove duplicate consensus entries, fix inconsistent data format)
Edge Case & Validation Improvements
- Improve negative parameter handling (currently returns empty data for negative months, should return appropriate error)
- Add more comprehensive input validation for all parameters across tools
- Enhance error messages for better user guidance on parameter limits and formats
Performance & Usability Optimizations
- Optimize multi-company comparison performance for large dataset requests (10+ companies)
- Add data freshness indicators to show cache age and last update times
- Implement progressive data loading for large result sets with pagination support
Testing & Quality Assurance
- Add automated validation tests for data format consistency across all tools
- Implement data completeness checks before returning results to users
- Create comprehensive integration tests covering all edge cases identified in evaluation
Target: Upgrade Company Research MCP from Grade B+ (89%) to Grade A- (95%) for production excellence


[ ] Review this project. Create a CLI with commands and text UI to run it.

[ ] Review the project including .claude/ folder contents, include src/, ignore artifact/ folder. Create a python package called `navam-stockai` which will be distributed via PyPi. Research and add dependencies for package management and distribution considering the project uses `uv` already.

[ ] The frontend will have a streaming chat interface built on top of Claude Code SDK, dashboard showing agents and tools activity traces both current and historical for explainability purposes. Recommend minimal stack, packaging and deployment options