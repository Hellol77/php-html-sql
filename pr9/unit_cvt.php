<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<style>
table {
	border: 4px solid red;
	border-collapse: collapse;
	text-align: center;
}

tr {
	border: 1px solid red;
}

td {
	border: 1px solid red;
	width: 200px;
}
</style>

<body>
	<?php 
		$a = $_POST["number"];
		$b = $_POST["unit2"];
		?>
	<h3>단위 변환기 :
		<?= $a?> <?= $b?>
	</h3>
	<table>
		<?php
		if($b == "미터(m)" ){
		$in = round($a * 39.370079,4);
		$ft = round($a * 3.28084,4);
		$yd = round($a * 1.093613,4);
		echo "<tr>";
			echo "<td>$a 미터(m)</td>";
			echo "<td>$in 인치(in)</td>";
			echo "</tr>";
			echo "<tr>";
			echo "<td>$ft 피트(ft)</td>";
			echo "<td>$yd 야드(yd)</td>";
			echo "</tr>";
		}
		elseif($b == "인치(in)"){
		$m = round($a * 0.0254,4);
		$ft = round($a * 0.083333,4);
		$yd = round($a * 0.027778,4);
		echo "<tr>";
			echo "<td>$m 미터(m)</td>";
			echo "<td>$a 인치(in)</td>";
			echo "</tr>";
			echo "<tr>";
			echo "<td>$ft 피트(ft)</td>";
			echo "<td>$yd 야드(yd)</td>";
			echo "</tr>";
		
		
		}
		elseif($b == "피트(ft)"){
		$m = round($a * 0.3048,4);
		$in = round($a * 12,4);
		$yd = round($a * 0.333333,4);
		echo "<tr>";
			echo "<td>$m 미터(m)</td>";
			echo "<td>$in 인치(in)</td>";
			echo "</tr>";
			echo "<tr>";
			echo "<td>$a 피트(ft)</td>";
			echo "<td>$yd 야드(yd)</td>";
			echo "</tr>";
		
		}
		elseif($b == "야드(yd)"){
		$m = round($a * 0.9144,4);
		$in = round($a * 36,4);
		$ft = round($a * 3,4);
		echo "<tr>";
			echo "<td>$m 미터(m)</td>";
			echo "<td>$in 인치(in)</td>";
			echo "</tr>";
			echo "<tr>";
			echo "<td>$ft 피트(ft)</td>";
			echo "<td>$a 야드(yd)</td>";
			echo "</tr>";
		}
		?>
	</table>
</body>

</html>