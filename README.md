# Language_culc
<img src="https://img.shields.io/badge/python-3.10.0-3776AB.svg?logo=python&style=plastic">&emsp;<img src="https://img.shields.io/badge/gensim-v4.3.3-99999.svg?logo=&style=plastic">&emsp;<img src="https://img.shields.io/badge/gdown-v5.2.0-ca97fc.svg?logo=&style=plastic">

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
`pyenv`を用いて、`python 3.10.0`をインストールし、適用。
```
pyenv install 3.10.0
pyenv local 3.10.0
```
設定後、`Language_culc.v1.0.0`に移動し、（カレントディレクトリに設定）仮想環境を作成。
```
cd your_path/Language_culc.v1.0.0
python -m venv myenv
```
※`your_path`は,`Language_culc.v1.0.0`をダウンロードしたディレクトリのこと。<br/>
`myenv`は、仮想環境名。任意で記入しても良いが、例として`myenv`にしている。<br/>
その後、ダウンロードすべきである`language_dateset3a.model.vectors.npy`を取得するため、[download_npy.py](Language_culc.v1.0.0/download_npy.py)を実行
```
python download_npy.py
```
また、仮想環境を反映（アクティベート）するために、以下のコマンドを入力。
```
source myenv/bin/activate
```
これを実行すると、
```
(myenv)username:~ user$
```
この画面が表示されたらアクティベートに成功したことになる。<br/>
ここに、`gdown`や、`gensim`といったライブラリをインストールする。
```
pip install gdown
pip install gensim
```
これを実行したら、環境構築は終了となる。
## how to use
本プロジェクトでは5つのpythonスクリプトが実行可能であり、以下の特性がある。
```
python vector.py
```
[vector.py](Language_culc.v1.0.0/vector.py)を実行すると、指定した単語のベクトルを取得することが可能となる。<br/>
※単語を指定するため上記コマンドを実行した後、単語の入力を行う。
```
python similar.py
```
[similar.py](Language_culc.v1.0.0/similar.py)を実行すると、指定した単語の似た単語を取得することが可能となる。
<br/>
※単語の指定をするため上記コマンドを実行した後、単語の入力を行う。<br/>
似ている単語を昇順に何個出力するかを指定できる。そのため、数値の入力が必要となる。<br/>
（但し、数値の入力が見られなかった場合、20個の単語が出力される。
```
python similarity.py
```
[similarity.py](Language_culc.v1.0.0/similarity.py)を実行すると、指定した２単語間の類似度を取得することが可能となる。<br/>
※２つの単語の指定をするため上記コマンドを実行した後、単語の入力を行う。<br/>
```
python add.py
```
[add.py](Language_culc.v1.0.0/add.py)を実行すると、指定した複数の単語を加法した単語を取得することが可能となる。<br/>
※複数の単語を指定するため上記コマンドを実行した後、単語の入力を行う。<br/>
指定した複数の単語は、半角コンマで区切る必要がある。<br/>
指定した複数の単語を合成した意味に最も近いものを昇順に何個出力するかを指定できるため、数値の入力が必要となる。<br/>
```
python subtraction.py
```
[subtraction.py](Language_culc.v1.0.0/subtraction.py)を実行すると、指定した複数の単語を減法した単語を取得することが可能になる。<br/>
※引かれる単語、引く単語の両者において複数の単語を指定できるため、上記コマンドを実行した後単語の入力を行う。<br/>
指定した単語は、半角コンマで区切る必要がある。<br/>
指定した複数の単語を減法した意味に最も近いものを何個出力するか指定できるため、数値の入力が必要である。
```
python meaningless.py
```
[meaningless.py](Language_culc.v1.0.0/meaninless.py)を実行すると、指定した単語の意味と最も異なるものを取得することが可能になる。<br/>
※指定した複数の単語を減法した意味に最も近いものを何個出力するか指定できるため、数値の入力が必要である。<br/>
出力された単語は、対義的なものではなくcos類似度の仕様上最も関連性のない単語が出力されます。

また、全てのスクリプトにおいて、指定した単語がデータベース内に含まれていなかった場合エラーを返す。<br/>
また、仕組みや学習法については[readme.pdf](description/readme.pdf)で詳しく記述している。<br/>
また、制作フローは[language_culc_makingflow.pdf](description/language_culc_makingflow.pdf)によって図示している。
## license
このプロジェクトは **MIT ライセンス** の下で提供される。  
ただし、本プロジェクトは以下のライブラリを利用している。

- **gensim** (ライセンス: LGPL-2.1-only)  
  https://github.com/RaRe-Technologies/gensim  

`gensim` は **LGPL-2.1-only** ライセンスのもとで提供され、  
本プロジェクトを使用するには `gensim` のライセンスに従う必要がある。

詳細なライセンス条文については、以下を確認。  
- [GNU Lesser General Public License v2.1](https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html)

- **gdown** (ライセンス: MIT)  
  https://github.com/wkentaro/gdown  

`gdown` は **MITライセンス** のもとで提供されており、そのライセンスの条件に従う必要がある。  

詳細については、以下を参照。  
- [MIT License](https://opensource.org/licenses/MIT)


　












