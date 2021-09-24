
#encoding=utf-8
# 使用示例
from tkitSeg import tkitSeg
text = [" 张杨，男，汉族，黑龙江双城人，1988年2月6日生于贵州省贵阳市", " 自学习结合部分句法分析的汉语词性标注"]

Seg=tkitSeg()
datas = Seg.autoSeg(text)
print(datas)
