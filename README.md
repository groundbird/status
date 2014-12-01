Status of GroundBIRD
--------------------

- URL: http://ahiru.kek.jp:8080/status (KEK internal only)

各ファイルの説明と使い方
------------------------

- status.py

    main file. 端末から,

        $ python status.py
        
    とすると, 上記のアドレスから現在のステータスが見られる.

- status.tpl

    status.py のテンプレート.

- status_plots.py

    各期間 (hour/day/week/month) の温度を描写するスクリプト. crontab で使う. 現在 ahiru では

        */10 * * * *  nice -n 19 /home/hikaru/public_html/status/status_plots.py >/dev/null 2>&1

    として, 10 分毎に図を描写している.

- todlib.py

    TOD (Time order data) を扱うクラス. status_plot.py の中で使う.

- monitor.py

    ステータスページに温度履歴 (保持時間と最低到達温度) を表示するためのスクリプト.

- monitor.sh

    monitor.py を操作して, tempHist.txt に追記するスクリプト. 温度履歴をとりたいときは, monitor.py を直接叩くのではなく, こちらを使う. オプションや引数はとらずに,

	    $ ./monitor.sh

    とすることで起動する.

- tempHist.txt

    monitor.py によってはきだされた温度履歴のテキストファイル.

- status_update.txt

    ステータスページの更新情報を記したテキストファイル.


ToDo
----

- Run status page on port 80 (Apache)
