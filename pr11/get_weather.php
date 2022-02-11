<?php
	$city=$b;
	$con = mysqli_connect("localhost","user1","12345","sample");
	$sql = "select * from weather where city='$city'";
	$result = mysqli_query($con,$sql);
	$row= mysqli_fetch_array($result);
	$high_temp=$row["high_temp"];
	$low_temp=$row["low_temp"];
	$rain_ratio=$row["rain_ratio"];
	$rain_mm=$row["rain_mm"];
	echo "<h3>$city";
	echo "의 날씨</h3>";
	echo "<span>최고 기온 $high_temp";
	echo "도</span><br/>";
	echo "<span>최저 기온 $low_temp";
	echo "도</span><br/>";
	echo "<span>비올 확률 $rain_ratio";
	echo "%</span><br/>";
	echo "<span>예상 강수량 $rain_mm";
	echo "mm</span><br/>";
	?>