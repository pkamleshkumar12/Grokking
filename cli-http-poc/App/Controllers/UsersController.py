from cement.core.controller import CementBaseController, expose


class UsersController(CementBaseController):
    class Meta:
        label = 'users_controller'
        aliases = ['users']
        description = ''
        stacked_on = '?'
        stacked_type = 'nested'

    @expose(help='woot')
    def example(self):
        print 'Entering: UsersController.example()'