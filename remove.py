import re

with open("language_culc_wakati.txt", 'r', encoding='UTF-8') as f:
    data = f.read()
data = re.sub(r"<.*?>", r"", data)
half_width_symbols = r'[!"#$%&\'\\()*+,-./:;<=>?@[\\]^_`{|}~「」〔〕“”〈〉『』【】＆＊・（）＄＃＠。、？！｀＋￥％]'
data = re.sub(half_width_symbols, '', data)
full_width_symbols = r"[\uFF01-\uFF0F\uFF1A-\uFF20\uFF3B-\uFF40\uFF5B-\uFF65\u3000-\u303F]"
data = re.sub(full_width_symbols, '', data)
output_file = 'your_path/language_culc_wakati_comp.txt'
with open(output_file, 'w', encoding='UTF-8') as wf:
    wf.write(data)
print("記号削除が完了しました。結果は 'language_culc_wakati_comp.txt' に保存されました。")
