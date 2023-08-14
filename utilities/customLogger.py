import logging  # Import the logging module to enable logging functionality.

class LogGen:

    @staticmethod
    def logGen():
        # Configure the logging settings using the basicConfig function.
        # This configures the root logger for the entire application.
        logging.basicConfig(
            filename="/Users/vivek/PycharmProjects/Python_Hybrid_Automation_Framework/Logs/automation.log",  # Set the file path where log messages will be saved.
            format='%(asctime)s: %(levelname)s: %(message)s',  # Set the format of each log message.
            datefmt='%m/%d/%Y %I:%M:%S %p'  # Set the date and time format for log messages.
        )

        # Get the root logger instance.
        logger = logging.getLogger()

        # Set the logging level for the root logger to INFO.
        # This means that log messages with severity INFO and above will be captured.
        logger.setLevel(logging.INFO)

        # Return the configured logger instance to be used for logging in other parts of the code.
        return logger