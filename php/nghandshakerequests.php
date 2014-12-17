<?

include("../cod/php/utils.php");

if(isset($_POST["usrID"]))
{
    $usrID = $_POST["usrID"];
    
    $result = mysql_query("select contactID from ngHandshakes 
                            where usrID=$usrID");
    
    $jsonData = array();
    
    while($row = mysql_fetch_row($result) )
    {
        $contactID = $row[0];
        
        #check if this user has online devices
        $res = mysql_query("select usrID from ngDevices where devLastPing > DATE_SUB(NOW(), INTERVAL 1 MINUTE) and usrID=$friendID ");
        
        if($res)
        {
            if($r = mysql_fetch_row($res))
            {
                $jsonData[$usrNickName] = $friendID;
            }
        }

    }
    
    echo json_encode($jsonData);
    
}
else
{
    echo "NODATA";
}

?>
