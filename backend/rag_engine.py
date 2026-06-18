import os
import re
import google.generativeai as genai

from embeddings import MultilingualEmbeddings
from vector_store import VectorStore
from document_processor import DocumentProcessor
from translator import MultilingualTranslator


class RAGEngine:
    def __init__(self, persist_directory="./vector_db"):
        print("🚀 Initializing RAG Engine...")

        self.embeddings = MultilingualEmbeddings()
        self.vector_store = VectorStore(persist_directory=persist_directory)
        self.doc_processor = DocumentProcessor()
        self.translator = MultilingualTranslator()
        self.embedding_dim = self.embeddings.get_dimension()

        api_key = os.getenv("GEMINI_API_KEY")

        if api_key:
            genai.configure(api_key=api_key)
            self.gemini_model = genai.GenerativeModel("gemini-2.0-flash-lite")
            print("✅ Gemini connected!")
        else:
            self.gemini_model = None
            print("⚠️ GEMINI_API_KEY missing!")

        print(f"✅ RAG Engine ready! Dim: {self.embedding_dim}")

    def add_document(self, file_path, original_filename=None):
        if original_filename is None:
            original_filename = os.path.basename(file_path)

        print(f"\n📄 Processing: {original_filename}")

        try:
            text = self.doc_processor.load_document(file_path)
        except Exception as e:
            return {"status": "error", "message": f"Read error: {e}"}

        if not text or not text.strip():
            return {"status": "error", "message": "Document empty hai ya read nahi ho saka"}

        try:
            detected_lang = self.translator.detect_language(text[:500])
            lang_name = self.translator.get_language_name(detected_lang)
        except Exception:
            detected_lang = "en"
            lang_name = "English"

        try:
            chunks = self.doc_processor.split_into_chunks(text, chunk_size=700, overlap=80)
        except Exception as e:
            return {"status": "error", "message": f"Chunking error: {e}"}

        if not chunks:
            return {"status": "error", "message": "Koi chunks nahi ban sake"}

        try:
            chunk_embeddings = self.embeddings.embed_documents(chunks)
        except Exception as e:
            return {"status": "error", "message": f"Embedding error: {e}"}

        metadatas = [
            {
                "source": original_filename,
                "chunk_index": i,
                "language": detected_lang,
                "language_name": lang_name
            }
            for i in range(len(chunks))
        ]

        try:
            self.vector_store.add_documents(
                chunks=chunks,
                embeddings=chunk_embeddings,
                metadatas=metadatas
            )
        except Exception as e:
            return {"status": "error", "message": f"Vector store error: {e}"}

        return {
            "status": "success",
            "message": "Document added successfully!",
            "filename": original_filename,
            "chunks": len(chunks),
            "detected_language": lang_name,
            "total_documents": self.vector_store.get_count()
        }

    def _retrieve_context(self, question, n_results=2):
        if self.vector_store.get_count() == 0:
            return None, None, None, "Pehle document upload karo!"

        try:
            question_embedding = self.embeddings.embed_query(question)
            results = self.vector_store.search(
                query_embedding=question_embedding,
                n_results=n_results
            )
        except Exception as e:
            return None, None, None, f"Search error: {e}"

        if not results.get("documents") or not results["documents"][0]:
            return None, None, None, "Koi relevant content nahi mila."

        return (
            results["documents"][0],
            results["metadatas"][0],
            results["distances"][0],
            None
        )

    def _build_prompt(self, question, context_docs, target_language="en"):
        context = "\n\n---\n\n".join(context_docs[:2])

        language_names = {
            "en": "English",
            "hi": "Hindi",
            "es": "Spanish",
            "fr": "French",
            "de": "German",
            "zh": "Chinese",
            "ar": "Arabic",
            "bn": "Bengali",
            "ta": "Tamil",
            "te": "Telugu",
            "mr": "Marathi",
            "ur": "Urdu",
            "pt": "Portuguese",
            "ru": "Russian",
            "ja": "Japanese",
            "ko": "Korean"
        }

        language_name = language_names.get(target_language, "English")

        return f"""
You are a helpful multilingual RAG assistant.

Use ONLY the uploaded document context to answer.
If the answer is not available in the context, say clearly:
"I could not find this information in the uploaded documents."

IMPORTANT:
You MUST answer only in {language_name}.
Do not answer in English unless the selected language is English.

Document Context:
{context}

User Question:
{question}

Give a clear and useful answer.
Use bullet points when helpful.
"""

    def _generate_llm_answer(self, question, context_docs, target_language="en"):
        prompt = self._build_prompt(
            question=question,
            context_docs=context_docs,
            target_language=target_language
        )

        try:
            if not self.gemini_model:
                return "Gemini API key missing. Please set GEMINI_API_KEY."

            response = self.gemini_model.generate_content(prompt)
            answer = response.text or "No response from Gemini."

            return answer

        except Exception as e:
            return f"Gemini error: {e}"

    def query(self, question, target_language="en", n_results=2):
        print(f"\n❓ Query: {question} | Lang: {target_language}")

        try:
            question_lang = self.translator.detect_language(question)
        except Exception:
            question_lang = "en"

        retrieved_docs, retrieved_metas, retrieved_distances, error = self._retrieve_context(
            question,
            n_results=n_results
        )

        if error:
            return {
                "answer": error,
                "summary_points": [],
                "sources": [],
                "query_language": self.translator.get_language_name(question_lang),
                "num_sources": 0
            }

        answer = self._generate_llm_answer(
            question=question,
            context_docs=retrieved_docs,
            target_language=target_language
        )

        sources = self._format_sources(retrieved_docs, retrieved_metas, retrieved_distances)

        return {
            "answer": answer,
            "summary_points": [],
            "sources": sources,
            "query_language": self.translator.get_language_name(question_lang),
            "num_sources": len(sources)
        }

    def query_stream(self, question, target_language="en", n_results=2):
        retrieved_docs, retrieved_metas, retrieved_distances, error = self._retrieve_context(
            question,
            n_results=n_results
        )

        if error:
            yield error
            return

        answer = self._generate_llm_answer(
            question=question,
            context_docs=retrieved_docs,
            target_language=target_language
        )

        for char in answer:
            yield char

    def _format_sources(self, docs, metas, distances):
        sources = []

        for doc, meta, dist in zip(docs, metas, distances):
            cleaned_content = self._clean_text(doc)

            sources.append({
                "content": cleaned_content[:400] + "..." if len(cleaned_content) > 400 else cleaned_content,
                "source": meta.get("source", "Unknown"),
                "language": meta.get("language_name", "Unknown"),
                "relevance_score": float(1 - dist) if dist is not None else 0.0
            })

        return sources

    def _clean_text(self, text):
        if not text:
            return ""

        return re.sub(r"\s+", " ", text).strip()

    def get_stats(self):
        try:
            count = self.vector_store.get_count()
        except Exception:
            count = 0

        return {
            "total_chunks": count,
            "supported_languages": list(self.translator.supported_languages.keys()),
            "embedding_model": "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
            "vector_dim": self.embedding_dim,
            "llm_model": "gemini-1.5-flash"
        }