# Language_culc
<img src="https://img.shields.io/badge/python-3.10.0-3776AB.svg?logo=python&style=plastic"><img src="https://img.shields.io/badge/gensim-v4.3.3-99999.svg?logo=&style=plastic"><img src="https://img.shields.io/badge/gdown-v5.2.0-ca97fc.svg?logo=&style=plastic">

このプロジェクトは日本語の文章データを形態素解析により、分かち書きを行いword2vecを用いて単語のベクトル化を行う。
そして、ベクトル化した単語にcos類似度を適用することで複数単語の加法や減法、２単語間の相関関係及び最も意味の近しい単語を探すことのできる自然言語処理である。

This project uses morphological analysis of Japanese text data to create word vectors using word2vec.
Then, by applying cos similarity to the vectorized words, it is possible to add or subtract multiple words, examine the correlation between two words, or find words that are closest in meaning.

## How to set
まず、本プロジェクトの環境は、
- Python 3.10.0
- MacOS Sequoia 15.0.1(windowsでも可)
- gensim 4.3.3
- gdown 5.2.0
また、今回はMacOSでの実装について説明する。（その為、ターミナル内での実行）


最初に本プロジェクトをダウンロードし、`HomeBrew`をダウンロード。
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
`pyenv`(pythonのバージョン管理用ソフトウェア）をインストール。
```
brew install pyenv
```
シェルの設定ファイルに追記する為、以下のコマンドを実装。
```
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
```
`pyenv`を用いて、`python 3.10.0`をインストールし,適用。
```
pyenv install 3.10.0
pyenv local 3.10.0
```
設定後、`Language_culc.v1.0.0`に移動し、（カレントディレクトリに設定）仮想環境を作成。
```
cd your_path/Language_culc.v1.0.0
python -m venv myenv
```
※`your_path`は,`Language_culc.v1.0.0`をダウンロードしたディレクトリのこと。/
※`myenv`は、仮想環境名。任意で記入しても良いが例として`myenv`にしている。/
また、仮想環境を反映（アクティベート）するために、以下のコマンドを入力。
```
source myenv/bin/activate
```
これを行うと、
```
(myenv)username:~ user$
```
となり、これがアクティベートに成功したことの証明となる。










