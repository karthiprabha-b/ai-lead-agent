import requests

# 🔑 Add your real API key here or from environment variable
SERP_API_KEY = "a74c9bfa042543ea769b366227147a51b5487933833d9b3e68956136f7224fe6"

def get_google_leads(query, location):
    url = "https://serpapi.com/search.json"
    
    params = {
        "engine": "google_maps",
        "q": query,
        "location": location,
        "api_key": SERP_API_KEY,
        "type": "search",
        "num": 20,      # Fetch up to 20 results
        "hl": "en"      # English results
    }

    res = requests.get(url, params=params)
    data = res.json()

    leads = []
    for result in data.get("local_results", []):
        address = result.get("address", "")
        
        # ✅ Filter to include only leads with exact location match
        if location.lower() in address.lower():
            lead = {
                "name": result.get("title", "N/A"),
                "phone": result.get("phone", "N/A"),
                "address": address if address else "N/A",
                "website": result.get("website", "N/A"),
                "description": result.get("description", result.get("website", "No description"))
            }
            leads.append(lead)

    return leads
