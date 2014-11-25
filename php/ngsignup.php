<?

include("../cod/php/utils.php");

if(isset($_POST["email"]))
{
    $usrNickName = $_POST["username"];
    $usrUserName = $_POST["username"];
    $usrPassword = $_POST["password"];
    $usrEmail = $_POST["email"];
    
    $result = mysql_query("insert into ngUsers(usrNickName, usrUserName, usrPassword, usrEmail) 
                                        values('$usrNickName', '$usrUserName', '$usrPassword', '$usrEmail')");
                                        
    if($result)
    {
        echo "OK";
    }
    else
    {
        echo "FAIL";
    }
}
else
{
    echo "NODATA";
}

?>
