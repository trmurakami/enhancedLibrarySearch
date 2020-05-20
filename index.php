<!DOCTYPE html>
<html lang="pt-br" dir="ltr">
    <head>
        <?php             
            include('inc/meta-header.php');
        ?> 
        <title>Busca</title>
        <!-- Facebook Tags - START 
        <meta property="og:locale" content="pt_BR">
        <meta property="og:url" content="< ?php echo $url_base ?>">
        <meta property="og:title" content="< ?php echo $branch ?> - Página Principal">
        <meta property="og:site_name" content="< ?php echo $branch ?>">
        <meta property="og:description" content="< ?php echo $branch_description ?>">
        <meta property="og:image" content="< ?php echo $facebook_image ?>">
        <meta property="og:image:type" content="image/jpeg">
        <meta property="og:image:width" content="800"> 
        <meta property="og:image:height" content="600"> 
        <meta property="og:type" content="website">
        Facebook Tags - END -->

        <style>
            .bd-placeholder-img {
            font-size: 1.125rem;
            text-anchor: middle;
            -webkit-user-select: none;
            -moz-user-select: none;
            -ms-user-select: none;
            user-select: none;
            }
            @media (min-width: 768px) {
            .bd-placeholder-img-lg {
                font-size: 3.5rem;
            }
            }
            .jumbotron {
            background-image: url("<?php echo $background_1 ?>");
            background-size: 100%;
            background-repeat: no-repeat;            
            }    
        </style>
        
    </head>

    <body>
        <div class="jumbotron">
            <div class="container bg-light p-5 rounded mt-5">
                <h1 class="display-5">Pesquisar</h1>
                <p><?php echo $branch_description; ?></p>

                <form class="mt-3" action="result.php">                
                    <div class="input-group">                    
                        <input type="text" name="search" class="form-control" id="searchQuery" aria-describedby="searchHelp" placeholder="Pergunte algo sobre a Biblioteca?">
                        <div class="input-group-append">
                            <button type="submit" class="btn btn-primary">Pesquisar</button>
                        </div>
                    </div>                       
                    <small id="searchHelp" class="form-text text-muted">Atualmente só estão classificadas as categorias HORARIO e NORMALIZAÇÃO.</small>
                </form>

            </div>
        </div>
    </body>
</html>