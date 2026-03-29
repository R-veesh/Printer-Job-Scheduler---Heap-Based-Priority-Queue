from print_job import PRIORITY_MAP


def validate_priority(priority):
    if priority.lower() not in PRIORITY_MAP:
        return False
    return True


def validate_pages(pages_str):
    try:
        pages = int(pages_str)
        return pages > 0
    except ValueError:
        return False


def validate_non_empty(value):
    return bool(value and value.strip())


def format_job_table(jobs):
    if not jobs:
        print("\n  (No jobs to display)\n")
        return

    header = f"  {'ID':<5} {'Document':<25} {'User':<15} {'Priority':<10} {'Pages':<7} {'Status':<12}"
    separator = "  " + "-" * 74
    print(f"\n{separator}")
    print(header)
    print(separator)
    for job in jobs:
        print(
            f"  {job.job_id:<5} {job.document_name:<25} {job.user_name:<15} "
            f"{job.priority:<10} {job.pages:<7} {job.status:<12}"
        )
    print(separator)
    print(f"  Total: {len(jobs)} job(s)\n")


def print_banner():
    print("\n" + "=" * 50)
    print("        PRINTER JOB SCHEDULER")
    print("    Heap-Based Priority Queue System")
    print("=" * 50)


def print_menu():
    print("\n  1. Submit a New Print Job")
    print("  2. Print Next Job")
    print("  3. View Print Queue")
    print("  4. Cancel a Print Job")
    print("  5. View Completed Jobs")
    print("  6. View System Status")
    print("  7. Exit")
    print("-" * 40)
