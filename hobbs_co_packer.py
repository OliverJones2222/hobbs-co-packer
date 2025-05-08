import streamlit as st
import openai

# Set page config
st.set_page_config(page_title="Hobbs Co. Vacation Packer", layout="centered")

# Beachside sunset background
st.markdown("""
    <style>
    body {
        background-image: url('https://images.unsplash.com/photo-1507525428034-b723cf961d3e');
        background-size: cover;
        background-attachment: fixed;
    }
    .stApp {
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 12px;
        padding: 2rem;
        margin-top: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Hobbs Co. Title
st.title("Hobbs Co. Vacation Packing Assistant")

# User Inputs
destination = st.text_input("Where are you going?")
days = st.number_input("How many days are you staying?", min_value=1, max_value=90)
nice_meals = st.number_input("How many nice dinners will you have?", min_value=0, max_value=14)

# Generate packing list
if st.button("Get Your Packing List"):
    if not destination:
        st.warning("Please enter a destination.")
    else:
        openai.api_key = st.secrets["OPENAI_API_KEY"]

        prompt = (
            f"I'm going to {destination} for {days} days and plan to have {nice_meals} nice dinners. "
            "Help me pack efficiently: include clothes, toiletries, travel documents, and anything people often forget. "
            "Make the list smart, fun, and personalized."
        )

        with st.spinner("Packing your bags..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "You are a stylish and smart vacation packing assistant for Hobbs Co."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7,
                    max_tokens=700
                )
                packing_list = response.choices[0].message["content"]
                st.subheader("Your Personalized Packing List:")
                st.markdown(packing_list)
            except Exception as e:
                st.error(f"Something went wrong: {e}")
