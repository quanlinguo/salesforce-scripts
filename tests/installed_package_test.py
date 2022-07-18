import salesforce_scripts

def test_list_installed_packages():
    (instance, token) = salesforce_scripts.get_instance_and_access_token()
    assert salesforce_scripts.list_installed_packages(instance, token)

    ''' Shun a more obscure version
    assert salesforce_scripts.list_installed_packages(*salesforce_scripts.get_instance_and_access_token())
    '''