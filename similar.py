# -*- coding: utf-8 -*-

from gensim.models import KeyedVectors

def get_similar_words(model, word, topn=20):
    try:
        # 類似単語を取得
        results = model.most_similar(word, topn=topn)
        
        # 結果を表示
        print(f"\nMost similar words to '{word}':")
        for word, similarity in results:
            print(f"{word}: {similarity}")
    except KeyError as e:
        print(f"Error: {e}. この単語は学習モデルに存在しませんでした.")

def main():
    # モデルを読み込む
    model = KeyedVectors.load('language_dateset3a.model')

    # ユーザーから入力を受け取る
    word_input = input("似た単語を探したい単語を入力: ")
    topn_input = input("似ている単語を昇順に何個出力しますか (デフォルト→20): ")

    # 入力を処理
    topn = int(topn_input) if topn_input else 20

    # 類似単語の取得
    get_similar_words(model, word_input, topn)

if __name__ == "__main__":
    main()
