import requests
import json

def list_installed_packages(instance, access_token):
    """ List Installed Packages

    Imlementation: 
        Need tooling API
        https://developer.salesforce.com/docs/atlas.en-us.api_tooling.meta/api_tooling/intro_rest_resource_examples.htm
        req.setEndpoint('https://MyDomainName.my.salesforce.com/services/data/v55.0/tooling/query/?q=Select+id,Name+from+MetadataContainer+Where+ID=\'' + containerID +  '\'');
    """
    q = """
        SELECT Id, SubscriberPackageId, SubscriberPackage.NamespacePrefix,
            SubscriberPackage.Name, SubscriberPackageVersion.Id,
            SubscriberPackageVersion.Name, SubscriberPackageVersion.MajorVersion,
            SubscriberPackageVersion.MinorVersion,
            SubscriberPackageVersion.PatchVersion,
            SubscriberPackageVersion.BuildNumber
        FROM InstalledSubscriberPackage
        ORDER BY SubscriberPackageId
    """

    instance_url = 'https://' + instance
    service_url = instance_url + "/services/data/v55.0/tooling/query/"
    url = service_url + "?q=" + q.strip().replace(' ', '+')

    headers = {
            'Authorization': "OAuth " + access_token, 
            'Accept': "application/json" }

    response = requests.get(url=url, headers=headers)
    response_json = json.loads(response.text)

    return response_json

if __name__ == "__main__":
    import get_access_token
    import json
    (instance, token) = get_access_token.get_instance_and_access_token("wisdom")
    print(json.dumps(list_installed_packages(instance, token), indent=4))
