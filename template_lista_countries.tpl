<!DOCTYPE html>
<html lang="es">
<head>
<title>Lista de libros</title>
<meta charset="utf-8" />
</head>
 
<body>
    <header>
       <h1>Paises y usuarios</h1>
    </header>
    <ul>
    % for pais in lista:
      <li> {{pais[0]}} {{pais[1]}} </li>
    % end
    </ul>    
</body>
</html>