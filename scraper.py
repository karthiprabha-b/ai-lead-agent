import requests

SERP_API_KEY = "a74c9bfa042543ea769b366227147a51b5487933833d9b3e68956136f7224fe6"

def get_google_leads(query, location):
    url = "https://serpapi.com/search.json"
    
    # 🔥 Boost match chance using OR terms
    full_query = f"{query} OR vendors OR service providers OR companies"

    params = {
        "engine": "google_maps",
        "q": full_query,
        "location": location,
        "api_key": SERP_API_KEY,
        "type": "search",
        "num": 20,
        "hl": "en"
    }

    response = requests.get(url, params=params)
    data = response.json()

    leads = []

    for result in data.get("local_results", []):
        address = result.get("address", "N/A").lower()

        # ✅ Make location check optional/flexible
        if location.lower() in address or address == "n/a":
            leads.append({
                "name": result.get("title", "N/A"),
                "phone": result.get("phone", "N/A"),
                "address": result.get("address", "N/A"),
                "website": result.get("website", "N/A"),
                "description": result.get("description", result.get("website", "No info"))
            })

    return leads
