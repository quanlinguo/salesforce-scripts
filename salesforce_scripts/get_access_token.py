import os
import json
import time
import pathlib

def get_config_dir():
    return "~/.salesforce-scripts/"

def get_default_username():
    """Geerate the default username of a SFDX project, assuming we are in a SFDX project directory
    """
    
    cmd = "sfdx force:config:get defaultusername --json"
    stream = os.popen(cmd)
    output_json = json.loads(stream.read())

    if "result" in output_json and "value" in output_json["result"][0]:
        return output_json["result"][0]["value"]
    else:
        cwd = os.getcwd()
        e = Exception("Can't find default username with `%s` with current directory: %s" % (cmd, cwd))
        raise e

def refresh_access_token(username=''):
    """Refresh an access token using a given auth file.

    Args:
        username (string): username to be used with Salesforce CLI commands
            Default to empty string for we can get the defaultusername in a SFDX project

    Assumtion:
        An auth file is the right place: ~/.salesforce-scripts/<defaultusername>-auth-file.json

        Here is how to create one: 

            mkdir ~/.salesforce-scripts
            sfdx force:org:display --verbose --json > ~/.salesforce-scripts/<defaultusername>-auth-file.json

    Implementation: 

        sfdx auth:sfdxurl:store -f authFile.json --json

    """

    if username == '':
        username = get_default_username()

    config_dir = get_config_dir()

    auth_file_path = config_dir + username + '-auth-file.json'

    stream = os.popen("sfdx auth:sfdxurl:store -f %s --json" % auth_file_path)
    output_json = json.loads(stream.read())

    config_dir_abs = os.path.expanduser(config_dir)
    token_file_path = config_dir_abs + username + '-token-file.json'

    with open(token_file_path, 'w') as f:
        pretty_json = json.dumps(output_json, indent=4, sort_keys=False)
        f.write(pretty_json)

    if "result" in output_json and "accessToken" in output_json["result"]:
        return output_json["result"]["accessToken"]

def get_access_token(username=''):
    """Get an access token using a given auth file.

    Args:
        username (string): username to be used with Salesforce CLI commands
            Default to empty string for we can get the defaultusername in a SFDX project

    Assumtion:
        A token file is the right place: ~/.salesforce-scripts/<defaultusername>-token-file.json
        Otherwise, we will create one with refresh_access_token()

    Implementation: 

        sfdx auth:sfdxurl:store -f authFile.json --json

    """

    if username == '':
        username = get_default_username()

    config_dir = get_config_dir()
    config_dir_abs = os.path.expanduser(config_dir)
    token_file_path = config_dir_abs + username + '-token-file.json'

    token = ''
    if time.time() - os.path.getmtime(token_file_path) < 24 * 60 * 60:
        ''' make sure the file is not more than a day old
        '''
        if os.path.exists(token_file_path):
            with open(token_file_path, 'r') as f:
                token_json = json.loads(f.read())
                if "result" in token_json and "accessToken" in token_json["result"]:
                    token = token_json["result"]["accessToken"]
                    pathlib.Path(token_file_path).touch()

    if token == '':
        token = refresh_access_token(username)

    return token

if __name__ == "__main__":
    # get_default_username()
    print(get_access_token("wisdom"))
