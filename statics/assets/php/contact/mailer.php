<?php

include '../email.php';

$nameForm = $_POST['nameForm'];
$emailForm = $_POST['emailForm'];
$phoneForm = $_POST['phoneForm'];
$subjectForm = $_POST['subjectForm'];
$messageForm = $_POST['messageForm'];

$mailheader = "From:".$nameForm."<".$emailForm.">\r\n";
$mailheader .= "MIME-Version: 1.0\r\n";
$mailheader .= "Content-Type: text/html; charset=ISO-8859-1\r\n";

$htmlContent = "<strong>Full Name: </strong> ".$nameForm."<br><br>";
$htmlContent .= "<strong>Email Address: </strong> ".$emailForm."<br><br>";
$htmlContent .= "<strong>Phone Number: </strong> ".$phoneForm."<br><br>";
$htmlContent .= "<strong>Subject: </strong> ".$subjectForm."<br><br>";
$htmlContent .= "<strong>Message: </strong> <br>".nl2br($messageForm)."<br><br><br><br><br><br>";

$htmlContent .= "-------------------------------------------<br>";
$htmlContent .= "Note: this email is sent from your website!";

mail($recipient, $subjectForm, $htmlContent, $mailheader) or die("Error!");


echo'Email Sent';

?>