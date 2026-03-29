# Printer Job Scheduler — Master Plan
## Heap-Based Priority Queue Implementation

---

## 1. Project Overview

Build a **Printer Job Scheduler** using a **Heap-based Priority Queue** data structure. The system accepts print jobs with varying priorities (High, Medium, Low), stores them in a max-heap, and processes them in priority order — ensuring urgent documents print first.

---

## 2. Technology Stack

| Component       | Choice               | Reason                                      |
|-----------------|----------------------|---------------------------------------------|
| Language        | Python 3.x           | Clean syntax, ideal for data structure work  |
| Data Structure  | Max-Heap (manual)     | Core requirement — no `heapq` wrapper hiding logic |
| UI              | Console (CLI menu)    | Simple, meets all input/output requirements  |
| Testing         | `unittest` / manual   | Validate heap operations and edge cases      |
| Optional UI     | Tkinter (stretch goal)| Graphical interface if time permits          |

---

## 3. Data Structure Design

### 3.1 PrintJob (Entity)

```
PrintJob:
    - job_id        : int          (auto-incremented)
    - document_name : str
    - user_name     : str
    - priority      : str          ("High" | "Medium" | "Low")
    - priority_value: int          (High=3, Medium=2, Low=1)
    - pages         : int
    - timestamp     : datetime     (submission time, tie-breaker)
    - status        : str          ("Waiting" | "Printing" | "Completed" | "Cancelled")
```

### 3.2 MaxHeap (Core Data Structure)

```
MaxHeap:
    - heap[]              : list of PrintJob

    Methods:
    + insert(job)         : Add job, bubble up to maintain heap property
    + extract_max()       : Remove & return highest-priority job, heapify down
    + peek()              : View highest-priority job without removing
    + remove(job_id)      : Cancel a specific job, rebuild heap
    + size()              : Return number of jobs in heap
    + is_empty()          : Check if heap is empty
    + display()           : Show all jobs in priority order

    Internal:
    - _bubble_up(index)   : Restore heap property upward after insert
    - _heapify_down(index): Restore heap property downward after extract
    - _swap(i, j)         : Swap two elements in the array
    - _parent(i)          : Return parent index
    - _left_child(i)      : Return left child index
    - _right_child(i)     : Return right child index
```

### 3.3 Priority Comparison Logic

```
Comparison order:
  1. priority_value (High=3 > Medium=2 > Low=1)
  2. timestamp (earlier submission wins ties — FIFO within same priority)
```

### 3.4 PrinterScheduler (Controller)

```
PrinterScheduler:
    - queue             : MaxHeap
    - job_counter       : int        (auto-increment ID)
    - completed_jobs    : list       (history)
    - current_job       : PrintJob   (currently printing, or None)

    Methods:
    + add_job(doc_name, user, priority, pages)  : Create job & insert to heap
    + print_next()       : Extract max, simulate printing
    + cancel_job(job_id) : Remove job from queue
    + view_queue()       : Display all pending jobs in priority order
    + view_completed()   : Show history of printed jobs
    + get_status()       : Show current system state
```

---

## 4. Module / File Structure

```
c:\PDSA\cw\
│
├── main.py                  # Entry point — CLI menu loop
├── print_job.py             # PrintJob class
├── max_heap.py              # MaxHeap implementation (core data structure)
├── printer_scheduler.py     # PrinterScheduler (business logic controller)
├── utils.py                 # Helper functions (display formatting, input validation)
├── tests/
│   ├── test_max_heap.py     # Unit tests for heap operations
│   ├── test_scheduler.py    # Unit tests for scheduler logic
│   └── test_print_job.py    # Unit tests for PrintJob
├── MASTER_PLAN.md           # This file
└── README.md                # Usage instructions
```

---

## 5. Feature Breakdown & Menu System

```
========================================
      PRINTER JOB SCHEDULER
========================================
1. Submit a New Print Job
2. Print Next Job
3. View Print Queue
4. Cancel a Print Job
5. View Completed Jobs
6. View System Status
7. Exit
========================================
Enter your choice:
```

### Feature Details

| # | Feature                  | Input                                      | Output                                        | Heap Operation       |
|---|--------------------------|-------------------------------------------|-----------------------------------------------|----------------------|
| 1 | Submit New Print Job     | doc name, user, priority, pages            | "Job #X added (Priority: High)"               | `insert()`           |
| 2 | Print Next Job           | None                                       | Simulate printing top-priority job             | `extract_max()`      |
| 3 | View Print Queue         | None                                       | Sorted list of all waiting jobs                | `display()`          |
| 4 | Cancel a Print Job       | job_id                                     | "Job #X cancelled" or "Job not found"          | `remove()`           |
| 5 | View Completed Jobs      | None                                       | History of printed/cancelled jobs              | N/A (list read)      |
| 6 | View System Status       | None                                       | Current job, queue size, stats                 | `peek()`, `size()`   |
| 7 | Exit                     | None                                       | Goodbye message                                | N/A                  |

---

## 6. Implementation Phases

### Phase 1: Core Data Structure (Day 1-2)
- [ ] Implement `PrintJob` class with all attributes
- [ ] Implement `MaxHeap` class with array-based heap
  - [ ] `insert()` with bubble-up
  - [ ] `extract_max()` with heapify-down
  - [ ] `peek()`, `size()`, `is_empty()`
  - [ ] `remove(job_id)` with heap rebuild
  - [ ] `display()` — show all jobs sorted
- [ ] Write unit tests for all heap operations
  - [ ] Test insert maintains heap property
  - [ ] Test extract returns highest priority
  - [ ] Test tie-breaking by timestamp
  - [ ] Test remove specific job
  - [ ] Test empty heap edge cases

### Phase 2: Scheduler Logic (Day 3)
- [ ] Implement `PrinterScheduler` class
  - [ ] `add_job()` — validate input, create PrintJob, insert to heap
  - [ ] `print_next()` — extract max, simulate printing, move to completed
  - [ ] `cancel_job()` — find and remove job by ID
  - [ ] `view_queue()` — display pending jobs
  - [ ] `view_completed()` — display history
  - [ ] `get_status()` — current state summary
- [ ] Write unit tests for scheduler logic

### Phase 3: CLI Interface (Day 4)
- [ ] Build `main.py` menu loop
- [ ] Input validation (priority must be High/Medium/Low, pages > 0, etc.)
- [ ] Formatted output tables for queue display
- [ ] Error messages for empty queue, invalid job ID, etc.
- [ ] Printing simulation (progress indicator)

### Phase 4: Testing & Polish (Day 5)
- [ ] End-to-end testing with sample scenarios
- [ ] Edge cases: empty queue operations, duplicate priorities, large queue
- [ ] Clean up output formatting
- [ ] Write README with usage instructions

### Phase 5 (Optional Stretch): GUI with Tkinter
- [ ] Simple window with buttons for each operation
- [ ] Live queue display table
- [ ] Status bar showing current printing job

---

## 7. Heap Operations — Algorithm Detail

### Insert (Bubble Up)
```
1. Append new job to end of heap array
2. Compare with parent: if new job has higher priority, swap
3. Repeat step 2 until heap property restored or root reached
Time: O(log n)
```

### Extract Max (Heapify Down)
```
1. Save root element (highest priority)
2. Move last element to root position
3. Compare root with children: swap with larger child if violated
4. Repeat step 3 until heap property restored or leaf reached
Time: O(log n)
```

### Remove by ID
```
1. Linear search for job_id in heap array — O(n)
2. Replace with last element
3. Bubble up or heapify down as needed
4. Time: O(n) search + O(log n) fix
```

### Display (Sorted Order)
```
1. Create a copy of the heap
2. Repeatedly extract_max from copy to get sorted order
3. Time: O(n log n)
```

---

## 8. Sample Test Scenario

```
Action                                          Expected Heap State (top → bottom)
──────────────────────────────────────────────────────────────────────────────────
Add Job("Report.pdf", "Alice", High, 10)        [Report.pdf(H)]
Add Job("Notes.txt", "Bob", Low, 2)             [Report.pdf(H), Notes.txt(L)]
Add Job("Agenda.docx", "Carol", Medium, 5)      [Report.pdf(H), Notes.txt(L), Agenda.docx(M)]
Add Job("Urgent.pdf", "Dave", High, 1)          [Report.pdf(H), Urgent.pdf(H), Agenda.docx(M), Notes.txt(L)]
Print Next → should print Report.pdf (High, earlier timestamp)
Print Next → should print Urgent.pdf (High)
Print Next → should print Agenda.docx (Medium)
Cancel Notes.txt → removed from queue
Print Next → empty queue error
```

---

## 9. Error Handling

| Scenario                         | Response                                    |
|----------------------------------|---------------------------------------------|
| Print when queue is empty        | "No jobs in queue."                         |
| Cancel non-existent job ID       | "Job #X not found."                         |
| Invalid priority input           | "Invalid priority. Use High, Medium, or Low." |
| Pages ≤ 0                        | "Page count must be a positive number."     |
| Empty document name              | "Document name cannot be empty."            |

---

## 10. Complexity Summary

| Operation    | Time Complexity | Space Complexity |
|-------------|-----------------|------------------|
| Insert       | O(log n)        | O(1)             |
| Extract Max  | O(log n)        | O(1)             |
| Peek         | O(1)            | O(1)             |
| Remove by ID | O(n)            | O(1)             |
| Display All  | O(n log n)      | O(n)             |
| Space (heap) | —               | O(n)             |

---

## 11. Deliverables Checklist

- [ ] Working MaxHeap implementation (no built-in heap library)
- [ ] PrintJob class with all required attributes
- [ ] PrinterScheduler with full CRUD operations
- [ ] Interactive CLI with menu system
- [ ] Input validation and error handling
- [ ] Unit tests for heap and scheduler
- [ ] README with setup and usage instructions
- [ ] Sample run demonstrating all features
