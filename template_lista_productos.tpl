<!DOCTYPE html>
<html lang="es">
<head>
<title>Lista de libros</title>
<meta charset="utf-8" />
</head>
 
<body>
    <header>
       <h1>Ventas de cada producto</h1>
    </header>
    <ul>
    % for producto in lista:
      <li> {{producto[0]}} {{producto[1]}} {{producto[2]}} </li>
    % end
    </ul>    
</body>
</html>