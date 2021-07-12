<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Основные команды Linux</title>
    <style>
        html {
			font: 1em ubuntu;
    	}
    	body {
      		background:#fafafa;
      		margin:auto;
    	}
        h2 {
			margin-top:0px;
			background: #338;
			box-shadow: 0px 0px 10px;
			text-align:center;
			color:white;
			margin:0px;
			line-height:30px;
			padding:10px;
			background:linear-gradient(30deg, #448, #77a);
			font-size:24px;
			text-align:center;
		}
        ul {
            margin:auto;
            padding:0px;
            list-style:none;
            max-width:700px;
        }
        li {
            background:white;
            max-width:700px;
			display:block;
			padding:15px 0 0 10px;
			position:relative;
			margin:5px;
			border-top: 1px solid lightgrey;
            border-left: 5px solid #aaf;
            margin-top:20px;
        }
        li:hover {
            border-left-color: #448;
        }
        section {
            padding:5px ;
        }
        .main {
            background: white;
            max-width: 700px;
            margin: auto;
            padding: 15px 10px; 
        }
    </style>
</head>
<body>

<?php
    $task = $_GET['name'];
    $config = json_decode(file_get_contents("tasks/$task/config.json"), true);
    $taskName = $config["taskName"];
    $container = $config["container"];
    $status = trim(shell_exec("lxc info $container | grep Status | grep -o Running"));
?>

<h2><?=$taskName?></h2>

<section class="main">

<?php
    include("tasks/$task/summary.php");
?>

<button class="btn btn-success" id="run" <?=$status === "" ? "" : "disabled"?>>Запустить</button>
<button class="btn btn-danger" id="stop" <?=$status !== "" ? "" : "disabled"?>>Остановить</button>
<hr>

<?php
    include("tasks/$task/description.php");
?>
</section>

<script>
    function init(run, stop, action) {
        document.getElementById(run).onclick = () => {
            let req = new XMLHttpRequest();
            req.responseType = 'json';
            req.open('GET', `/${action}.php?container=<?= $container?>`, true);
            console.log('request');
            document.getElementById(run).disabled=true;
            req.onload = (response) => {
                console.log('response', req.response);
                document.getElementById(stop).disabled=false;
            };
            req.send();
        }   
    }
    init("run", "stop", "start-container");
    init("stop", "run", "stop-container");
</script>
</body>