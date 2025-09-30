# ZHLID: 中文语言识别工具包
<p align="center">
    <a href="https://huggingface.co/MusubiAI/ZHLID"><img alt="Model" src="https://img.shields.io/badge/🤗%20Model%20Page-zhlid-yellow"></a>
    <a href="https://github.com/Musubi-ai/Musubi/blob/main/LICENSE"><img alt="GitHub" src="https://img.shields.io/badge/license-Apache_2.0-blue"></a>
    <a href="https://github.com/Musubi-ai"><img alt="Team" src="https://img.shields.io/badge/Built%20by-Musubi%20Team-blue"></a>

</p>

[English](../README.md) | 简体中文 | [繁體中文](docs/README_zh-TW.md)

ZHLID 是一个开源的、基于模型的语言识别工具，专注于区分中文的变体。

## 功能特点
与通用 LID 工具不同，ZHLID 聚焦于区分密切相关的中文变体，包括：

**繁体中文 (Traditional Chinese)** – 使用繁体字书写，常见于正式和古典文本。  
**简体中文 (Simplified Chinese)** – 使用简化字书写，便于阅读和书写。  
**粤语 (Cantonese)** – 书面形式反映口语粤语，具有独特的词汇和语法。  
**文言文（繁体） (Classical Chinese, Traditional)** – 使用繁体字的文言文，句式简练古雅。  
**文言文（简体） (Classical Chinese, Simplified)** – 使用简体字的文言文，常见于现代重印本和教育领域。

这使得 ZHLID 在语言学研究、语料分析、NLP 任务的预处理，或任何需要精准识别中文文本形式的场景中都非常有用。

以下表格比较了 ZHLID 与其他常见的中文检测工具：

| 识别能力 | 一般中文 | 繁体中文 | 简体中文 | 文言文 | 粤语 |
|------|:----:|:----:|:----:|:----:|:----:|
| ZHLID (ours) | ✅ | ✅ | ✅ | ✅ | ✅ |
| [langdetect](https://github.com/Mimino666/langdetect) | ✅ | ✅ | ✅ | ❌ | ❌ |
| [GlotLID](https://github.com/cisnlp/GlotLID/tree/main) | ✅ | ❌ | ❌ | ❌ | ✅ |
| [langid.py](https://github.com/saffsd/langid.py) | ✅ | ❌ | ❌ | ❌ | ❌ |
| [CLD3](https://github.com/google/cld3?tab=readme-ov-file#supported-languages) | ✅ | ❌ | ❌ | ❌ | ❌ |
| [Lingua](https://github.com/pemistahl/lingua-py) | ✅ | ❌ | ❌ | ❌ | ❌ |

## 安装
### 使用 pip 安装
```bash
pip install zhlid
```

### 从源码安装
```bash
pip install git+https://github.com/Musubi-ai/ZHLID
```

## 使用示例
```python
from zhlid import load_model

model = load_model("MusubiAI/ZHLID", device_map="auto")

text = [
    "王夫之者，字而農，衡陽人，明末清初哲學家。張獻忠陷衡州，夫之匿南嶽，賊執其父以為質。夫之自引刀遍刺肢體，舁往易父。",
    "金山阿伯係清末民初時嘅一種現象。金山阿伯係指嗰啲生活喺廣東地方，因為搵唔夠錢畀家人生活，要出洋到舊金山或新金山做苦工，掘金礦。",
    "燧人氏，古之三皇，有巢氏之子。 风姓，讳允婼，华夏族。燧人钻火，教人熟食，立国曰燧明，为后世奉为「火祖」，号燧皇。立一百一十年，崩，子伏羲嗣。\n\n**引据**\n《风俗通义·皇霸篇》\n*",
    "在量子力学中，量子涨落（quantum fluctuation。或量子真空涨落，真空涨落）是在空间任意位置对于能量的暂时变化。 \n从维尔纳·海森堡的不确定性原理可以推导出这结论。",
    "在政治中，政治議程是政府官員以及政府以外的個人在任何給定時間都認真關注的主題或問題/議題的列表。"
]

res = model.predict(text, batch_size=5)
print(res)
# [
#     {'label': 'zhtw_classical', 'confidence_score': 0.9999634027}, 
#     {'label': 'yue', 'confidence_score': 0.9376096725}, 
#     {'label': 'zhcn_classical', 'confidence_score': 0.9999793768}, 
#     {'label': 'zhcn', 'confidence_score': 0.9944804907}, 
#     {'label': 'zhtw', 'confidence_score': 0.9998573065}
# ]
```

## 评测
要使用我们的基准数据集评测 ZHLID，只需运行：
```bash
python evaluate.py
```

我们将 top-1 准确率与 [GlotLID](https://github.com/cisnlp/GlotLID/tree/main) 和 [langdetect](https://github.com/Mimino666/langdetect) 进行比较。需要注意的是，由于 GlotLID 只提供一个通用的 “cmn_Hani” 标签，因此它在繁体和简体上的表现是通过是否同时输出该标签来衡量的。

| Top-1 准确率                                              | 繁体中文 | 简体中文 | 文言文（繁体） | 文言文（简体） |  粤语  |
| ------------------------------------------------------ | :--: | :--: | :-----: | :-----: | :--: |
| ZHLID (ours)                                           |  1.0 |  1.0 |   0.9   |   1.0   | 0.96 |
| [GlotLID](https://github.com/cisnlp/GlotLID/tree/main) | 0.98 | 0.98 |    -    |    -    |  0.9 |
| [langdetect](https://github.com/Mimino666/langdetect)  |  0.3 |  0.9 |    -    |    -    |   -  |

## 引用
如果你在研究中使用 ZHLID，请引用本项目：
```bibtex
@misc{zhlid2025 ,
  title  = {ZHLID: Fine-grained Chinese Language Identification Package},
  author = {Lung-Chuan Chen},
  year   = {2025},
  howpublished = {\url{https://github.com/Musubi-ai/ZHLID}}
}
```