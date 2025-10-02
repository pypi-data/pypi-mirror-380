"""API routers"""

from . import (
    auth_router,
    model_router,
    prediction_router,
    portfolio_router,
    data_router,
    trade_router,
    backtest_router,
    monitoring_router,
    admin_router,
    websocket_router,
)

__all__ = [
    "auth_router",
    "model_router",
    "prediction_router",
    "portfolio_router",
    "data_router",
    "trade_router",
    "backtest_router",
    "monitoring_router",
    "admin_router",
    "websocket_router",
]