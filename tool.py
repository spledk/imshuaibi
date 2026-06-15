def readfile(filename1):
    if filename1=='':
        print('读取文件名不能为空')
        readfile()
        exit(1)
    try:
        with open(f'{filename1}','r',encoding='utf-8')as f:
            lines=f.readlines()
    except FileNotFoundError:
        print("没有找到该文件")
        exit(1)
    except PermissionError:
        print("没有权限读取")
        exit(1)
    return(lines)
def writefile(filename2,lines,filename1):
    if filename2=='':
            print('写入文件名不能为空')
            writefile()
            exit(1)
    try:
        with open(f'{filename2}','w',encoding='utf-8')as f:
                f.writelines(f'{i}:{j}' for i,j in enumerate(lines,1))    
    except PermissionError:
        print("没有权限写入")
        exit(1)
    print(f'成功将{filename1}写入{filename2}')
if __name__=='__main__':
    f1=input('读取文件名为：')
    readfile(f1)
    f2=input('写入文件名为：')
    writefile(f2)
