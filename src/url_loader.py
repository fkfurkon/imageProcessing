def load_image_from_url(url):
    import requests
    from PIL import Image
    from io import BytesIO

    response = requests.get(url)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        return image
    else:
        raise Exception("Failed to load image from URL")