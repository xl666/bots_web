sudo apt update; sudo apt upgrade

# Sólo actualiza el sistema si se sincronizaron los repos
sudo apt update && sudo apt upgrade

sudo apt || echo "Algo salió mal"
