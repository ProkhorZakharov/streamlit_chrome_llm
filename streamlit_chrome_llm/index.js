
async function onDataFromPython(event){
    Streamlit.setComponentValue('Thinking...')

    const session = await window.ai.createTextSession({'temperature' : event.detail.args.temperature, 'topK' : event.detail.args.topK
    });

    const stream = session.promptStreaming(event.detail.args.user_input);

    for await (const chunk of stream) {
        Streamlit.setComponentValue(chunk);
      }

}

Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onDataFromPython);
Streamlit.setComponentReady();