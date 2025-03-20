# -*- coding: utf-8 -*-

from gensim.models import KeyedVectors

def get_similar_words_by_subtraction(model, positive_words, negative_words, topn=20):
    try:
        # 引き算（negative引数を使う）による類似単語の取得
        results = model.most_similar(positive=positive_words, negative=negative_words, topn=topn)
        
        # 結果を表示
        print(f"\nMost similar words to the result of subtraction:")
        for word, similarity in results:
            print(f"{word}: {similarity}")
    except KeyError as e:
        print(f"Error: {e}. この単語は学習モデルに存在しませんでした.")

def main():
    # モデルを読み込む
    model = KeyedVectors.load('language_dateset3a.model')

    # ユーザーから入力を受け取る
    positive_input = input("引かれる単語を入力、ただし何個でも指定可能です。（半角コンマで区切ってください）: ")
    negative_input = input("引かれる単語を入力、ただし何個でも指定可能です。(半角コンマで区切ってください): ")
    topn_input = input("結果の単語を昇順に何個出力しますか (デフォルト→20): ")

    # 入力を処理
    positive_words = [word.strip() for word in positive_input.split(',')]
    negative_words = [word.strip() for word in negative_input.split(',')]
    topn = int(topn_input) if topn_input else 20

    # 引き算による類似単語の取得
    get_similar_words_by_subtraction(model, positive_words, negative_words, topn)

if __name__ == "__main__":
    main()
