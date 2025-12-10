from repository import LogRepository

class LogService:
    def __init__(self):
        self.repository = LogRepository()

    def register_log(self, event, details):
        self.repository.save_log(event, details)
        print(f"LOG REGISTRADO: {event} - {details}")