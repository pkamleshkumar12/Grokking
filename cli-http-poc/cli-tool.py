from cement.core.foundation import CementApp
from cement.core.controller import CementBaseController, expose

class ToolBaseController(CementBaseController):
    class Meta:
        label = 'base'
        description = 'cli tool for Cement project'


class ScaffoldController(CementBaseController):
    class Meta:
        label = 'generate'
        description = "Generate Scaffolds"
        stacked_on = 'base'
        stacked_type = 'nested'
        arguments = [
            (['name_arg'], dict(action='store', nargs='*'))
        ]

    @expose(aliases=['controller'], help='Generate Embedded Controller. Enter name of controller without the word "Controller"')
    def scaffold_controller(self):
        controller_name = self.app.pargs.name_arg[0].title()
        controller_name = controller_name + 'Controller'

        controller_label = self.app.pargs.name_arg[0].lower() + '_controller'
        controller_alias = self.app.pargs.name_arg[0].lower()

        stacked_on = raw_input("What Controller will this controller be stacked on? (base): ")
        if stacked_on == '':
            stacked_on = 'base'

        stacked_type = raw_input("embedded or nested? (embedded): ")
        if stacked_type == '':
            stacked_type = 'embedded'

        print "Generating %s which is %s in %s...\n" % (controller_name, stacked_type, stacked_on)

        with open('lib/skel/controller.py', 'r') as controller:
            data = controller.read()

        data = data.replace('__CONTROLLER_NAME__', controller_name)
        data = data.replace('__CONTROLLER_LABEL__', controller_label)
        data = data.replace('__STACKED_ON__', stacked_on)
        data = data.replace('__STACKED_TYPE__', stacked_type)
        data = data.replace('__CONTROLLER_ALIAS__', controller_alias)

        output_file = open('App/Controllers/' + controller_name + '.py', 'w')
        output_file.write(data)

        print "Wait! Theres a few things left to do before your new controller will work!"
        print "--------------------------------------------------------------------------"
        print "- Add %s to the handlers list in the main CementApp. (App/project.py)" % controller_name
        print "- Import this new controller into the app. (App/project.py)"
        print "\t from App.Controllers.%s import %s" % (controller_name, controller_name)

        # print "Dont forget to add %s to the handlers section in the main CementApp...\n" % controller_name

class MyApp(CementApp):
    class Meta:
        label = 'cli-tool'
        handlers = [
            ToolBaseController,
            ScaffoldController
        ]

with MyApp() as app:
    app.run()
