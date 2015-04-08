<?
include("utils.php");

$fields = "";
$fields2 = "";
$values = "";

$tablename = $_POST["varname"];
unset($_POST["varname"]);

$newobj = {};

//CREATE TABLE PART
foreach($_POST as $key => $val)
{
    if($fields != "")
    {
        $fields .= ",";
        $fields2 .= ",";
        $values .= ",";
    }
    
    $newobj[$key] = val;
        
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
        //Only for if you need to know if was created or not
        ;
    }

    //INSERT THE NEW OBJECT
    $sql = "insert into $tablename($fields2) values($values)";

    if($mysqli->query( $sql ) )
    {
        echo json_encode($newobj);
    }
    else
    {
        echo "Fail";
    }
}
else
{
    //update object
    
}

?>
