import json
import simple_salesforce

def list_objects(instance, access_token):
    """ describe
    """

    sf = simple_salesforce.Salesforce(instance=instance, session_id=access_token)
    return sf.describe()

def describe_object(instance, access_token, object_name):
    """ describe: works better than sfdx force:schema:sobject:describe, which misses formula fields!
    """

    sf = simple_salesforce.Salesforce(instance=instance, session_id=access_token)

    describe_response = sf.mdapi.CustomObject.describe()
    custom_object = sf.mdapi.CustomObject.read(object_name)
    return custom_object

if __name__ == "__main__":
    import access_token
    import json
    (instance, token) = access_token.get_instance_and_access_token("wisdom")
    print(describe_object(instance, token, "Account"))
