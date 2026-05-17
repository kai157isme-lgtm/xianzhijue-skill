#!/bin/bash
# Setup SSH key for Hermes Agent
mkdir -p ~/.ssh
chmod 700 ~/.ssh
echo 'ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJ8hDPHwGJ4VvQyFqXsxkRJLYmBZSHjFKLxmVqPlGXsL hermes-agent' >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
echo "SSH key added successfully"
cat ~/.ssh/authorized_keys
