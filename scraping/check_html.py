#HTML取得確認
import requests

#サイトのURL
url = "https://transit.yahoo.co.jp/search/result?from=%E6%B1%9F%E5%9D%82&to=%E4%BA%AC%E6%A9%8B(%E5%A4%A7%E9%98%AA%E5%BA%9C)&fromgid=&togid=&flatlon=,,25850&tlatlon=,,25901&via=&viacode=&y=2025&m=03&d=22&hh=12&m1=5&m2=0&type=4&ticket=ic&expkind=1&userpass=1&ws=3&s=0&al=1&shin=1&ex=1&hb=1&lb=1&sr=1"  # (Yahoo! 路線情報のURL)
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print(response.text[:1000])  # 最初の1000文字だけ表示
else:
    print("Failed to retrieve the page:", response.status_code)
