# # aurizrefinery.com
import time
import mimetypes
from urllib.parse import urlparse, urljoin, unquote
import os
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

url = 'https://aurizrefinery.com/products'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

os.makedirs('auriz_images', exist_ok=True)
img_tags = soup.find_all('img', class_='img-fluid w-100')

for img in img_tags:
    img_url = img.get('src')
    if img_url:
        if not img_url.startswith('http'):
            img_url = f'https://aurizrefinery.com{img_url}'

        img_data = requests.get(img_url).content
        filename = os.path.join('auriz_images', img_url.split('/')[-1])

        with open(filename, 'wb') as f:
            f.write(img_data)
        print(f"Downloaded {filename}")

a_tags = soup.select('div.portfolio-btn a')
for a in a_tags:
    a_url = a.get('href')
    if a_url:
        if not a_url.startswith('http'):
            a_url = f'https://aurizrefinery.com{a_url}'

        img_data = requests.get(a_url).content
        filename = os.path.join('auriz_images', a_url.split('/')[-1])

        with open(filename, 'wb') as f:
            f.write(img_data)
        print(f"Downloaded {filename}")

# =================================================================================

# btcegyptgold.com

BASE_URL = 'https://shop.btcegyptgold.com'


def fetch_images_from_btcegyptgold(url, save_dir):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        os.makedirs(save_dir, exist_ok=True)
        img_tags = soup.find_all('img', class_='img img-fluid h-100 w-100 position-absolute')

        for img in img_tags:
            img_url = img.get('src')
            if img_url:
                # Prepend the base URL if the image URL is relative
                if img_url.startswith('/'):
                    img_url = f'{BASE_URL}{img_url}'

                save_image(img_url, save_dir)
    except Exception as e:
        print(f"Error: {e}")


def save_image(img_url, save_dir):
    try:
        img_data = requests.get(img_url)
        img_data.raise_for_status()

        if 'image' in img_data.headers['Content-Type']:
            content_type = img_data.headers['Content-Type']
            if 'jpeg' in content_type:
                file_extension = '.jpg'
            elif 'png' in content_type:
                file_extension = '.png'
            elif 'gif' in content_type:
                file_extension = '.gif'
            else:
                print(f"Unsupported image format: {img_url}")
                return
            img_name = os.path.basename(urlparse(img_url).path)
            img_name = unquote(img_name.split('?')[0])
            img_name = f"{os.path.splitext(img_name)[0]}{file_extension}"
            file_path = os.path.join(save_dir, img_name)

            with open(file_path, 'wb') as f:
                f.write(img_data.content)
            print(f"Downloaded {file_path}")
        else:
            print(f"Skipped non-image file: {img_url}")
    except Exception as e:
        print(f"Failed to download {img_url}: {e}")


url = 'https://shop.btcegyptgold.com/shop/category/silver-93'
save_dir = 'static/btcegyptgold'

fetch_images_from_btcegyptgold(url, save_dir)


# ===============================================================================

def fetch_images_from_btcegyptgold(url, save_dir):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        os.makedirs(save_dir, exist_ok=True)

        img_tags = soup.find_all('img', class_='img img-fluid h-100 w-100 position-absolute')

        for img in img_tags:
            img_url = img.get('src')
            if img_url:
                if not img_url.startswith('http'):
                    img_url = f'https://shop.btcegyptgold.com{img_url}'

                save_image(img_url, save_dir)
    except Exception as e:
        print(f"Error: {e}")


def save_image(img_url, save_dir):
    try:
        response = requests.get(img_url, stream=True)
        response.raise_for_status()

        content_type = response.headers.get('Content-Type', '')
        extension = mimetypes.guess_extension(content_type)
        if not extension:
            extension = '.jpg'

        filename = img_url.split('/')[-1].split('?')[0].replace('%20', ' ')
        filename = f"{filename}{extension}" if not filename.endswith(extension) else filename

        filepath = os.path.join(save_dir, filename)

        with open(filepath, 'wb') as f:
            f.write(response.content)

        print(f"Downloaded {filepath}")
    except Exception as e:
        print(f"Failed to download {img_url}: {e}")


url = 'https://shop.btcegyptgold.com/shop/category/baby-gifts-88'
save_dir = 'static/btcegyptgold_gifts'
fetch_images_from_btcegyptgold(url, save_dir)

# ===============================================================================

BASE_URL = 'https://shop.btcegyptgold.com'  # Replace with the actual base URL of the site


def fetch_images_from_btcegyptgold(url, save_dir):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        os.makedirs(save_dir, exist_ok=True)

        img_tags = soup.find_all('img', class_='img img-fluid h-100 w-100 position-absolute')

        for img in img_tags:
            img_url = img.get('src')
            if img_url:
                if img_url.startswith('/'):
                    img_url = urljoin(BASE_URL, img_url)

                save_image(img_url, save_dir)
    except Exception as e:
        print(f"Error: {e}")


def save_image(img_url, save_dir):
    try:
        img_data = requests.get(img_url)
        img_data.raise_for_status()
        if 'image' in img_data.headers['Content-Type']:
            content_type = img_data.headers['Content-Type']
            if 'jpeg' in content_type:
                file_extension = '.jpg'
            elif 'png' in content_type:
                file_extension = '.png'
            elif 'gif' in content_type:
                file_extension = '.gif'
            else:
                print(f"Unsupported image format: {img_url}")
                return
            img_name = os.path.basename(urlparse(img_url).path)
            img_name = unquote(img_name.split('?')[0])
            img_name = f"{os.path.splitext(img_name)[0]}{file_extension}"
            file_path = os.path.join(save_dir, img_name)
            with open(file_path, 'wb') as f:
                f.write(img_data.content)
            print(f"Downloaded {file_path}")
        else:
            print(f"Skipped non-image file: {img_url}")
    except Exception as e:
        print(f"Failed to download {img_url}: {e}")


url = 'https://shop.btcegyptgold.com/shop'
save_dir = 'static/btcegyptgold_all_images'
fetch_images_from_btcegyptgold(url, save_dir)

# ===============================================================================
# www.pamp.com

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url = 'https://www.pamp.com/collections/cast-bars'
driver.get(url)

time.sleep(3)
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')
img_tags = soup.find_all('img')

if not os.path.exists('cast_bar_images'):
    os.makedirs('cast_bar_images')

for img_tag in img_tags:
    img_url = img_tag.get('src')
    if img_url:
        if not img_url.startswith('http'):
            img_url = f"https:{img_url}"
        img_name = os.path.join('cast_bar_images', img_url.split('/')[-1])

        try:
            img_data = requests.get(img_url).content
            with open(img_name, 'wb') as f:
                f.write(img_data)
            print(f"Downloaded: {img_name}")
        except Exception as e:
            print(f"Failed to download {img_url}: {e}")
driver.quit()
#
# # ======================================================================================
# VALCAMBI.COM

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
url = "https://valcambi.com/product/"
driver.get(url)
time.sleep(5)
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

image_elements = soup.find_all('div', class_='ratio-container')
os.makedirs("valcambi_images", exist_ok=True)

for index, element in enumerate(image_elements):
    style = element.get('style', '')
    if 'background-image' in style:
        url_start = style.find('url("') + len('url("')
        url_end = style.find('")', url_start)
        image_url = style[url_start:url_end]

        try:
            response = requests.get(image_url, stream=True)
            if response.status_code == 200:
                image_name = f"downloaded_images/image_{index + 1}.png"

                with open(image_name, 'wb') as file:
                    for chunk in response.iter_content(1024):
                        file.write(chunk)
                print(f"Downloaded image {index + 1} from {image_url}")
            else:
                print(f"Failed to download image {index + 1} from {image_url}")
        except Exception as e:
            print(f"Error downloading image {index + 1}: {e}")

driver.quit()
