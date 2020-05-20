<!DOCTYPE html>
<html lang="pt-br" dir="ltr">
    <head>
        <?php             
            include('inc/meta-header.php');

            error_reporting(E_ALL); 
            ini_set('display_errors', 1);
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

      
    </head>

    <body class="text-center">
        <div class="cover-container d-flex w-100 h-100 p-3 mx-auto flex-column">
            
            <main role="main" class="inner cover">
                <br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
                <h1 class="cover-heading"><?php print_r('Você pesquisou por '.$_REQUEST["search"].''); ?></h1>
                <p class="lead">A categoria da sua pergunta é: 
                <?php 
                    $json = file_get_contents('http://localhost:5000/api/v1/title?title='. htmlentities(urlencode($_REQUEST["search"]), ENT_QUOTES).'');
                    var_dump($json);
                ?>.
                </p>
            </main>

        </div>
    </body>
</html>