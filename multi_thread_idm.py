import requests
import time
import concurrent.futures
 
img_urls = [
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623210949/download21.jpg',
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623211125/d11.jpg',
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623211655/d31.jpg',
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623212213/d4.jpg',
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623212607/d5.jpg',
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623235904/d6.jpg',
]
 
t1 = time.perf_counter()

def download_image(img_url,image_name):
    time.sleep(1)
    img_bytes = requests.get(img_url).content
    with open(f"images/{image_name}",'wb') as image_obj:
       image_obj.write(img_bytes)
    print("Downloading..")
 
# Download images 1 by 1 => slow
i = 0
for img in img_urls:
  i= i +1
  download_image(img,f"temp{i}.jpg")
t2 = time.perf_counter()
print(f'Single Threaded Code Took :{t2 - t1} seconds')
 
# print('*'*50)
 
t1 = time.perf_counter()
def download_image(img_url):
    time.sleep(1)
    img_bytes = requests.get(img_url).content
    print("Downloading..")
 
# Fetching images concurrently thus speeds up the download.
with concurrent.futures.ThreadPoolExecutor(3) as executor:
    executor.map(download_image, img_urls)
 
t2 = time.perf_counter()
print(f'MultiThreaded Code Took:{t2 - t1} seconds')
