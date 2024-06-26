
import streamlit.components.v1 as components

_prompt_func = components.declare_component('prompt', path = './streamlit_chrome_llm')

def prompt(user_input : str, temperature = 0.8, topK = 3):
    component_value = _prompt_func(user_input = user_input, temperature = temperature, topK = int(topK))
    return component_value


        