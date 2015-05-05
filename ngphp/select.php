<?

include("utils.php");


$collection = $_POST["collection"];
$cols = $_POST["cols"];
$conditions = json_decode(str_replace("\\", "", $_POST["conditions"]));

/*
echo $_POST["conditions"];
echo urldecode($_POST["conditions"]);
echo str_replace("\\", "", $_POST["conditions"]);
var_dump( json_decode(str_replace("\\", "", $_POST["conditions"])) );
exit();
*/

$where = "";

foreach($conditions as $key => $val)
{
    if($key == "equalTo")
    {
        foreach($val as $subkey => $subval)
        {
            if($where != "") $where .= " and ";
            
            $where .= "$subkey='$subval' ";
        }
    }
}

$sql = "select $cols from $collection where $where";

$res = array();

if($result = $mysqli->query( $sql ))
{
    while($r = $result->fetch_assoc())
        array_push($res, $r);
}

echo json_encode( $res );
//echo $sql;
?>
