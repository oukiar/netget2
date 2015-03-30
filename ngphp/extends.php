<?
include("utils.php");

$fields = "";
$fields2 = "";
$values = "";

$tablename = $_POST["varname"];
unset($_POST["varname"]);

//CREATE TABLE PART
foreach($_POST as $key => $val)
{
    if($fields != "")
    {
        $fields .= ",";
        $fields2 .= ",";
        $values .= ",";
    }
        
    if($key == "objectId")
    {
        $fields .= "$key INTEGER AUTO_INCREMENT NOT NULL PRIMARY KEY";
        
        $fields2 = substr($fields2, 0, strlen($fields2)-1); 
        $values = substr($values, 0, strlen($values)-1); 
        
        $objectId = $val;
        continue;
    }
    
    $fields .= "$key TEXT";
    $fields2 .= "$key";
    $values .= "'$val'";
}

if($objectId == "-1")
{
    //try to create table
    if($mysqli->query( "CREATE TABLE $tablename($fields)" ) )
    {
        echo "New,";
    }
    else echo "Fail,";

    //INSERT THE NEW OBJECT
    $sql = "insert into $tablename($fields2) values($values)";

    if($mysqli->query( $sql ) )
    {
        echo "Created";
    }
    else
    {
        echo "Fail: $sql";
    }
}
else
{
    //update object
    
}

?>
