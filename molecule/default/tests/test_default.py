import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_haproxy_installed(host):
    assert host.package("haproxy").is_installed


def test_config_file(host):
    f = host.file('/etc/haproxy/haproxy.cfg')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    # assert f.mode == 0o755


def test_haproxy_running_and_enabled(host):
    service = host.service('haproxy')

    assert service.is_running
    assert service.is_enabled
