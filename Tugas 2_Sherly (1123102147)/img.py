import os
import MainFungsi
import requests
from bs4 import BeautifulSoup

url = 'https://www.lazada.co.id'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
}
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

datax = soup.find_all('img')

images = []
for img in datax:
    img_url = img.get('data-lazy-src') or img.get('src')
    if img_url and img_url.startswith('http') and img_url.endswith(('.jpg', '.png', '.gif')):
        images.append(img_url)

print("Gambar yang ditemukan:", images)

folder_tugas = "Tugas 2"
direktori = os.path.join(folder_tugas, "Hasil Gambar")

if not os.path.exists(folder_tugas):
    os.makedirs(folder_tugas)

if not os.path.exists(direktori):
    os.makedirs(direktori)

for gmb in images:
    try:
        response = requests.get(gmb, headers=headers, stream=True)
        if response.status_code == 200:
            filename = os.path.basename(gmb.split('?')[0])
            alt_text = img.get('alt') or 'default_name'
            filename = f"{alt_text}_{filename}"
            file_path = os.path.join(direktori, filename)
            with open(file_path, 'wb') as f:
                f.write(response.content)
            print(f"Sukses menyimpan: {filename}")
        else:
            print(f"Gagal mengunduh: {gmb}")
    except Exception as e:
        print(f"Error saat mengunduh {gmb}: {e}")
