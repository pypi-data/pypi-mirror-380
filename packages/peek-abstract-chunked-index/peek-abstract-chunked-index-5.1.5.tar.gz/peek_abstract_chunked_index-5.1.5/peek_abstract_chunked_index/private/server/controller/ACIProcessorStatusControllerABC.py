import json
from abc import ABCMeta
from datetime import datetime, timezone
from pathlib import Path

from twisted.internet import reactor
from twisted.internet import task
from vortex.DeferUtil import deferToThreadWrapWithLogger
from vortex.TupleSelector import TupleSelector
from vortex.handler.TupleDataObservableHandler import TupleDataObservableHandler


class ACIProcessorStatusControllerABC(metaclass=ABCMeta):
    _StateTuple = None
    _logger = None

    NOTIFY_PERIOD = 2.0

    def __init__(self, metricsWriteDirectory: Path):
        self._metricsWriteDirectory = metricsWriteDirectory
        self.status = self._StateTuple()
        self._tupleObservable = None
        self._notifyPending = False
        self._lastNotifyDatetime = datetime.now(timezone.utc)

        self._metricsLoopingCall = task.LoopingCall(self._writeMetrics)
        self._metricsLoopingCall.start(30, now=True)

    def setTupleObservable(self, tupleObservable: TupleDataObservableHandler):
        self._tupleObservable = tupleObservable

    def shutdown(self):
        self._tupleObservable = None

        if self._metricsLoopingCall.running:
            self._metricsLoopingCall.stop()

    # ---------------
    # Search Object Processor Methods

    # ---------------
    # Notify Methods

    def notify(self):
        if self._notifyPending:
            return

        self._notifyPending = True

        deltaSeconds = (
            datetime.now(timezone.utc) - self._lastNotifyDatetime
        ).seconds
        if deltaSeconds >= self.NOTIFY_PERIOD:
            self._sendNotify()
        else:
            reactor.callLater(
                self.NOTIFY_PERIOD - deltaSeconds, self._sendNotify
            )

    def _sendNotify(self):
        if not self._tupleObservable:
            return
        self._notifyPending = False
        self._lastNotifyDatetime = datetime.now(timezone.utc)
        self._tupleObservable.notifyOfTupleUpdate(
            TupleSelector(self._StateTuple.tupleType(), {})
        )

    def _writeMetrics(self):
        wrappedFunction = deferToThreadWrapWithLogger(
            self._logger, consumeError=True
        )(self._writeMetricsWrapped)
        return wrappedFunction()

    def _writeMetricsWrapped(self):
        with open(self._metricsWriteDirectory / "compiler.json", "w") as f:
            f.write(
                json.dumps(
                    self.status.tupleToRestfulJsonDict(),
                    indent=4,
                    separators=(",", ": "),
                )
            )
