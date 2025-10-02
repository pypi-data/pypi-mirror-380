"""Backtesting framework for trading strategies"""

from .backtest_engine import (
    BacktestEngine,
    BacktestConfig,
    BacktestResult,
    TradingStrategy,
    PositionManager,
)

from .performance_metrics import (
    PerformanceAnalyzer,
    PortfolioMetrics,
    RiskMetrics,
    plot_performance,
)

from .trading_simulator import (
    TradingSimulator,
    Order,
    Position,
    Portfolio,
    MarketSimulator,
)

__all__ = [
    "BacktestEngine",
    "BacktestConfig",
    "BacktestResult",
    "TradingStrategy",
    "PositionManager",
    "PerformanceAnalyzer",
    "PortfolioMetrics",
    "RiskMetrics",
    "plot_performance",
    "TradingSimulator",
    "Order",
    "Position",
    "Portfolio",
    "MarketSimulator",
]