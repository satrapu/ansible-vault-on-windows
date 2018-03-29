#!/usr/bin/python

# This Python script will read the contents of the vault_password file and its output will be feed back to
# the caller, which is Ansible Vault.

# When editing this file, please make sure you are using "LF" as line ending instead of the usual "CRLF", 
# otherwise running ansible-vault from Docker container will fail!
# In case you're using Visual Studio Code, please check this SO article for instructions: 
# https://stackoverflow.com/a/39532890.

# Read vault_password file using read mode.
file = open("/opt/ansible-vault-password/vault_password", "r")

# Print the contents of this file () to the console
print file.read()