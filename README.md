

# 🤖 Context-Grounded Chatbot API
A FastAPI-based backend that leverages OpenAI-compatible models to perform text synthesis, rewriting, and context-strict answering. This bot is designed to be **text-grounded**, meaning it will not answer questions using external knowledge—only the data you provide.

## ✨ Features
* **Strict Context Answering:** Provide a "Context" (document/text), and the bot will answer questions based *only* on that source.
* **Formal Summarization:** Generates professional summaries strictly under 10 words.
* **Tone Transformation:** Rewrites text into an informal style while preserving 100% of the original data points.
* **Error Handling:** Robust validation to ensure context is set before querying.

---

## 🛠️ Tech Stack
* **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
* **AI SDK:** [OpenAI Python Library](https://github.com/openai/openai-python)
* **Environment:** `python-dotenv`

---

## 🚀 Installation & Setup

1.  **Clone the Repository**
    ```bash
    git clone <your-repo-url>
    cd chatbot-backend
    ```

2.  **Install Dependencies**
    ```bash
    pip install fastapi openai python-dotenv uvicorn
    ```

3.  **Configure Environment Variables**
    Create a `.env` file in the root directory:
    ```env
    API_KEY=your_api_key_here
    Base_Url=your_model_base_url
    model_name=your_model_name
    ```

4.  **Run the Server**
    ```bash
    uvicorn main:app --reload
    ```

---

## 🛰️ API Endpoints

### 1. Set Chatbot Context
**`POST /set_context`**
Sets the authoritative text the chatbot will use to answer questions.
* **Input:** `Context1` (string)
* **Response:** `201 Created` - "Context Successfully Set"

### 2. Context-Based Answering
**`GET /ask`**
Ask questions or request transformations based on the previously set context.
* **Query Parameter:** `Prompt` (Max 400 characters)
* **Logic:** If no context is set, it returns a `ValueError`.

### 3. Professional Summary
**`POST /summarize`**
Returns a formal summary of the input text in under 10 words.

### 4. Informal Rewrite
**`POST /edit`**
Rewrites the input text into a clean, informal tone without losing specific data details.

---

## 🛡️ AI Guardrails
The `Context_Based_Answering` function uses a high-instruction system prompt to prevent **Hallucinations**:
* **Strictly Grounded:** Only uses information in the provided context.
* **Fallback:** If the answer isn't in the text, it replies: *"Not specified in the text."*
* **Direct:** No conversational "fluff" or sugar-coating.

---

## 📝 Example Usage
1.  **Set Context:** "The company holiday policy allows 20 days of PTO and 5 sick days."
2.  **Ask Question:** "How many sick days do I get?"
3.  **AI Response:** "5 sick days."
4.  **Ask Out-of-Bounds:** "What is the capital of France?"
5.  **AI Response:** "Not specified in the text."
