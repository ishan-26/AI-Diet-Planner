from distutils.command import upload
from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image


load_dotenv()  ## load all the environment variables


genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_prompt, image):
    # ... (your existing code)
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input_prompt, image[0]])

    text = response.text
    return text

def input_image_setup(uploaded_file):
    # check if file uploaded or not
    if uploaded_file is not None:
        # read the bytes of file
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts

    else:
        print("No file uploaded")

# initialize streamlit app

st.set_page_config(page_title="Calories Advisor")
st.header("Calories Count")

uploaded_file = st.file_uploader("Choose an image...",type=["jpg","jpeg","png"])
image=""

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    #instructs Streamlit to use the image's natural width, but not exceeding the column width.
    st.image(image,use_column_width=True)

submit = st.button("Tell me about the total calories of the dish")

input_prompt="""
You are an expert Nutritionist.
    If the input contains list of items like fruits or vegetables etc, you have to always give Indian diet plan and suggest different
    breakfast, lunch, dinner with respect to the given items provided by the user. Do not include any items apart from input provided.
    Also if possible provide dish along with the receipes.

    If the input contains total number of calories, then create a Indian meal plan within a total calorie limit provided by the user for breakfast, lunch and dinner.

    Only respond if input pertains to food items else respond with not appropriate items mentioned.
"""

if submit:
    image_data = input_image_setup(uploaded_file)
    response = get_gemini_response(input_prompt,image_data)

    st.subheader("Your dish summary:")
    st.write(response)
