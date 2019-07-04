import pytest
import os
from testinfra.utils.ansible_runner import AnsibleRunner
testinfra_hosts = AnsibleRunner(
                    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('file, content', [
  ("root/.bashrc", "alias ls='ls  --color=auto'"),
  ("/etc/skel/.bashrc", "HISTSIZE=1000")
])
def test_files(host, file, content):
    file = host.file(file)

    assert file.exists
    assert file.contains(content)
