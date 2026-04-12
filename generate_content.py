import random
from datetime import datetime
import requests
import os

# Ensure content folder exists
os.makedirs("content", exist_ok=True)

# ---- TECH FACTS ----
tech_facts = [
    "Python was named after Monty Python.",
    "The first computer bug was a moth.",
    "JavaScript was built in 10 days.",
    "Git was created by Linus Torvalds.",
    "AI learns patterns, not true understanding."
]

# ---- QUOTES ----
quotes = [
    "Discipline beats motivation.",
    "Consistency creates success.",
    "Small daily progress compounds.",
    "Focus on systems, not goals.",
    "Stay relentless."
]

# ---- AI NEWS ----
def get_ai_news():
    try:
        url = "https://newsapi.org/v2/everything?q=artificial intelligence&sortBy=publishedAt&apiKey=3fe76714b74441d9a963d96648c8fd0c"
        res = requests.get(url).json()
        articles = res.get("articles", [])
        if articles:
            return articles[0]["title"]
    except:
        pass
    return "AI is evolving rapidly every day."

# ---- GENERATE ----
today = datetime.utcnow().strftime("%Y-%m-%d")

content = f"""# {today}

## 💬 Quote
{random.choice(quotes)}

## 🧠 Tech Fact
{random.choice(tech_facts)}

## 🤖 AI News
{get_ai_news()}
"""

# ---- SAVE FILE ----
with open(f"content/{today}.md", "w") as f:
    f.write(content)

print("Generated:", today)