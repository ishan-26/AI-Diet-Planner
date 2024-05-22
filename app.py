from dotenv import load_dotenv
import os
import google.generativeai as genai
from PIL import Image
import streamlit as st

#Load API Key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#Function to load Google Gemini Pro model and get response
def get_response_diet(prompt, input):
    model = genai.GenerativeModel('gemini-pro')

    response = model.generate_content([prompt, input])
    return response.text

st.image('logo.jpg', width=70)
st.header("Diet Planner")

input_prompt_diet = """
    You are an expert Nutritionist.
    If the input contains list of items like fruits or vegetables, you have to always give Indian diet plan and suggest different
    breakfast, lunch, dinner with respect to the given items provided by the user. Extra extra items apart from input.
    Also if possible provide dish along with the receipes.
    If the input contains numbers, you have to suggest diet plan for breakfast, lunch, dinner within
    given number of calorie for the whole day both vegetarian and non-vegetarian.
    Return the response using markdown.
    Only respond if the image pertains to food items else respond with not appropriate items mentioned.
    """

input_diet = st.text_area(" Input the list of items that you have at home and get diet plan! OR \
                              Input how much calorie you want to intake perday?:")

submit = st.button("Plan my Diet")

if submit:
 response = get_response_diet(input_prompt_diet, input_diet)

 st.subheader("Your Diet:")
 st.write(response)
