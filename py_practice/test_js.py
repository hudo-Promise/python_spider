'''
这个文件的作用就是测试抓取下来的js文件，
通过pyexecjs包获取最终js代码块的生成结果
具体方式如下
'''

import execjs

# 打开并读取js文件
with open('test_node.js', 'r') as f:
    js_data = f.read()
# 创建execjs对象
exec_obj = execjs.compile(js_data)
# 执行并获取返回结果
sign = exec_obj.eval('e("tiger")')
print(sign)