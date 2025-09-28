from .RelayQueueCommand import RelayQueueCommand


class RelayQueue:
    _queue: list[RelayQueueCommand]

    def __init__(self):
        self._queue = []

    def add_command(self, relay_id: int, state: bool):
        command = RelayQueueCommand(relay_id, state)
        self._queue.append(command)
        return command

    def peek_next_command(self):
        if self._queue:
            return self._queue[0]
        else:
            return None

    def get_next_command(self):
        if self._queue:
            return self._queue.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self._queue) == 0

    def clear_queue(self):
        for command in self._queue:
            command.finished.set()
        self._queue = []
