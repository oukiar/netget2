<?

include("../cod/php/utils.php");

if(isset($_POST["usrID"]))
{
    $usrID = $_POST["usrID"];
    
    $result = mysql_query("select usrNickName, usrID from ngUsers 
                            where usrID in (select friendID from ngRelationships 
                                                where usrID=$usrID)");
    
    $jsonData = array();
    
    while($row = mysql_fetch_row($result) )
    {
        $usrNickName = $row[0];
        $usrID = $row[1];
        
        #check if this user has online devices
        $res = mysql_query("select usrID from ngDevices where devLastPing > DATE_SUB(NOW(), INTERVAL 5 MINUTE) and usrID=$usrID ");
        
        if($res)
        {
            if($r = mysql_fetch_row($res))
            {
                $jsonData[$usrNickName] = $usrID;
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
