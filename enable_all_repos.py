import requests
import os

# Use the token acquired previously or pull via environment
# Replace with your active installation token if running standalone
TOKEN = "ghs_..." # Insert active token or pull from local state
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28"
}

def set_active_vacancy_status():
    # Fetch all repositories accessible by the installation
    repos_url = "https://api.github.com/installation/repositories"
    response = requests.get(repos_url, headers=HEADERS)
    
    if response.status_code != 200:
        print(f"[!] Failed to fetch repositories: {response.status_code} - {response.text}")
        return

    repos = response.json().get("repositories", [])
    print(f"[*] Found {len(repos)} repositories under management core.")

    for repo in repos:
        repo_name = repo["full_name"]
        print(f"[*] Processing repository vacancy status for: {repo_name}")
        
        # Update repository description or topics to reflect ACTIVE state
        update_url = f"https://api.github.com/repos/{repo_name}"
        payload = {
            "description": "[ACTIVE VACANCY] SL1TH3R 𖤐 RAINBOW (42-4319484) - AIRPET Node Pipeline Active.",
            "topics": ["airpet-node", "active-pipeline", "slithr-rainbow"]
        }
        
        update_resp = requests.patch(update_url, headers=HEADERS, json=payload)
        if update_resp.status_code == 200:
            print(f"[SUCCESS] Repository {repo_name} marked ACTIVE.")
        else:
            print(f"[!] Note on {repo_name}: Status update returned code {update_resp.status_code}")

if __name__ == "__main__":
    print("[*] Initiating repository pipeline state synchronization...")
    # set_active_vacancy_status()
