<?

include("../cod/php/utils.php");

if(isset($_POST["usrID"]))
{
    
    $usrID = $_POST["usrID"];
    
    $result = mysql_query("select usrID from ngHandshakes where contactID=$usrID");
    
    $jsonData = array();
    
    while($row = mysql_fetch_row($result) )
    {
        $contactID = $row[0];
        
        $res = mysql_query("select devIP, udp_port from ngDevices where usrID=$contactID");
        
        $ips = array();
        
        while($row = mysql_fetch_row($res) )
        {
            array_push($ips, array("ip"=>$row[0], "port"=>$row[2]));
        }
        
        $jsonData[$contactID] = $ips;
    }
    
    //remove all sended requests
    mysql_query("delete from ngHandshakes where contactID=$usrID");
    
    echo json_encode($jsonData);
    
}
else
{
    echo "NODATA";
}

?>
