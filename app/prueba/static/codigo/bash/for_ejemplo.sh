for fruta in manzana pera mango; do
    echo "$fruta"
done

separador=$IFS
IFS=""
IFS=$(echo -en "\n\b") # sólo salto de línea como separador
for linea in $(cat "$ruta"); do
    echo "$linea";
done
IFS=$separador # volver a original

