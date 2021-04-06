from cement.core.controller import CementBaseController, expose


class TestController(CementBaseController):
    class Meta:
        label = 'test_controller'
        aliases = ['test']
        description = ''
        stacked_on = 'base'
        stacked_type = 'embedded'

    @expose(help='woot')
    def example(self):
        print 'Entering: TestController.example()'