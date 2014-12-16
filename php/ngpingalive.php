<?

include("../cod/php/utils.php");

if(isset($_POST["usrID"]))
{
    $devID = $_POST["devID"];
    $usrID = $_POST["usrID"];
    mysql_query("update ngDevices set devLastPing=NOW() where devID=$devID)");
    echo "PINGACK";
}
else
{
    echo "NODATA";
}

?>
