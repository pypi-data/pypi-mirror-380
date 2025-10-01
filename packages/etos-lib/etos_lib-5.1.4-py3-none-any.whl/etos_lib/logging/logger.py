# Copyright Axis Communications AB.
#
# For a full list of individual contributors, please see the commit history.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""ETOS logger.

Example::

    import logging
    from uuid import uuid4
    from etos_lib.logging.logger import setup_logging, FORMAT_CONFIG

    FORMAT_CONFIG.identifier = str(uuid4())
    setup_logging("myApp", "1.0.0", "production")
    logger = logging.getLogger(__name__)
    logger.info("Hello!")
    >>> [2020-12-16 10:35:00][cb7c8cd9-40a6-4ecc-8321-a1eae6beae35] INFO: Hello!

"""

import atexit
import logging
import logging.config
import sys
import threading
from pathlib import Path

from opentelemetry.exporter.otlp.proto.grpc._log_exporter import OTLPLogExporter
from opentelemetry.instrumentation.logging import LoggingInstrumentor
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from opentelemetry.sdk.resources import Resource
from yaml import SafeLoader, load

from etos_lib.lib.config import Config
from etos_lib.lib.debug import Debug
from etos_lib.logging.filter import EtosFilter
from etos_lib.logging.formatter import EtosLogFormatter
from etos_lib.logging.log_processors import ToStringProcessor
from etos_lib.logging.log_publisher import RabbitMQLogPublisher
from etos_lib.logging.rabbitmq_handler import RabbitMQHandler

DEFAULT_CONFIG = Path(__file__).parent.joinpath("default_config.yaml")
DEFAULT_LOG_PATH = Debug().default_log_path

FORMAT_CONFIG = threading.local()


def setup_file_logging(config: dict, log_filter: EtosFilter) -> None:
    """Set up logging to file using the ETOS log formatter.

    Cofiguration file parameters ('file' must exist or no file handler is set up):

        logging:
          file:
            # Log level for file logging. Default=DEBUG.
            loglevel: INFO
            # Where to store logfile. Default=/home/you/etos/output.log.json
            logfile: path/to/log/file
            # Maximum number of files to rotate. Default=10
            max_files: 5
            # Maximum number of bytes in each logfile. Default=1048576/1MB
            max_bytes: 100

    :param config: File logging configuration.
    :type config: dict
    :param log_filter: Logfilter to add to file handler.
    :type log_filter: :obj:`EtosFilter`
    """
    loglevel = getattr(logging, config.get("loglevel", "DEBUG"))
    logfile = Path(config.get("logfile", DEFAULT_LOG_PATH))
    logfile.parent.mkdir(parents=True, exist_ok=True)

    max_files = config.get("max_files", 10)
    max_bytes = config.get("max_bytes", 10485760)  # Default is 10 MB
    root_logger = logging.getLogger()

    file_handler = logging.handlers.RotatingFileHandler(
        logfile,
        maxBytes=max_bytes,
        backupCount=max_files,
    )
    file_handler.setFormatter(EtosLogFormatter())
    file_handler.setLevel(loglevel)
    file_handler.addFilter(log_filter)
    root_logger.addHandler(file_handler)


def setup_stream_logging(config: dict, log_filter: EtosFilter) -> None:
    """Set up logging to stdout stream.

    Cofiguration file parameters ('stream' must exist or no stream handler is set up):

        logging:
          stream:
            # Log level for stream logging. Default=INFO.
            loglevel: ERROR
            # Format to print logs with.
            # Default: [%(asctime)s][%(identifier)s] %(levelname)s:%(name)s: %(message)s
            logformat: %(message)s
            # Dateformat for %(asctime) format. Default: %Y-%m-%d %H:%M:%S
            dateformat: %Y-%d-%m %H:%M:%S

    :param config: Stream logging configuration.
    :type config: dict
    :param log_filter: Logfilter to add to stream handler.
    :type log_filter: :obj:`EtosFilter`
    """
    loglevel = getattr(logging, config.get("loglevel", "INFO"))

    logformat = config.get(
        "logformat",
        "[%(asctime)s][%(identifier)s] %(levelname)s:%(name)s: %(message)s",
    )
    dateformat = config.get("dateformat", "%Y-%m-%d %H:%M:%S")
    root_logger = logging.getLogger()
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(logging.Formatter(logformat, datefmt=dateformat))
    stream_handler.setLevel(loglevel)
    stream_handler.addFilter(log_filter)

    root_logger.addHandler(stream_handler)


def setup_rabbitmq_logging(log_filter: EtosFilter) -> None:
    """Set up rabbitmq logging.

    :param log_filter: Logfilter to add to stream handler.
    :type log_filter: :obj:`EtosFilter`
    """
    loglevel = logging.DEBUG

    root_logger = logging.getLogger()

    # These loggers need to be prevented from propagating their logs
    # to RabbitMQLogPublisher. If they aren't, this may cause a deadlock.
    logging.getLogger("pika").propagate = False
    logging.getLogger("eiffellib.publishers.rabbitmq_publisher").propagate = False
    logging.getLogger("etos_lib.eiffel.publisher").propagate = False
    logging.getLogger("base_rabbitmq").propagate = False

    rabbitmq = RabbitMQLogPublisher(**Config().etos_rabbitmq_publisher_data(), routing_key=None)
    if Debug().enable_sending_logs:
        rabbitmq.start()
        atexit.register(close_rabbit, rabbitmq)

    rabbit_handler = RabbitMQHandler(rabbitmq)
    rabbit_handler.setFormatter(EtosLogFormatter())
    rabbit_handler.setLevel(loglevel)
    rabbit_handler.addFilter(log_filter)

    root_logger.addHandler(rabbit_handler)


def setup_otel_logging(
    log_filter: EtosFilter,
    resource: Resource,
    log_level: int = logging.INFO,
) -> None:
    """Set up OpenTelemetry logging signals.

    :param log_filter: Logfilter to add to OpenTelemetry handler.
    :param resource: OpenTelemetry Resource to use when instrumenting logs
    :param log_level: Log level to set in the OpenTelemetry log handler
    """
    logger_provider = LoggerProvider(resource)
    logger_provider.add_log_record_processor(ToStringProcessor())
    logger_provider.add_log_record_processor(BatchLogRecordProcessor(OTLPLogExporter()))
    otel_log_handler = LoggingHandler(logger_provider=logger_provider)

    otel_log_handler.setFormatter(EtosLogFormatter())
    otel_log_handler.addFilter(log_filter)
    otel_log_handler.setLevel(log_level)

    logging.getLogger().addHandler(otel_log_handler)

    LoggingInstrumentor().instrument(set_logging_format=False)


def setup_logging(
    application: str,
    version: str,
    environment: str = None,  # pylint: disable=unused-argument # This is kept to maintain backward compatibility
    otel_resource: Resource = None,
    config_file: Path = DEFAULT_CONFIG,
) -> None:
    """Set up basic logging.

    :param application: Name of application to setup logging for.
    :type application: str
    :param version: Version of application to setup logging for.
    :type version: str
    :param environment: Environment in which this application resides.
    :type environment: str
    :param config_file: Filename of logging configuration.
    :type config_file: str
    """
    with open(config_file, encoding="utf-8") as yaml_file:
        config = load(yaml_file, Loader=SafeLoader)
    logging_config = config["logging"]

    log_filter = EtosFilter(application, version, FORMAT_CONFIG)

    # Create a default logger which will not propagate messages
    # to the root logger. This logger will create records for all
    # messages, but not print them to stdout. Stdout printing
    # is setup in "setup_stream_logging" if the "stream" key exists
    # in the configuration file.
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    root_logger.propagate = 0

    # The gql transport loggers are incredibly spammy so we need
    # to supress some of it so that our logs are actually useful.
    logging.getLogger("gql.transport.requests").setLevel(logging.WARNING)
    logging.getLogger("gql.transport.aiohttp").setLevel(logging.WARNING)

    if logging_config.get("stream"):
        setup_stream_logging(logging_config.get("stream"), log_filter)
    if logging_config.get("file"):
        setup_file_logging(logging_config.get("file"), log_filter)
    setup_rabbitmq_logging(log_filter)
    if otel_resource:
        setup_otel_logging(log_filter, otel_resource)


def close_rabbit(rabbit: RabbitMQLogPublisher) -> None:
    """Close down a rabbitmq connection."""
    rabbit.wait_for_unpublished_events()
    rabbit.close()
