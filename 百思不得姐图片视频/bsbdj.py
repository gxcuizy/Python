import requests, bs4, os

print('百思不得姐……')
url = 'http://www.budejie.com/detail-27974418.html'
os.makedirs('bsbdj', exist_ok=True)
statusValue = True
while statusValue:
    # 下载网页
    print('Downloading page %s...' % url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }
    result = requests.get(url, headers=headers)
    soup = bs4.BeautifulSoup(result.text, "html.parser")
    # 查找图像
    comicElem = soup.select('.j-r-list-c-img img')
    if comicElem == []:
        print('Could not find comic image')
        break
    else:
        # 下载图像
        comicUrl = comicElem[0].get('src')
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
        imageFile = open(os.path.join('bsbdj', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
        nextLink = soup.select('.c-next-btn-content .c-next-btn')[0]
        url = 'http://www.budejie.com' + nextLink.get('href')
# 爬图结束
print('Done...')
