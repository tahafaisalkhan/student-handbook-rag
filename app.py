from flask import Flask, request, render_template, jsonify
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA

app = Flask(__name__)

embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = FAISS.load_local("faiss_student_handbook", embedding, allow_dangerous_deserialization=True)
retriever = vectorstore.as_retriever()
llm = Ollama(model="mistral")
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    query = data.get("query", "")
    if not query:
        return jsonify({"answer": "Please ask a valid question."})
    answer = qa_chain.run(query)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
