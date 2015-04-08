<?
$mysqli = new mysqli("localhost", "devsincc", "torusberry1986", "devsincc_ngcloud");
if ($mysqli->connect_errno) {
    echo "Failed to connect to MySQL: (" . $mysqli->connect_errno . ") " . $mysqli->connect_error;
}
//echo $mysqli->host_info . "\n";
//echo "Conexion correcta con la base de datos";
?>
