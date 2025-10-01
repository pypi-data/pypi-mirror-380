import requests
from typing import Optional
import logging

# Настройка логирования
logger = logging.getLogger("PayvoSDK")
logger.setLevel(logging.DEBUG)  # Можно менять на INFO для меньше подробностей
handler = logging.StreamHandler()
formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


class Payvo:
    PRODUCTION_URL = "https://api.payvo.ru/public/"

    def __init__(self, merchant_id: str, merchant_secret_key: str):
        self.merchant_id = merchant_id
        self.secret_key = merchant_secret_key
        self.base_url = self.PRODUCTION_URL
        self.headers = {
            "Content-Type": "application/json",
            "merchant-id": self.merchant_id,
            "merchant-secret-key": self.secret_key
        }

    def create_payment(self, amount: float, description: str,
                       return_url: str,
                       payment_method_type: str = None,
                       extra: Optional[dict] = None):
        if not return_url:
            raise ValueError("return_url обязателен для поля confirmation")

        data = {
            "amount": amount,
            "description": description,
            "confirmation": {
                "type": "redirect",
                "return_url": return_url
            }
        }

        if payment_method_type:
            data["payment_method_type"] = payment_method_type

        if extra:
            data.update(extra)

        logger.debug("Создание платежа: %s", data)

        try:
            resp = requests.post(f"{self.base_url}payments", json=data, headers=self.headers)
            resp.raise_for_status()
            logger.info("Платеж успешно создан: %s", resp.json())
            return resp.json()
        except requests.exceptions.HTTPError as e:
            logger.error("HTTPError при создании платежа: %s %s", e.response.status_code, e.response.text)
            raise
        except requests.exceptions.RequestException as e:
            logger.error("Ошибка запроса при создании платежа: %s", str(e))
            raise

    def get_payment(self, payment_uuid: str):
        logger.debug("Получение информации о платеже: %s", payment_uuid)
        try:
            resp = requests.get(f"{self.base_url}payments/{payment_uuid}", headers=self.headers)
            resp.raise_for_status()
            logger.info("Информация о платеже: %s", resp.json())
            return resp.json()
        except requests.exceptions.HTTPError as e:
            logger.error("HTTPError при получении платежа: %s %s", e.response.status_code, e.response.text)
            raise
        except requests.exceptions.RequestException as e:
            logger.error("Ошибка запроса при получении платежа: %s", str(e))
            raise

    def create_refund(self, payment_uuid: str, amount: float, description: Optional[str] = None):
        data = {"payment_uuid": payment_uuid, "amount": amount, "description": description}
        logger.debug("Создание возврата: %s", data)
        try:
            resp = requests.post(f"{self.base_url}refunds", json=data, headers=self.headers)
            resp.raise_for_status()
            logger.info("Возврат успешно создан: %s", resp.json())
            return resp.json()
        except requests.exceptions.HTTPError as e:
            logger.error("HTTPError при создании возврата: %s %s", e.response.status_code, e.response.text)
            raise
        except requests.exceptions.RequestException as e:
