from urllib import request
from urllib import parse

url = "https://www.baidu.com/s?"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/83.0.4103.61 Safari/537.36'}

word = input("请输入要搜索的内容：")
query_string = parse.urlencode({'wd': word})

url = url + query_string

req = request.Request(url, headers=headers)
res = request.urlopen(req)
html = res.read().decode("utf-8")
print(html)

filename = "{}.html".format(word)
with open(filename, 'w', encoding='utf-8') as f:
    f.write(html)
