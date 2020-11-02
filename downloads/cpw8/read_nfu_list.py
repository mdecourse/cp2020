"""
semester=1091

courseno=0762

cp

1a 1091/0762

1b 1091/0776

cad

2a 1091/0788

2b 1091/0801
"""
# 導入 urllib.request: https://docs.python.org/3/library/urllib.request.html
# 透過 urllib.request 模組中的 urlopen() 開啟網路 url 連結資料
import urllib.request  # the lib that handles the url stuff
# 定義一個輸入學期與課號,就能夠輸出各課程修課人員數列的函式

def getRegList(semester, courseno):
    # 因為課號可能以 0 開頭, 因此採字串型別輸入, 為了一致, 輸入變數一律採字串輸入
    target_url = "https://nfulist.herokuapp.com/?semester=" + semester + "&courseno=" + courseno
    regList = []
    for line in urllib.request.urlopen(target_url):
        # 由於 urlopen() 取下的網際資料為 binary 格式, 可以透過 decode() 解碼為 ASCII 資料
        regList.append(line.decode('utf-8').rstrip())
    # 此一函式利用 return 將資料傳回
    return regList
    
print(getRegList("1091", "0776"))


# 1b_from_nfu.txt is one line file
with open("1b_from_nfu.txt") as f:
    # read() will read the whole content of file
    cRead = f.read()
#print(cRead)

with open("1b_from_nfu.txt") as f:
    # readline() only read one line
    cReadline = f.readline()
#print(cReadline)

with open("1b_from_nfu.txt") as f:
    # readlines() will read line by line and put into list
    cReadlines = f.readlines()
#print(cReadlines)

# user split() to cut cRead string into list with " "
cReadSplit = cRead.split(" ")
#print(cReadSplit)

for i in range(len(cReadSplit)):
    print(cReadSplit[i])


