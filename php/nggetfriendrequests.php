<?

include("../cod/php/utils.php");

if(isset($_POST["usrID"]))
{
    $usrID = $_POST["usrID"];
    
    //obtenemos todos los contactos que me tienen como amigo
    $result = mysql_query("select usrID from ngRelationships where friendID=$usrID");
    
    $jsonData = array();
    
    while($row = mysql_fetch_row($result))
    {
        $friendID = $row[0];
        
        //verificamos si tenemos amistad con esta persona
        $res = mysql_query("select friendID from ngRelationships where usrID=$usrID and friendID=$friendID");
        
        if($row2 = mysql_fetch_row($res))
        {
            ;
        }
        else
        {
            array_push($jsonData, $friendID);
        }
        
    }
    
    echo json_encode($jsonData);
}
else
{
    echo "NODATA";
}

?>
