from .hello_world import hello_world
from .hello_world import hello_world_with_helper
from .hello_world import get_hello_world

from .access_token import get_config_dir
from .access_token import get_default_username
from .access_token import refresh_access_token
from .access_token import get_instance_and_access_token
from .access_token import get_instance_url_and_access_token

from .users import query_users

from .describe import list_objects
from .describe import describe_object

from .installed_packages import list_installed_packages

__version__ = "0.1.0"
__author__ = 'Charlie Guo'
__credits__ = 'The Python and Salesforce communities'
