<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<link rel="stylesheet" href="http://ahiru.kek.jp/~hikaru/css/style.css">
<script src="http://ahiru.kek.jp/~hikaru/js/jquery-1.6.1.min.js"></script>
<script src="http://ahiru.kek.jp/~hikaru/js/jquery.tablefix_1.0.1.js"></script>
<script src="http://ahiru.kek.jp/~hikaru/js/jquery.todate.js"></script>
<title>Status of GroundBIRD</title>
<script type="text/javascript">
// jquery.tablefix
$(function() {
  $('#tempHist').tablefix({width: 1000, height: 151, fixRows: 1});
});

// jquery.todate
// http://shanabrian.com/web/jquery/date01.php
$(document).ready(function() {
  $('#now').toDate({
    format: 'w, M d, Y at H:i:s (JST)'
  });
});
</script>
</head>
<body>

<h1>Status of GroundBIRD</h1>

<table class="info-header">
  <tr><td>Data:</td><td id="now"></td></tr>
  <tr><td>Comment:</td><td>各温度表示は 1 分毎、プロットは 10 分毎に更新されます。プロットは順に、1 (時間|日|週間|ヶ月) の期間です。</td></tr>
</table>

<h2>Temperature (He-10)</h2>

<table>
  <thead>
    <tr><th rowspan="2">Date</th><th colspan="3">Temperature [K]</th></tr>
    <tr id="tempTh">
      <th>He3U head</th>
      <th>He3I head</th>
      <th>He4 head</th>
    </tr>
  </thead>
  <tr class="center">
  %for v in now:
    <td>{{ v }}</td>
  %end
  </tr>
</table>

<p>
%for i in img[:4]:
  <a href="{{ i }}"><img src="{{ i }}" width=240 class="grow"></a>
%end
</p>

<h2>Temperature (GM)</h2>

<table>
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
    <td class="tempTd">{{v}}</td>
  %end
  </tr>
</table>

<p class="fig-align">
% i = 0
%for fig in imgGM:
  %if i == 0:
  <a href="{{ fig }}"><img src="{{ fig }}" width=240 class="grow grow-left"></a>
  %elif i == 3:
  <a href="{{ fig }}"><img src="{{ fig }}" width=240 class="grow grow-right"></a>
  %else:
  <a href="{{ fig }}"><img src="{{ fig }}" width=240 class="grow"></a>
  %end
  % i += 1
%end
</p>

<p>指定した時間範囲の各温度をプロットできます。時間は「2014 年 10 月 20 日 15 時 00 分」であれば、「2014-10-20-1500」とします。各末尾は省略可能です。<br>（注意）プロットするまでに 1 分以上かかる場合があります。自分でデータを料理したい人は<a href="http://ahiru.kek.jp/~hikaru/status/usage_todlib.html">こちら</a>を参照してください。</p>
<form method="GET" action="/status#plot">
<p>begin: </code><input type="text" value="2014-10-20-15" name="start"> end: <input type="text" value="2014-10-20-16" name="end"> <input type="submit" value="Plot"></p>
</form>
<p></p>

%if requestPlot:
  <p id="plot"><a href="{{ requestPlot }}"><img src="{{ requestPlot }}"></a></p>
%end


<h2>Temperature History (He-10)</h2>

<table id="tempHist">
<!-- <table> -->
  <thead>
  <!-- <thead class="fixed-header"> -->
    <!-- <tr id="tempTh"> -->
    <tr>
      <th>Date</th><th>He3U head [K]</th><th>He3I head [K]</th><th>He4 head [K]</th><th>Hold time [h]</th><th>Lowest temp. [K]</th><th>State</th>
      <!-- <th class="date">Date</th><th class="temp">He3U head [K]</th><th class="temp">He3I head [K]</th><th class="temp">He4 head [K]</th><th>Hold time [h]</th><th>Lowest temp. [K]</th><th>State</th> -->
    </tr>
  </thead>
  <!-- <tfoot> -->
  <!--   <tr> -->
  <!--     <td></td> -->
  <!--   </tr> -->
  <!-- </tfoot> -->
  <tbody>
  <!-- <tbody class="scroll-body"> -->
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
<p>Last Modified: {{ mod }}</p>

<p>Updates:</p>
<ul class="update-log">
%for l in lists:
  <li>{{ l }}</li>
%end
</ul>
</div>

<hr>
<p class="update">&copy; 2014 The GroundBIRD Experiment</p>
</body>
</html>
