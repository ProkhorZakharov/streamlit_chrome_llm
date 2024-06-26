
import streamlit as st
from streamlit_chrome_llm import prompt

st.title('Chrome LLM Demo')   
st.info('This is a demo of the Built-In AI by Google. It requires the latest Chrome Canary release. \n\nFor details [click here](https://developer.chrome.com/docs/ai/built-in#get_an_early_preview)')

# Set temperature
temperature = st.slider('Temperature', 0.0, 1.0, 0.8)
topK = st.slider('Top K', 1, 10, 3)


# Get user input
your_prompt = st.text_input('Prompt:    ', value = '')
st.caption(f'Temperature: {temperature}' )
st.caption(f'Top K: {topK}' )

# Print results
if your_prompt!='':
    res = prompt(your_prompt, temperature, topK) 
    st.write(res)

else:
    st.write('Enter a prompt to get started')