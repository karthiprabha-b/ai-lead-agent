import requests

# Paste your SerpAPI key here
SERP_API_KEY = "a74c9bfa042543ea769b366227147a51b5487933833d9b3e68956136f7224fe6"

def get_google_leads(query, location):
    url = "https://serpapi.com/search.json"
    
    params = {
        "engine": "google_maps",
        "q": query,
        "location": location,
        "api_key": SERP_API_KEY,
        "type": "search"
    }

    response = requests.get(url, params=params)
    
    if response.status_code != 200:
        raise Exception("Failed to get data from SerpAPI")

    data = response.json()
    leads = []

    for result in data.get("local_results", []):
        lead = {
            "name": result.get("title", "N/A"),
            "address": result.get("address", "N/A"),
            "phone": result.get("phone", "N/A"),
            "website": result.get("website", "N/A"),
            "description": result.get("description", "N/A"),
        }
        leads.append(lead)

    return leads
