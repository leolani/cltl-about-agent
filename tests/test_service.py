import unittest
from queue import Queue, Empty
from unittest.mock import Mock

from emissor.representation.scenario import TextSignal

from cltl.combot.infra.event import Event
from cltl.combot.infra.event.memory import SynchronousEventBus
from cltl.combot.event.emissor import TextSignalEvent

from cltl.about.api import About
from cltl_service.about.service import AboutService


class AboutServiceTest(unittest.TestCase):
    def setUp(self) -> None:
        self.service = None

    def tearDown(self) -> None:
        if self.service:
            self.service.stop()

    def test_service_handled_event(self):
        about_mock = unittest.mock.MagicMock(About)
        about_mock.respond.side_effect = [f"response {i}" for i in range(10)]

        self.event_bus = SynchronousEventBus()
        self.service = AboutService("inputTopic", "responseTopic", None, about_mock, None, None, self.event_bus, None)

        events = Queue()

        def handler(ev):
            events.put(ev)

        self.event_bus.subscribe("responseTopic", handler)

        self.service.start()

        input_signal = TextSignal.for_scenario("scenario", 0, 1, None, "bla")
        self.event_bus.publish("inputTopic", Event.for_payload(TextSignalEvent.for_speaker(input_signal)))

        event = events.get(timeout=1)
        self.assertEqual("TextSignalEvent", event.payload.type)
        self.assertEqual("response 0", event.payload.signal.text)
        self.assertRaises(Empty, lambda: events.get(timeout=0.01))

    def test_service_unhandled_event_without_topic(self):
        about_mock = unittest.mock.MagicMock(About)
        about_mock.respond.side_effect = [None]

        self.event_bus = SynchronousEventBus()
        self.service = AboutService("inputTopic", "responseTopic", None, about_mock, None, None, self.event_bus, None)

        events = Queue()

        def handler(ev):
            events.put(ev)

        self.event_bus.subscribe("responseTopic", handler)

        self.service.start()

        input_signal = TextSignal.for_scenario("scenario", 0, 1, None, "bla")
        self.event_bus.publish("inputTopic", Event.for_payload(TextSignalEvent.for_speaker(input_signal)))

        self.assertRaises(Empty, lambda: events.get(timeout=0.01))

    def test_service_unhandled_event_with_topic(self):
        about_mock = unittest.mock.MagicMock(About)
        about_mock.respond.side_effect = [None]

        self.event_bus = SynchronousEventBus()
        self.service = AboutService("inputTopic", "responseTopic", "forwardTopic", about_mock, None, None,
                                    self.event_bus, None)

        response_events = Queue()
        forwarded_events = Queue()

        def response_handler(ev):
            response_events.put(ev)
        def forwarded_handler(ev):
            forwarded_events.put(ev)

        self.event_bus.subscribe("responseTopic", response_handler)
        self.event_bus.subscribe("forwardTopic", forwarded_handler)

        self.service.start()

        input_signal = TextSignal.for_scenario("scenario", 0, 1, None, "bla")
        self.event_bus.publish("inputTopic", Event.for_payload(TextSignalEvent.for_speaker(input_signal)))

        event = forwarded_events.get(timeout=1)
        self.assertEqual("TextSignalEvent", event.payload.type)
        self.assertEqual("bla", event.payload.signal.text)
        self.assertRaises(Empty, lambda: response_events.get(timeout=0.01))
