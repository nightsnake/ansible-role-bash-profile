ansible-role-bash-profile
=========

This role create a custom .bashrc for users and configure fancy bash prompt


## Role Variables

All default variables are predefined in defaults/main.yml.


### Playbook example

```bash
---
- hosts: localhost
  roles:
    - bash-profile
```

## Requirements
- Ansible >= 2.25
- git (in case you want to see the branch)

## License
MIT

## Author
nightsnake

## Support
Please create the issue in case of bugs
