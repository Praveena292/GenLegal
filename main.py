import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Legal Jargon Simplifier", page_icon="⚖️")
st.title("⚖️ Legal Jargon Simplifier")

# Input Gemini API key
api_key = st.text_input("🔑 Enter your Gemini API key", type="password")

# Audience selection
audience = st.selectbox(
    "👥 Choose audience (style of simplification)",
    ["General User", "Lawyer", "Judge"]
)

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "text": "👩‍⚖️ Welcome! Paste some legal text and I’ll simplify it for you."}
    ]

# Display messages
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").markdown(msg["text"])
    else:
        st.chat_message("assistant").markdown(msg["text"])

# Chat input
if prompt := st.chat_input("Paste legal text or ask a question..."):
    if not api_key:
        st.error("⚠️ Please enter your Gemini API key first.")
    else:
        # Show user message
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role": "user", "text": prompt})

        try:
            # Configure Gemini
            genai.configure(api_key=api_key)

            # Audience-specific instructions
            style_instructions = {
                "General User": "Explain in simple everyday language, avoid legal jargon.",
                "Lawyer": "Simplify while keeping legal precision, clarify ambiguous terms.",
                "Judge": "Summarize clearly, highlighting intent, obligations, and implications."
            }

            system_prompt = f"""
            You are a helpful assistant that simplifies complex legal documents.
            Audience: {audience}.
            Guidelines:
            - {style_instructions[audience]}
            - Use simple words, short sentences.
            - Avoid jargon unless explained.
            - Never change the actual meaning of the text.
            """

            # Call Gemini
            model = genai.GenerativeModel(
                "gemini-1.5-flash",
                system_instruction=system_prompt
            )
            response = model.generate_content(prompt)

            reply = response.text.strip()
        except Exception as e:
            reply = f"❌ Error: {str(e)}"

        # Show bot message
        st.chat_message("assistant").markdown(reply)
        st.session_state.messages.append({"role": "assistant", "text": reply})
