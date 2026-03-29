# Printer Job Scheduler

A Printer Job Scheduler built using a **Heap-Based Priority Queue** data structure. The system manages print job requests with varying priorities (High, Medium, Low), ensuring urgent documents are printed first.

## Features

- **Priority-based scheduling** — High-priority jobs print before low-priority ones
- **Max-Heap implementation** — Custom array-based heap (no built-in library)
- **File browser** — Select local files (PDF, DOCX, TXT, XLSX, images, etc.)
- **Auto page detection** — Reads actual page count from PDFs, estimates for other formats
- **Auto-fill** — User name from OS, priority suggestion based on file type
- **Single/Double-sided** printing option
- **Auto Print mode** — Automatically prints the next job when the printer is free
- **Print simulation** — Progress bar showing page-by-page printing
- **Job cancellation** — Cancel any pending job from the queue
- **Color-coded tables** — Red (High), Orange (Medium), Green (Low) priority rows
- **CLI + GUI** — Both text-based and graphical interfaces available

## Project Structure

```
c:\PDSA\cw\
├── main.py                 # CLI entry point (text-based menu)
├── gui.py                  # Tkinter GUI entry point
├── print_job.py            # PrintJob class
├── max_heap.py             # MaxHeap data structure (core)
├── printer_scheduler.py    # PrinterScheduler controller
├── utils.py                # Input validation & formatting helpers
├── tests/
│   ├── test_print_job.py   # Unit tests for PrintJob
│   ├── test_max_heap.py    # Unit tests for MaxHeap
│   └── test_scheduler.py   # Unit tests for PrinterScheduler
├── MASTER_PLAN.md          # Detailed project plan
└── README.md               # This file
```

## Requirements

- Python 3.10+
- PyPDF2 (for PDF page detection)
- python-docx (for DOCX word count estimation)
- openpyxl (for XLSX sheet counting)
- Pillow (for image handling)
- Tkinter (included with Python on Windows)

## Setup

```bash
# Create virtual environment
python -m venv .venv

# Activate (Windows)
.venv\Scripts\activate

# Install dependencies
pip install PyPDF2 python-docx openpyxl Pillow
```

## Usage

### GUI (Graphical Interface)

```bash
python gui.py
```

### CLI (Command Line Interface)

```bash
python main.py
```

### CLI Menu Options

```
1. Submit a New Print Job
2. Print Next Job
3. View Print Queue
4. Cancel a Print Job
5. View Completed Jobs
6. View System Status
7. Exit
```

## Data Structure

### Max-Heap Priority Queue

Jobs are stored in an array-based max-heap where:
- **Comparison**: Higher priority value wins (High=3 > Medium=2 > Low=1)
- **Tie-breaking**: Earlier submission timestamp wins (FIFO within same priority)

| Operation    | Time Complexity |
|-------------|-----------------|
| Insert       | O(log n)        |
| Extract Max  | O(log n)        |
| Peek         | O(1)            |
| Remove by ID | O(n)            |
| Display All  | O(n log n)      |

## Running Tests

```bash
python -m unittest discover -s tests -v
```

## Sample Workflow

1. Click **Browse** → select a PDF file
2. Pages, user name, and priority auto-fill
3. Choose Single or Double-sided
4. Click **Add Job**
5. Repeat for more documents
6. Click **Print Next** or enable **Auto Print** to process the queue
