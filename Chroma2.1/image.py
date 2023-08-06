from PIL import Image
import io
import requests

API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
headers = {"Authorization": "Bearer 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"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content


s = "Astronaut riding a horse"
image_bytes = query({
    "inputs": s
})
# You can access the image with PIL.Image for example
image = Image.open(io.BytesIO(image_bytes))
image.show()
