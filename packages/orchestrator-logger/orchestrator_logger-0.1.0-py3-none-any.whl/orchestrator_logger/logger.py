import requests
import datetime

def orchestrator_Logger(LogStatus: str, LogMessage: str, token: str,
                        ProcessName: str = "LinkedIn (Selenium)", MachineName: str = "PC07-VM01"):
    """
    Logs messages to the orchestrator API.

    Args:
        LogStatus (str): Log level/status (e.g., INFO, ERROR, DEBUG, WARNING).
        LogMessage (str): The message to log.
        token (str): API authorization token.
        ProcessName (str, optional): Name of the process.
        MachineName (str, optional): Machine name.

    Returns:
        dict: API response (JSON or error).
    """
    url = "https://app.kis-systems.com/api/v1/app/botlogs-add.php"

    payload = {
        "ProcessName": ProcessName,
        "MachineName": MachineName,
        "LogStatus": LogStatus,
        "LogMessage": LogMessage,
        "DateCreated": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": token
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


def UpdateMachineStatus(token: str, ProcessName: str, MachineName: str, ProcessStatus: str):
    """
    Updates the machine status in the orchestrator API.

    Args:
        token (str): API authorization token.
        ProcessName (str): Name of the process.
        MachineName (str): Machine name.
        ProcessStatus (str): Status of the process (e.g., "true", "false").

    Returns:
        dict: API response (JSON or error).
    """
    url = "https://app.kis-systems.com/api/v1/app/robot-status-update.php"

    payload = {
        "ProcessName": ProcessName,
        "MachineName": MachineName,
        "ProcessStatus": ProcessStatus
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": token
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}