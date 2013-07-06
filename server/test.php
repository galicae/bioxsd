<?php

//echo "test";
echo shell_exec('ls -l');
mkdir("testMKDIR");
file_put_contents("testMKDIR/blub.txt","Hi, im a file");
echo("DONE");
?>
