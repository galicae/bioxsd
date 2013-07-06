<?php

$XML_decl = '<?xml version="1.0" encoding="UTF-8" standalone="no" ?>'."\n";
$xmlns_msg = "xmlns:msg=\"http://alex.tbl/webservice/disulfinder\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"http://alex.tbl/webservice/disulfinder/RESTdisulfinder http://alex.tbl/webservice/disulfinder/disulfinder_rest.wsdl\"";


$a = substr($_SERVER["PATH_INFO"],0,1);
if(substr($_SERVER["PATH_INFO"], 0, 1) == '/')
{
	$operation = substr($_SERVER["PATH_INFO"], 1);
	switch($operation)
	{
	case "getDsBonds":
	case "getVersion":
		header("Content-Type: application/xml"); // http://www.w3.org/TR/wsdl20-adjuncts/#_http_operation_xml_encoding
		break;
	}

	try{
		error_reporting(E_ALL);
		switch($operation)
		{
			case "getDsBonds":
				$dsBonds = NULL;
				// <getContactsRequest> is in php://input
				$getDisulfinderRequest_string = file_get_contents("php://input");
				if(!$getDisulfinderRequest_string) throw new Exception('no request in POST message body');
				error_log($getDisulfinderRequest_string);

				$input_alignment_string = NULL;
				$dom = new DOMDocument();
				$dom->loadXML($getDisulfinderRequest_string);
				//$reqElem = $dom->documentElement;
				$seqElem = $dom->getElementsByTagNameNS('http://rostlab.org/disulfinder/input', 'sequence')->item(0);
				//$dom->replaceChild($aliElem, $reqElem);

				//$schloc = $dom->createAttributeNS('http://www.w3.org/2001/XMLSchema-instance', 'xsi:schemaLocation');
				//$schloc->value = "http://rostlab.org/freecontact/input http://rostlab.org/~lkajan/freecontact_input.xsd";
				//$aliElem->appendChild($schloc);

				//error_log($dom->saveXML());

				$time_ms = microtime(true);
				$tmpFolder = "tmp/" . $time_ms;
				$outFolder = $tmpFolder."/out";
				mkdir($tmpFolder,0755);
				mkdir($outFolder,0755);
				// write input file
				$inFile = $tmpFolder . "/sequence.fasta";
				file_put_contents($inFile,$seqElem->nodeValue);

				// execute disulfinder
				$out = shell_exec("disulfinder -f ".$inFile." -o ".$outFolder." -r ".$tmpFolder." -d /data/uniprot_sprot -c");
				error_log($out);
				$handle = opendir($outFolder);
				
				$outFile = $outFolder."/".readdir($handle);
				closedir($handle);
				error_log($outFile); 
				// parseOutput
				$parseOut = shell_exec("./disulfxml -i " .$outFile." -o ".$tmpFolder."/sequence.xml");
				error_log($parseOut);
				
				//return output
				$dsOutputXML = file_get_contents($tmpFolder."/sequence.xml");


				
				if($dsOutputXML != NULL)
				{
					echo $XML_decl;
					printf("<msg:getDisulfinderResponse $xmlns_msg>%s</msg:getDisulfinderResponse>\n", trim($dsOutputXML));
				}
				else throw new Exception('not results from disulfinder');
				break;

			case "getVersion":
				$dsVersion = exec('/usr/bin/disulfinder --version 2>&1', $out, $dsVersion);
				
				if($dsVersion != NULL)
				{
					echo $XML_decl;
					printf("<msg:getVersionResponse $xmlns_msg>%s</msg:getVersionResponse>\n", htmlspecialchars(trim($dsVersion)));
				}
				else throw new Exception('failed to pipe from disulfinder');
				break;
			default:
				phpinfo();
		}
	}
	catch (Exception $e) {
		// Fault: return disulfinder Error element and HTTP code 500
		header('HTTP/1.1 500 Internal Server Error');
		echo $XML_decl;
		printf("<msg:disulfinderError $xmlns_msg>error: %s</msg:disulfinderError>", $e->getMessage());
	}
}

// vim:syntax=php
?>
