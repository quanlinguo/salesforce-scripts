import simple_salesforce

def query_users(instance, access_token):
    q = """
        SELECT Id, Username
          FROM User
    """

    sf = simple_salesforce.Salesforce(instance=instance, session_id=access_token)
    rows = sf.query(q)
    return rows

if __name__ == "__main__":
    import get_access_token
    import json
    (instance, token) = get_access_token.get_instance_and_access_token("wisdom")
    print(json.dumps(query_users(instance, token), indent=4))
