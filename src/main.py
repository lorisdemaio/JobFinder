import os
import csv
import pandas as pd
from rich.console import Console
from find_jobs import getJobs
from parse_arguments import parse_arguments

if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(BASE_DIR, "data", "jobs.csv")

    console = Console()
    args = parse_arguments()

    jobs = getJobs(
        keyword=args.keyword,
        location=args.location,
        limit=args.limit
    )

    print(f"\n Job offers found {len(jobs)} \n")
    for job in jobs:
        console.print(f"- {job['title']} | {job['company']} | {job['location']}", style="bold white")
        console.print(f"  {job['url']} \n", style="blue")

# Save CSV
if args.csv:
    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        rows = []

        for job in jobs:
            writer.writerow([])

            writer.writerow(["Title: " + job["title"]])
            writer.writerow(["Company: " + job["company"]])
            writer.writerow(["Location: " + job["location"]])
            writer.writerow(["Url: " + job["url"]])

            writer.writerow([])
            writer.writerow(["=================================="])

        console.print(f"{len(jobs)} job offers saved", style="bold green")