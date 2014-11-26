<?

include("../cod/php/utils.php");

if(isset($_POST["txt_search"]))
{
    $txt_search = $_POST["txt_search"];
    
    //Usuarios
    $sql = "";
    
    //dividimos el texto de busqueda en palabras
    $tokens = split(' ', $txt_search);
    
    //recorremos cada palabra para ir formando la sentencia sql
    foreach($tokens as $i)
    {
        if($sql == "")
            $sql = "select usrNickName, usrID from ngUsers where usrNickName like '%$i%' ";
        else
            $sql += " and usrNickName like '%$i%'";
    }
    
    $result = mysql_query($sql);
    
    $jsonData = array();
    
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
