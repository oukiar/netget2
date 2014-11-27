<?

include("../cod/php/utils.php");

if(isset($_POST["usrID"]))
{
    $usrID = $_POST["usrID"];
    $newnickname = $_POST["newnickname"];
    
    $result = mysql_query("update ngUsers set usrNickName='$newnickname' where usrID=$usrID");
    
    if($result)
    {
        echo "PROFILE_SAVED";
    }
    else
    {
        echo "ERROR_SAVING_PROFILE";
    }
}
else
{
    echo "NODATA";
}

?>
