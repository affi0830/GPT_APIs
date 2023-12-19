from PIL import Image
import numpy as np
from sklearn.cluster import KMeans


def convert_img2pix(img, size, k):
    img = img.resize(size)
    # img = img.convert("RGB")
    mode = img.mode
    img = np.array(img)
    if mode == "RGBA":
        alpha = img[:,:,-1][:,:,None]
        img = img[:,:,:-1]
        pixels = img.reshape(-1, 3)
    elif mode == "RGB":
        alpha = np.full([*img.shape[:-1], 1], 255)
        pixels = img.reshape(-1, 3)
    elif mode == "L":
        alpha = np.full([*img.shape, 1], 255)
        pixels = img.reshape(-1, 1)
    alpha = alpha.astype(np.uint8)

    kmeans = KMeans(n_clusters=k)  # 16色にクラスタリング
    kmeans.fit(pixels)
    colors = kmeans.cluster_centers_
    indices = kmeans.predict(pixels)

    pixel_img = colors[indices].astype(np.uint8)
    pixel_img = pixel_img.reshape(*size, colors.shape[-1])

    if pixel_img.shape[-1] == 1:
        pixel_img = np.tile(pixel_img, [1,1,3])

    pixel_img = np.round(pixel_img)
    pixel_img = np.concatenate([pixel_img, alpha], axis=-1)

    pixel_img = Image.fromarray(pixel_img)
    return pixel_img
