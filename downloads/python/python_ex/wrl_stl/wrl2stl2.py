#coding:utf-8
#import函数库
import time, re, linecache
from sys import argv
#命令行输入脚本文件及所需转换文件
#script ,filename = argv
filename = "base.wrl"
print ("the input file name is:%r." %filename)
 
start = time.time()
print ("open the file...")
file = open(filename,"r+")
 
count = 0

keywords = "texCoord DEF texcoord0 TextureCoordinate" #wrl转换时自带的点索引
 
#统计源文件的点数,actually count-22才是真实的点云个数。count个数根据自己的wrl文件确定

for line in file:
    count=count+1
    if re.search(keywords, line):  
        print ("from delete %d" %count)
        break
 
#output = open("out.pcd","w+")
f_prefix = filename.split('.')[0]
output_filename = '{prefix}.pcd'.format(prefix=f_prefix)
output = open(output_filename,"w+")
 
list = ['# .PCD v.5 - Point Cloud Data file format\n','VERSION .5\n','FIELDS x y z\n','SIZE 4 4 4\n','TYPE F F F\n','COUNT 1 1 1\n']
 
output.writelines(list)
output.write('WIDTH ') #注意后边有空格
output.write(str(count-37))
output.write('\nHEIGHT ')
output.write(str(1))  #强制类型转换，文件的输入只能是str格式
output.write('\nPOINTS ')
output.write(str(count-37))
output.write('\nDATA ascii\n')
file1 = open(filename,"r")
for line in  file1.readlines()[34:count-3]:  #同样，去掉不需要的数据
    output.write(line)
 
 
file.close()
output.close()
file1.close()
 
end = time.time()
print ("points: ", count-37)
print ("run time is: ", end-start)
