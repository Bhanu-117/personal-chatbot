import streamlit as st
from dotenv import load_dotenv
load_dotenv(dotenv_path="token1.env")  # Load token from file

from intent_classifier import classify_intent
from huggingface_client import ask_hf

st.set_page_config(page_title="💰 Smart Finance Advisor", layout="wide", page_icon="📊")

# Custom dark UI styling
st.markdown("""
    <style>
        .main {
            background-color: #121212;
            color: #ffffff;
        }
        .block-container {
            padding-top: 2rem;
        }
        .stTextInput>div>div>input,
        .stTextArea>div>textarea,
        .stNumberInput>div>input,
        .stSelectbox>div>div>div>div {
            border-radius: 8px;
            background-color: #2a2a2a;
            color: #fff;
        }
        .stButton>button {
            border-radius: 10px;
            background-color: #ba68c8;
            color: white;
            font-weight: bold;
        }
        .stButton>button:hover {
            background-color: #ab47bc;
        }
        .stMarkdown h2 {
            color: #ffb6ff;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <h1 style='text-align: center; color: #ffb6ff;'>🤖 Smart Personal Finance Chatbot</h1>
    <p style='text-align: center; font-size: 18px;'>Get personalized financial insights and improve your savings & investments!</p>
""", unsafe_allow_html=True)

st.markdown("---")

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("👤 User Profile")
    user_type = st.selectbox("Who are you?", ["Student", "Professional"])
    income = st.number_input("Monthly Income (₹)", min_value=0, step=100)
    expenses = st.number_input("Monthly Expenses (₹)", min_value=0, step=100)
    categories = st.text_input("Spending Categories (comma-separated)", placeholder="e.g., food, rent, travel")

with col2:
    st.subheader("❓ Your Financial Query")
    user_query = st.text_area("Ask a question", placeholder="How can I increase my savings?", height=150)

    if st.button("💡 Get Advice"):
        if not user_query.strip():
            st.warning("Please enter a financial question.")
        else:
            with st.spinner("Analyzing your query..."):
                intent = classify_intent(user_query)
                prompt = (
                    f"You are a financial advisor chatbot for {user_type}s. "
                    f"The user has a monthly income of ₹{income} and expenses of ₹{expenses}. "
                    f"Their top spending categories include: {categories}. "
                    f"Provide detailed and personalized financial advice with clear bullet points. "
                    f"Use simple and helpful language.\n\n"
                    f"User query: {user_query}\n"
                    f"Intent detected: {intent}\n\n"
                    f"Response:"
                )
                response = ask_hf(prompt)
            st.markdown("### 📬 Personalized Advice")
            st.success(response)
