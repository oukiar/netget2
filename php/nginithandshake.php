<?

include("../cod/php/utils.php");

if(isset($_POST["usrID"]))
{
    $usrID = $_POST["usrID"];
    $contactID = $_POST["contactID"];
    
    mysql_query("insert into ngHandshakes values($usrID, $contactID)");
    
    //obtener las ips del usuario contacto
    $res = mysql_query("select devIP from ngDevices where usrID=$contactID");
    
    $ips = array();
    
    while($row = mysql_fetch_row($res) )
    {
        array_push($ips, $row[0]);
    }
    
    
    echo "HANDSHAKESAVED:$ips";
}
else
{
    echo "NODATA";
}

?>
