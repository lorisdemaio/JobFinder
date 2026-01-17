import requests
from rich.console import Console
from rich.spinner import Spinner

console = Console()

def getJobs(keyword, location="", limit=10):
    try:
        with console.status("[bold green]Searching..."):
            res = requests.get("https://remotive.com/api/remote-jobs")
            data = res.json()

            jobs = []

            for job in data["jobs"]:
                
                # If the keyword is in the job title, save the job offer.
                # Otherwise, move to the next one.
                if keyword.lower() not in job["title"].lower(): 
                    continue
                
                # If the user has used the location parameter and it appears in the 
                # job title, save the job offer. Otherwise, move to the next one. 
                if location and location.lower() not in job["candidate_required_location"].lower(): 
                    continue
                
                # Add job offers
                jobs.append({
                    "title": job["title"],
                    "company": job["company_name"],
                    "location": job["candidate_required_location"],
                    "url": job["url"]
                })

                if len(jobs) >= limit:
                    break
        
    except requests.RequestException as e:
        console.print("Error: " + e, style="bold red")

    return jobs