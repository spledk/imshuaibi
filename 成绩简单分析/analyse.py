students=[]
try:
    with open('成绩.txt','r',encoding='utf-8') as r:
        lines=r.readlines()
        for num,line in enumerate(lines,start=1):
            m=line.split()
            if  len(m)!=2:
                print(f'{num}号学生格式有问题')
                exit(1)
            else:
                m[1]=int(m[1])
                students.append(m)
except PermissionError:
    print('无法读取成绩文件')
    exit(1)
except FileNotFoundError:
    print('无法找到成绩文件')
    exit(1)
if len(students)==0:
    print('成绩文件内无信息')
    exit(1)
else:
    students.sort(key=lambda x:x[1])
    top=max(students,key=lambda x:x[1])
    low=min(students,key=lambda x:x[1])
    ave=sum(i[1] for i in students)/len(students)
    print(f'成绩最高的是{top}\n成绩最低的是{low}\n平均分为{ave}分')
    