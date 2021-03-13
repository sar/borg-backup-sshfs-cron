#!/bin/bash

# -------------------
# Borg: Create new instance of backup to remote path
# Docs: https://borgbackup.readthedocs.io/en/stable/usage/create.html
# -------------------

#!/bin/bash

tstamp=`date +"%s"`

source .venv/bin/activate
BACKUP_PATH=`echo $CWD`

read -p '[sshfs] Set local dir of remote mounted path: ' LOCAL_PATH
read -p '[borg] Borg repository name subdir in mounted path: ' BACKUP_NAME
read -p '[local] Path to backup: ' BACKUP_PATH

borg create --stats $LOCAL_PATH/$BACKUP_NAME::$tstamp $BACKUP_PATH

set +x;
