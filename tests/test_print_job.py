import unittest
import time
from print_job import PrintJob, PRIORITY_MAP


class TestPrintJob(unittest.TestCase):
    def test_creation(self):
        job = PrintJob(1, "Report.pdf", "Alice", "High", 10)
        self.assertEqual(job.job_id, 1)
        self.assertEqual(job.document_name, "Report.pdf")
        self.assertEqual(job.user_name, "Alice")
        self.assertEqual(job.priority, "High")
        self.assertEqual(job.priority_value, 3)
        self.assertEqual(job.pages, 10)
        self.assertEqual(job.status, "Waiting")

    def test_priority_values(self):
        high = PrintJob(1, "a.pdf", "U", "high", 1)
        med = PrintJob(2, "b.pdf", "U", "Medium", 1)
        low = PrintJob(3, "c.pdf", "U", "LOW", 1)
        self.assertEqual(high.priority_value, 3)
        self.assertEqual(med.priority_value, 2)
        self.assertEqual(low.priority_value, 1)

    def test_priority_capitalize(self):
        job = PrintJob(1, "a.pdf", "U", "medium", 1)
        self.assertEqual(job.priority, "Medium")

    def test_repr(self):
        job = PrintJob(1, "Report.pdf", "Alice", "High", 10)
        text = repr(job)
        self.assertIn("Job #1", text)
        self.assertIn("Report.pdf", text)
        self.assertIn("Alice", text)


if __name__ == "__main__":
    unittest.main()
