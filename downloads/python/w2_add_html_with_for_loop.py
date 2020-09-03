'''
參考用的 html 字串為
<p><img class="add_border" height="342" src="/images/1_cp_git_and_cmsimde.png" width="600"></p>
'''
firstSegment = '''<p><img class="add_border" height="342" src="/images/'''

secondSegment = '''_cp_git_and_cmsimde.png" width="600"></p>'''

for i in range(2, 12):
    print(firstSegment + str(i) + secondSegment)