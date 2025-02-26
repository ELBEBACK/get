# How to create SSH-key
    1. To generate public SSH-key enter next command line *ssh-keygen -t ecdsa* \
    1. Leave preset placement of the key as it proposed \
# How to add SSH-key to GitHub account
    1. After the creation of the key, enter next command line to print the content of a file *cat ~/.ssh/id_ecdsa.pub* \
    1. Then copy the content to the GitHub->Settings->SSH and GPG keys->SSH keys \
# How to clone repositories
    1. To clone repositories we have a command line *git clone git@github.com:username/repository.git* \