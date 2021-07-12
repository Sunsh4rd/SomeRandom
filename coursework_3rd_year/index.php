<!DOCTYPE html>
<html>
<head>
	<title>Система подготовки к CTF</title>
	<style>		 
		html {
			font: 1em ubuntu;
    	}
    	body {
      		background:#fafafa;
      		margin:auto;
    	}
		h1 {
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
		ul.task-list {
			margin:auto;
			padding:0px;
			list-style:none;
			display:flex;
			justify-content:space-around;
			justify-content:center;
			flex-wrap: wrap;
		}
		ul.task-list li {
			background:white;
			width:350px;
			display:inline-block;
			padding:0px;
			position:relative;
			margin:5px;
			box-shadow:0 0 5px #000;
		}
		ul.task-list li:hover {
			box-shadow:0 0 15px #000;
		}
		ul.task-list li section {
			background: #fff;
			line-height:15px;
			padding:10px;
			margin:0px;
			border:1px #999;
			border-top:none;
		}
		ul.task-list li section p {
			text-align:justify;
			margin:0;
		}
		ul.task-list li section p:first-letter {
			padding-left:15px;
		}
		ul.task-list li header {
			margin:0px;
			line-height:30px;
			padding:10px;
			background:linear-gradient(30deg, #448, #77a);
			border:1px solid #999;
			border-bottom:none;
			font-size:24px;
			color:#fff;
			text-align:center;
		}
		ul.task-list a {
			border:1px solid #000;
			background:#448;
			border-radius:10px;
			display:block;
			width:110px;
			margin:10px;;
			padding:0;
			height:30px;
			color:#fff;
			text-decoration:none;
			font-size:20px;
			line-height:30px;
			text-align:center;
			float:right;
			box-shadow:0px 0px 6px #000;		
		}
		ul.task-list a:hover {
			background:#66a;
		}
		ul.task-list a:active {
			background:#88f;
		}
	</style>
</head>
<body>
	<h1>Тренировочные задачи:</h1>
	<?php 
		$tasks = scandir("tasks");
		echo "<ul class=\"task-list\">";
		for ($i = 0; $i < count($tasks); $i++) {
			if (($tasks[$i][0] === ".")) {
				continue;
			}
			$config = json_decode(file_get_contents("tasks/$tasks[$i]/config.json"), true);
			$taskName = $config["taskName"];
			$container = $config["container"];
			
			echo "<li>".
				  "<header>$taskName</header>".
				  "<section>";
				   include("tasks/$tasks[$i]/summary.php");
				   echo
				    "<a href=\"/task.php?name=$tasks[$i]\">Подробнее</a>".
				  "</section>".
				 "</li>";
		}
		echo "</ul>";
	?> 
</body>
</html>