from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_files(host):
    present = [
        "/etc/systemd/system/snmp_exporter.service",
        "/opt/snmp_exporter/snmp_exporter",
        "/opt/snmp_exporter/snmp.yml"
    ]
    if present:
        for file in present:
            f = host.file(file)
            assert f.exists
            assert f.is_file


def test_service(host):
    present = [
        "snmp_exporter"
    ]
    if present:
        for service in present:
            s = host.service(service)
            assert s.is_enabled
            assert s.is_running


def test_socket(host):
    present = [
        "tcp://127.0.0.1:9116"
    ]
    for socket in present:
        s = host.socket(socket)
        assert s.is_listening
