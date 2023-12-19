import base64

from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_hotpepper():
    # POSTリクエストのデータ（JSON形式で指定)
    data = {
        "keyword": "鍋　名古屋"
    }

    response = client.get(
            "/hotpepper/",
            params=data,
        )
    # POSTリクエストを送信
    # レスポンスを表示
    print("Response:", response.status_code, response.json())




def test_img2pix():
    # POSTリクエストのデータ（JSON形式で指定)
    data = {
        "URL": "https://livedoor.blogimg.jp/rose_time/imgs/5/2/52d6eb74.png",
        "W": 100,
        "H": 100,
        "k": 10
    }

    response = client.get(
            "/img2pix/",
            params=data,
        )
    # POSTリクエストを送信
    # レスポンスを表示
    print("Response:", response.status_code)
    
    urlData = response.content
    with open("test_pix.png" ,mode='wb') as f: # wb でバイト型を書き込める
        f.write(urlData)


test_img2pix()