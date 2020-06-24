import json

app_info = {'应用名称': '呵呵列表'}

with open('xiaomi.json', 'a') as f:
    json.dump(app_info, f, ensure_ascii=False)