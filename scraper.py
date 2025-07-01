import requests

SERP_API_KEY = "a74c9bfa042543ea769b366227147a51b5487933833d9b3e68956136f7224fe6"

def get_google_leads(query, location):
    url = "https://serpapi.com/search.json"
    
    # Add more keywords to help Google return more vendors
    full_query = f"{query} vendors OR suppliers OR service providers"

    params = {
        "engine": "google_maps",
        "q": full_query,
        "location": location,
        "api_key": SERP_API_KEY,
        "type": "search",
        "num": 20,
        "hl": "en"
    }

    res = requests.get(url, params=params)
    data = res.json()

    leads = []
    for result in data.get("local_results", []):
        address = result.get("address", "")
        
        # Only keep results that mention the location
        if location.lower() in address.lower():
            leads.append({
                "name": result.get("title", "N/A"),
                "phone": result.get("phone", "N/A"),
                "address": address if address else "N/A",
                "website": result.get("website", "N/A"),
                "description": result.get("description", result.get("website", "No info"))
            })

    return leads
