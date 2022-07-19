#  Salesforce Scripts

##  Setup

 *  [Install Salesforce CLI](https://developer.salesforce.com/docs/atlas.en-us.sfdx_setup.meta/sfdx_setup/sfdx_setup_install_cli.htm)

 *  Create a DX project
    ```
    sfdx force:project:create --projectname project1

    cd project1
    sfdx force:auth:web:login --setalias project1 --setdefaultusername
    sfdx force:org:display --verbose --json > ~/.salesforce-scripts/project1-auth-file.json
    ```
 *  Install this package
    ```
    git clone git@github.com:quanlinguo/salesforce-scripts.git
    cd salesforce-scripts
    pip install .
    ```

##  Use Case 1: Get Access Token

    import salesforce_scripts

    '''Assume you are still in the project1 directory'''
    (instance, token) = salesforce_scripts.get_instance_and_access_token()

    '''If you are not in the project1 directory, pass the username alias as a parameter'''
    (instance, token) = salesforce_scripts.get_instance_and_access_token(username="project1")

##  Use Case 2: Query for Users

    import salesforce_scripts
    import json

    (instance, token) = salesforce_scripts.get_instance_and_access_token()
    print(json.dumps(salesforce_scripts.query_users(instance, token), indent=4))
    

##  Use Case 3: List Installed Packages

    import salesforce_scripts
    import json

    (instance, token) = salesforce_scripts.get_instance_and_access_token()
    print(json.dumps(salesforce_scripts.list_installed_packages(instance, token), indent=4))

## Design Principles

 *  Practical use cases > style
 *  Productivity > minimalism
    -  Use Salesforce CLI
    -  Use [simple-salesforce](https://github.com/simple-salesforce/simple-salesforce)
    -  Use [Pandas](https://pandas.pydata.org/pandas-docs/version/0.15/tutorials.html), [sort of like SQL](https://towardsdatascience.com/pandas-vs-sql-compared-with-examples-3f14db65c06f)
    -  Use BigQuery & dbt
    -  Use Elasticsearch
 *  Help friends first

##  Testing with [Pytest](https://docs.pytest.org/en/7.1.x/how-to/index.html)

 *  [Pytest is simpler than unittest](https://www.pythonpool.com/python-unittest-vs-pytest/)

##  Coding Style

 *  Use [Google style](https://google.github.io/styleguide/pyguide.html) [comments for ease of reading](https://queirozf.com/entries/python-docstrings-reference-examples), instead of ReStructuredText
    ```
    def func(arg1, arg2):
        """Summary line.

        Extended description of function.

        Args:
            arg1 (int): Description of arg1
            arg2 (str): Description of arg2

        Returns:
            bool: Description of return value

        Raises:
            AttributeError: The ``Raises`` section is a list of all exceptions
                that are relevant to the interface.
            ValueError: If `arg2` is equal to `arg1`.

        Examples:
            Examples should be written in doctest format, and should illustrate how to use the function.

            >>> a=1
            >>> b=2
            >>> func(a,b)
            True
        """
        if arg1 == arg2:
            raise ValueError('arg1 must not be equal to arg2')

        return True
    ```
