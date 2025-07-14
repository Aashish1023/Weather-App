from PIL import Image
from io import BytesIO
import requests

url = "https://openweathermap.org/img/wn/10d@2x.png"
img_data = requests.get(url).content

image = Image.open(BytesIO(img_data))
image.show()
