from src.controllers.system_controller import SystemControllerInterface
from utils.logger.logger import Logger


def main():
    """
    Entry point to the FibriNet Application.
    """
    # CONFIGURES LOGGER WITH DEFAULT FILE STORAGE
    Logger.initialize()

    # INITIALIZE THE SCI
    controller = SystemControllerInterface()

    # START THE TKINER VIEW
    controller.initiate_view("cli")

if __name__ == "__main__":
    main()