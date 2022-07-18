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
        SELECT Id, 
            SubscriberPackage.NamespacePrefix,
            SubscriberPackage.Name, 
            SubscriberPackageVersion.Name, 
            SubscriberPackageVersion.MajorVersion,
            SubscriberPackageVersion.MinorVersion
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

    packages = []
    for rec in response_json["records"]:
        pkg = {
                "Id": rec["Id"],
                "NamespacePrefix": rec["SubscriberPackage"]["NamespacePrefix"],
                "Name": rec["SubscriberPackage"]["Name"],
                "Version": str(rec["SubscriberPackageVersion"]["Name"]) + " "
                         + str(rec["SubscriberPackageVersion"]["MajorVersion"]) + "."
                         + str(rec["SubscriberPackageVersion"]["MinorVersion"])
                }
        packages.append(pkg)

    packages_json = {"packages": packages}

    return packages_json

if __name__ == "__main__":
    import get_access_token
    import json
    (instance, token) = get_access_token.get_instance_and_access_token("wisdom")
    print(json.dumps(list_installed_packages(instance, token), indent=4))
