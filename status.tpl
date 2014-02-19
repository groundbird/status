<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<link rel="stylesheet" href="http://ahiru.kek.jp/~hikaru/css/style.css">
<script src="http://ahiru.kek.jp/~hikaru/js/jquery-1.6.1.min.js"></script>
<script src="http://ahiru.kek.jp/~hikaru/js/jquery.tablefix_1.0.1.js"></script>
<title>Status of GroundBIRD</title>
<script type="text/javascript">
// jquery.tablefix
$(function(){
  $('#tempHist').tablefix({
    width: 1024,
    height: 300,
    fixRows: 2
  });
});
</script>
</head>

<body>
<h1>Status of GroundBIRD</h1>

<h2>Temperature (He-10 Cooler)</h2>
<table>
  <thead>
    <tr id="tempTh">
      <th>Date</th><th>He3U Head [K]</th><th>He3I Head [K]</th><th>He4 Head [K]</th>
    </tr>
  </thead>
  <tr class="center">
  %for v in now:
    <td>{{v}}</td>
  %end
  </tr>
</table>


<p>
%for i in img:
  <a href="{{i}}"><img src="{{i}}" width=240></a>
%end
</p>


<h3>Temperature History</h3>

<table id="tempHist">
  <thead>
    <tr id="tempTh">
      <th>Date</th><th>He3U Head [K]</th><th>He3I Head [K]</th><th>He4 Head [K]</th><th>Hold Time [h]</th><th>Lowest Temp. [K]</th><th>State</th>
    </tr>
  </thead>
  <tfoot>
    <tr>
      <td></td>
    </tr>
  <tfoot>
  <tbody>
%for row in rows:
  <tr class="center">
  %for col in row:
    <td>{{col}}</td>
  %end
  </tr>
%end
  </tbody>
</table>

<div class="update" align="right">
<p>Last Modified: {{mod}}</p>

<p>Updates:</p>
<ul style="list-style-type: none">
%for list in lists:
  <li>{{list}}</li>
%end
</ul>
</div>

<hr>
<p class="update">&copy; 2013 The GroundBIRD Experiment</p>
</bod>
</html>
