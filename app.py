import os
from io import BytesIO
import requests

from PIL import Image
from fastapi import FastAPI
from fastapi.responses import Response
from utils.img2pixel import convert_img2pix

HOTPEPPER_APIKEY = os.environ["HOTPEPPER_APIKEY"]
DMM_APIKEY = os.environ["DMM_APIKEY"]
DMM_ID = os.environ["DMM_ID"]

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/img2pix/")
async def upload_image(URL: str, W: int = 100, H: int = 100, k: int = 20):
    urlData = requests.get(URL).content
    image = Image.open(BytesIO(urlData))
    image = convert_img2pix(image, [W, H], k)
    img_bytes = BytesIO()
    image.save(img_bytes, format='png')
    return Response(content=img_bytes.getvalue(), media_type="image/png")

# ホットペッパーAPI KEY:c816e8b6a0ce51fc
@app.get("/hotpepper/")
async def upload_image(keyword: str=None, lat: float = None, lng: float = None, _range: int = None,
        count: int = 10,):
    Hotpepper_lolaction_api_url = "http://webservice.recruit.co.jp/hotpepper/gourmet/v1/"
    params = {"key": HOTPEPPER_APIKEY}
    if keyword is not None:
        params["keyword"] = keyword
    if lat is not None:
        params["lat"] = lat
    if lng is not None:
        params["lng"] = lng
    if _range is not None:
        params["range"] = _range
    if count is not None:
        params["count"] = count
    
    params["type"] = "lite"
    params["format"] = "json"
    response = requests.get(Hotpepper_lolaction_api_url, params=params)
    # レスポンスをJSONファイルに保存
    data = response.json()  # レスポンスをJSON形式に変換
    return data

# http://webservice.recruit.co.jp/hotpepper/gourmet/v1/