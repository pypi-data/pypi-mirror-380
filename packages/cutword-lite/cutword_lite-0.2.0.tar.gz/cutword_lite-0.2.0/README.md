
![cutword](./cutword-logo.svg)


**jieba不维护了，所以有了cutword。**

cutword 是一个中文分词库，字典文件根据截止到2024年1月份的最新数据统计得到，词频更加合理。
基于ac自动机实现的分词算法，分词速度是jieba的两倍。

cutword-lite 基于原项目 cutword 精简而成，移除了命名实体识别（NER），专注提供中文分词能力。

可通过 python -m cutword.comparewithjieba 进行测试。

Note：本项目只专注于中文分词。需要其他 NLP 能力时请结合合适的工具链。

# 1、安装：
```
pip install -U cutword-lite
```

# 2、使用：

## 2.1分词功能

```python
from  cutword import Cutter

cutter = Cutter()
res = cutter.cutword("你好，世界")
print(res)

```
本分词器提供两种词典库，一种是基本的词库，默认加载。一种是升级词库，升级词库总体长度会比基本词库更长一点。

如需要加载升级词库，需要将 want_long_word 设为True
```python
from  cutword import Cutter

cutter = Cutter()
res = cutter.cutword("精诚所至，金石为开")
print(res) # ['精诚', '所', '至', '，', '金石为开']

cutter = Cutter(want_long_word=True)
res = cutter.cutword("精诚所至，金石为开")
print(res) # ['精诚所至', '，', '金石为开']

```
初始化Cutter时，支持传入用户自定义的词典，词典格式需要和本项目的dict文件保持一致，词典中的词性一列，暂时没有使用，可随意填写。

本项目借鉴了苏神的[bytepiece](https://github.com/bojone/bytepiece)的代码，在此表示感谢。

