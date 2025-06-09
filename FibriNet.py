from src.controllers.system_controller import SystemController
from utils.logger.logger import Logger


def main():
    """
    Entry point to the FibriNet Application.
    """
    # CONFIGURES LOGGER WITH DEFAULT FILE STORAGE
    Logger.initialize()
    Logger.disable_logging() 

    # INITIALIZE THE SCI
    controller = SystemController()

    # START THE TKINER VIEW
    controller.initiate_view("tkinter")

if __name__ == "__main__":
    main()