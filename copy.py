import tool
def main():
    f1 = input('读取文件名：')
    f2 = input('写入文件名：')
    lines=tool.readfile(f1)
    tool.writefile(f2,lines,f1)
if __name__=='__main__':
    main()
