class MaxHeap:
    """Array-based Max-Heap ordered by (priority_value DESC, timestamp ASC)."""

    def __init__(self):
        self.heap = []

    # ---- public API ----

    def insert(self, job):
        self.heap.append(job)
        self._bubble_up(len(self.heap) - 1)

    def extract_max(self):
        if self.is_empty():
            return None
        self._swap(0, len(self.heap) - 1)
        max_job = self.heap.pop()
        if not self.is_empty():
            self._heapify_down(0)
        return max_job

    def peek(self):
        if self.is_empty():
            return None
        return self.heap[0]

    def remove(self, job_id):
        index = self._find_index(job_id)
        if index is None:
            return None
        self._swap(index, len(self.heap) - 1)
        removed = self.heap.pop()
        if index < len(self.heap):
            self._bubble_up(index)
            self._heapify_down(index)
        return removed

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    def get_sorted_jobs(self):
        """Return all jobs sorted by priority (highest first) without mutating the heap."""
        copy = MaxHeap()
        copy.heap = list(self.heap)
        result = []
        while not copy.is_empty():
            result.append(copy.extract_max())
        return result

    # ---- comparison helper ----

    def _higher_priority(self, a, b):
        """Return True if job a has higher priority than job b."""
        if a.priority_value != b.priority_value:
            return a.priority_value > b.priority_value
        return a.timestamp < b.timestamp  # earlier timestamp wins tie

    # ---- internal heap operations ----

    def _bubble_up(self, index):
        while index > 0:
            parent = self._parent(index)
            if self._higher_priority(self.heap[index], self.heap[parent]):
                self._swap(index, parent)
                index = parent
            else:
                break

    def _heapify_down(self, index):
        size = len(self.heap)
        while True:
            largest = index
            left = self._left_child(index)
            right = self._right_child(index)

            if left < size and self._higher_priority(self.heap[left], self.heap[largest]):
                largest = left
            if right < size and self._higher_priority(self.heap[right], self.heap[largest]):
                largest = right

            if largest != index:
                self._swap(index, largest)
                index = largest
            else:
                break

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _parent(self, i):
        return (i - 1) // 2

    def _left_child(self, i):
        return 2 * i + 1

    def _right_child(self, i):
        return 2 * i + 2

    def _find_index(self, job_id):
        for i, job in enumerate(self.heap):
            if job.job_id == job_id:
                return i
        return None
