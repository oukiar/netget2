<?

include("../cod/php/utils.php");

if(isset($_POST["usrID"]))
{
    $usrID = $_POST["usrID"];
    $friendID = $_POST["friendID"];
    
    $result = mysql_query("insert into ngRelationships values('$usrID', '$friendID')");
    
    if($result)
    {
        echo "CONTACT_ADDED";
    }
    else
    {
        echo "ERROR_ADDING_CONTACT";
    }
}
else
{
    echo "NODATA";
}

?>
