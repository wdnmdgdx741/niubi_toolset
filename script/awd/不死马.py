<?php
while (1) {
    $pid=1064661;
    @unlink('shell.php');
    exec('kill -9 $pid');
}
?>