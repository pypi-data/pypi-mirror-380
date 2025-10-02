"""API routes and endpoints for ML system"""

from .routers import (
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

from .app import create_app, get_application

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
    "create_app",
    "get_application",
]