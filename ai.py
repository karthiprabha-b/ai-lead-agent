import openai

# Paste your OpenAI key here
openai.api_key = "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"

# ----- 1. Classify Lead into Niche Category -----
def classify_niche(name, description):
    prompt = f"""
You are a smart business classifier. Classify this business into one of the following categories:
["Event Planner", "Wedding Planner", "Photographer", "Furniture Retailer", "Online Reseller", "Law Firm", 
"Interior Designer", "F&B Vendor", "Contractor", "E-commerce Seller", "Digital Agency", "Real Estate Agent", 
"Resident", "Student", "Art Collector", "Caterer", "NGO", "Construction Firm", "Baker", "Expats", 
"Drop Shipper", "Retail Shop", "Gardener", "Mover", "Importer", "Consultant", "Seasonal Resident"]

Business Name: {name}
Description: {description}

Category:
"""

    try:
        response = openai.Completion.create(
            model="gpt-3.5-turbo-instruct",  # Lightweight and cheap
            prompt=prompt,
            temperature=0.2,
            max_tokens=15
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return "Unclassified"

# ----- 2. Generate Outreach Message -----
def generate_message(niche, name):
    prompt = f"""
Write a short and friendly outreach message for a business in the '{niche}' niche.
The business is called '{name}' and they are based in Abu Dhabi.
You're offering them flexible, secure storage solutions at Vertex Storage.
Mention 1 benefit relevant to their niche and end with a call to action like 'DM us' or 'Call now'.

Message:
"""

    try:
        response = openai.Completion.create(
            model="gpt-3.5-turbo-instruct",
            prompt=prompt,
            temperature=0.7,
            max_tokens=70
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return "Hi! We’d love to help your business with secure storage. Contact us today!"
