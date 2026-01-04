import json
from datetime import datetime
from pathlib import Path

DATA_FILE = Path("applications.json")


def load_applications():
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


def save_applications(applications):
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(applications, f, indent=2)


def add_application(applications):
    print("\nAdd New Job Application")

    company = input("Company name: ").strip()
    title = input("Job title: ").strip()
    location = input("Location (or Remote): ").strip()
    status = input("Status (Applied / Interview / Rejected / Offer): ").strip()
    notes = input("Notes (optional): ").strip()

    application = {
        "company": company,
        "title": title,
        "location": location,
        "status": status,
        "date_applied": datetime.now().strftime("%Y-%m-%d"),
        "notes": notes,
    }

    applications.append(application)
    save_applications(applications)
    print("Application saved.")


def view_applications(applications):
    if not applications:
        print("\nNo applications found.")
        return

    print("\nYour Job Applications:")
    for idx, app in enumerate(applications, start=1):
        print(
            f"{idx}. {app['company']} — {app['title']} | "
            f"{app['status']} | Applied: {app['date_applied']}"
        )


def main():
    applications = load_applications()

    while True:
        print("\n=== Job Application Tracker ===")
        print("1) Add application")
        print("2) View applications")
        print("3) Quit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            add_application(applications)
        elif choice == "2":
            view_applications(applications)
        elif choice == "3":
            print("Good luck with your job search!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
