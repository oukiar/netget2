<?

include("../cod/php/utils.php");

if(isset($_POST["username"]))
{
    $usrUserName = $_POST["username"];
    $usrPassword = $_POST["password"];
    
    if(exists("ngUsers", "usrUserName", $usrUserName) )
    {
        $password = get_value('ngUsers', 'usrPassword', 'usrUserName', $usrUserName);
        
        if($usrPassword == $password)
        {
            echo "OK_LOGIN";
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
