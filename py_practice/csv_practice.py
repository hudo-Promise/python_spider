import csv

# 以写入的方式打开文件
with open('test.csv', 'w') as f:
    # 初始化写入对象
    writer = csv.writer(f)
    # 写入数据
    '''写一行'''
    writer.writerow([])
    '''写多行'''
    writer.writerows([(), (), ()])

# 以追加的方式打开文件
with open('test.csv', 'a', newline='') as f:
    # 初始化写入对象
    writer = csv.writer(f)
    # 写入数据
    '''写一行'''
    writer.writerow([])
    '''写多行'''
    writer.writerows([(), (), ()])


