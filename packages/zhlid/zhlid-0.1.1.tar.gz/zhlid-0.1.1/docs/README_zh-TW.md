# ZHLID: 中文語言識別工具包
<p align="center">
    <a href="https://huggingface.co/MusubiAI/ZHLID"><img alt="Model" src="https://img.shields.io/badge/🤗%20Model%20Page-zhlid-yellow"></a>
    <a href="https://github.com/Musubi-ai/Musubi/blob/main/LICENSE"><img alt="GitHub" src="https://img.shields.io/badge/license-Apache_2.0-blue"></a>
    <a href="https://github.com/Musubi-ai"><img alt="Team" src="https://img.shields.io/badge/Built%20by-Musubi%20Team-blue"></a>

</p>

[English](../README.md) | [简体中文](docs/README_zh-CN.md) | 繁體中文

ZHLID 是一個開源的、基於模型的語言識別工具，專注於區分中文的變體。

## 功能特色
與通用 LID 工具不同，ZHLID 聚焦於區分彼此接近的中文變體，包括：

**繁體中文 (Traditional Chinese)** – 使用繁體字書寫，常見於正式和古典文本。  
**簡體中文 (Simplified Chinese)** – 使用簡化字書寫，便於閱讀與書寫。  
**粵語 (Cantonese)** – 書面形式反映口語粵語，具有獨特的詞彙與語法。  
**文言文（繁體） (Classical Chinese, Traditional)** – 使用繁體字的文言文，句式簡練古雅。  
**文言文（簡體） (Classical Chinese, Simplified)** – 使用簡體字的文言文，常見於現代重印本與教育領域。

這使得 ZHLID 在語言學研究、語料分析、NLP 任務的前處理，或任何需要精準識別中文文本形式的場景中都非常有用。

以下表格比較了 ZHLID 與其他常見的中文檢測工具：

| 識別能力 | 一般中文 | 繁體中文 | 簡體中文 | 文言文 | 粵語 |
|------|:----:|:----:|:----:|:----:|:----:|
| ZHLID (ours) | ✅ | ✅ | ✅ | ✅ | ✅ |
| [langdetect](https://github.com/Mimino666/langdetect) | ✅ | ✅ | ✅ | ❌ | ❌ |
| [GlotLID](https://github.com/cisnlp/GlotLID/tree/main) | ✅ | ❌ | ❌ | ❌ | ✅ |
| [langid.py](https://github.com/saffsd/langid.py) | ✅ | ❌ | ❌ | ❌ | ❌ |
| [CLD3](https://github.com/google/cld3?tab=readme-ov-file#supported-languages) | ✅ | ❌ | ❌ | ❌ | ❌ |
| [Lingua](https://github.com/pemistahl/lingua-py) | ✅ | ❌ | ❌ | ❌ | ❌ |

## 安裝
### 使用 pip 安裝
```bash
pip install zhlid
```

### 從原始碼安裝
```bash
pip install git+https://github.com/Musubi-ai/ZHLID
```

## 使用範例
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

## 評測
要使用我們的基準資料集評測 ZHLID，只需執行：
```bash
python evaluate.py
```

我們將 top-1 準確率與 [GlotLID](https://github.com/cisnlp/GlotLID/tree/main) 和 [langdetect](https://github.com/Mimino666/langdetect) 進行比較。需要注意的是，由於 GlotLID 只提供一個通用的 “cmn_Hani” 標籤，因此它在繁體和簡體上的表現是透過是否同時輸出該標籤來衡量的。

| Top-1 準確率                                              | 繁體中文 | 簡體中文 | 文言文（繁體） | 文言文（簡體） |  粵語  |
| ------------------------------------------------------ | :--: | :--: | :-----: | :-----: | :--: |
| ZHLID (ours)                                           |  1.0 |  1.0 |   0.9   |   1.0   | 0.96 |
| [GlotLID](https://github.com/cisnlp/GlotLID/tree/main) | 0.98 | 0.98 |    -    |    -    |  0.9 |
| [langdetect](https://github.com/Mimino666/langdetect)  |  0.3 |  0.9 |    -    |    -    |   -  |

## 引用
如果你在研究中使用 ZHLID，請引用本專案：
```bibtex
@misc{zhlid2025 ,
  title  = {ZHLID: Fine-grained Chinese Language Identification Package},
  author = {Lung-Chuan Chen},
  year   = {2025},
  howpublished = {\url{https://github.com/Musubi-ai/ZHLID}}
}
```