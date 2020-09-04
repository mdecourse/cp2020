'''
根據評分表單中的 自評分數, 互評得分, 教師評分, 計算學員課程成績
'''
# diff 函式傳回兩輸入分數的絕對差值 
def diff(分數1, 分數2):
    return abs(分數1 - 分數2)
     
# getHigh函式傳回兩分數中較高者
def getHigh(分數1, 分數2):
    if  分數1 > 分數2:
        return 分數1
    else:
        return 分數2

# getLow 函式傳回兩分數中較低者
def getLow(分數1, 分數2):
    if  分數1 < 分數2:
        return 分數1
    else:
        return 分數2

# 分組評分函式取自評與教師評分比較, 若差距大於 5 分取其低者
# 否則依自評 40%, 教師 60% 計算
def 分組評分(自評分數, 教師評分):
    return getLow(自評分數, 教師評分)
    if diff(自評分數, 教師評分) > 5:
        return getLow(自評分數, 教師評分)
    else:
        return int(自評分數*0.4 + 教師評分*0.6)

# 全班比分函式取互評與分組評分比較, 若差距小於 5 分取其高者
# 否則依互評得分 40%, 分組評分 60% 計算     
def 全班比分(互評得分, 分組評分):
    if diff(互評得分, 分組評分) < 5:
        學員成績 = getHigh(互評得分, 分組評分)
    else:
        學員成績 = int(互評得分*0.4 + 分組評分*0.6)
    return 學員成績

# 學員之學期成績依照上述分組評分與全班比分函式計算 
def 學員成績(自評分數, 互評得分, 教師評分):
    學員課程成績 = 全班比分(互評得分, 分組評分(自評分數, 教師評分))
    return 學員課程成績

# 利用迴圈從 50 起每次增量 5 分, 分別列出各評分組合下的成績計算結果    
for i in range(10):
    self_score = 50 + i*5
    for j in range(10):
        peer_score = 50 + j*5
        for k in range(10):
            teacher_score = 50 + k*5
            print(self_score, peer_score, teacher_score, "=", 學員成績(self_score, peer_score, teacher_score))