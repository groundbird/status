# Status of GroundBIRD
- URL: http://ahiru.kek.jp:8080/status (KEK internal only)

# ファイルの説明と使い方
`status.py`
: He-10の状態をブラウザで確認するスクリプト.
	
`status.tpl`
: `status.py`のテンプレート.

`monitor.py`
: ステータスページにそれまでの温度履歴を表示するスクリプト.

`monitor.sh`
: `monitor.py`を操作して, `tempHist.txt`に追記するスクリプト.

`tempHist.txt`
: 温度履歴のテキストファイル.

`status_update.txt`
: ステータスページの更新情報.


## ToDo List
- Read data more smartly
- Run status page on port 80
