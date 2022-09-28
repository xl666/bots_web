# Mandar un mensaje cuando no tienes internet
while curl https://google.com &> /dev/null; do
    sleep 10;
done
eho "No tienes internet"
