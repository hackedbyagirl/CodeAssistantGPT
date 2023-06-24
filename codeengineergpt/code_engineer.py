#!/usr/bin/python3

# imports
from codeengineergpt.utils.colors import Color
from codeengineergpt.config import Config
from codeengineergpt.utils.display import Display
from codeengineergpt.utils.cli import CLI


class CodeEngineerGPT(object):
    """
    An AI-powered tool designed to assist with a variety of coding tasks.
    This includes:
        - Understanding the structure, dependencies, and other details of a codebase.
        - Getting assistance in setting up a new coding project, including planning and setup.
        - Having the AI generate code snippets based on your requirements.
        - Getting help in debugging your code and suggestions for improvements.
    """

    def __init__(self):
        """
        Main Entry point for the code
        
        Args:
            self : Argument

        """
        Display.display_banner()
        Display.display_main_description()

        # Initialize Config
        Config.init()

    def launch(self):
        """
        Launches the main interactive interface.
        
        Args:
            self : Argument

        """
        app = CLI()
        app.launc_main_cli()