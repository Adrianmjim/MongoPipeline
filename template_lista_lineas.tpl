<!DOCTYPE html>
<html lang="es">
<head>
<title>Lista de libros</title>
<meta charset="utf-8" />
</head>
 
<body>
    <header>
       <h1>Promedio de lineas por pedido en cada pais</h1>
    </header>
    <ul>
    % for pais in lista:
      <li> {{pais['_id']}} {{pais['lineas']}} </li>
    % end
    <li> Numero de entradas {{len(lista)}}</li>
    </ul>    
</body>
</html>