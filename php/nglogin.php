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
            
            if($_POST["devID"] == -1)
            {
                //save the device ID
                $deviceName = $_POST["deviceName"];
                $deviceIP = $_SERVER['REMOTE_ADDR'];
                
                mysql_query("insert into ngDevices(devName, devIP, devLastPing, usrID) values('$deviceName', '$deviceIP', NOW(), $usrID)");
                
                $devID = mysql_insert_id();
            }
            else
            {
                $deviceName = $_POST["deviceName"];
                $deviceIP = $_SERVER['REMOTE_ADDR'];
                
                //try to verify the devID
                $devID = $_POST["devID"];
                
                if(exists("ngDevices", "devID", $devID) )
                {
                    mysql_query("update ngDevices set devIP='$deviceIP', devLastPing=NOW() where devID=$devID");
                }
                else
                {
                    mysql_query("insert into ngDevices(devName, devIP, devLastPing, usrID) values('$deviceName', '$deviceIP', NOW(), $usrID)");
                
                    $devID = mysql_insert_id();
                }
            }
            
            
            echo "OK_LOGIN:$usrID:$usrNickName:$devID";
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
