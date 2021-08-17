Ansible Role: Antigen Bundles
=============================

[![Tests](https://github.com/gantsign/ansible_role_antigen_bundles/workflows/Tests/badge.svg)](https://github.com/gantsign/ansible_role_antigen_bundles/actions?query=workflow%3ATests)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-gantsign.antigen__bundles-blue.svg)](https://galaxy.ansible.com/gantsign/antigen_bundles)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/gantsign/ansible_role_antigen_bundles/master/LICENSE)

Ansible role to add bundles to your [Antigen](http://antigen.sharats.me/)
configuration for Zsh. It is useful to combine this role with
[Ansible tags](https://docs.ansible.com/ansible/latest/user_guide/playbooks_tags.html)
to conditionally install particular bundles.

**Important:** you must have installed Antigen using the
[gantsign.antigen](https://galaxy.ansible.com/gantsign/antigen) role (and
configured Antigen for the same user) for this role to work.

Requirements
------------

* Ansible >= 2.8

* Linux Distribution

    * Debian Family

        * Debian

            * Jessie (8)
            * Stretch (9)

        * Ubuntu

            * Xenial (16.04)
            * Bionic (18.04)

    * RedHat Family

        * CentOS

            * 7

        * Fedora

            * 31

    * SUSE Family

        * openSUSE

            * 15.1

    * Note: other versions are likely to work but have not been tested.

Role Variables
--------------

The following variables will change the behavior of this role:

```yaml
# Antigen is configured per user so you need to specify the users to install it for
users:
  - username: # The username of the user to install Antigen for
    antigen_bundles:
      - name: # The name of the Antigen bundle (e.g. one of the plugins that come with Oh-My-Zsh)
        url: # Optional. If the it's not one of the Oh-My-Zsh plugins you must specify the URL (use owner/repo shorthand for GitHub)
        location: # Optional. The directory in the repository containing the plugin
        branch: # Optional. Git branch to checkout.
        tag: # Optional. Git tag to checkout (takes preference over branch)
        args: [] # Optional. Command line arguments to pass to Antigen
        env: {} # Optional. Environnement variables to set
      # more bundles here
  # more users here
```

Example Playbooks
-----------------

Example showing just the configuration for this role:

```yaml
- hosts: servers
  roles:
    - role: gantsign.antigen_bundles
      users:
        - username: example
          antigen_bundles:
            # Bundle from the default repo (robbyrussell's oh-my-zsh)
            - name: command-not-found
            # Syntax highlighting bundle
            - name: zsh-syntax-highlighting # `name` is required (any valid file name will do so long as it's unique for the bundles)
              url: zsh-users/zsh-syntax-highlighting
```

Example with the required companion `gantsign.antigen` role:

```yaml
- hosts: servers
  roles:
    - role: gantsign.antigen
      users:
        - username: example
          antigen_libraries:
            - name: oh-my-zsh
          antigen_theme:
            name: robbyrussell
          antigen_bundles:
            - name: command-not-found
            - name: docker
            - name: git

    - role: gantsign.antigen_bundles
      tags:
        - java
      users:
        - username: example
          antigen_bundles:
            - name: mvn
```

In the above example the `mvn` bundle/plugin will not be installed if you tell
Ansible to skip tasks with the `java` tag.

More Roles From GantSign
------------------------

You can find more roles from GantSign on
[Ansible Galaxy](https://galaxy.ansible.com/gantsign).

Development & Testing
---------------------

This project uses [Molecule](http://molecule.readthedocs.io/) to aid in the
development and testing; the role is unit tested using
[Testinfra](http://testinfra.readthedocs.io/) and
[pytest](http://docs.pytest.org/).

To develop or test you'll need to have installed the following:

* Linux (e.g. [Ubuntu](http://www.ubuntu.com/))
* [Docker](https://www.docker.com/)
* [Python](https://www.python.org/) (including python-pip)
* [Ansible](https://www.ansible.com/)
* [Molecule](http://molecule.readthedocs.io/)

Because the above can be tricky to install, this project includes
[Molecule Wrapper](https://github.com/gantsign/molecule-wrapper). Molecule
Wrapper is a shell script that installs Molecule and it's dependencies (apart
from Linux) and then executes Molecule with the command you pass it.

To test this role using Molecule Wrapper run the following command from the
project root:

```bash
./moleculew test
```

Note: some of the dependencies need `sudo` permission to install.

License
-------

MIT

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
