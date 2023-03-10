# Todo-
インターン課題

# 概要
Todoアプリ。カレンダーやジャンル分けされたタスクリストを用意することで視認性を高めようとしています。

# デモ
## 以下アプリの実行手順です。

Runserver すると最初にログインページが表示されます。

基本的な想定としては、
ログインページ→メニューページと遷移することを考えています。そのメニューページ内では、タスクの登録、確認、更新を行うページへのリンクを並べています。

初回にはログインページの下にあるリンクから遷移するサインアップページから登録を行う作業が入ります。初回登録時には登録終了後自動的にメニューページにリダイレクトします。

メニューページの、全部は全てのタスクを、
大学、趣味、仕事、その他は登録したタスクがそれぞれ対応するcategory(データベース内のジャンル分けをするために設けているもの)であった場合に、
対応するタスクを表示するページです。(ジャンル分けはタスクの更新時に行います。そのためタスクの登録をしただけでは“戻る”以外表示されません)

タスクの登録はscheduleCalendarというURL先のページから行います。カレンダーを選択、もしくは範囲選択することで登録するタスクの名前を入力するポップアップが表示され、
入力しokすることでタスクの登録を行います。また、このページはタスクをカレンダーで確認するページも兼ねています。

また、メニューページの下部からログアウト出来るようになっています。

# 環境
- python 3.6
- MySQL 5.7
- Django
- phpmyadmin

# 注意事項
M1 MACだと"No matching manifest for linux/arm64/v8 in the manifest list entries"と出て上手く動作しない場合があるようです。
その際には、お手数ですが"docker-composed.yml"のdb:の部分に、"platform: linux/x64"を追加してください。
