from bs4 import BeautifulSoup

file = open("./baidu.html", "rb")
html = file.read()
bs = BeautifulSoup(html, "html.parser")
print(bs.title)
print(bs.title.string)
print(bs.a.attrs)
print(bs.a.string)

# 文档的遍历
print(bs.head.contents)
print(bs.head.contents[1])

# 文档的搜索
t_list = bs.find_all("a")  # 字符串过滤
# kwargs
t2_list = bs.find_all(id="head")
# text参数
t3_list = bs.find_all(text="hao123")  # 也可以是一个列表
# limit 参数
t4_list = bs.find_all("a", limit=3)
# css选择器
print(bs.select('title'))
print(t_list)
# 正则表达式