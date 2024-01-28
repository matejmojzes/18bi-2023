import base64
import os
import requests
import streamlit as st

engine_id = "stable-diffusion-v1-6"
api_host = os.getenv('API_HOST', 'https://api.stability.ai')
api_key = "<YOUR_API_KEY>"

if api_key is None:
    raise Exception("Missing Stability API key.")

def generateImage(prompt):
    response = requests.post(
        f"{api_host}/v1/generation/{engine_id}/text-to-image",
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {api_key}"
        },
        json={
            "text_prompts": [
                {
                    "text": prompt,
                }
            ],
            "cfg_scale": 7,
            "height": 512,
            "width": 512,
            "samples": 1,
            "steps": 30,
        },
    )

    if response.status_code != 200:
        raise Exception("Non-200 response: " + str(response.text))

    data = response.json()
    return base64.b64decode(data["artifacts"][0]["base64"])

st.title("Stability.ai")
prompt = st.text_area(label="Prompt", value="A beautiful painting of a landscape")
button = st.button(label="Generate")
if button:
    with st.spinner(text="Generating image..."):
        image = generateImage(prompt)
        st.image(image, width=1024)
        st.download_button(
            label="Download",
            data=image,
            file_name="generated.png",
            mime="image/png",
        )
