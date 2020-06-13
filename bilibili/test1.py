import urllib.request, urllib.error
# try:
#     response = urllib.request.urlopen("http://www.baidu.com", timeout=5)
#     print(response.read().decode('utf-8'))  # 对获取到的网页进行解码
# except urllib.error.URLError as e:
#     print("time out...")
# # 获取post请求
# # httpbin.org
url = "http://www.douban.com"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                         " AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/81.0.4044.113 Safari/537.36"}
# data = bytes(urllib.parse.urlencode({'name':'eric'}), encoding="utf-8")
req = urllib.request.Request(url=url, headers=headers,)
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))
# print(response.status)
# print(req.getheader("Server"))


