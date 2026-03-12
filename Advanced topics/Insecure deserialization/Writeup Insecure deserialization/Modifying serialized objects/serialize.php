<?php
$desialize = 'O:4:"User":2:{s:8:"username";s:6:"wiener";s:5:"admin";b:0;}';
$serialized = serialize($desialize);
echo "Serialized: " . $serialized . "\n";
var_dump($desialize);
?>