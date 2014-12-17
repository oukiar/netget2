<?

include("../cod/php/utils.php");

if(isset($_POST["usrID"]))
{
    $usrID = $_POST["usrID"];
    $contactID = $_POST["contactID"];
    
    mysql_query("insert into ngHandshakes values($usrID, $contactID)");
    
    echo "HANDSHAKESAVED:$usrID:$contactID";
}
else
{
    echo "NODATA";
}

?>
