import requests


url = "https://www.3839.com/top/hot.html"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/81.0.4044.92 Safari/537.36"}
cookies = {"Cookie": "_uuid=9FE6F7AB-93BB-8F34-AC08-06995351012058687infoc; "
                     "buvid3=43C9DC37-A8A0-4892-8B15-6A81991BAAD353939infoc; "
                     "CURRENT_FNVAL=16; LIVE_BUVID=AUTO6115850606102582; "
                     "pdid=|(umJullm|R)0J'ul)l|Y|YuJ; sid=c97q1lad; "
                     "PVID=1; "
                     "bsource=seo_baidu"}
response = requests.get(url, headers=headers, cookies=cookies)
a = response.text.encode()
print(a)