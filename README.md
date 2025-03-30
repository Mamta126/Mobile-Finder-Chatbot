# Mobile Finder Chatbot

## 📌 Project Overview
The **Mobile Finder Chatbot** is an AI-powered chatbot that helps users find the latest mobile phones by any brand (Samsung, iPhone, OnePlus, etc.). It retrieves real-time data about mobile **models, features, specifications, and prices** using **SerpAPI** and **OpenAI GPT-4** for structured responses.

### 🔥 Key Features:
- **Find any phone** (e.g., "Latest iPhones", "Best Samsung phones under $1000")
- **Real-time search** using SerpAPI
- **AI-powered responses** (GPT-4 structures details neatly)
- **Easy-to-use UI** built with **Streamlit**

---

## 🛠️ Technology Stack
- **Python** - Programming language
- **Streamlit** - User-friendly UI
- **LangChain** - AI chatbot framework
- **OpenAI GPT-4** - Smart text processing
- **SerpAPI** - Fetches real-time mobile phone data
- **dotenv** - Manages API keys securely

---

## ⚙️ How It Works

### 1️⃣ User Input
A user enters a query like:
  - "Latest iPhones available"
  - "Best Samsung phone under $800"
  - "OnePlus 12 specs and price"

### 2️⃣ Fetch Mobile Data (SerpAPI)
The chatbot sends this query to **SerpAPI**, which retrieves the latest search results from Google.

### 3️⃣ AI Enhances the Response (GPT-4)
Since raw search results **lack structured details**, **GPT-4 processes the data** and:
- Extracts **display, camera, processor, battery** specs
- Adds **pricing & links**
- Formats it **beautifully**

### 4️⃣ Display Results on Streamlit UI
The chatbot **presents the final response** in a **clear, bullet-point format** to the user.

---

## 🚀 How to Run This Chatbot

### Step 1: Install Dependencies
```bash
pip install streamlit langchain openai serpapi python-dotenv
```

### Step 2: Set Up API Keys
Create a `.env` file and add:
```
OPENAI_API_KEY = "your-openai-key"
SERPAPI_API_KEY = "your-serpapi-key"
```

### Step 3: Run the Chatbot
```bash
streamlit run mobile_chatbot.py
```

### Step 4: Ask Any Mobile-Related Question
🎯 Example Queries:
- "Latest iPhones available"
- "Samsung Galaxy S24 specs and price"
- "Best budget smartphones in 2025"

---

## 🎯 Why This Chatbot is Impressive?
✅ **Handles any phone brand dynamically** (iPhone, Samsung, OnePlus, etc.)  
✅ **Uses AI (GPT-4) for structured & detailed responses**  
✅ **Fetches real-time mobile data via SerpAPI**  
✅ **User-friendly UI built with Streamlit**  
✅ **Secures API keys using dotenv**  

---

## 🏆 Conclusion
The **Mobile Finder Chatbot** is an **AI-powered assistant** that makes it easy to find **any smartphone** with detailed specifications, prices, and links. With **real-time search** and **GPT-4's smart formatting**, it delivers **accurate and well-structured responses** in seconds.  
 

**💡 Created by Mamta Sharma**
