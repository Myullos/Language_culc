import os
from gensim.models import word2vec
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
save_dir = "your_path"
save_path = os.path.join(save_dir, "language_dateset3a.model")

if not os.path.exists(save_dir):
    os.makedirs(save_dir)
    logging.info(f"ディレクトリ '{save_dir}' を作成しました。")

sentences = word2vec.Text8Corpus('language_culc_wakati_comp.txt')

model = word2vec.Word2Vec(sentences, vector_size=200, min_count=5, window=15,sg=0,hs=0,negative=10,epochs=10,workers=8)
model.wv.save_word2vec_format (save_path, binary=True)
logging.info(f"モデルを '{save_path}' に保存しました。")
