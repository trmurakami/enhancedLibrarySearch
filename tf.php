<!DOCTYPE html>
<html>

<head>
    <title>Previsão de Texto</title>
    <link rel="stylesheet" type="text/css" href="styles.css">
</head>

<body>
    <h1>Previsão de Texto</h1>
    <textarea id="text-input" placeholder="Digite o texto para prever"></textarea>
    <button onclick="predict()">Consultar</button>
    <div id="result"></div>

    <script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@3.9.0/dist/tf.js"></script>
    <script src="script.js"></script>
</body>

</html>