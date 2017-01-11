<!DOCTYPE html>
<html lang="es">
<head>
<title>Lista de libros</title>
<meta charset="utf-8" />
</head>
 
<body>
    <header>
       <h1>Rango de edad en paises con un minimo de usuarios</h1>
    </header>
    <ul>
    % for pais in lista:
      <li> {{pais['_id']}} {{pais['rango']}} </li>
    % end
    <li> Numero de resultados: {{len(lista)}}</li>
    </ul>    
</body>
</html>