<?php 
 
//$link = mysql_connect('natorgnet.fatcowmysql.com', 'plusultra', 'la440880'); 
//$link = mysql_connect('localhost', 'devsincc', 'dexware86'); 
//$link = mysql_connect('localhost', 'root', 'root'); 
$link = mysql_connect('localhost', 'orgboat', '6318c7C654'); 
//$link = mysql_connect('localhost', 'root', ''); 


if (!$link) 
{ 
    die('Could not connect: ' . mysql_error()); 
} 


//if(mysql_select_db("devsincc_plusultra") == false)
//if(mysql_select_db("main") == false)
if(mysql_select_db("orgboat") == false)
{
    echo "Error seleccionado en base de datos";
}

function exists($table, $field, $value)
{
        $result = mysql_query("select count($field) from $table where $field='$value'");
 
        $row = mysql_fetch_row($result);
        
        if($row[0] > 0)
                return true;
        else
                return false;
}
 
function get_value($table, $selected_field, $field, $value)
{
    try 
    {
        $result = mysql_query("select $selected_field from $table where $field='$value'");
        
        if($row = mysql_fetch_row($result) )
        {
            return $row[0];
        }
        else
        {
            return -1;
        }
    }
    catch (Exception $e) 
    {
        echo 'Excepción capturada: ',  $e->getMessage(), "\n";
        var_dump(debug_backtrace());
    }

}   

function get_count($table, $selected_field, $conditionfield, $value)
{
    $result = mysql_query("select count($selected_field) from $table where $conditionfield='$value'");
    
    if($row = mysql_fetch_row($result) )
    {
        return $row[0];
    }
    else
    {
        return -1;
    }
}

//obtiene el maximo de un campo (sin condicion) ... util para obtener
//el ID del ultimo registro insertado
//outdated: Para obtener el ultimo registro usar: mysql_insert_id();
//el proposito de esta funcion sique siendo valido
function get_max($table, $selected_field)
{
    $result = mysql_query("select max($selected_field) from $table");
    
    if($row = mysql_fetch_row($result) )
    {
        return $row[0];
    }
    else
    {
        return -1;
    }
}

//Determina si un usuario es administrador de su organizacion (si pertenece a la division directives)
function is_admin($usrID)
{
    $usrDivID = get_value('usrTable', 'divID', 'usrID', $usrID);
    $orgID = get_value('divTable', 'orgID', 'divID', $usrDivID);
    
    //obtener el divID de la tabla directives
    $result = mysql_query("select divID from divTable where orgID='$orgID' and (divName='Directives' or divName='Directors') ");
    
    if($row = mysql_fetch_row($result) )
    {
        if($usrDivID == $row[0])
            return true;
    }
    
    return false;
}

//Determina si un usuario es superior directo de otro usuario
function is_superior($superiorID, $usrID)  
{
    //get the division of the user
    $usrSuperiorID = get_value('usrTable', 'usrSuperiorID', 'usrID', $usrID);
    
    //check if the relationsship  exists
    if( $usrSuperiorID == $superiorID )
    {
        return true;
    }
    else
    {
        return false;
    }
}

//Determina si un usuario es superior directo o indirecto de otro usuario
function is_superior_superior($superiorID, $usrID)  
{
    //get the division of the user
    $usrSuperiorID = get_value('usrTable', 'usrSuperiorID', 'usrID', $usrID);
    
    //check if the relationsship  exists
    if( $usrSuperiorID == $superiorID )
    {
        return true;
    }
    else
    {
        return false;
    }
}

/*
//retorna True si el usuario es el asignado como superior de su division
function is_division_superior($usrID)
{
    //get the division of the user
    $usrDivID = get_value('usrTable', 'divID', 'usrID', $usrID);
    
    //get the usrID of the superior of the division
    $superiorDivID = get_value('divTable', 'divSuperiorID', 'divID', $usrDivID);
        
    if($superiorDivID == $usrID)
        return true;
    else 
        return false;
}
* */

//retorna True si el usuario es el asignado como superior de su division
function is_superior_of_division($usrID, $divID)
{   
    $is_sup = get_value('usrTable', 'isDivisionSuperior', 'usrID', $usrID);
    $_divID = get_value('usrTable', 'divID', 'usrID', $usrID);
    
    if($is_sup && $_divID == $divID)
        return true;

    return false;
}

function alert($msg)
{
    echo "<script>alert('$msg');</script>";
}

function str_to_date($strdate)
{
    if($strdate[4] == '-')
        return $strdate;
    
    list($month, $day, $year) = split('[/.-]', $strdate);
    return "$year-$month-$day";
}

?>
