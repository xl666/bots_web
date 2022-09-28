# las rutas pueden tener espacios
ruta="$1"

comando "Este es un solo parámetro" "segundo param"

# muestra el valor de la variable, osea expande
echo "$ruta"

# imprime literalmente $ruta, no expande
echo '$ruta'
