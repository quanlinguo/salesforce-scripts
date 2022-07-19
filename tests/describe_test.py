import salesforce_scripts

def test_list_objects():
    (instance, token) = salesforce_scripts.get_instance_and_access_token()
    assert salesforce_scripts.list_objects(instance, token)

def test_describe_object():
    (instance, token) = salesforce_scripts.get_instance_and_access_token()
    assert salesforce_scripts.describe_object(instance, token, 'Account')
