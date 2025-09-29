import logging
from datetime import datetime

# Códigos ANSI para cor
RESET = "\033[0m"
BOLD = "\033[1m"

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"

def insertTimestamp(text: str, delimiterAfter: str = " ") -> str:
    """
    Insert the current datetime before the given text, optionally setting a delimiter.

    Args:
        text (str):  The text to be stamped.
        delimiterAfter (str): The delimiter used to separate the timestamp and the text.

    Returns:
        New text with Timestamp
    """

    return f"{datetime.now().isoformat()}{delimiterAfter}{text}"

def logSuccess(message: str, *args, withTimestamp: bool = False, **kwargs) -> None:
    """
    Log a success message in green.

    Args:
        message (str): The message to log.
        *args: Extra positional arguments for logging.
        **kwargs: Extra keyword arguments for logging.
        withTimestamp: If True, prepend current timestamp in ISO 8601 format.
    """

    newMessage = f"[{GREEN}{BOLD}✅ SUCCESS{RESET}]: {message}"
    if withTimestamp:
        newMessage = insertTimestamp(newMessage)
    logging.info(newMessage, *args, **kwargs)


def logFail(message: str, *args, withTimestamp: bool = False, **kwargs) -> None:
    """
    Log a failure message in red.

    Args:
        message (str): The message to log.
        *args: Extra positional arguments for logging.
        **kwargs: Extra keyword arguments for logging.
        withTimestamp: If True, prepend current timestamp in ISO 8601 format.
    """

    newMessage = f"[{RED}{BOLD}❌ FAILURE{RESET}]: {message}"
    if withTimestamp:
        newMessage = insertTimestamp(newMessage)
    logging.error(newMessage, *args, **kwargs)


def logWarn(message: str, *args, withTimestamp: bool = False, **kwargs) -> None:
    """
    Log a warning message in yellow.

    Args:
        message (str): The message to log.
        *args: Extra positional arguments for logging.
        **kwargs: Extra keyword arguments for logging.
        withTimestamp: If True, prepend current timestamp in ISO 8601 format.
    """

    newMessage = f"[{YELLOW}{BOLD}⚠️ WARNING{RESET}]: {message}"
    if withTimestamp:
        newMessage = insertTimestamp(newMessage)
    logging.warning(newMessage, *args, **kwargs)


def logDebug(message: str, *args, withTimestamp: bool = False, **kwargs) -> None:
    """
    Log a debug message in blue.

    Args:
        message (str): The message to log.
        *args: Extra positional arguments for logging.
        **kwargs: Extra keyword arguments for logging.
        withTimestamp: If True, prepend current timestamp in ISO 8601 format.
    """

    newMessage = f"[{BLUE}{BOLD}🐞 DEBUG{RESET}]: {message}"
    if withTimestamp:
        newMessage = insertTimestamp(newMessage)
    logging.debug(newMessage, *args, **kwargs)


def logCritical(message: str, *args, withTimestamp: bool = False, **kwargs) -> None:
    """
    Log a critical message in magenta.

    Args:
        message (str): The message to log.
        *args: Extra positional arguments for logging.
        **kwargs: Extra keyword arguments for logging.
        withTimestamp: If True, prepend current timestamp in ISO 8601 format.
    """

    newMessage = f"[{MAGENTA}{BOLD}🔥 CRITICAL{RESET}]: {message}"
    if withTimestamp:
        newMessage = insertTimestamp(newMessage)
    logging.critical(newMessage, *args, **kwargs)