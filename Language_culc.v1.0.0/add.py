# -*- coding: utf-8 -*-

from gensim.models import KeyedVectors

def get_similar_words(model, positive_words, topn=20):
    try:
        # 類似単語を取得（足し算のみ）
        results = model.most_similar(positive=positive_words, topn=topn)
        
        # 結果を表示
        print("\nMost similar words:")
        for word, similarity in results:
            print(f"{word}: {similarity}")
    except KeyError as e:
        print(f"Error: {e}. この単語は学習モデルに存在しませんでした.")

def main():
    # モデルを読み込む
    model = KeyedVectors.load('language_dateset3a.model')

    # ユーザーから入力を受け取る
    positive_input = input("足したい単語を入力,ただし何個でも指定可能です。(半角コンマで区切ってください): ")
    topn_input = input("結果の単語を昇順に何個出力しますか。(デフォルト→20): ")

    # 入力を処理
    positive_words = [word.strip() for word in positive_input.split(',')]
    topn = int(topn_input) if topn_input else 20

    # 類似単語の取得
    get_similar_words(model, positive_words, topn)

if __name__ == "__main__":
    main()
