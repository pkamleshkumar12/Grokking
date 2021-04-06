from cement.core.controller import CementBaseController, expose


class MainController(CementBaseController):
    """
    This is where you will want to add all of your standard commands.
    This controller is stacked on the Base Controller as embedded. All commands here
    will show up transparently in the main application.

    Follow the example below to mimic new commands, or see:
    http://cement.readthedocs.io/en/latest/dev/controllers/
    for examples on creating new commands.
    """
    class Meta:
        label = 'main_controller'
        stacked_on = 'base'
        stacked_type = 'embedded'
        arguments = [
            (['-a', '--arg'],
             dict(
                action='store',
                help='This is an example argument'
             )
            )
        ]

    @expose(help="Default Action for application", hide=True)
    def default(self):
        """
        This is the default action for the application. If you run without
        any arguments, this method will fire.
        """
        print "Entering: MainController.default()"

    @expose(aliases=['examp'], help='This is an example command', hide=False)
    def main_example(self):
        """
        Example method. Put your documentation here.
        PEP-257 Compliant
        PyCharm Friendly: <https://www.jetbrains.com/help/pycharm/documenting-source-code-in-pycharm.html>
        """
        print "Entering MainController.example() with example arg %s" % ()

        # Example Configuration Parse (check config.conf)
        print self.app.config.get('Example', 'foo')
        print self.app.config.get('Example', 'bar')