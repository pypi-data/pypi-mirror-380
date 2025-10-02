"""Feature Engineering Module for Stock Recommendation Models"""

from .stock_features import (
    StockRecommendationFeatures,
    TechnicalIndicatorFeatures,
    MarketRegimeFeatures,
    CrossAssetFeatures,
)
from .political_features import (
    PoliticalInfluenceFeatures,
    CongressionalTrackingFeatures,
    PolicyImpactFeatures,
)
from .ensemble_features import (
    EnsembleFeatureBuilder,
    FeatureInteractionEngine,
    DynamicFeatureSelector,
)
from .recommendation_engine import (
    StockRecommendationEngine,
    RecommendationConfig,
    RecommendationResult,
)

__all__ = [
    "StockRecommendationFeatures",
    "TechnicalIndicatorFeatures",
    "MarketRegimeFeatures",
    "CrossAssetFeatures",
    "PoliticalInfluenceFeatures",
    "CongressionalTrackingFeatures",
    "PolicyImpactFeatures",
    "EnsembleFeatureBuilder",
    "FeatureInteractionEngine",
    "DynamicFeatureSelector",
    "StockRecommendationEngine",
    "RecommendationConfig",
    "RecommendationResult",
]
