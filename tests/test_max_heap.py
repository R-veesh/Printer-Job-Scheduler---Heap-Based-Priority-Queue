import unittest
import time
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from print_job import PrintJob
from max_heap import MaxHeap


class TestMaxHeap(unittest.TestCase):
    def _make_job(self, job_id, priority, priority_value):
        job = PrintJob(job_id, f"doc{job_id}.pdf", "User", priority, 1)
        job.priority_value = priority_value
        return job

    def test_insert_and_peek(self):
        heap = MaxHeap()
        j1 = self._make_job(1, "Low", 1)
        j2 = self._make_job(2, "High", 3)
        heap.insert(j1)
        heap.insert(j2)
        self.assertEqual(heap.peek().job_id, 2)

    def test_extract_max_order(self):
        heap = MaxHeap()
        heap.insert(self._make_job(1, "Low", 1))
        time.sleep(0.01)
        heap.insert(self._make_job(2, "Medium", 2))
        time.sleep(0.01)
        heap.insert(self._make_job(3, "High", 3))

        self.assertEqual(heap.extract_max().job_id, 3)
        self.assertEqual(heap.extract_max().job_id, 2)
        self.assertEqual(heap.extract_max().job_id, 1)

    def test_extract_from_empty(self):
        heap = MaxHeap()
        self.assertIsNone(heap.extract_max())

    def test_peek_empty(self):
        heap = MaxHeap()
        self.assertIsNone(heap.peek())

    def test_size_and_is_empty(self):
        heap = MaxHeap()
        self.assertTrue(heap.is_empty())
        self.assertEqual(heap.size(), 0)
        heap.insert(self._make_job(1, "High", 3))
        self.assertFalse(heap.is_empty())
        self.assertEqual(heap.size(), 1)

    def test_remove_job(self):
        heap = MaxHeap()
        heap.insert(self._make_job(1, "High", 3))
        time.sleep(0.01)
        heap.insert(self._make_job(2, "Medium", 2))
        time.sleep(0.01)
        heap.insert(self._make_job(3, "Low", 1))

        removed = heap.remove(2)
        self.assertIsNotNone(removed)
        self.assertEqual(removed.job_id, 2)
        self.assertEqual(heap.size(), 2)

    def test_remove_nonexistent(self):
        heap = MaxHeap()
        heap.insert(self._make_job(1, "High", 3))
        self.assertIsNone(heap.remove(999))

    def test_tie_breaking_by_timestamp(self):
        heap = MaxHeap()
        j1 = self._make_job(1, "High", 3)
        time.sleep(0.05)
        j2 = self._make_job(2, "High", 3)

        heap.insert(j2)
        heap.insert(j1)

        # j1 has earlier timestamp, should come out first
        extracted = heap.extract_max()
        self.assertEqual(extracted.job_id, 1)

    def test_get_sorted_jobs(self):
        heap = MaxHeap()
        heap.insert(self._make_job(1, "Low", 1))
        time.sleep(0.01)
        heap.insert(self._make_job(2, "High", 3))
        time.sleep(0.01)
        heap.insert(self._make_job(3, "Medium", 2))

        sorted_jobs = heap.get_sorted_jobs()
        self.assertEqual(len(sorted_jobs), 3)
        self.assertEqual(sorted_jobs[0].job_id, 2)
        self.assertEqual(sorted_jobs[1].job_id, 3)
        self.assertEqual(sorted_jobs[2].job_id, 1)
        # Original heap is not mutated
        self.assertEqual(heap.size(), 3)

    def test_many_inserts_maintain_heap(self):
        heap = MaxHeap()
        priorities = [1, 3, 2, 1, 3, 2, 1, 3]
        for i, p in enumerate(priorities):
            names = {1: "Low", 2: "Medium", 3: "High"}
            heap.insert(self._make_job(i + 1, names[p], p))
            time.sleep(0.01)

        prev_priority = 4
        while not heap.is_empty():
            job = heap.extract_max()
            self.assertLessEqual(job.priority_value, prev_priority)
            prev_priority = job.priority_value


if __name__ == "__main__":
    unittest.main()
