import json
import simple_salesforce

def describe(instance, access_token):
    """ describe
    """

    sf = simple_salesforce.Salesforce(instance=instance, session_id=access_token)
    sf.describe()

    for x in sf.describe()["sobjects"]:
        print(x["name"], "\t", x["label"])

def describe_object(instance, access_token, object_name):
    """ describe
    """

    sf = simple_salesforce.Salesforce(instance=instance, session_id=access_token)

    describe_response = sf.mdapi.CustomObject.describe()
    custom_object = sf.mdapi.CustomObject.read(object_name)
    print(custom_object)

if __name__ == "__main__":
    import get_access_token
    import json
    (instance, token) = get_access_token.get_instance_and_access_token("wisdom")
    # describe(instance, token)
    # describe_object(instance, token, "AAA_Case__c")
    describe_object(instance, token, "Contact")
