from stack           import Stack
from emergency_level import EmergencyLevel
from queue_events    import Event, EventQueue

EMERGENCIES = {
    "Panic":       EmergencyLevel("Panic",       "Heart rate critical  — injecting sedative"),
    "Overheating": EmergencyLevel("Overheating", "Temp too high        — cooling system on"),
    "LowEnergy":   EmergencyLevel("LowEnergy",   "Energy critical      — redirecting power"),
}

EVENTS = [
    Event("Calm zone",            "No interference detected",        0,   0,  0),
    Event("Solar flare",          "Radiation spike hits the suit",  -10,  +8, +3),
    Event("Micrometeorite",       "Impact on suit exterior",        -8,  +12, +2),
    Event("Calm zone",            "No interference detected",        0,   0,  0),
    Event("Oxygen leak",          "Minor seal breach detected",     -15,  +5, +1),
    Event("Calm zone",            "No interference detected",        0,   0,  0),
    Event("Temperature anomaly",  "External temp spike",            -5,   0,  +5),
    Event("Final approach",       "Solar panel in sight",            0,   0,  0),
]


class Suit:
    TOTAL_STEPS = len(EVENTS)

    def __init__(self):
        self.energy      = 100
        self.heart_rate  = 65
        self.temperature = 37
        self.step_count  = 0
        self._stack      = Stack()
        self._queue      = EventQueue(EVENTS)
        self._messages   = []
        self._active     = set()

    def take_step(self, action: str) -> None:
        self._messages = []
        self.step_count += 1

        self._apply_action(action)
        self._apply_event()
        self._check_emergencies()
        self._resolve_top()

    def _apply_action(self, action: str) -> None:
        if action == "1":
            self.energy      -= 10
            self.heart_rate  += 5
            self.temperature += 2
            self._messages.append("  > You advance through the void.")
        else:
            self.heart_rate  -= 5
            self.temperature -= 1
            self._messages.append("  > You stay calm and breathe slowly.")

    def _apply_event(self) -> None:
        event = self._queue.next()
        if event and (event.energy != 0 or event.heart_rate != 0 or event.temperature != 0):
            self.energy      += event.energy
            self.heart_rate  += event.heart_rate
            self.temperature += event.temperature
            self._messages.append(f"  🌍 Event: {event}")

    def _check_emergencies(self) -> None:
        if self.heart_rate  >= 85 and "Panic"       not in self._active:
            self._push("Panic")
        if self.temperature >= 40 and "Overheating" not in self._active:
            self._push("Overheating")
        if self.energy      <= 20 and "LowEnergy"   not in self._active:
            self._push("LowEnergy")

    def _push(self, name: str) -> None:
        self._stack.push(EMERGENCIES[name])
        self._active.add(name)
        self._messages.append(f"  ⚠  PUSH → {EMERGENCIES[name]}")

    def _resolve_top(self) -> None:
        if self._stack.is_empty():
            return
        top = self._stack.peek()
        still_critical = (
            (top.name == "Panic"       and self.heart_rate  >= 85) or
            (top.name == "Overheating" and self.temperature >= 40) or
            (top.name == "LowEnergy"   and self.energy      <= 20)
        )
        if not still_critical:
            resolved = self._stack.pop()
            self._active.discard(resolved.name)
            self._messages.append(f"  ✔  POP  → {resolved.name} resolved")

    def is_dead(self) -> bool:
        return self.energy <= 0

    def is_done(self) -> bool:
        return self.step_count >= self.TOTAL_STEPS

    def get_messages(self) -> list:
        return self._messages

    def stack_display(self) -> str:
        if self._stack.is_empty():
            return "empty"
        return "  |  ".join(e.name for e in self._stack.all_items())

    def queue_remaining(self) -> int:
        return self._queue.remaining()

    def vitals(self) -> str:
        e  = max(self.energy, 0)
        hr = self.heart_rate
        t  = self.temperature
        return (
            f"  Energy:     {e:<4}  {'▓' * (e // 10)}\n"
            f"  Heart Rate: {hr:<4}  {'▓' * min(hr // 10, 10)}\n"
            f"  Temp:       {t}°C"
        )
