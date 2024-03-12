import requests

from pywhatkit.core import exceptions


def text_to_handwriting(
    string: str, save_to: str = "pywhatkit.png", rgb: tuple = (0, 0, 0)
) -> None:
    """Convert the given String to Handwritten Characters"""

    data = requests.get(
        f"https://pywhatkit.herokuapp.com/handwriting?text={string}&rgb={rgb[0]},{rgb[1]},{rgb[2]}"
    )
    status_code = (
        data.status_code
    )  # source = https://www.geeksforgeeks.org/http-status-codes-successful-responses/
    
    with open(save_to, "wb") as file:
        file.write(data.content)
        file.close()
    

