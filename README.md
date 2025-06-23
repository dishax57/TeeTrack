TeeTrack – T-Shirt Data Assistant
TeeTrack is an intelligent, interactive web app that allows users to query AtliQ’s T-shirt inventory and sales data using natural language. Powered by LangChain and Streamlit, it bridges the gap between business users and databases—no SQL knowledge required!

🔍 Features

📊 Ask in plain English – No need for complex SQL
🤖 Powered by LangChain – NLP-to-SQL via few-shot learning
🧠 Context-aware results – Understands brand, size, discount, stock, revenue, etc.
🎨 Sleek frontend – Built with Streamlit for a clean, responsive UI
🧵 Focused on T-shirt data – Optimized for retail & inventory insights

🛠️ Tech Stack

Python
LangChain
Streamlit
SQLite / MySQL (as the database)
LLM (e.g., OpenAI / Google Generative AI via LangChain)

🚀 How It Works

User types a question like “What’s the revenue from Puma t-shirts with discounts?”
LangChain converts it into SQL using a few-shot prompt template.
The app runs the SQL on the t-shirt database.
The result is shown as a clean, readable answer.

📁 Project Structure
bash
Copy
Edit
teetrack/
│
├── langchain_helper.py       # Sets up the few-shot chain
├── main.py                   # Streamlit frontend logic
├── t_shirt_data.db           # (Or connect to MySQL)
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
