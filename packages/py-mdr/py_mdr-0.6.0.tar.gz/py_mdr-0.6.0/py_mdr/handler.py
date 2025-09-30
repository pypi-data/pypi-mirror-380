import importlib.metadata
import os
import queue
import threading
from datetime import datetime, timezone
import logging

from py_mdr.client import MDRClient
from py_mdr.ocsf_models.events import SeverityID
from py_mdr.ocsf_models.events.system_activity.event_log_activity import EventLogActivity, LogTypeID
from py_mdr.ocsf_models.objects.actor import Actor
from py_mdr.ocsf_models.objects.enrichment import Enrichment
from py_mdr.ocsf_models.objects.file import File
from py_mdr.ocsf_models.objects.metadata import Metadata
from py_mdr.ocsf_models.objects.process import Process
from py_mdr.ocsf_models.objects.product import Product


class MDRHandler(logging.Handler):
    """
    Logger handler that can interact with the MDR service. The intention is that
    all logging information can be sent in the right format without hassle.
    """

    def __init__(self,
                 dataset_name: str,
                 namespace: str,
                 host: str = os.getenv("MDR_HOST", ""),
                 token: str = os.getenv("MDR_TOKEN", ""),
                 ssl_verify=True,
                 product: Product = Product(name="py-mdr", vendor_name="SBP"),
                 flush_interval: int = 1
                ):
        """
        Create main MDR handler
        :param dataset_name: Name of the dataset to use when storing data
        :param namespace: Namespace to use when storing data
        :param host: Host to where to send the log information with port (e.g. host.name.com:8088)
        :param token: Splunk token for authentication
        :param ssl_verify: Enable or disable SSL verification
        :param product: Additional product information to send with the log
        """
        super().__init__()
        self.client = MDRClient(
            dataset_name=dataset_name,
            namespace=namespace,
            host=host,
            token=token,
            ssl_verify=ssl_verify
        )
        self.product = product
        self.queue = queue.Queue()
        self._stop_event = threading.Event()
        self.flush_interval = flush_interval
        self.worker = threading.Thread(target=self._process_queue, daemon=True)
        self.worker.start()

    def emit(self, record):
        try:
            data = self.map_log_record(record)
            self.queue.put_nowait(data)
        except Exception:
            self.handleError(record)

    def _process_queue(self):
        while not self._stop_event.is_set():
            try:
                log_entry = self.queue.get(timeout=self.flush_interval)
                self.client.send(log_entry)
            except queue.Empty:
                continue
            except Exception as e:
                # optional: retry logic or logging
                print("Failed to send log:", e)

    def close(self):
        self._stop_event.set()
        self.worker.join()
        super().close()

    def get_client(self):
        """
        Returns the client being used by the handler.
        :return:
        """
        return self.client

    @classmethod
    def _convert_severity(cls, log_severity: int) -> SeverityID:
        """
        Convert a python logging severity to OCSF SeverityID
        :param log_severity:
        :return:
        """
        if log_severity == logging.DEBUG:
            return SeverityID.Other
        elif log_severity == logging.INFO:
            return SeverityID.Informational
        elif log_severity == logging.WARNING:
            return SeverityID.Medium
        elif log_severity == logging.ERROR:
            return SeverityID.High
        elif log_severity == logging.FATAL:
            return SeverityID.Fatal
        elif log_severity == logging.CRITICAL:
            return SeverityID.Critical
        else:
            return SeverityID.Unknown

    def map_log_record(self, record: logging.LogRecord) -> EventLogActivity:
        metadata = Metadata(
            log_level=record.levelname,
            log_provider=__name__,
            log_version=importlib.metadata.version("py_mdr"),
            logged_time=datetime.now(timezone.utc),
            product=self.product,
        )

        enrichments = [
            Enrichment(name="file_information", data={
                "line_number": record.lineno,
                "module": record.module,
                "function_name": record.funcName
            })
        ]

        process = Process(
            name=record.processName,
            pid=record.process,
        )

        severity = MDRHandler._convert_severity(record.levelno)
        event = EventLogActivity(
            time=datetime.fromtimestamp(record.created),
            file=File(name=record.filename),
            log_name=record.name,
            log_provider=__name__,
            log_type_id=LogTypeID.Application,
            log_type=LogTypeID.Application.name,
            message=record.msg,
            metadata=metadata,
            raw_data=str(record),
            severity=severity.name,
            severity_id=severity,
            enrichments=enrichments,
            actor=Actor(process=process)
        )

        return event
