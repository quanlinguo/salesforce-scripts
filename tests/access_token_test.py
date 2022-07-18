import salesforce_scripts

def test_get_config_dir():
    assert salesforce_scripts.get_config_dir()

def test_get_default_username():
    assert salesforce_scripts.get_default_username()

def test_refresh_access_token():
    assert salesforce_scripts.refresh_access_token()

def test_get_instance_and_access_token():
    assert salesforce_scripts.get_instance_and_access_token()

def test_get_instance_url_and_access_token():
    assert salesforce_scripts.get_instance_url_and_access_token()

