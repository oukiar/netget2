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
        $friendID = $row[1];
        
        #check if this user has online devices
        $res = mysql_query("select count(usrID) from ngDevices where devLastPing > DATE_SUB(NOW(), INTERVAL 1 MINUTE) and usrID=$friendID ");
        
        if($res)
        {
            if($r = mysql_fetch_row($res))
            {
                
                if($r[0])
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
