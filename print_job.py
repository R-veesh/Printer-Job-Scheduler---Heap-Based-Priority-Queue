from datetime import datetime


PRIORITY_MAP = {
    "high": 3,
    "medium": 2,
    "low": 1,
}


class PrintJob:
    def __init__(self, job_id, document_name, user_name, priority, pages):
        self.job_id = job_id
        self.document_name = document_name
        self.user_name = user_name
        self.priority = priority.capitalize()
        self.priority_value = PRIORITY_MAP[priority.lower()]
        self.pages = pages
        self.timestamp = datetime.now()
        self.status = "Waiting"

    def __repr__(self):
        return (
            f"Job #{self.job_id} | {self.document_name} | "
            f"User: {self.user_name} | Priority: {self.priority} | "
            f"Pages: {self.pages} | Status: {self.status}"
        )
