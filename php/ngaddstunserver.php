<?

include("../cod/php/utils.php");

if(isset($_POST["machinename"]))
{
    $machinename = $_POST["machinename"];
    $ip = $_SERVER['REMOTE_ADDR'];
    #$port = $_SERVER['REMOTE_PORT'];
    $port = $_SERVER['31415'];
    
    $result = mysql_query("insert into ngstunservers(servername, ip, port, lastupdate) values('$machinename', '$ip', '$port', NOW())");
    
    if($result)
    {
        echo "SERVER_REGISTERED";
    }
    else
    {
        echo "ERROR_SAVING_SERVER";
    }
}
else
{
    echo "NODATA";
}

?>
