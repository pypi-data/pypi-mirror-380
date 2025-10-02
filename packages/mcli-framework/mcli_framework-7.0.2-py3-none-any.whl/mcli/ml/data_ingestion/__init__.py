"""Real-time data ingestion pipeline"""

from .stream_processor import (
    StreamProcessor,
    DataStream,
    KafkaConsumer,
    WebSocketConsumer,
)

from .api_connectors import (
    CongressionalDataAPI,
    StockMarketAPI,
    AlphaVantageConnector,
    YahooFinanceConnector,
    PolygonIOConnector,
    QuiverQuantConnector,
)

from .data_pipeline import (
    IngestionPipeline,
    DataValidator,
    DataTransformer,
    DataLoader,
)

__all__ = [
    "StreamProcessor",
    "DataStream",
    "KafkaConsumer",
    "WebSocketConsumer",
    "CongressionalDataAPI",
    "StockMarketAPI",
    "AlphaVantageConnector",
    "YahooFinanceConnector",
    "PolygonIOConnector",
    "QuiverQuantConnector",
    "IngestionPipeline",
    "DataValidator",
    "DataTransformer",
    "DataLoader",
]