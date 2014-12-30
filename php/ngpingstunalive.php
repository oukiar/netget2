<?

include("../cod/php/utils.php");

#for now, never delete, only delete under user demand
#mysql_query("delete from ngstunservers where lastupdate < DATE_SUB(NOW(), INTERVAL 1 DAY)");

$ip = $_SERVER["REMOTE_ADDR"];

mysql_query("update ngstunservers set lastupdate=NOW() where ip='$ip'");

echo $ip;


?>
