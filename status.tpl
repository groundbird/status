<!DOCTYPE html>
<html lang="ja">
  <head>
    <meta charset="UTF-8">
    <link rel="shortcut icon" href="http://faviconist.com/icons/5e45ee788465a3f2a8f1375450c1ce5f/favicon.ico" />
    <link rel="stylesheet" href="http://ahiru.kek.jp/~hikaru/css/style.css">
    <script src="http://ahiru.kek.jp/~hikaru/js/jquery-1.6.1.min.js"></script>
    <script src="http://ahiru.kek.jp/~hikaru/js/jquery.tablefix_1.0.1.js"></script>
    <script src="http://ahiru.kek.jp/~hikaru/js/jquery.todate.js"></script>
    <title>Status of GroundBIRD</title>
    <script type="text/javascript">
      // jquery.tablefix
      $(function() {
        $('#tempHist').tablefix({width: 1000, height: 152, fixRows: 1});
      });

      // jquery.todate
      // ref., http://shanabrian.com/web/jquery/date01.php
      $(document).ready(function() {
        $('#now').toDate({
        format: 'w, M j, Y at H:i:s (JST)'
        });
      });
    </script>
  </head>
<body>

<h1>Status of GroundBIRD</h1>

<table class="info-header">
  <tr>
    <td>Date:</td>
    <td id="now"></td>
  </tr>
  <tr><td>Comment:</td>
    <td>各温度表示は 1 分毎、プロットは 10 分毎に更新されます。プロットする期間は、順に、1 (時間|日|週間|ヶ月) です。</td>
  </tr>
</table>

<h2>Temperatures</h2>

<h3>He-10</h3>

<table cellspacing="0">
  <thead>
    <tr>
      <th rowspan="3">Date</th>
      <th colspan="10">Temperature [K]</th>
    </tr>
    <tr>
      <th colspan="3" class="left-line">Head</th>
      <th class="left-line">FB</th>
      <th colspan="3" class="left-line">Pump</th>
      <th colspan="3" class="left-line">SW</th>
    </tr>
    <tr id="tempTh">
      <th class="left-line">He3U</th>
      <th>He3I</th>
      <th>He4</th>
      <th class="left-line">He4</th>
      <th class="left-line">He4</th>
      <th>He3I</th>
      <th>He3U</th>
      <th class="left-line">He4</th>
      <th>He3I</th>
      <th>He3U</th>
    </tr>
  </thead>
  <tr class="center">
  %j = 0
  %for v in temp_He10:
  %if len(v) > 7:
  <td class="tempTd">{{ v }}</td>
  %elif (j == 1 or j == 4 or j == 5 or j == 8):
  <td class="tempTd left-line">
    {{ "{0:.3f}".format(float(v)) }}
  </td>
  %else:
  <td class="tempTd">{{ "{0:.3f}".format(float(v)) }}</td>
  %end
  %j += 1
  %end
  </tr>
</table>

<h4>log-scale</h4>
<p class="fig-align">
  %i = 0
  %for fig in imgHe10_log:
  %if i == 0:
  <a href="{{ fig }}"><img src="{{ fig }}" width=240 class="grow grow-left"></a>
  %elif i == 3:
  <a href="{{ fig }}"><img src="{{ fig }}" width=240 class="grow grow-right"></a>
  %else:
  <a href="{{ fig }}"><img src="{{ fig }}" width=240 class="grow"></a>
  %end
  %i += 1
  %end
</p>

<h4>linear-scale</h4>
<p class="fig-align">
  %i = 0
  %for fig in imgHe10_linear:
  %if i == 0:
  <a href="{{ fig }}"><img src="{{ fig }}" width=240 class="grow grow-left"></a>
  %elif i == 3:
  <a href="{{ fig }}"><img src="{{ fig }}" width=240 class="grow grow-right"></a>
  %else:
  <a href="{{ fig }}"><img src="{{ fig }}" width=240 class="grow"></a>
  %end
  %i += 1
  %end
</p>

<h3>PTC</h3>

<table cellspacing="0">
  <thead>
    <tr><th rowspan="2">Date</th><th colspan="8">Temperature [K]</th></tr>
    <tr id="tempTh">
      <th>ch. 0</th>
      <th>ch. 1</th>
      <th>ch. 2</th>
      <th>ch. 3</th>
      <th>ch. 4</th>
      <th>ch. 5</th>
      <th>ch. 6</th>
      <th>ch. 7</th>
    </tr>
  </thead>
  <tr class="center">
  %for v in temp_GM:
    %if isinstance(v, str):
      <td class="tempTd">{{ v }}</td>
    %else:
      <td class="tempTd">{{ "{0:.3f}".format(float(v)) }}</td>
    %end
  %end
  </tr>
</table>

<h4>log-scale</h4>
<p class="fig-align">
  %i = 0
  %for fig in imgGM_log:
  %if i == 0:
  <a href="{{ fig }}"><img src="{{ fig }}" width=240 class="grow grow-left"></a>
  %elif i == 3:
  <a href="{{ fig }}"><img src="{{ fig }}" width=240 class="grow grow-right"></a>
  %else:
  <a href="{{ fig }}"><img src="{{ fig }}" width=240 class="grow"></a>
  %end
  %i += 1
  %end
</p>

<h4>linear-scale</h4>
<p class="fig-align">
  %i = 0
  %for fig in imgGM_linear:
  %if i == 0:
  <a href="{{ fig }}"><img src="{{ fig }}" width=240 class="grow grow-left"></a>
  %elif i == 3:
  <a href="{{ fig }}"><img src="{{ fig }}" width=240 class="grow grow-right"></a>
  %else:
  <a href="{{ fig }}"><img src="{{ fig }}" width=240 class="grow"></a>
  %end
  %i += 1
  %end
</p>

<p>指定した時間範囲の各温度をプロットできます。時間の指定は、「2014 年 10 月 20 日 15 時 00 分」であれば、「2014-10-20-1500」とします。各末尾は省略可能です。<br><small>（注意）プロットするまでに 1 分以上かかる場合があります。自分でデータを料理したい人は<a href="http://ahiru.kek.jp/~hikaru/status/usage_todlib.html">こちら</a>を参照してください。</small></p>
<form method="GET" action="/status#plot">
<p>begin: <input type="text" value="2014-10-20-15" name="start"> end: <input type="text" value="2014-10-20-16" name="end"> <input type="submit" value="Plot"></p>
</form>
%if requestPlot:
  <p id="plot"><a href="{{ requestPlot }}"><img src="{{ requestPlot }}"></a></p>
%end

<h3>History (He-10 head)</h3>

<table id="tempHist">
  <thead>
    <tr>
      <th>Date</th>
      <th>He3U head [K]</th>
      <th>He3I head [K]</th>
      <th>He4 head [K]</th>
      <th>Hold time [h]</th>
      <th>Lowest temp [K]</th>
      <th>State</th>
    </tr>
  </thead>
  <tbody>
    %for row in rows:
    <tr class="center">
      %for col in row:
      <td>{{ col }}</td>
      %end
    </tr>
    %end
  </tbody>
</table>

<div class="update" align="right">
  <p class="update-li">Last Modified: {{ mod }}</p>
  <p class="update-li">Updates:</p>
  <ul class="update-log">
    %for l in lists:
    <li class="update-li">{{ l }}</li>
    %end
  </ul>
</div>

<hr class="update-hr">
<p class="update">&copy; 2014&ndash;2015 The GroundBIRD experiment. Powered by <a href="http://bottlepy.org/">Bottle</a>.</p>
</body>
</html>
