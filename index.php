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
            <h1 class="display-5">Classificador de SDGs <a href="https://www.un.org/sustainabledevelopment/"
                    target="_blank"><img src="images/SDG.png" width="80px"></a></h1>
            <p>
                <a href="https://www.un.org/sustainabledevelopment/poverty" target="_blank" nofollow><img
                        src="images/SDG01.png" alt="SDG icons" width="80px"></a>
                <a href="https://www.un.org/sustainabledevelopment/hunger" target="_blank" nofollow><img
                        src="images/SDG02.png" alt="SDG icons" width="80px"></a>
                <a href="https://www.un.org/sustainabledevelopment/health" target="_blank" nofollow><img
                        src="images/SDG03.png" alt="SDG icons" width="80px"></a>
                <a href="https://www.un.org/sustainabledevelopment/education" target="_blank" nofollow><img
                        src="images/SDG04.png" alt="SDG icons" width="80px"></a>
                <a href="https://www.un.org/sustainabledevelopment/gender-equality" target="_blank" nofollow><img
                        src="images/SDG05.png" alt="SDG icons" width="80px"></a>
                <a href="https://www.un.org/sustainabledevelopment/water-and-sanitation" target="_blank" nofollow><img
                        src="images/SDG06.png" alt="SDG icons" width="80px"></a>
                <a href="https://www.un.org/sustainabledevelopment/energy" target="_blank" nofollow><img
                        src="images/SDG07.png" alt="SDG icons" width="80px"></a>
                <a href="https://www.un.org/sustainabledevelopment/economic-growth" target="_blank" nofollow><img
                        src="images/SDG08.png" alt="SDG icons" width="80px"></a>
                <a href="https://www.un.org/sustainabledevelopment/infrastructure-industrialization" target="_blank"
                    nofollow><img src="images/SDG09.png" alt="SDG icons" width="80px"></a>
                <a href="https://www.un.org/sustainabledevelopment/inequality" target="_blank" nofollow><img
                        src="images/SDG10.png" alt="SDG icons" width="80px"></a>
                <a href="https://www.un.org/sustainabledevelopment/cities" target="_blank" nofollow><img
                        src="images/SDG11.png" alt="SDG icons" width="80px"></a>
                <a href="https://www.un.org/sustainabledevelopment/sustainable-consumption-production" target="_blank"
                    nofollow><img src="images/SDG12.png" alt="SDG icons" width="80px"></a>
                <a href="https://www.un.org/sustainabledevelopment/climate-change" target="_blank" nofollow><img
                        src="images/SDG13.png" alt="SDG icons" width="80px"></a>
                <a href="https://www.un.org/sustainabledevelopment/oceans" target="_blank" nofollow><img
                        src="images/SDG14.png" alt="SDG icons" width="80px"></a>
                <a href="https://www.un.org/sustainabledevelopment/biodiversity" target="_blank" nofollow><img
                        src="images/SDG15.png" alt="SDG icons" width="80px"></a>
                <a href="https://www.un.org/sustainabledevelopment/peace-justice" target="_blank" nofollow><img
                        src="images/SDG16.png" alt="SDG icons" width="80px"></a>
                <a href="https://www.un.org/sustainabledevelopment/globalpartnerships" target="_blank" nofollow><img
                        src="images/SDG17.png" alt="SDG icons" width="80px"></a>
            </p>

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