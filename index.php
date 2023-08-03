<!DOCTYPE html>
<html lang="pt-br" dir="ltr">

<head>
    <?php
        include('inc/meta-header.php');
    ?>
    <!-- Load TensorFlow.js -->
    <script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@latest/dist/tf.min.js"></script>
    <title>Classificador de SDGs</title>

</head>

<body>
    <div class="jumbotron">
        <div class="container bg-light p-5 rounded mt-5">
            <h1 class="display-5">Classificador de SDGs</h1>
            <p><?php echo $branch_description; ?></p>

            <div class="ml-container">
                <label for="search" class="form-label">Digite título e resumo</label>
                <textarea class="form-control" id="userInput" rows="6"
                    placeholder="Digite um título e resumo em inglês"></textarea>
                <div id="submit-button">
                    <button type="submit" class="btn btn-primary mt-2" id="predict-btn" disabled=True>Predict!</button>
                </div>
            </div>

            <table id="predictions-table" class="table mt-5">
                <tr>
                    <th>Exemplo</th>
                    <th>Classe Mais Provável</th>
                    <th>Probabilidade</th>
                    <th>Top 3 Classes</th>
                </tr>
            </table>

        </div>
    </div>


    <script src="./index.js"></script>
</body>

</html>