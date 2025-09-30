from zhlid import load_model


model = load_model("MusubiAI/ZHLID")

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