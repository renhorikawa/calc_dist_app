# ピクセル単位の距離を計算するツール

Pythonを使って簡単な操作でピクセル単位の距離を計算するツールです。主に超音波画像内での距離を計測する目的で作成しました。 

OSはWindowsでのみ動作確認をしています。

## 使い方手順
### 1. 実行環境の構築

#### プログラムのダウンロード

[こちら](https://github.com/renhorikawa/calc_dist_app/blob/main/calc_dist.py)のプログラムが保存されているページに移動します。
赤丸をクリックしてファイルをダウンロードします。
![demo3](https://github.com/renhorikawa/calc_dist_app/blob/main/assets/6.png)


#### コマンドプロンプトの起動とフォルダの移動
コマンドプロンプトは、コマンドを使ってプログラムを操作するためのツールです。Windowsでは、次の手順でコマンドプロンプトを起動できます。

検索窓でコマンドプロンプトを検索してクリックします。(Macの場合はターミナルを使用)
![demo1](https://github.com/renhorikawa/calc_dist_app/blob/main/assets/1.png)

コマンドプロンプトに「cd」と半角スペースを入れて、先ほど解凍したフォルダをドラッグ＆ドロップして下さい。（cdはフォルダを変更するコマンド）

![demo4](https://github.com/renhorikawa/calc_dist_app/blob/main/assets/5.png)


#### Pythonのインストール
Web上にインストール方法を説明するサイトが沢山ありますので、例えば[こちら](https://udemy.benesse.co.jp/development/python-work/python-install.html)を参考にしながらPythonをお使いのPCへインストールして下さい。


#### 仮想環境の作成
仮想環境は、プロジェクトに必要なライブラリ（必要な機能を提供するコードやツール）や依存関係を他のプロジェクトやシステム全体から隔離して管理するために使用します。

まずコマンドプロンプトに以下を入力・実行して仮想環境を作ります（ここでは「venv」という名前で仮想環境を作ります）。

```bash
python -m venv venv
```

仮想環境を実行します。

```bash
venv\Scripts\activate
```
仮想環境が立ち上がれば、以下のようになります。
![demo4](https://github.com/renhorikawa/calc_dist_app/blob/main/assets/7.png)

Macの場合、仮想環境実行のコマンドは以下となります。
```bash
source venv/bin/activate
```

#### 必要なライブラリのインストール

`pip`というライブラリをインストールするためのツールを最新の状態にアップグレードするため、コマンドプロンプトに以下を入力して実行します。
```bash
python -m pip install --upgrade pip
```

アップグレードできたら、ライブラリをインストールします。
```bash
pip install opencv-python 
```

### 2. その他、プログラム実行のために必要なもの

ご使用の超音波検査機器で一定間隔の距離を計測し、その画像を静止画保存します。下の画像のような形で保存してください。
![demo3](https://github.com/renhorikawa/calc_dist_app/blob/main/assets/8.jpg)


ファイルパスが長くなったり、複雑になるとプログラムが正しく動作しない場合があるので、動画ファイルは先ほど解凍したフォルダ内に入れておくことをお勧めします。

### 3. プログラムの実行
動画切り取りのプログラムを起動して実行します。

```bash
python calc_dist.py
```

### 4. プログラムの使用方法
1. プログラムを実行すると、「画像のパスを入力してください」と出ますのでファイル名を書いて実行します。  

2. 次に、「基準となる距離（mm）を入力してください」と出ますので、使用している機器に出力されている、指定した距離に該当する数値を入力してください。
  ![demo6](https://github.com/renhorikawa/calc_dist_app/blob/main/assets/2.jpg) 

3. するとウインドウが立ち上がりますので、下の図のように赤丸の距離の始点と終点の中心をクリックしてください。クリックした点が青丸で表示されます。
  ![demo6](https://github.com/renhorikawa/calc_dist_app/blob/main/assets/3.png) 

4. うまくいくと、コマンドプロンプトはこのような表示になっているはずです。クリックした座標2つの位置と、ピクセルとしての全距離、1ピクセルあたりの距離（mm）が出力されます。
  ![demo7](https://github.com/renhorikawa/calc_dist_app/blob/main/assets/4.png) 

   <br> 
   ※途中で止める場合には、コマンドプロンプト上で「Ctrl + C」キーを入力してプログラムを終了してください。


### 5. プログラムを次に使う場合の注意点
- コマンドプロンプトの起動、cdコマンドを使ってのフォルダ移動、仮想環境の実行（作成は不要）は毎回必要です。

## お問い合わせ

何か質問やご意見があれば、[renhoript@gmail.com](mailto:renhoript@gmail.com) までお気軽にお知らせください。
