# Borg Backup over SSHFS using Python

Encrypted + Incremental backups with borg to SSHFS remote dir, automated with Cron.

## Getting Started

Borg provides incremental, version controlled, and encrypted backups ideal for homelabs. This repo makes it simple to get started by automating the host dependency install (using Ansible playbooks), mounting remote paths over SSHFS, and running Borg (using Python).

Planned features include cron file and playbook.yml for automating runnning backup commands that can be deployed to multi-node environments.

### System Requirements

Borg requires dependencies on the host environment, Ansible playbooks are included for targeting yum, apt package manger based Linux environments with the required host packages. For more information refer to [borg:docs:setup]().

To run the Ansible playbook, use the command structure:

```bash
$ ansible-playbook -i <inventory_file> \
    --ask-pass --ask-become-pass \
    --user <user> \
    ./ansible/<playbook>.yml
```

Next, create and activate a local python3 venv to install dependencies from [requirements.txt](requirements.txt) including [borgbackup](https://pypi.org/project/borgbackup/).

```bash
$ ./py3_venv_init.sh
```

## License

Project made available under [MIT License](LICENSE).
