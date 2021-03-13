#!/bin/bash

DEFAULT_ARGS=Compression=no,Ciphers=aes128-ctr,allow_other,auto_cache,reconnect,no_readahead

read -p '[sshfs] Remote username: ' REMOTE_USER
read -p '[sshfs] Remote hostname or IP: ' REMOTE_HOST
read -p '[sshfs] Remote path for backups: ' REMOTE_PATH
read -p '[local] Mount dir for remote path: ' LOCAL_PATH

sshfs -o $DEFAULT_ARGS \
    $REMOTE_USER@$REMOTE_HOST:$REMOTE_PATH \
    $LOCAL_PATH

set +x;
