<?php
    $container = $_GET['container'];
    $container = str_replace("'","\\'", $container);
    shell_exec("lxc stop '$container'");
    echo json_encode(true);
?>