<?

include("../cod/php/utils.php");

if(isset($_POST["usrID"]))
{
    $usrID = $_POST["usrID"];
    $contactID = $_POST["contactID"];
    
    //almacenar peticion de handshake
    mysql_query("insert into ngHandshakes values($usrID, $contactID)");
    
    //obtener las ips del usuario contacto
    $res = mysql_query("select devIP, udp_port from ngDevices where usrID=$contactID");
    
    $ips = array();
    
    while($row = mysql_fetch_row($res) )
    {
        array_push($ips, array("ip"=>$row[0], "port"=>$row[1]));
    }
    
    $jsonData = array();
    $jsonData["response"] = "HANDSHAKESAVED";
    $jsonData["contactID"] = $contactID;
    $jsonData["ips"] = $ips;
    
    
    echo json_encode($jsonData);
}
else
{
    echo "NODATA";
}

?>
