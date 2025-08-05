# 🦎 LeadSightAI

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![OpenPyXL](https://img.shields.io/badge/OpenPyXL-025E8C?logo=excel&logoColor=white)](https://openpyxl.readthedocs.io/)
[![Selenium](https://img.shields.io/badge/Selenium-43B02A?logo=selenium&logoColor=white)](https://www.selenium.dev/)
[![LangChain](https://img.shields.io/badge/LangChain_Community-000000?logo=data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiB2aWV3Qm94PSIwIDAgMzYgMzYiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTI4LjQ1IDE4Ljg1Yy0uNjQtMS44My0xLjk4LTMuMzEtMy44My00LjE2bC0xMS43Ni01LjM1QzkuMTcgOC45NCA3IDExLjEyIDcgMTMuNzd2OC40NmwtNS4zNS0yLjU3VjExLjRjMC0xLjU3LjkyLTMuMDEgMi4zNS0zLjc1TDExLjU2IDQuNDVjLjY3LS4zNC44Mi0xLjE2LjMxLTEuNzNsLjM1LjE2YzIuMzMgMS4wNSAzLjYyIDMuNSAzLjE4IDYuMDhsMTEuNzYgNS4zNWMxLjQyLjY0IDIuMyAyLjA3IDIuMyAzLjY0djguNDUtNS4zNSAyLjU3di04LjA3YzAtLjU3LS4wOC0xLjEzLS4yNS0xLjY3WiIvPjwvc3ZnPg==)](https://github.com/langchain-ai/langchain)
[![LangChain Ollama](https://img.shields.io/badge/LangChain_Ollama-000000?logo=llama&logoColor=white)](https://github.com/langchain-ai/langchain)

---

## 📝 About the Project
**LeadSightAI** is a Streamlit-based application designed to help users discover and analyze company information for lead generation and business intelligence. It features a searchable company database and an interactive ChatRAG (Retrieval-Augmented Generation) interface, allowing users to extract insights from company websites. With built-in export options for CSV and Excel, it’s a practical tool for marketers, analysts, and researchers.


## 📝 About the Project
LeadSightAI is a Streamlit-based application designed to assist users in discovering and analyzing company information for lead generation and business intelligence. It combines a searchable company database with an interactive ChatRAG (Retrieval-Augmented Generation) feature, enabling users to extract insights from company websites. With built-in export options for CSV and Excel, it’s a practical tool for marketers, analysts, and researchers looking to streamline their workflows.

---

## 🎯 Purpose
- Provide an intuitive interface to filter and explore company data by industry, location, and keywords.
- Offer real-time ChatRAG interactions to dive deeper into company details using web-scraped content.
- Enable easy data export for further analysis or reporting.
- Serve as a foundation for future enhancements in AI-driven lead generation.

---

## 🌟 Key Features
- **Company Search Dashboard**: Filter companies with customizable criteria and view detailed profiles.
- **ChatRAG Integration**: Engage in conversational queries about selected companies using RAG with OllamaLLM.
- **Data Export**: Download filtered company data in CSV or Excel formats.
- **Dynamic Scraping**: Utilize SeleniumURLLoader to fetch and process live website content.

---

## 🛠️ Technology Stack
| Component         | Tool/Technology      | Purpose                          |
|-------------------|----------------------|----------------------------------|
| **UI Framework**  | Streamlit            | Interactive and responsive dashboard |
| **Scraping**      | SeleniumURLLoader    | Extract data from dynamic websites  |
| **Language Model**| OllamaLLM (Llama 3.2:3b)            | Power ChatRAG with local LLM       |
| **Vector Storage**| InMemoryVectorStore  | Store and retrieve document chunks |
| **Data Handling** | Pandas               | Manage and export company data     |

---

## 🏗️ How It Works
1. **Explore Companies**: Use the dashboard to search and filter companies based on industry, location, or name.
2. **Select a Company**: Click "Chat" to initiate a ChatRAG session for a specific company.
3. **Scrape Content**: The app scrapes the company’s website using SeleniumURLLoader.
4. **Generate Insights**: ChatRAG processes the scraped data with OllamaLLM to answer your questions.
5. **Export Results**: Save filtered company data to CSV or Excel for offline use.

---

## 🏗️ Architecture Diagram
![](Diagram.png)

---

## ⚙️ Getting Started

### 📥 Installation
1. Clone the repository
```bash
git clone https://github.com/yourusername/leadsightai.git
cd leadsightai
```

2. Create and activate a virtual environment
```bash
python3 -m venv venv

# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Pull the Ollama Model 
```bash
ollama pull llama3.2:3b
```

5. Run the app
```bash
streamlit run app.py
```

### 🌐 Prerequisites
- Python 3.8 or higher
- Internet connection (for live scraping)
- Optional: Update `config.py` to customize OllamaLLM settings

---

## 📁 Project Structure
```bash
leadsightai/
├── app.py                  # Main Streamlit app
├── config.py               # Configuration for LLM and settings
├── requirements.txt        # Required Python packages
├── static/
│   └── styles.css          # Custom UI styling
├── modules/
│   ├── data_handling.py    # Company data management
│   ├── scraping.py         # Website scraping logic
│   ├── chat_rag.py         # ChatRAG and LLM pipeline
│   └── ui_components.py    # UI components and layout
└── data/
    └── company_data.csv    # Sample dataset
```

---

## 📬 Contact & Contributions
Feel free to fork or submit issues! Created by [@kderrylo](https://github.com/kderrylo) for exploration and research in lead generation tools using open-source LLMs.
