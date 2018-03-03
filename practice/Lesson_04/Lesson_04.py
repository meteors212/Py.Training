import re
import sys
'''
s=""" 
            en: Regular expression is a powerful tool for manipulating text.  
            zh: 汉语是世界上最优美的語言，正则表达式是一个很有用的工具 
            jp: 正規表現は非常に役に立つツールテキストを操作することです。  
            jp-char: あアいイうウえエおオ  
            kr:정규 표현식은 매우 유용한 도구 텍스트를 조작하는 것입니다.  
            """

#re_words = re.compile(u"[\u4e00-\u9fa5]+")
m =  re_words.match(s,0)
print("unicode 中文")
print("--------")
print(m)
#print("--------")
#print(m.group())
#res = re.findall(re_words, s)       # 查询出所有的匹配字符串
#if res:
#    print("There are %d parts:\n"% len(res))
#    for r in res:
#        print("\t",r)
#        print()
#print("--------\n")
'''

#比對手機
phones = ['0912345678', '0233638488','0912-111-222', '0912-122222', '3446443333039944847','0946474844938383736363', '+886-987654321','+886987654321']
#{0,1} 可簡化成 => ?
new_pattern = '(0|\+886-?)9\d{2}-?\d{3}-?\d{3}$'

# 以下寫法可以把list插入index, enumerate()可以把list加上索引編號
for idx,p in enumerate(phones):
    print(idx, re.match(new_pattern, p))


article = '''
註冊及課務Email：sdd@mail.shu.edu.tw.
24小時緊急聯絡
軍訓室值班辦公室：[ 專線：(02)2236-7935 / 免付費電話：0800022566 ]
監控室：[ 校內分機：#2113 ]
'''
'''
pattern = '\(02\)\d{4}-?\d{4}'
print(re.search(pattern, article))
'''