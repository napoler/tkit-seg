# tkitSeg文档

多领域中文分词工具


安装
```bash
pip install tkitSeg
```

或者从源码安装
```bash
pip install git+https://github.com/napoler/tkit-seg.git

```


```python
# 使用示例
from tkitSeg import tkitSeg
text = [" 张杨，男，汉族，黑龙江双城人，1988年2月6日生于贵州省贵阳市", " 自学习结合部分句法分析的汉语词性标注"]

Seg=tkitSeg()
datas = Seg.autoSeg(text)
print(datas)

> [{'text': ' 张杨，男，汉族，黑龙江双城人，1988年2月6日生于贵州省贵阳市', 'pos': [{'word': '张杨', 'wtype': 'nr'}, {'word': '，', 'wtype': 'w'}, {'word': '男', 'wtype': 'b'}, {'word': '，', 'wtype': 'w'}, {'word': '汉族', 'wtype': 'nz'}, {'word': '，', 'wtype': 'w'}, {'word': '黑龙江', 'wtype': 'ns'}, {'word': '双城人', 'wtype': 'ns'}, {'word': '，', 'wtype': 'w'}, {'word': '1988年', 'wtype': 't'}, {'word': '2月', 'wtype': 't'}, {'word': '6日', 'wtype': 't'}, {'word': '生于', 'wtype': 'v'}, {'word': '贵州省', 'wtype': 'ns'}, {'word': '贵阳市', 'wtype': 'ns'}, {'word': ' \n', 'wtype': 'v'}], 'seg': ['张杨', '，', '男', '，', '汉族', '，', '黑龙江', '双城人', '，', '1988年', '2月', '6日', '生于', '贵州省', '贵阳市', ' \n']}, {'text': ' 自学习结合部分句法分析的汉语词性标注', 'pos': [{'word': '自学', 'wtype': 'p'}, {'word': '习结', 'wtype': 'n'}, {'word': '分句法', 'wtype': 'zzz'}, {'word': '分析', 'wtype': 'n'}, {'word': '的', 'wtype': 'u'}, {'word': '汉语词性', 'wtype': 'nz'}, {'word': '标注', 'wtype': 'n'}, {'word': ' \n', 'wtype': 'zzz'}], 'seg': ['自学', '习结', '分句法', '分析', '的', '汉语词性', '标注', ' \n']}]
```

