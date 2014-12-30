<?

include("../cod/php/utils.php");

if(isset($_POST["devID"]))
{
    #for now, never delete, only delete under user demand
    #mysql_query("delete from ngDevices where devLastPing < DATE_SUB(NOW(), INTERVAL 1 DAY)");
    
    $devID = $_POST["devID"];
    $usrID = $_POST["usrID"];
    mysql_query("update ngDevices set devLastPing=NOW() where devID=$devID");
    echo "PINGACK:$devID";
}
else
{
    echo "NODATA";
}

?>
