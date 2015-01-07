<?

include("../cod/php/utils.php");

if(isset($_POST["email"]))
{
    $usrNickName = $_POST["username"];
    $usrUserName = $_POST["username"];
    $usrPassword = $_POST["password"];
    $usrEmail = $_POST["email"];
    $deviceName = $_POST["deviceName"];
    
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
          
    $usrID = mysql_insert_id();
    
    //save the user's machine
    $deviceIP = $_SERVER['REMOTE_ADDR'];
    
    mysql_query("insert into ngDevices(devName, devIP, devLastPing, usrID) values('$deviceName', '$deviceIP', NOW(), $usrID)");
    
    $devID = mysql_insert_id();
                                        
    if($result)
    {
        //FIXME: respuesta con campos separados por :   reemplazar por json si se cree pertinente
        echo "OK:$usrID:$usrNickName:$devID";
        
        //TODO: Mejorar el formato del email.
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
