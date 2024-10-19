# My AtCoder Answer

## コマンド一覧
- `accsetup`: AtCoderのアカウントでログインする
- `accnew {contestID}`: {contestID}のテストデータを取得する
- `accsw {problemName}`: 問題{problemName}に移動する
- `acct`: テストケースを実行する
- `accs`: 回答を提出する

### 備考
Docker環境において、`/etc/bash.bashrc`を`./.bashrc.local`で上書きすることによってコマンドを使えるようにしている

## 使用ライブラリ
- atcoder-cli (`acc`)
- online-judge-tools (`oj`)

## ディレクトリ構造
- [archive](./archive/) には、自動化ツールを使う前の回答を格納
- [contest](./contest/) には、自動化ツールを使った回答を格納
