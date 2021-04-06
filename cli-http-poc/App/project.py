from cement.core.foundation import CementApp
from App.Controllers.BaseController import BaseController
from App.Controllers.MainController import MainController


class MyApp(CementApp):
    class Meta:
        label = 'MyApp'
        handlers = [
            BaseController,
            MainController
        ]


def main():
    with MyApp() as app:
        app.config.parse_file('config.conf')
        app.run()

