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
        
        $res = mysql("select devIP from ngDevices where usrID=$contactID");
        
        $ips = array();
        
        while($row = mysql_fetch_row($res) )
        {
            array_push($ips, $row[0]);
        }
        
        $jsonData[$contactID] = $ips;
    }
    
    echo json_encode($jsonData);
    
}
else
{
    echo "NODATA";
}

?>
