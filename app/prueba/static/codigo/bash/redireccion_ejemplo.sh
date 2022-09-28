# Salida a un archivo, borra el archivo si existe
ls -la > /tmp/archivos.txt

# Esta versión no borra y agrega al final
ls -la >> /tmp/archivos.txt

# Entrada a un comando
# Funciona si el comando lee de entrada estándar
grep patron < /tmp/entrada.txt

# Si el comando falla
touch /hola 2> /tmp/errores.txt

# conectar dos comandos
ls -la | wc -l

# Si no te interesan las salidas
curl https://uv.mx &> /dev/null
