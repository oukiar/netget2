<?

include("../cod/php/utils.php");

if(isset($_POST["email"]))
{
    $usrNickName = $_POST["username"];
    $usrUserName = $_POST["username"];
    $usrPassword = $_POST["password"];
    $usrEmail = $_POST["email"];
    
    if(exists("ngUsers", "usrEmail", $usrEmail) )
    {
        echo "EMAIL_EXISTS";
        exit();
    }
    else if(exists("ngUsers", "usrUserName", $usrUserName) )
    {
        echo "USER_EXISTS";
        exit();
    }
    
    $result = mysql_query("insert into ngUsers(usrNickName, usrUserName, usrPassword, usrEmail) 
                                        values('$usrNickName', '$usrUserName', '$usrPassword', '$usrEmail')");
                                        
    if($result)
    {
        echo "OK";
        mail($usrEmail, "Welcome to netget network", "Hi $usrNickName.</br>Login data:");
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
