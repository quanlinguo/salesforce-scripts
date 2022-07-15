##  Salesforce Scripts

##  Use Case 1: Get Access Token

### Setup

    sfdx force:project:create --projectname project1

    cd project1
    sfdx force:auth:web:login --setalias project1 --setdefaultusername
    sfdx force:org:display --verbose --json > ~/.salesforce-scripts/project1-auth-file.json

    pip install .

### Code

    from salesforce_scripts import get_access_token
    get_access_token()

### Design & Development Principles

 *  Practical use cases > style
 *  Productivity > minimalism
    -  Use Salesforce CLI
    -  Use simple-python
    -  Use BigQuery
    -  Use dbt
    -  Use Elasticsearch
 *  Help friends first

 * [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
 *  Use Google Style Comments for Ease of Reading, instead of ReStructuredText
    -  [Google Style Comments](https://queirozf.com/entries/python-docstrings-reference-examples)
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
