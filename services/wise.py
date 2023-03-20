import requests
from decouple import config


TARGET_CURRENCY = "BGN"


class WiseService:
    def __init__(self):
        self.base_url = config("WISE_URL")
        self.headers = {
            "Authorization": f"Bearer {config('WISE_TOKEN')}",
            "Content-Type": "application/json",
        }
        self.profile_id = config("WISE_PROFILE_ID")

    def create_quota(self, amount):
        url = f"{self.base_url}/v3/profiles/{self.profile_id}/quotes"
        body = {
            "sourceCurrency": "EUR",
            "targetCurrency": TARGET_CURRENCY,
            "sourceAmount": amount,
        }
        response = requests.post(url, json=body, headers=self.headers)
        return response.json()["id"]

    def create_recipient(self, full_name, iban):
        url = f"{self.base_url}/v1/accounts"
        body = {
            "currency": TARGET_CURRENCY,
            "type": "iban",
            "profile": self.profile_id,
            "ownedByCustomer": False,
            "accountHolderName": full_name,
            "details": {"legalType": "PRIVATE", "iban": iban},
        }
        response = requests.post(url, json=body, headers=self.headers)
        return response.json()["id"]

    def create_transfer(self, quote_id, recipient_id, custom_transaction_id):
        url = f"{self.base_url}/v1/transfers"
        body = {
            "targetAccount": recipient_id,
            "quoteUuid": quote_id,
            "customerTransactionId": custom_transaction_id,
            "details": {},
        }
        response = requests.post(url, json=body, headers=self.headers)
        return response.json()["id"]

    def fund_transfer(self, transfer_id):
        url = f"{self.base_url}/v3/profiles/{self.profile_id}/transfers/{transfer_id}/payments"
        body = {"type": "BALANCE"}
        response = requests.post(url, json=body, headers=self.headers)
        return response

    def cancel_transfer(self, transfer_id):
        url = f"{self.base_url}/v1/transfers/{transfer_id}/cancel"
        response = requests.put(url, json={}, headers=self.headers)
        return response


if __name__ == "__main__":
    wise_service = WiseService()
    # quote_id = wise_service.create_quota(150)
    # recipient_id = wise_service.create_recipient("Ines KenovaFlas", "BG80BNBG96611020345678")
    # custom_transaction_id = str(uuid.uuid4())
    # transfer_id = wise_service.create_transfer(quote_id, recipient_id, custom_transaction_id)
    wise_service.cancel_transfer(51782855)
