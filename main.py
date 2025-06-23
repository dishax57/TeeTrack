import streamlit as st
from langchain_helper import get_few_shot_db_chain

# Page config with new name
st.set_page_config(
    page_title="TeeTrack ",
    page_icon="👕",
    layout="centered"
)

# Custom CSS styling
st.markdown("""
    <style>
        .main {
            background-color: #f9f9f9;
        }
        h1 {
            color: #1e3d59;
            font-family: 'Segoe UI', sans-serif;
            text-align: center;
            font-size: 2.6rem;
        }
        .stTextInput > label {
            font-weight: bold;
        }
        .answer-box {
            background-color: #ffffff;
            padding: 1.5rem;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            margin-top: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# App Title
st.title("👕 TeeTrack – T-Shirt Data Assistant")

# Optional Sidebar
with st.sidebar:
    st.markdown("### ℹ️ How to use TeeTrack")
    st.write("Ask any question related to T-shirt inventory, sales, or pricing:")
    st.markdown("- How many t-shirts do we have left for Nike in XS size and white color?")
    st.markdown("- How much is the total price of the inventory for all S-size t-shirts?")
    st.markdown("- If we have to sell all the Levi’s T-shirts today with discounts applied. How much revenue  our store will generate (post discounts)?")

# Input
question = st.text_input("Enter your question below:")

# Submit button
if st.button("Submit"):
    if question.strip() != "":
        with st.spinner("Querying the database..."):
            chain = get_few_shot_db_chain()
            response = chain.run(question)

        # Output
        st.markdown("### ✅ Answer")
        st.markdown(f"<div class='answer-box'>{response}</div>", unsafe_allow_html=True)
    else:
        st.warning("Please enter a question before submitting.")
