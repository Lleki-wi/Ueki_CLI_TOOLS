うえき(TwitterID:@Ll_e_ki)です　こんにちは

CLIに住まわせているツール類を公開してみましたへへへ

## 初期設定
Python3でsetup_uekirc.pyを実行し、その後に表示されるコマンドを実行してください。（[your rcfile]は~/.bashrcなどで置き換えてください）

## 環境
.pyプログラムは全てPython3での実行を想定しています
あとなのですが、これ、ディレクトリを動かすたびにsetup_uekirc.pyを動かさないとなので頑張ってください

## コマンドの一覧と使用方法
### ベータじゃないです！
- lprime
  - 引数に渡された整数が素数かどうかを判定します
- lec
  - 引数を2つ渡した場合、第一引数の文字列を第二引数回繰り返した文字列を改行なしで出力します。引数が3つの場合、第二引数の文字列を第三引数回繰り返した文字列について、末尾に改行を挿入して出力します
- lpat
  - 第一引数に指定した長さのパターン文字列を出力します

### ベータです！！！
- lrotn（[web版](https://lleki-wi.github.io/about_ueki/webtools/rotn)）
  - 第一引数に渡された文のアルファベット部分のみを第二引数に渡された値分シフトします

### 非推奨コマンドです（動作はします）
- lmorse （[推奨版（web）](https://lleki-wi.github.io/about_ueki/webtools/morse_code_translator)）
  - 第一, 第二, 第三引数に渡された文字をそれぞれ短音, 長音, 区切り文字と解釈し、第一引数に渡された文をモールス信号からアルファベットにデコードします


ではよいCLIライフを！！！さようなら...
