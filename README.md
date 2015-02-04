Status of GroundBIRD
--------------------

- URL: http://ahiru.kek.jp:8080/status (KEK internal only)

各ファイルの説明と使い方
------------------------

- status.py

    メインファイル. 端末から,

        $ python status.py
        
    として, ウェブサーバを立てると上記のアドレスからアクセスできる.

- status.tpl

    status.py のテンプレート.

- status_plots.py

    各期間 (hour/day/week/month) の温度を描写するスクリプト.
	crontab で運用する. ahiru では, 以下の設定にしている.

        */10 * * * *  nice -n 19 /home/hikaru/public_html/status/status_plots.py >/dev/null 2>&1

- todlib.py

    TOD (Time order data) を扱うクラス. status_plot.py の中で使う.
	Ref., https://github.com/i-hikaru/todlib.git

- monitor.py

    ステータスページに温度履歴 (保持時間と最低到達温度) を表示するスクリプト.

- monitor.sh

    monitor.py を操作して, tempHist.txt に追記するスクリプト.
	温度履歴をとる際は, monitor.py を直接叩くのではなく, こちらを使う.
	オプションや引数はとらずに, 次のようにする.

	    $ ./monitor.sh

- tempHist.txt

    monitor.py で生成した温度履歴.

- status_update.txt

    更新履歴.


ToDo
----

- Display He-10's heater current 
- Run status page on port 80 (Apache)
