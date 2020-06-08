import pytest
from jfrogcli_pkg import jfrog_cli


def test_read_artifactory_from_config_1():
    artifact= 'https://esiesel.jfrog.io/artifactory'
    conf_file = "config.properties"
    assert jfrog_cli.read_artifactory_from_config(conf_file) == artifact

def test_read_artifactory_from_config_2():
    artifact= 'balabalii'
    conf_file = "config.properties"
    assert jfrog_cli.read_artifactory_from_config(conf_file) != artifact


