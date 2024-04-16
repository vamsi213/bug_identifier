from openai import OpenAI 
import streamlit as st




st.title("Bugs Identifier using Gen AI")


# Read the API key and Setup an OpenAI Client
f = open("keys/.openai_demo2_key.txt")
key = f.read()
client = OpenAI(api_key=key)


# Take User's input 
prompt = st.text_area("Enter a Python code...")

# If the button is clicked , generate responses
if st.button("Generate") == True:
    response = client.chat.completions.create(
                model="gpt-3.5-turbo-0301",
                messages=[
            {"role": "system", "content": """You are a helpful AI Assistant.
                
                                            Given a code you need to check the code and find the errors in the code,explain them more clearly with examples and fix them."""},

            {"role": "user", "content": prompt}
            ]
    )
    
    # Print the respnse on web app
    st.write(response.choices[0].message.content)
