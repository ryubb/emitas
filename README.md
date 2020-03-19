# emitas

## ローカルでの開発の仕方について

### dockerあり

git clone emitas
docker-compose up --build → 初めてcloneするとき、docker imageに変更が加えられたときに行う  
docker-compose up → 移行開発する場合はこちら
docker-compose exec web pipenv run migration  
docker-compose exec web pipenv run migrate  
docker-compose exec web pipenv run loaddata → ダミーデータの投入  
  
### dockerなし

pip install pipenv → pipenvのインストール  
git clone emitas
pipenv shell  
pipenv run local  
  
### pipでパッケージをインストールする方法

docker-compose exec web pipenv install [パッケージ名]  
ex.) docker-compose exec web pipenv install django  
  
### pipenvのコマンド一覧

pipenv run type-check 型のチェック  
pipenv run lint       コーディング規約チェック（flake8(pep8)に準拠）
pipenv run test       djangoのテストを実行  
  
## ディレクトリ構成について

pythonではアプリを作成する際、python manage.py startapp hoge とコマンドを打ち個別のアプリディレクトリを作成しているが、  
ディレクトリ構成がやや煩雑になること、アプリという単位でmodelやviewを分割すべきでないこと、などの理由により、上記のコマンドでアプリを作成しない  
その代わり、appディレクトリ配下のmodels, viewsディレクトリに固有のmodelやviewを追加していく  

|-app  
|  
|-config  
|  
|-  
  
## 開発ルールに関して

### コーディング規約

細かいコーディング規約はpep8に準拠  
  
リソースごとに、model, view, templateを定義  
ex.)Userリソースを作成する場合  
・model  
ファイル名： user_model.py  
クラス名：   UserModel  
  
※ 新しいモデルを追加したとき、今後の開発のためにもダミーデータを作成しておく方が望ましい  
そのため、initial_data.jsonに作成したモデルのダミーデータを作成する  
  
・view  
ファイル名： user_views.py  
クラス名：   UserXxxView  
  
・template  
Userディレクトリを作成し、その下にhtmlファイルを定義  
  
・form  
ファイル名： user_forms.py  
クラス名：   UserForm  
  
・test  
ファイル名： test_user_model.py, test_user_views.py  
クラス名：   TestUserModel, TestUserViews  
関数名：     test_hoge  
  
### CSSの記法

BEMを採用（ここら辺参照：<https://qiita.com/Takuan_Oishii/items/0f0d2c5dc33a9b2d9cb1）>  
BEMのルールをカスタムした、以下のルールを使用する  
　　
BlockとElementの区切りはアンスコ1個(_)  
ElementとModifierの区切りはハイフン1個 (-)  
Block, Element, Modifierで2つ以上の単語を表す場合は、キャメルケースで表す  
ModifierのKey, Valueの区切りは？？ → 検討中  
  
### ブランチ命名規約

ex.)feature/issue-xxx/create_admin_resource  
  →ブランチタイプ/イシュー番号/ブランチ名  
  
#### ブランチタイプ一覧

feature：新機能開発  
bugfix：バグ修正  
hotfix：緊急リリース対応  
release：リリースブランチ  
  