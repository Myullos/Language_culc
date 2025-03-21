# -*- coding: utf-8 -*-

from gensim.models import KeyedVectors

def get_word_vector(model, word):
    try:
        # 単語のベクトル値を取得
        vector = model[word]
        print(f"\nVector representation of '{word}':\n{vector}\n")
    except KeyError as e:
        print(f"Error: {e}. この単語は学習モデルに存在しませんでした.")

def main():
    # モデルを読み込む
    model = KeyedVectors.load('language_dateset3a.model')
    
    # ユーザーから入力を受け取る
    word_input = input("ベクトルを取得したい単語を入力: ")
    
    # 単語のベクトル表示
    get_word_vector(model, word_input)

if __name__ == "__main__":
    main()
