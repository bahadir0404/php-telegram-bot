<?php
$botToken = "YOUR_BOT_TOKEN_HERE";
$apiUrl = "https://api.telegram.org/bot" . $botToken;
$update = file_get_contents("php://input");
$update = json_decode($update, true);
$chatId = $update["message"]["chat"]["id"];
$message = $update["message"]["text"];
if ($message == "/start") {
    $response = "Salom! Men sizning botman.";
    file_get_contents($apiUrl . "/sendMessage?chat_id=" . $chatId . "&text=" . urlencode($response));
}
?>
