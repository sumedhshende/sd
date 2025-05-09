# Update package lists and install required tools
sudo apt update
sudo apt install -y curl git python3 python3-pip

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER
newgrp docker

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Create project directory
mkdir event-processing-system
cd event-processing-system

# Create subdirectories for components
mkdir kafka flink cassandra monitoring producer api

# Create docker-compose.yml file
touch docker-compose.yml

# Initialize Git repository (optional, for version control)
git init
