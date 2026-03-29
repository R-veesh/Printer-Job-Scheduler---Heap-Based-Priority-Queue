import time

from print_job import PrintJob, PRIORITY_MAP
from max_heap import MaxHeap


class PrinterScheduler:
    def __init__(self):
        self.queue = MaxHeap()
        self.job_counter = 0
        self.completed_jobs = []
        self.current_job = None

    def add_job(self, document_name, user_name, priority, pages):
        self.job_counter += 1
        job = PrintJob(self.job_counter, document_name, user_name, priority, pages)
        self.queue.insert(job)
        return job

    def print_next(self):
        if self.queue.is_empty():
            return None

        job = self.queue.extract_max()
        job.status = "Printing"
        self.current_job = job

        print(f"\n  Printing Job #{job.job_id}: {job.document_name}")
        print(f"  User: {job.user_name} | Priority: {job.priority} | Pages: {job.pages}")
        print("  Progress: ", end="", flush=True)

        for i in range(job.pages):
            time.sleep(0.15)
            print("█", end="", flush=True)
        print(" Done!")

        job.status = "Completed"
        self.completed_jobs.append(job)
        self.current_job = None
        return job

    def cancel_job(self, job_id):
        removed = self.queue.remove(job_id)
        if removed is None:
            return None
        removed.status = "Cancelled"
        self.completed_jobs.append(removed)
        return removed

    def view_queue(self):
        return self.queue.get_sorted_jobs()

    def view_completed(self):
        return list(self.completed_jobs)

    def get_status(self):
        return {
            "current_job": self.current_job,
            "queue_size": self.queue.size(),
            "completed_count": len(self.completed_jobs),
            "next_job": self.queue.peek(),
        }
