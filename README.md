# 🎓 Student Handbook RAG

An interactive **Retrieval-Augmented Generation (RAG)** system powered by LangChain, Ollama, FAISS, and Flask. Users can ask natural language questions about the LUMS Student Handbook and get AI-generated answers with context-based retrieval. The project aims to solve the issue of scrolling all 300 pages of the handbook and rather just asking the question they want answered.

https://github.com/user-attachments/assets/e591a81c-b9e9-42b6-a6fa-a25a11f5ab49

---

## 📦 Features

- 🔍 PDF Parsing & Chunking (via PyMuPDF)
- 🧠 Semantic Embeddings with `MiniLM-L6-v2`
- ⚡ Local LLM (`Mistral`) served via [Ollama](https://ollama.com/)
- 🔎 Vector store search with FAISS
- 💬 Minimal, modern frontend with TailwindCSS & typing animation
- 🛰️ Dynamic AJAX-based Q&A (no page reloads)

---

## 🛠️ Installation & Setup

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/student-handbook-rag.git
cd student-handbook-rag
```

### 2. Set up Python environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Start Ollama locally
Make sure Ollama is installed.

```bash
ollama serve         # Terminal tab 1
ollama run mistral   # Terminal tab 2
```

### 4. Build vector store
Extract text from the handbook and generate embeddings:

```bash
cd rag-implementation
jupyter notebook rag.ipynb
```

### 5. Launch Flask app
```bash
cd ..
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

## 🧠 Technologies Used

| Tool | Purpose |
|------|---------|
| LangChain | LLM Orchestration |
| Ollama | Local model server (Mistral) |
| Sentence-Transformers | Embedding models |
| FAISS | Vector similarity search |
| Flask | Backend web framework |
| TailwindCSS | Modern UI styling |

## 📁 Project Structure

```
student-handbook-rag/
│
├── app.py                       # Flask server
├── requirements.txt
├── student_handbook.pdf
├── student_handbook.txt
├── faiss_student_handbook/     # FAISS index files
├── rag-implementation/         # Jupyter notebook to build the vector store
│   └── rag.ipynb
├── templates/
│   └── index.html              # Main frontend
└── venv/                       # Virtual environment
```

## 🚀 Deployment

To deploy on Vercel:
1. Use Flask Vercel Adapter
2. Add `vercel.json`:

```json
{
  "builds": [
    { "src": "app.py", "use": "@vercel/python" }
  ],
  "routes": [
    { "src": "/(.*)", "dest": "app.py" }
  ]
}
```

3. Push to GitHub and import into Vercel

## 🙌 Acknowledgments

Created by **Taha Faisal Khan**

## 📜 License

MIT License
