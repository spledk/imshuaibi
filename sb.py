file=input("读取文件名：")
target=input("写入文件名：")
if file=='' or target=='':
    print('文件名不能为空')
try:
    with open(f'{file}.txt','r',encoding='utf-8')as f:
        lines=f.readlines()
except FileNotFoundError:
    print("没有找到该文件")
    exit(1)
except PermissionError:
    print("没有权限读取")
    exit(1)
try:
    with open(f'{target}.txt','w',encoding='utf-8')as f:
        for i,j in enumerate(lines,1):
            f.write(f'{i}:{j}')
except PermissionError:
    print("没有权限写入")
    exit(1)