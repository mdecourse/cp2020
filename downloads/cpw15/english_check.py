# read 5kwords.txt
filename = "5kwords.txt"
# since file has chinese character, need to specify encoding
with open(filename,'r', encoding="utf-8") as fileHandle:
    lines = fileHandle.readlines()
words = []
for i in range(len(lines)):
    # remove \n and split with " "
    # first element is word
    words.append(lines[i].rstrip().split(" ")[0])
    # the other
    words.append(lines[i].rstrip().split(" ")[1:])
    #print(words)
it = iter(words)
wordDict = dict(zip(it, it))
try:
    print(wordDict["dynamic"][0])
except:
    print("can not find it")