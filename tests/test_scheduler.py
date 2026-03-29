import unittest
import time
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from printer_scheduler import PrinterScheduler


class TestPrinterScheduler(unittest.TestCase):
    def setUp(self):
        self.scheduler = PrinterScheduler()

    def test_add_job(self):
        job = self.scheduler.add_job("Report.pdf", "Alice", "High", 10)
        self.assertEqual(job.job_id, 1)
        self.assertEqual(job.document_name, "Report.pdf")
        self.assertEqual(self.scheduler.queue.size(), 1)

    def test_add_multiple_jobs_increments_id(self):
        j1 = self.scheduler.add_job("a.pdf", "U1", "High", 1)
        j2 = self.scheduler.add_job("b.pdf", "U2", "Low", 2)
        j3 = self.scheduler.add_job("c.pdf", "U3", "Medium", 3)
        self.assertEqual(j1.job_id, 1)
        self.assertEqual(j2.job_id, 2)
        self.assertEqual(j3.job_id, 3)

    def test_print_next_priority_order(self):
        self.scheduler.add_job("low.pdf", "U", "Low", 1)
        time.sleep(0.01)
        self.scheduler.add_job("high.pdf", "U", "High", 1)
        time.sleep(0.01)
        self.scheduler.add_job("med.pdf", "U", "Medium", 1)

        job = self.scheduler.print_next()
        self.assertEqual(job.document_name, "high.pdf")
        self.assertEqual(job.status, "Completed")

    def test_print_next_empty_queue(self):
        result = self.scheduler.print_next()
        self.assertIsNone(result)

    def test_cancel_job(self):
        self.scheduler.add_job("a.pdf", "U", "High", 1)
        j2 = self.scheduler.add_job("b.pdf", "U", "Low", 1)

        cancelled = self.scheduler.cancel_job(j2.job_id)
        self.assertIsNotNone(cancelled)
        self.assertEqual(cancelled.status, "Cancelled")
        self.assertEqual(self.scheduler.queue.size(), 1)

    def test_cancel_nonexistent(self):
        self.scheduler.add_job("a.pdf", "U", "High", 1)
        result = self.scheduler.cancel_job(999)
        self.assertIsNone(result)

    def test_view_queue(self):
        self.scheduler.add_job("a.pdf", "U", "Low", 1)
        time.sleep(0.01)
        self.scheduler.add_job("b.pdf", "U", "High", 2)

        jobs = self.scheduler.view_queue()
        self.assertEqual(len(jobs), 2)
        self.assertEqual(jobs[0].document_name, "b.pdf")

    def test_view_completed(self):
        self.scheduler.add_job("a.pdf", "U", "High", 1)
        self.scheduler.print_next()
        completed = self.scheduler.view_completed()
        self.assertEqual(len(completed), 1)
        self.assertEqual(completed[0].status, "Completed")

    def test_get_status(self):
        self.scheduler.add_job("a.pdf", "U", "High", 1)
        status = self.scheduler.get_status()
        self.assertEqual(status["queue_size"], 1)
        self.assertEqual(status["completed_count"], 0)
        self.assertIsNone(status["current_job"])
        self.assertIsNotNone(status["next_job"])


if __name__ == "__main__":
    unittest.main()
