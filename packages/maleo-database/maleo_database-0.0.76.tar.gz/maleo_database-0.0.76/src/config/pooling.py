from pydantic import BaseModel, ConfigDict, Field, model_validator
from typing import Annotated, Self, Set, TypeVar
from maleo.types.dict import OptionalStringToStringDict, StringToAnyDict
from maleo.types.integer import ListOfIntegers
from maleo.types.string import OptionalString
from maleo.utils.formatters.case import to_camel
from ..enums import PoolingStrategy


class BasePoolingConfig(BaseModel):
    """Base configuration class for database connection pooling."""


PoolingConfigT = TypeVar("PoolingConfigT", bound=BasePoolingConfig)


class MySQLPoolingConfig(BasePoolingConfig):
    """MySQL-specific pooling configuration."""

    pool_size: Annotated[
        int, Field(8, description="Number of connections in the pool", ge=1, le=500)
    ] = 8
    max_overflow: Annotated[
        int,
        Field(15, description="Maximum number of overflow connections", ge=0, le=200),
    ] = 15
    pool_timeout: Annotated[
        float,
        Field(
            20.0,
            description="Timeout in seconds for getting connection",
            ge=1.0,
            le=300.0,
        ),
    ] = 20.0
    pool_recycle: Annotated[
        int,
        Field(7200, description="Connection recycle time in seconds", ge=60, le=86400),
    ] = 7200
    pool_pre_ping: Annotated[
        bool, Field(True, description="Validate connections before use")
    ] = True
    strategy: Annotated[
        PoolingStrategy, Field(PoolingStrategy.FIXED, description="Pooling strategy")
    ] = PoolingStrategy.FIXED
    # Add autocommit to pooling since it affects connection behavior in the pool
    autocommit: Annotated[bool, Field(False, description="Enable autocommit mode")] = (
        False
    )
    # Move connect_timeout here since it's about pool connection establishment
    connect_timeout: Annotated[
        float, Field(10.0, description="Connection timeout in seconds", ge=1.0, le=60.0)
    ] = 10.0

    @property
    def engine_kwargs_exclusions(self) -> Set[str]:
        return {"strategy"}

    @property
    def engine_kwargs(self) -> StringToAnyDict:
        return self.model_dump(exclude=self.engine_kwargs_exclusions, exclude_none=True)


class PostgreSQLPoolingConfig(BasePoolingConfig):
    """PostgreSQL-specific pooling configuration."""

    pool_size: Annotated[
        int, Field(10, description="Number of connections in the pool", ge=1, le=1000)
    ] = 10
    max_overflow: Annotated[
        int,
        Field(20, description="Maximum number of overflow connections", ge=0, le=500),
    ] = 20
    pool_timeout: Annotated[
        float,
        Field(
            30.0,
            description="Timeout in seconds for getting connection",
            ge=1.0,
            le=300.0,
        ),
    ] = 30.0
    pool_recycle: Annotated[
        int,
        Field(3600, description="Connection recycle time in seconds", ge=60, le=86400),
    ] = 3600
    pool_pre_ping: Annotated[
        bool, Field(True, description="Validate connections before use")
    ] = True
    # Keep strategy and prepared_statement_cache_size as they're pooling-related
    strategy: Annotated[
        PoolingStrategy, Field(PoolingStrategy.DYNAMIC, description="Pooling strategy")
    ] = PoolingStrategy.DYNAMIC
    prepared_statement_cache_size: Annotated[
        int, Field(100, description="Prepared statement cache size", ge=0, le=10000)
    ] = 100
    pool_reset_on_return: Annotated[
        bool, Field(True, description="Reset connection state on return to pool")
    ] = True

    @model_validator(mode="after")
    def validate_overflow(self) -> Self:
        if self.max_overflow > self.pool_size * 5:
            raise ValueError("max_overflow should not exceed 5x pool_size")
        return self

    @property
    def engine_kwargs_exclusions(self) -> Set[str]:
        return {
            "strategy",
            "prepared_statement_cache_size",
            "pool_reset_on_return",
        }

    @property
    def engine_kwargs(self) -> StringToAnyDict:
        return self.model_dump(exclude=self.engine_kwargs_exclusions, exclude_none=True)


class SQLitePoolingConfig(BasePoolingConfig):
    """SQLite-specific pooling configuration."""

    pool_size: Annotated[
        int,
        Field(1, description="Number of connections (limited for SQLite)", ge=1, le=10),
    ] = 1
    max_overflow: Annotated[
        int, Field(5, description="Maximum overflow connections", ge=0, le=20)
    ] = 5
    pool_timeout: Annotated[
        float, Field(30.0, description="Timeout in seconds", ge=1.0, le=300.0)
    ] = 30.0
    # SQLite-specific pooling options
    wal_mode: Annotated[
        bool, Field(True, description="Enable WAL mode for better concurrency")
    ] = True
    busy_timeout: Annotated[
        int,
        Field(30000, description="Busy timeout in milliseconds", ge=1000, le=300000),
    ]

    @property
    def engine_kwargs_exclusions(self) -> Set[str]:
        return {
            "strategy",
            "wal_mode",
            "busy_timeout",
        }

    @property
    def engine_kwargs(self) -> StringToAnyDict:
        return self.model_dump(exclude=self.engine_kwargs_exclusions, exclude_none=True)


class SQLServerPoolingConfig(BasePoolingConfig):
    """SQL Server-specific pooling configuration."""

    pool_size: Annotated[
        int, Field(10, description="Number of connections in the pool", ge=1, le=500)
    ]
    max_overflow: Annotated[
        int,
        Field(20, description="Maximum number of overflow connections", ge=0, le=200),
    ] = 20
    pool_timeout: Annotated[
        float,
        Field(
            30.0,
            description="Timeout in seconds for getting connection",
            ge=1.0,
            le=300.0,
        ),
    ] = 30.0
    pool_recycle: Annotated[
        int,
        Field(3600, ge=60, le=86400, description="Connection recycle time in seconds"),
    ] = 3600
    pool_pre_ping: Annotated[
        bool, Field(True, description="Validate connections before use")
    ] = True
    strategy: Annotated[
        PoolingStrategy, Field(PoolingStrategy.DYNAMIC, description="Pooling strategy")
    ] = PoolingStrategy.DYNAMIC
    # SQL Server-specific pooling settings
    connection_timeout: Annotated[
        int, Field(30, description="Connection timeout in seconds", ge=1, le=300)
    ] = 30
    command_timeout: Annotated[
        int, Field(30, description="Command timeout in seconds", ge=1, le=3600)
    ]
    packet_size: Annotated[
        int, Field(4096, description="Network packet size", ge=512, le=32767)
    ] = 4096
    trust_server_certificate: Annotated[
        bool, Field(False, description="Trust server certificate")
    ] = False
    # Move encrypt here since it affects connection pool behavior
    encrypt: Annotated[bool, Field(True, description="Encrypt connection")] = True

    @model_validator(mode="after")
    def validate_overflow(self) -> Self:
        if self.max_overflow > self.pool_size * 3:
            raise ValueError("max_overflow should not exceed 3x pool_size")
        return self

    @property
    def engine_kwargs_exclusions(self) -> Set[str]:
        return {
            "connection_timeout",
            "command_timeout",
            "packet_size",
            "trust_server_certificate",
        }

    @property
    def engine_kwargs(self) -> StringToAnyDict:
        return self.model_dump(exclude=self.engine_kwargs_exclusions, exclude_none=True)


class ElasticsearchPoolingConfig(BasePoolingConfig):
    """Elasticsearch-specific pooling configuration."""

    # Connection pool settings
    maxsize: Annotated[
        int,
        Field(25, description="Maximum number of connections in pool", ge=1, le=100),
    ]
    connections_per_node: Annotated[
        int, Field(10, description="Connections per Elasticsearch node", ge=1, le=50)
    ]

    # Timeout settings
    timeout: Annotated[
        float, Field(10.0, description="Request timeout in seconds", ge=1.0, le=300.0)
    ]
    max_retries: Annotated[
        int, Field(3, description="Maximum number of retries", ge=0, le=10)
    ]
    retry_on_timeout: Annotated[bool, Field(False, description="Retry on timeout")] = (
        False
    )
    retry_on_status: Annotated[
        ListOfIntegers,
        Field(
            [502, 503, 504],
            description="HTTP status codes to retry on",
        ),
    ] = [502, 503, 504]

    # Connection behavior (move from connection config)
    http_compress: Annotated[
        bool, Field(True, description="Enable HTTP compression")
    ] = True
    verify_certs: Annotated[
        bool, Field(True, description="Verify SSL certificates")
    ] = True
    ca_certs: Annotated[
        OptionalString, Field(None, description="Path to CA certificates")
    ] = None

    # Advanced pool settings
    block: Annotated[bool, Field(False, description="Block when pool is full")] = False
    headers: Annotated[
        OptionalStringToStringDict,
        Field(None, description="Default headers for requests"),
    ] = None
    dead_timeout: Annotated[
        float, Field(60.0, description="Dead node timeout in seconds", ge=5.0, le=600.0)
    ] = 60.0

    @model_validator(mode="after")
    def validate_overflow(self) -> Self:
        if self.connections_per_node > self.maxsize:
            raise ValueError("connections_per_node must not exceed maxsize")
        return self

    @property
    def client_kwargs_exclusions(self) -> Set[str]:
        return {
            "connections_per_node",
            "block",
            "headers",
            "dead_timeout",
        }

    @property
    def client_kwargs(self) -> StringToAnyDict:
        return self.model_dump(exclude=self.client_kwargs_exclusions, exclude_none=True)


class MongoPoolingConfig(BasePoolingConfig):
    """Mongo-specific pooling configuration."""

    model_config = ConfigDict(alias_generator=to_camel)

    max_pool_size: Annotated[
        int,
        Field(
            100,
            alias="maxPoolSiza",
            description="Maximum number of connections in pool",
            ge=1,
            le=500,
        ),
    ] = 100
    min_pool_size: Annotated[
        int,
        Field(
            0,
            alias="minPoolSize",
            description="Minimum number of connections in pool",
            ge=0,
            le=100,
        ),
    ] = 0
    max_idle_time_ms: Annotated[
        int,
        Field(
            600000,
            alias="maxIdleTimeMS",
            description="Max idle time in milliseconds",
            ge=1000,
            le=3600000,
        ),
    ] = 600000
    connect_timeout_ms: Annotated[
        int,
        Field(
            20000,
            alias="connectTimeoutMS",
            description="Connection timeout in milliseconds",
            ge=1000,
            le=300000,
        ),
    ] = 20000
    server_selection_timeout_ms: Annotated[
        int,
        Field(
            30000,
            alias="serverSelectionTimeoutMS",
            description="Server selection timeout",
            ge=1000,
            le=300000,
        ),
    ] = 30000
    max_connecting: Annotated[
        int,
        Field(
            2,
            alias="maxConnecting",
            description="Maximum number of concurrent connection attempts",
            ge=1,
            le=10,
        ),
    ] = 2

    @property
    def client_kwargs(self) -> StringToAnyDict:
        return self.model_dump(by_alias=True, exclude_none=True)


class RedisPoolingConfig(BasePoolingConfig):
    """Redis-specific pooling configuration."""

    max_connections: Annotated[
        int,
        Field(50, description="Maximum number of connections in pool", ge=1, le=1000),
    ] = 50
    retry_on_timeout: Annotated[
        bool, Field(True, description="Retry on connection timeout")
    ] = True
    health_check_interval: Annotated[
        int, Field(30, description="Health check interval in seconds", ge=5, le=300)
    ] = 30
    connection_timeout: Annotated[
        float, Field(5.0, description="Connection timeout in seconds", ge=1.0, le=60.0)
    ] = 5.0
    socket_timeout: Annotated[
        float, Field(5.0, description="Socket timeout in seconds", ge=1.0, le=60.0)
    ] = 5.0
    socket_keepalive: Annotated[
        bool, Field(True, description="Enable TCP keepalive")
    ] = True
    decode_responses: Annotated[
        bool, Field(True, description="Decode responses to strings")
    ] = True

    @property
    def client_kwargs_exclusions(self) -> Set[str]:
        return {"health_check_interval", "connection_timeout"}

    @property
    def client_kwargs(self) -> StringToAnyDict:
        return self.model_dump(exclude=self.client_kwargs_exclusions, exclude_none=True)
