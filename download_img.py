import requests
from concurrent.futures import ThreadPoolExecutor
import urllib.request

def download_batch(page,crop=True):
    # TODO replace with concurrent.futures multithreading
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(download_page_batch,range(1,page+1),[crop for _ in range(page)])
    # for idx in range(page):
    #     download_page_batch(page=idx,crop=crop)


def download_page_batch(page=1,crop=True):
    print(f"downloading page {page}")
    url=f"https://picsum.photos/v2/list?page={page}&limit={100}"
    response=requests.get(url)
    if response.status_code!=200:
        raise Exception("Failed to download images")
    else:
        images_data=response.json()
        if crop:
            for idx,image_data in enumerate(images_data):
                _id=image_data.get('id')
                download_url=image_data.get('download_url')
                urllib.request.urlretrieve(download_url, f'./assets/downloads/{_id}.jpg')
        else:
            for idx,image_data in enumerate(images_data):
                _id=image_data.get('id')
                download_url=image_data.get('download_url')
                urllib.request.urlretrieve(download_url, f'./assets/downloads/{_id}.jpg')


download_batch(10,True)