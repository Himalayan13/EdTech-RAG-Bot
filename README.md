EdTech-RAG-Bot: AI-Powered FAQ Chatbot for EdTech Platforms 🎓🤖
🚀 EdTech-RAG-Bot is an AI-powered chatbot designed to handle high-volume student queries on ed-tech platforms. Built with Retrieval-Augmented Generation (RAG), this chatbot efficiently fetches accurate answers from a knowledge base, reducing the workload on support teams while enhancing user experience.



🌟 Why This Project?
Ed-tech companies experience high traffic from students asking similar queries about courses, pricing, schedules, certifications, etc. Handling these manually:

❌ Increases response time ⏳
❌ Burdens support teams 😵
❌ Affects user experience 👎

✅ Solution: AI-Powered RAG Chatbot
EdTech-RAG-Bot efficiently retrieves relevant answers from a structured FAQ dataset using vector embeddings and enhances responses using an LLM-based RAG pipeline.

🛠️ Tech Stack
LLM: Google Gemini 1.5 Pro
Embeddings: HuggingFace Embeddings (Instructor-XL)
Vector Database: FAISS
Framework: LangChain
Frontend: Streamlit
Deployment: GitHub + Cloud
⚙️ How It Works
Preprocess FAQs: Cleans, formats, and vectorizes the FAQ dataset.
Build Vector Store: Uses FAISS to store and retrieve query-specific embeddings.
Query Processing: Maps user queries to the most relevant FAQ vector.
LLM Augmentation: Uses Gemini for contextual refinement of the retrieved answer.
Response Generation: Delivers an accurate, AI-powered response in real-time.
🚀 Setup & Installation
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/Himalayan13/EdTech-RAG-Bot.git
cd EdTech-RAG-Bot
2️⃣ Set Up Virtual Environment (Conda Recommended)
bash
Copy
Edit
conda create -n edtech-chatbot python=3.10
conda activate edtech-chatbot
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Set Up API Keys (Google Gemini)
Create a .env file and add:

env
Copy
Edit
GOOGLE_API_KEY=your_google_api_key_here
5️⃣ Run the Chatbot UI
bash
Copy
Edit
streamlit run main.py
Now, interact with your chatbot in the browser! 🎉

🧪 Future Enhancements
✅ Website Integration
Seamlessly embed the chatbot into any ed-tech website, allowing students to get answers without leaving the platform.

✅ Admin-Controlled Knowledge Upload
Feature Overview:
Enable admins to update the chatbot’s knowledge base directly from the frontend.

How It Works:
Admin uploads a CSV file with new FAQs and answers.
The system automatically processes, cleans, and vectorizes the data.
The chatbot instantly incorporates the new knowledge, improving its responses.
Impact:
No developer intervention needed for knowledge updates.
Faster adaptability to new courses, policies, and student FAQs.
Ensures chatbot always provides up-to-date responses.
✅ Fine-tuned EdTech-specific LLM for improved query resolution.
✅ Multilingual Support for wider accessibility.
📬 Feel Free to Reach Out!
💼 LinkedIn: www.linkedin.com/in/himnish-a-5b6838196
📧 Email: himnisha11@gmail.com

