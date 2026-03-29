from printer_scheduler import PrinterScheduler
from utils import (
    validate_priority,
    validate_pages,
    validate_non_empty,
    format_job_table,
    print_banner,
    print_menu,
)


def submit_job(scheduler):
    print("\n  --- Submit a New Print Job ---")

    doc_name = input("  Document name: ").strip()
    if not validate_non_empty(doc_name):
        print("  [Error] Document name cannot be empty.")
        return

    user_name = input("  Your name: ").strip()
    if not validate_non_empty(user_name):
        print("  [Error] User name cannot be empty.")
        return

    priority = input("  Priority (High / Medium / Low): ").strip()
    if not validate_priority(priority):
        print("  [Error] Invalid priority. Use High, Medium, or Low.")
        return

    pages_str = input("  Number of pages: ").strip()
    if not validate_pages(pages_str):
        print("  [Error] Page count must be a positive number.")
        return

    job = scheduler.add_job(doc_name, user_name, priority, int(pages_str))
    print(f"\n  [OK] Job #{job.job_id} added — \"{job.document_name}\" (Priority: {job.priority})")


def print_next(scheduler):
    print("\n  --- Print Next Job ---")
    job = scheduler.print_next()
    if job is None:
        print("  [Info] No jobs in the queue.")
    else:
        print(f"  [OK] Job #{job.job_id} \"{job.document_name}\" printed successfully.")


def view_queue(scheduler):
    print("\n  --- Current Print Queue ---")
    jobs = scheduler.view_queue()
    format_job_table(jobs)


def cancel_job(scheduler):
    print("\n  --- Cancel a Print Job ---")
    job_id_str = input("  Enter Job ID to cancel: ").strip()
    try:
        job_id = int(job_id_str)
    except ValueError:
        print("  [Error] Job ID must be a number.")
        return

    job = scheduler.cancel_job(job_id)
    if job is None:
        print(f"  [Error] Job #{job_id} not found in the queue.")
    else:
        print(f"  [OK] Job #{job.job_id} \"{job.document_name}\" has been cancelled.")


def view_completed(scheduler):
    print("\n  --- Completed / Cancelled Jobs ---")
    jobs = scheduler.view_completed()
    format_job_table(jobs)


def view_status(scheduler):
    print("\n  --- System Status ---")
    status = scheduler.get_status()
    current = status["current_job"]
    next_job = status["next_job"]

    print(f"  Jobs in queue   : {status['queue_size']}")
    print(f"  Jobs completed  : {status['completed_count']}")

    if current:
        print(f"  Currently printing: Job #{current.job_id} \"{current.document_name}\"")
    else:
        print("  Currently printing: None")

    if next_job:
        print(f"  Next in line    : Job #{next_job.job_id} \"{next_job.document_name}\" (Priority: {next_job.priority})")
    else:
        print("  Next in line    : None")


def main():
    scheduler = PrinterScheduler()
    print_banner()

    while True:
        print_menu()
        choice = input("  Enter your choice (1-7): ").strip()

        if choice == "1":
            submit_job(scheduler)
        elif choice == "2":
            print_next(scheduler)
        elif choice == "3":
            view_queue(scheduler)
        elif choice == "4":
            cancel_job(scheduler)
        elif choice == "5":
            view_completed(scheduler)
        elif choice == "6":
            view_status(scheduler)
        elif choice == "7":
            print("\n  Goodbye! All pending jobs have been discarded.\n")
            break
        else:
            print("  [Error] Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()
