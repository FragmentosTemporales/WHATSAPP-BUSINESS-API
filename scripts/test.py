import os
import requests


class WhatsappIntegrations:
    """App to send text"""

    def __init__(self):
        """Class initialization"""
        self.business_id = os.environ.get("WSP_BUSINESS")
        self.access_token = os.environ.get("ACCESS_TOKEN")
        self.auth = f"Bearer {self.access_token}"
        self.url_base = "https://graph.facebook.com/v17.0/"
        self.phone_numbers = ["56956172015", "56963410066"]

    def send_whatsapp_messages(self, template_name, language_code):
        """Send a WhatsApp message to the user

        Args:

        template_name: Without symbols, spaces, or capital letters. Example: 'defect_template'.

        language_code: Language encoding. Example: 'es_ES', 'en_US'.
        """

        self.phone_id = os.environ.get("PHONE_ID")
        self.template_name = template_name

        for phone_number in self.phone_numbers:
            url = f"{self.url_base}{self.phone_id}/messages"
            headers = {
                "Authorization": self.auth,
                "Content-Type": "application/json",
            }
            data = {
                "messaging_product": "whatsapp",
                "to": phone_number,
                "type": "template",
                "template": {
                    "name": f"{self.template_name}",
                    "language": {
                        "code": f"{language_code}"},
                },
            }

            try:
                response = requests.post(url, headers=headers, json=data)
                print(f"Message sent to {phone_number}: {response.text}")
            except requests.exceptions.RequestException as e:
                print(f"Error during the request to {phone_number}: {e}")

    def create_template(self):
        """Function to create a template 
        
        Args:
        
        data = {
            'name' : 'template_name',
            'languaje' : 'template_languaje_code'
            'category' : 'MARKETING',
            'components' : array[]
        }
        """
        url = f"{self.url_base}{self.business_id}/message_templates"
        headers = {
            "Authorization": self.auth,
            "Content-Type": "application/json",
        }
        data = {
            "name": "mensaje_bienvenida_2023",
            "language": "es_ES",
            "category": "MARKETING",
            "components": [
                {
                    "type": "HEADER", 
                    "format": "TEXT", 
                    "text": "MENSAJE DE PRUEBA PARA ALUMNOS CON TOUCHPOINT EN SIMULACIÓN"},
                {
                    "type": "BODY", 
                    "text": "Has pasado por el proceso de simulación y cuentas con el puntaje necesario para postular a nuestra Universidad. Sigue el proceso para iniciar tu matriculación."},
                {
                    "type": "FOOTER", 
                    "text": "¿No te interesa? Toca 'Detener promociones'"},
                {
                    "type": "BUTTONS",
                    "buttons": [
                        {
                            "type": "URL",
                            "text": "Ir a Matrícula",
                            "url": "https://www.facebook.com/business/help/2640149499569241",
                        },
                        {
                            "type": "QUICK_REPLY", 
                            "text": "Detener promociones"},
                    ],
                },
            ],
        }
        
        try:
            response = requests.post(url, headers=headers, json=data)
            print(response.json())
            id = response.json().get('id')
            response.raise_for_status()
            print(f"Plantilla creada con id : {id}")
        except requests.exceptions.RequestException as e:
            print(f"Error during the request : {e}")

    def delete_template(self, template_id, template_name):
        """ Function to Delete a template 
        
        Args:
        
        template_id : template ID to Delete

        template_name : template Name to delete
        """
        url = f"{self.url_base}{self.business_id}/message_templates?hsm_id={template_id}&name={template_name}"
        headers = {
            "Authorization": self.auth,
            "Content-Type": "application/json",
        }
        try:
            response = requests.delete(url, headers=headers)
            response.raise_for_status()
            print("Template success deleted")
        except requests.exceptions.RequestException as e:
            print(f"Error during the request : {e}")

if __name__ == "__main__":
    WhatsappIntegrations()