import os
import random
from datetime import datetime
import requests

os.makedirs("content", exist_ok=True)

# ---- TECH TOPICS ----
topics = {
    "Artificial Intelligence": [
        "Transformer Architecture",
        "Neural Network Backpropagation",
        "Large Language Models (LLMs)",
        "Reinforcement Learning Basics"
    ],
    "Machine Learning": [
        "Overfitting vs Underfitting",
        "Gradient Descent Optimization",
        "Feature Engineering Techniques",
        "Bias-Variance Tradeoff"
    ],
    "Robotics": [
        "SLAM (Simultaneous Localization and Mapping)",
        "PID Control Systems",
        "Robot Kinematics",
        "Autonomous Navigation Systems"
    ],
    "Innovation": [
        "AI Agents and Autonomous Systems",
        "Edge AI Computing",
        "Human-AI Collaboration",
        "Future of Robotics in Industry"
    ]
}

# ---- FETCH TECH NEWS ----
def get_tech_news():
    try:
        url = "https://newsapi.org/v2/everything?q=artificial intelligence OR robotics OR machine learning&sortBy=publishedAt&apiKey=3fe76714b74441d9a963d96648c8fd0c"
        res = requests.get(url).json()
        articles = res.get("articles", [])
        if articles:
            return articles[0]["title"]
    except:
        pass
    return "AI and robotics continue to evolve rapidly with new breakthroughs."

# ---- GENERATE TECH ARTICLE ----
def generate_article():
    category = random.choice(list(topics.keys()))
    topic = random.choice(topics[category])

    return f"""# 📅 {datetime.utcnow().strftime("%Y-%m-%d")}

# 🧠 {topic}

## 🏷️ Domain: {category}

## 📖 Concept Overview
{topic} is a fundamental concept in {category.lower()}. It plays a critical role in modern intelligent systems and computational models.

## ⚙️ How It Works
At a technical level, {topic.lower()} involves mathematical modeling, algorithmic optimization, and data-driven decision-making. These systems rely heavily on structured data and iterative learning processes.

## 🔬 Real-World Applications
- Autonomous vehicles  
- Recommendation systems  
- Industrial robotics  
- AI-powered assistants  

## 📊 Key Insights
- Efficiency improves with better data  
- Model performance depends on tuning  
- Real-world deployment requires robustness  

## 📰 Latest Tech Insight
{get_tech_news()}
"""

# ---- SAVE FILE ----
today = datetime.utcnow().strftime("%Y-%m-%d")
filename = f"content/{today}.md"

with open(filename, "w") as f:
    f.write(generate_article())

print("Tech content generated!")