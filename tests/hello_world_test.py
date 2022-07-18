import salesforce_scripts

def test_hello_world():
    assert not salesforce_scripts.hello_world()
    ### Assert that the function does not return anything. 

def test_get_hello_world():
    assert salesforce_scripts.get_hello_world() == 'Hello World!'
