import sys, os, requests, bs4

if len(sys.argv) < 2:
    sys.exit('使い方: python filckrloader.py キーワード ...\n例）python flickrloader.py white cat')

MAX_IMAGES = 10
DIR = 'images'
os.makedirs(DIR, exist_ok=True)
keyword = ' '.join(sys.argv[1:])

res = requests.get('https://www.flickr.com/search/?text=' + keyword)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
imgs = soup.select('.photo-list-photo-view img')

for i in range(min(MAX_IMAGES, len(imgs))):
    img_url = 'https:' + imgs[i].get('src')
    print(img_url)
    img_res = requests.get(img_url)
    img_res.raise_for_status()
    with open(os.path.join(DIR, os.path.basename(img_url)), 'wb') as img_file:
        img_file.write(img_res.content)

