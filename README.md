# Borg Backup over SSHFS using Python

Encrypted + Incremental backups with borg to SSHFS remote dir, automated with Cron.

## Getting Started

Borg provides incremental, version controlled, and encrypted backups ideal for homelabs. This repo makes it simple to get started by automating the host dependency install (using Ansible playbooks), mounting remote paths over SSHFS, and running Borg (using Python).

Planned features include cron file and playbook.yml for automating runnning backup commands that can be deployed to multi-node environments.

## License

Project made available under [MIT License](LICENSE).
