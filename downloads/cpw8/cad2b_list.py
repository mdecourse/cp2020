import urllib.request  # the lib that handles the url stuff
# 定義一個輸入學期與課號,就能夠輸出各課程修課人員數列的函式
"""
cp

1a 1091/0762

1b 1091/0776

cad

2a 1091/0788

2b 1091/0801
"""

def getRegList(semester, courseno, format=None):
    # 因為課號可能以 0 開頭, 因此採字串型別輸入, 為了一致, 輸入變數一律採字串輸入
    target_url = "https://nfulist.herokuapp.com/?semester=" + semester + "&courseno=" + courseno
    regList = []
    for line in urllib.request.urlopen(target_url):
        # 由於 urlopen() 取下的網際資料為 binary 格式, 可以透過 decode() 解碼為 ASCII 資料
        regList.append(line.decode('utf-8').rstrip())
    # 此一函式利用 return 將資料傳回
    if format == "list":
        return regList
    else:
        regData = ""
        for i in range(len(regList)):
            regData += regList[i] + "\n"
        return regData
    
#print(getRegList("1091", "0801"))

cad2b = getRegList("1091", "0801")
print(cad2b)


