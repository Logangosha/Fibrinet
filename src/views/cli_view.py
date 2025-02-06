from src.managers.view.view_strategy import ViewStrategy
from src.models.exceptions import StateTransitionError
from utils.logger.logger import Logger

class CommandLineView(ViewStrategy):
    """
    A command-line interface (CLI) view for user interaction.
    Handles input commands, updates the view, and interacts with the controller.
    """

    # CLEAR THE COMMAND LINE VIEW
    def clear_view(self):
        """
        Clears the terminal screen based on the operating system.
        """
        Logger.log("start clear_view()")
        import os
        import platform

        system = platform.system()
        if system == 'Windows':
            os.system('cls')
        else:
            os.system('clear')
        Logger.log("end clear_view()")

    # START THE COMMAND LINE INTERFACE
    def start_view(self):
        """
        Initializes and starts the command-line interface.
        Clears the screen and enters the main loop.
        """
        

        Logger.log("start start_view()")
        self.clear_view()
        print(">>> Command Line Interface started.")
        print(">>> To see all commands use: help")
        self.run()
        Logger.log("end start_view()")

    # STOP THE COMMAND LINE INTERFACE
    def stop_view(self):
        """
        Stops the command-line interface and prints a shutdown message.
        """
        

        Logger.log("start stop_view()")
        print(">>> Command Line Interface stopped.\n")
        Logger.log("end stop_view()")

    # RUN THE COMMAND LINE INTERFACE, PROCESS USER COMMANDS
    def run(self):
        """
        Runs the command-line interface, continuously accepting and processing user input.
        Supports various commands to interact with the system.
        """
        
        
        Logger.log("start run()")
        while True:
            Logger.log("Propting user for command.")
            command = input("\nEnter command: ").strip()
            if not command:
                continue

            parts = command.split(" ", 1)
            cmd = parts[0]
            arg = parts[1] if len(parts) > 1 else None
            
            self.clear_view()
            print(f">>> Command entered: {command}")
            Logger.log(f"Command entered: {command}")
            try:
                # HANDLE EXIT COMMAND
                if cmd.lower() in ["exit", "quit"]:
                    print(">>> Exiting system.")
                    break
                # HANDLE HELP COMMAND
                elif cmd.lower() == "help":
                    self.show_help()
                # HANDLE NETWORK INPUT COMMAND
                elif cmd == "input_network" and arg:
                    self.controller.input_network(arg)
                    print(f">>> Network input successfully processed: {arg}")
                    print(f">>> Network now able to modify.")
                # HANDLE NETWORK MODIFICATION COMMAND
                elif cmd == "modify_network" and arg:
                    print(f">>> NOT IMPLEMENTED")
                    #self.controller.modify_network(arg)
                    #print(f">>> Network modified with: {arg}")
                # HANDLE DATA EXPORT COMMAND
                elif cmd == "export_data" and arg:
                    print(f">>> NOT IMPLEMENTED")
                    #self.controller.export_data(arg)
                    #print(f">>> Data exported to: {arg}")
                # HANDLE VIEW REQUEST SUBMISSION COMMAND
                elif cmd == "submit_view_request" and arg:                    
                    print(f">>> NOT IMPLEMENTED")
                    #self.controller.submit_view_request(arg)
                    #print(f">>> View request submitted for: {arg}")
                # HANDLE CONFIGURE LOG COMMAND
                elif cmd == "configure_Logger" and arg:
                    enabled = True if arg.split()[0].lower() == "enable" else False
                    ### NOT HANDLING kwargs AT THIS TIME  ###
                    kwargs_dict = {}
                    # CALL CONTROLLER TO CONFIGURE Logger
                    self.controller.configure_Logger(enabled, **kwargs_dict)
                    print(f">>> Logger {"enabled" if enabled == True else "disabled"}")
                    Logger.log(f"Configured Logger request submitted with: enabled = {enabled}, and kwargs_dict = {kwargs_dict}")
                # HANDLE INVALID COMMANDS
                else:
                    print(">>> Invalid command or missing argument.")
            except StateTransitionError:
                print(">>> Unable to process request due to an invalid state transition.")

        self.stop_view()
        Logger.log("end run()")

    # UPDATE THE VIEW (NOT IMPLEMENTED)
    def update_view(self, update):
        """
        Updates the view with new data.
        To be implemented in subclasses.
        
        :param update: The data used to update the view.
        :raises NotImplementedError: If the method is not implemented.
        """
        

        Logger.log("start update_view()")
        raise NotImplementedError()
        Logger.log("end update_view()")

    # HANDLE A VIEW EVENT (NOT IMPLEMENTED)
    def handle_view_event(self, event):
        """
        Handles a specific event occurring in the view.
        To be implemented in subclasses.
        
        :param event: The event to be handled.
        :raises NotImplementedError: If the method is not implemented.
        """
        

        Logger.log("start handle_view_event()")
        raise NotImplementedError()
        Logger.log("end handle_view_event()")

    # UPDATE THE VIEW BASED ON AN EVENT TYPE AND DATA (NOT IMPLEMENTED)
    def update(self, event_type, data):
        """
        Updates the view based on an event type and associated data.
        To be implemented in subclasses.
        
        :param event_type: The type of event that occurred.
        :param data: The data associated with the event.
        :raises NotImplementedError: If the method is not implemented.
        """
        

        Logger.log("start update()")
        raise NotImplementedError()
        Logger.log("end update()")
    
    # REFRESH THE VIEW (NOT IMPLEMENTED)
    def refresh_view(self):
        """
        Refreshes the current view.
        To be implemented in subclasses.
        
        :raises NotImplementedError: If the method is not implemented.
        """
        

        Logger.log("start refresh_view()")
        raise NotImplementedError()
        Logger.log("end refresh_view()")
    
    # SET THE CONTROLLER FOR THE VIEW
    def set_controller(self, controller):
        """
        Sets the controller for the CLI view.
        
        :param controller: The controller responsible for handling commands.
        """
        

        Logger.log("start set_controller()")
        return super().set_controller(controller)
        Logger.log("end set_controller()")

    # DISPLAY AVAILABLE COMMANDS
    def show_help(self):
        """
        Displays the list of available commands in the CLI.
        """
        

        Logger.log("start show_help()")
        print(">>> Available commands:\n")
        print("   - help: Show available commands")
        print("   - exit / quit: Exit the CLI")
        print("   - input_network <arg>: Input network data")
        print("   - modify_network <arg>: Modify network (NOT IMPLEMENTED)")
        print("   - export_data <arg>: Export data to a file (NOT IMPLEMENTED)")
        print("   - submit_view_request <arg>: Submit a view request (NOT IMPLEMENTED)")
        print("   - configure_Logger <arg>: Configure Logger")
        print("       - enable")
        print("       - disable")
        Logger.log("end show_help()")
