from cement.core.controller import CementBaseController, expose
from ConfigParser import SafeConfigParser

# Generate Version Banner
# =============================================================================
parser = SafeConfigParser()
parser.read('config.conf')

app_desc = parser.get('App', 'description')
app_version = parser.get('App', 'version')
app_company = parser.get('App', 'company')

with open('banner.txt', 'r') as banner:
    data = banner.read()

data = data.replace('__VERSION__', app_version)
data = data.replace('__DESC__', app_desc)
data = data.replace('__COMPANY__', app_company)

banner = data

# Base Controller
# =============================================================================


class BaseController(CementBaseController):
    """
    Base controller.
    It has no function other than being a base for stacking other controllers on
    and providing a version output.
    """
    class Meta:
        label = 'base'
        description = app_desc
        arguments = [
            (['-v', '--version'], dict(action='version', version=banner))
        ]






