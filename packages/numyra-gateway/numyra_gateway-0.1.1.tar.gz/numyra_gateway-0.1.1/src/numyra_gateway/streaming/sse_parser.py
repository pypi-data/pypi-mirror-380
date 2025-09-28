from dataclasses import dataclass
from typing import List, Optional


@dataclass
class SSEEvent:
    event: Optional[str] = None
    data: Optional[str] = None
    id: Optional[str] = None
    retry: Optional[int] = None


class SSEParser:
    def __init__(self):
        self.buffer = ""

    def feed(self, chunk: str) -> List[SSEEvent]:
        self.buffer += chunk
        events = []

        while "\n\n" in self.buffer:
            event_text, self.buffer = self.buffer.split("\n\n", 1)
            event = self._parse_event(event_text)
            if event:
                events.append(event)

        return events

    def _parse_event(self, event_text: str) -> Optional[SSEEvent]:
        if not event_text.strip():
            return None

        event = SSEEvent()
        data_lines = []

        for line in event_text.split("\n"):
            line = line.strip()
            if not line or line.startswith(":"):
                continue

            if ":" in line:
                field, value = line.split(":", 1)
                field = field.strip()
                value = value.strip()

                if field == "event":
                    event.event = value
                elif field == "data":
                    data_lines.append(value)
                elif field == "id":
                    event.id = value
                elif field == "retry":
                    event.retry = int(value)
            else:
                data_lines.append("")

        if data_lines:
            event.data = "\n".join(data_lines)

        return event