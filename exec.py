import os
import re
import subprocess
from errbot import BotPlugin, botcmd, re_botcmd
from errbot.utils import ValidationException

class Exec(BotPlugin):
    """
    Execute a command when the bot is talked to
    """

    config_template = {
        'command': u'echo'
    }

    def activate(self):
        """
        Load configuration from config.by
        """
        super(Exec, self).activate()
        if (self.config == None and self.bot_config.EXEC):
            self.check_configuration(self.bot_config.EXEC)
            self.configure(self.bot_config.EXEC)

    def executable_exists(self, name):
        """
        Check if an executable exists
        """
        if len(name) == 0:
            raise ValidationException('Command is empty')

        found = False
        for path in os.environ['PATH'].split(os.pathsep):
            fullpath = path + os.sep + name
            if os.path.exists(fullpath):
                found = True
                break
        if not found:
            raise ValidationException('Command not in PATH')

    def get_configuration_template(self):
        """
        Defines the configuration structure this plugin supports
        """
        return self.config_template

    def check_configuration(self, configuration):
        """
        Triggers when the configuration is checked, shortly before activation
        """
        super(Exec, self).check_configuration(configuration)
        self.executable_exists(configuration['command'])

    @re_botcmd(pattern=r".*", prefixed=False)
    def runexec(self, msg, match):
        """
        Execute the commmand
        """
        for part in ("abc"):
            print "part: ", part
        try:
            output = subprocess.check_output(
                [self.config['command'], str(msg), str(msg.frm)],
                stderr=subprocess.STDOUT
            )
            if len(output) > 0:
                return output
            else:
                return "OK\n"
        except subprocess.CalledProcessError as err:
            if len(err.output):
                return err.output
            else:
                return "Error" 
