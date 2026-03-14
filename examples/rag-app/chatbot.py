from rag_pipeline import retrieve

def generate_answer(question):

    context = retrieve(question)

    prompt = f"""
    Answer the question using the context below.

    Context:
    {context}

    Question:
    {question}
    """

    # Placeholder LLM response
    return f"AI Answer based on retrieved docs: {context}"

# (You can replace with OpenAI or HuggingFace later.)
