from src.controllers.system_controller import SystemControllerInterface
from utils.logger.logger import Logger


def main():
    """
    Entry point to the FibriNet Application.
    """
    # CONFIGURES LOGGER WITH DEFAULT FILE STORAGE
    Logger.initialize()

    # INITIALIZE THE SCI
    SystemControllerInterface()


if __name__ == "__main__":
    main()