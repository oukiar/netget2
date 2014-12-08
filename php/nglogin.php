<?

include("../cod/php/utils.php");

if(isset($_POST["username"]))
{
    $usrUserName = $_POST["username"];
    $usrPassword = $_POST["password"];
    
    if(exists("ngUsers", "usrUserName", $usrUserName) )
    {
        $password = get_value('ngUsers', 'usrPassword', 'usrUserName', $usrUserName);
        $usrID = get_value('ngUsers', 'usrID', 'usrUserName', $usrUserName);
        $usrNickName = get_value('ngUsers', 'usrNickName', 'usrUserName', $usrUserName);
        
        if($usrPassword == $password)
        {
            //save the device ID
            $devID = $_POST["devID"];
            $deviceName = $_POST["deviceName"];
            
            
            
            echo "OK_LOGIN:$usrID:$usrNickName";
        }
        else
        {
            echo "PASSDIFF_LOGIN";
        }
    }
    else
    {
        echo "USERFAIL_LOGIN";
    }
}
else
{
    echo "NODATA";
}

?>
