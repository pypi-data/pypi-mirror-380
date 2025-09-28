#!/bin/bash

log() {
  if [ "$HARBOR_LOG_LEVEL" == "DEBUG" ]; then
    echo "[harbor-init] $1"
  fi
}

# Retrieve the correct GID from the mounted docker.sock
DOCKER_GROUP_GID=$(stat -c '%g' /var/run/docker.sock)

log "Ensuring Docker group has correct GID: $DOCKER_GROUP_GID"

# Recreate the docker group with the correct GID
# Remove the existing docker group
sudo groupdel docker || true
# Remove any group with the target GID
getent group $DOCKER_GROUP_GID | cut -d: -f1 | xargs -r sudo groupdel || true
# Add the correct group
sudo groupadd -g $DOCKER_GROUP_GID docker || true

# Add abc to the docker group
log "Adding abc user to Docker group with GID $DOCKER_GROUP_GID"
sudo usermod -aG docker abc

