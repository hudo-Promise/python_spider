import re

# html = '''
# <html>
#     <div><p>九霄龙吟惊天变</p></div>
#     <div><p>风云际会浅水游</p></div>
# </html>
# '''
#
# # 贪婪匹配
# pattern = re.compile('<div><p>.*</p></div>', re.S)
# r_list = pattern.findall(html)
# print(r_list)
#
# # 非贪婪匹配
# pattern = re.compile('<div><p>.*?</p></div>', re.S)
# r_list = pattern.findall(html)
# print(r_list)
#
# # 非贪婪匹配 + 只取数据
# pattern = re.compile('<div><p>(.*?)</p></div>', re.S)
# r_list = pattern.findall(html)
# print(r_list)

html = '''
<div class="animal">
    <p class="name">
    <a title="Tiger"></a>
    </p>
    <p class="content">
        Two tigers two tigers run fast
    </p>
</div>

<div class="animal">
    <p class="name">
    <a title="Rabbit"></a>
    </p>
    <p class="content">
        Small white rabbit white and white
    </p>
</div>
'''

# pattern = re.compile('<a title="(\w+)"></a>.*?<p class="content">(.*?)</p>', re.S)
# r_list = pattern.findall(html)
# print(r_list)

pattern = re.compile('<div class="animal">.*?title="(.*?)".*?'
                     'class="content">(.*?)</p>', re.S)
r_list = pattern.findall(html)
print(r_list)
for tuple in r_list:
        print("动物：%s" % tuple[0] + "    描述：%s" % tuple[1].strip())
        print("*" * 50)


# strip() 去掉左右空白
# split() 分割默认以空格切分，得到一个列表
# replace() 替换  (被替换对象，替换对象)
