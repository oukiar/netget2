<?
include("utils.php");

$fields = "";
$fields2 = "";
$values = "";

$tablename = $_POST["varname"];
unset($_POST["varname"]);

$newobj = array();

//CREATE TABLE PART
foreach($_POST as $key => $val)
{
    if($fields != "")
    {
        $fields .= ",";
        $fields2 .= ",";
        $values .= ",";
    }
    
    $newobj[$key] = $val;
        
    if($key == "objectId")
    {
        $fields .= "$key INTEGER AUTO_INCREMENT NOT NULL PRIMARY KEY, ";
        $fields .= "createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, ";
        $fields .= "updatedAt TIMESTAMP ";
        
        $fields2 = substr($fields2, 0, strlen($fields2)-1); 
        $values = substr($values, 0, strlen($values)-1); 
        
        $objectId = $val;
        continue;
    }
    

    $fields .= "$key TEXT";
    $fields2 .= "$key";
    $values .= "'$val'";

}

$fields2 .= ", updatedAt";
$values .= ", NOW()";


if($objectId == "-1")
{
    $sql_createtable = "CREATE TABLE $tablename($fields)";
    
    //try to create table
    if($mysqli->query( $sql_createtable ) )
    {
        //Only for if you need to know if was created or not
        ;
    }
    //else
    //    echo "ErrorCreateTable: $sql_createtable";

    //INSERT THE NEW OBJECT
    $sql = "insert into $tablename($fields2) values($values)";

    if($mysqli->query( $sql ) )
    {
        $newobj["objectId"] = mysqli_insert_id($mysqli);
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
