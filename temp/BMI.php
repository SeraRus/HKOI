<?php
$valid = true;

if (empty($_POST['height'])) {
    $valid = false;
} elseif ($_POST['height'] > 10) {
    $_POST['height'] /= 100;
}

if (empty($_POST['weight'])) {
    $valid = false;
}

if ($valid) {
    $bmi = round($_POST['weight'] / ($_POST['height'] ** 2), 1);
    echo "你的BMI是$bmi";
} else {
    echo "請完整填寫身高體重";
}

echo "<p><form method=\"post\" action=\"20240417bmi01.html\">
<input type=\"submit\" name=\"submit\" value=\"返回\">
</form></p>";