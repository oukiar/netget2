<?

include("../cod/php/utils.php");

if(isset($_POST["usrID"]))
{
    $usrID = $_POST["usrID"];
    
    $result = mysql_query("select usrNickName, usrID from ngUsers 
                            where usrID in (select friendID from ngRelationships where usrID=$usrID)");
    
    $jsonData = array('RES':'OK');
    
    while($row = mysql_fetch_row($result) )
    {
        $usrNickName = $row[0];
        $usrID = $row[1];
        
        $jsonData[$usrNickName] = $usrID;
    }
    
    echo json_encode($jsonData);
    
}
else
{
    echo "NODATA";
}

?>
