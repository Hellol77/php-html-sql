<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="UTF-8" />
	<meta http-equiv="X-UA-Compatible" content="IE=edge" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
	<title>Document</title>
</head>

<body>
	<?php 
	if(isset($_POST["unit2"])){
		$b = $_POST["unit2"];
		}
		else{
			$b = "과천";
		}
		?>
	<h3>수도권 날씨예보</h3>
	<form action="<?php echo $_SERVER['PHP_SELF'] ;?>" method="post" name="form1" onfocus="this.select()">
		<select name="unit2" id="city" onchange="this.form.submit(); ">
			<option value="과천" <?php if($b=="과천") echo " selected" ;?>>과천</option>
			<option value="서울" <?php if($b=="서울") echo " selected" ;?>>서울</option>
			<option value="성남" <?php if($b=="성남") echo " selected" ;?>>성남</option>
			<option value="수원" <?php if($b=="수원") echo " selected" ;?>>수원</option>
			<option value="용인" <?php if($b=="용인") echo " selected" ;?>>용인</option>
			<option value="인천" <?php if($b=="인천") echo " selected" ;?>>인천</option>
		</select>
		<label>의 날씨는?</label>

	</form>
	<?php include "get_weather.php"?>
</body>
<script>
function onFocus() {
	document.getElementById("city").focus();
}
onFocus();
</script>

</html>