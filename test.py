import requests
from io import BytesIO
from PIL import Image


openai_url = "https://files.oaiusercontent.com/file-LbReV7Tw5RhvvOdUs6uVQKkV?se=2023-12-19T07%3A19%3A53Z&sp=r&sv=2021-08-06&sr=b&rscc=max-age%3D299%2C%20immutable&rscd=attachment%3B%20filename%3DAI%25E3%2583%25AD%25E3%2582%25B4.png&sig=xt44dVWyiyLlui3mwx9kzuF6e3k9FTA2dBLM6JTG/sI%3D"
filename='openai_test.png'

urlData = requests.get(openai_url).content

with open(filename ,mode='wb') as f: # wb でバイト型を書き込める
    f.write(urlData)


image = Image.open(BytesIO(urlData))
image.save("openai_test2.png")
