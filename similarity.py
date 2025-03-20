# -*- coding: utf-8 -*-

from gensim.models import KeyedVectors

def calculate_similarity(model, word1, word2):
    try:
        # 2つの単語間の類似度を計算
        similarity = model.similarity(word1, word2)
        return similarity
    except KeyError as e:
        print(f"Error: 一つもしくは両方の単語が学習モデルに存在しませんでした. ({e})")
        return None

def main():
    # モデルを読み込む
    model_path = 'language_dateset3a.model'  # ここにWord2Vecのモデルのパスを指定してください
    model = KeyedVectors.load(model_path)

    # ユーザーから単語の入力を受け取る
    word1 = input("一つ目の単語を入力: ").strip()
    word2 = input("二つ目の単語を入力: ").strip()

    # 類似度の計算
    similarity = calculate_similarity(model, word1, word2)
    
    if similarity is not None:
        print(f"２単語の類似度 '{word1}' and '{word2}' is: {similarity}")
    else:
        print("計算することができませんでした.")

if __name__ == "__main__":
    main()
