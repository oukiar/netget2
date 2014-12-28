<?

include("../cod/php/utils.php");


#select the server
$res = mysql_query("select ip from ngstunservers where lastupdate > DATE_SUB(NOW(), INTERVAL 1 MINUTE) ");

if($res)
{
    if($r = mysql_fetch_row($res))
    {
        $ip = $r[0];
    }
}

echo $ip;

?>
