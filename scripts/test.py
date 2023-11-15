import os
import requests


class WhatsappIntegrations:
    """App to send text"""

    def __init__(self):
        """Class initialization"""
        self.phone_id = os.environ.get("PHONE_ID")
        self.access_token = os.environ.get("ACCESS_TOKEN")
        self.auth = f"Bearer {self.access_token}"
        self.phone_numbers = ["56956172015", "56963410066"]

        self.send_whatsapp_messages()

    def send_whatsapp_messages(self):
        """Send WhatsApp messages for each phone number"""
        for phone_number in self.phone_numbers:
            url = f"https://graph.facebook.com/v17.0/{self.phone_id}/messages"
            headers = {
                "Authorization": self.auth,
                "Content-Type": "application/json",
            }
            data = {
                "messaging_product": "whatsapp",
                "to": phone_number,
                "type": "template",
                "template": {"name": "touchpoint_simulacion", "language": {"code": "es"}},
            }

            try:
                response = requests.post(url, headers=headers, json=data)
                response.raise_for_status()
                print(f"Message sent to {phone_number}: {response.text}")
            except requests.exceptions.RequestException as e:
                print(f"Error during the request to {phone_number}: {e}")


if __name__ == "__main__":
    WhatsappIntegrations()
