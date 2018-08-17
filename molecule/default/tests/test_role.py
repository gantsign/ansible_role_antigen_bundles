import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_bundle_with_url_config(File):
    bundle = File('/home/test_usr1/.antigen-etc/bundle.d/git.zsh')
    assert bundle.exists
    assert bundle.is_file
    assert bundle.user == 'test_usr1'
    assert bundle.group in ['test_usr1', 'users']
    assert bundle.content_string.strip() == r'''
#
# Ansible managed: Do NOT edit this file manually!
#

antigen bundle \
    --url=git
'''.strip()


def test_bundle_with_location_config(File):
    bundle = File('/home/test_usr1/.antigen-etc/bundle.d/ant.zsh')
    assert bundle.exists
    assert bundle.is_file
    assert bundle.user == 'test_usr1'
    assert bundle.group in ['test_usr1', 'users']
    assert bundle.content_string.strip() == r'''
#
# Ansible managed: Do NOT edit this file manually!
#

antigen bundle \
    --url=robbyrussell/oh-my-zsh \
    --loc=plugins/ant
'''.strip()


def test_bundle_with_args_and_env_config(File):
    bundle = File('/home/test_usr2/.antigen-etc/bundle.d/mvn.zsh')
    assert bundle.exists
    assert bundle.is_file
    assert bundle.user == 'test_usr2'
    assert bundle.group in ['test_usr2', 'users']
    assert bundle.content_string.strip() == r'''
#
# Ansible managed: Do NOT edit this file manually!
#

ENV_TEST2=testValue2

antigen bundle \
    --url=mvn \
    --no-local-clone
'''.strip()


def test_bundle_with_tag_config(File):
    bundle = File('/home/test_usr2/.antigen-etc/bundle.d/gradle.zsh')
    assert bundle.exists
    assert bundle.is_file
    assert bundle.user == 'test_usr2'
    assert bundle.group in ['test_usr2', 'users']
    assert bundle.content_string.strip() == r'''
#
# Ansible managed: Do NOT edit this file manually!
#

ENV_TEST3=testValue3

antigen bundle \
    --url=https://example.com/gradle.git \
    --branch=1.0 \
    --no-local-clone
'''.strip()
