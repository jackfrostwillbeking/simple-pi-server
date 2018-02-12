# pi-server-isaax
A simple web server using isaax

# Usage

1. このリポジトリをForkしてください。
2. Forkしたリポジトリを[isaaxのプロジェクトとして登録](https://isaax.io/app/new)してください。
3. RaspberryPiにログインし、`curl -fsSL get.isaax.io | sudo bash -s stable my_token`コマンドを実行してデバイスを登録してください。  
`my_token`の部分はプロジェクトトークンに置き換えてください。
4. `http://<RaspberryPiのIPアドレス>:5000` にアクセスしてください。画面に**Cannot load the env** というメッセージが表示されます。
5. クラスターをクリックし、**環境変数タブ** --> **ユーザー変数** --> **環境変数追加** をクリックしてください。
6. 名を`MESSAGE`、タイプを**文字**に設定し、値に「Hello World」を入力します。
7. クラスターをクリックし「再起動」ボタンを押します。
8. `http://<RaspberryPiのIPアドレス>:5000` にアクセスしてください。画面に**Hello World** というメッセージが表示されたのを確認できます。
