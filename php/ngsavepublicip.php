<?

include("../cod/php/utils.php");

if(isset($_POST["devID"]))
{
    #for now, never delete, only delete under user demand
    #mysql_query("delete from ngDevices where devLastPing < DATE_SUB(NOW(), INTERVAL 1 DAY)");
    
    $devID = $_POST["devID"];
    
    /*
    if( ! exists('ngDevices', 'devID', $devID) )
    {
        //save the device ID
        $deviceName = $_SERVER["REMOTE_HOST"];
        $deviceIP = $_SERVER['REMOTE_ADDR'];
        
        mysql_query("insert into ngDevices(devName, devIP, devLastPing) values('$deviceName', '$deviceIP', NOW())");
        
        $devID = mysql_insert_id();
    }*/
    
    if($devID != "-1")
    {
        $ip = $_POST["ip"];
        $port = $_POST["port"];
        mysql_query("update ngDevices set devIP='$ip', udp_port=$port where devID=$devID");
        echo "ADDRESS_SAVED:$devID";
    }
    else
    {
        echo "Not devID to save: -1";
    }
}
else
{
    echo "NODATA";
}

?>
