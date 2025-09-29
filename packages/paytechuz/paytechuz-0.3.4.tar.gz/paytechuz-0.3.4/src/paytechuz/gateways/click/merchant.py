"""
Click merchant API operations.
"""
import hashlib
import logging
from typing import Dict, Any, Optional, Union

from paytechuz.core.http import HttpClient
from paytechuz.core.constants import ClickEndpoints
from paytechuz.core.utils import handle_exceptions, generate_timestamp

logger = logging.getLogger(__name__)


class ClickMerchantApi:
    """
    Click merchant API operations.

    This class provides methods for interacting with the Click merchant API,
    including checking payment status and canceling payments.
    """

    def __init__(
        self,
        http_client: HttpClient,
        service_id: str,
        merchant_user_id: Optional[str] = None,
        secret_key: Optional[str] = None
    ):
        """
        Initialize the Click merchant API.

        Args:
            http_client: HTTP client for making requests
            service_id: Click service ID
            merchant_user_id: Click merchant user ID
            secret_key: Secret key for authentication
        """
        self.http_client = http_client
        self.service_id = service_id
        self.merchant_user_id = merchant_user_id
        self.secret_key = secret_key

    def _generate_signature(self, data: Dict[str, Any]) -> str:
        """
        Generate signature for Click API requests.

        Args:
            data: Request data

        Returns:
            Signature string
        """
        if not self.secret_key:
            return ""

        # Sort keys alphabetically
        sorted_data = {k: data[k] for k in sorted(data.keys())}

        # Create string to sign
        sign_string = ""
        for key, value in sorted_data.items():
            if key != "sign":
                sign_string += str(value)

        # Add secret key
        sign_string += self.secret_key

        # Generate signature
        return hashlib.md5(sign_string.encode('utf-8')).hexdigest()

    @handle_exceptions
    def check_payment(self, id: Union[int, str]) -> Dict[str, Any]:
        """
        Check payment status.

        Args:
            account_id: Account ID or order ID

        Returns:
            Dict containing payment status and details
        """
        # Prepare request data
        data = {
            "service_id": self.service_id,
            "merchant_transaction_id": str(id),
            "request_id": str(generate_timestamp())
        }

        # Add signature if secret key is provided
        if self.secret_key:
            data["sign"] = self._generate_signature(data)

        # Make request
        response = self.http_client.post(
            endpoint=f"{ClickEndpoints.MERCHANT_API}/payment/status",
            json_data=data
        )

        return response

    @handle_exceptions
    def cancel_payment(
        self,
        id: Union[int, str],
        reason: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Cancel payment.

        Args:
            id: Account ID or order ID
            reason: Optional reason for cancellation

        Returns:
            Dict containing cancellation status and details
        """
        # Prepare request data
        data = {
            "service_id": self.service_id,
            "merchant_transaction_id": str(id),
            "request_id": str(generate_timestamp())
        }

        # Add reason if provided
        if reason:
            data["reason"] = reason

        # Add signature if secret key is provided
        if self.secret_key:
            data["sign"] = self._generate_signature(data)

        # Make request
        response = self.http_client.post(
            endpoint=f"{ClickEndpoints.MERCHANT_API}/payment/cancel",
            json_data=data
        )

        return response

    @handle_exceptions
    def create_invoice(
        self,
        id: Union[int, str],
        amount: Union[int, float],
        **kwargs
    ) -> Dict[str, Any]:
        """
        Create an invoice.

        Args:
            amount: Payment amount
            account_id: Account ID or order ID
            **kwargs: Additional parameters
                - description: Payment description
                - phone: Customer phone number
                - email: Customer email
                - expire_time: Invoice expiration time in minutes

        Returns:
            Dict containing invoice details
        """
        # Extract additional parameters
        description = kwargs.get('description', f'Payment for account {id}')
        phone = kwargs.get('phone')
        email = kwargs.get('email')
        expire_time = kwargs.get('expire_time', 60)  # Default 1 hour

        # Prepare request data
        data = {
            "service_id": self.service_id,
            "amount": float(amount),
            "merchant_transaction_id": str(id),
            "description": description,
            "request_id": str(generate_timestamp()),
            "expire_time": expire_time
        }

        # Add optional parameters
        if phone:
            data["phone"] = phone

        if email:
            data["email"] = email

        # Add signature if secret key is provided
        if self.secret_key:
            data["sign"] = self._generate_signature(data)

        # Make request
        response = self.http_client.post(
            endpoint=f"{ClickEndpoints.MERCHANT_API}/invoice/create",
            json_data=data
        )

        return response

    @handle_exceptions
    def check_invoice(self, invoice_id: str) -> Dict[str, Any]:
        """
        Check invoice status.

        Args:
            invoice_id: Invoice ID

        Returns:
            Dict containing invoice status and details
        """
        # Prepare request data
        data = {
            "service_id": self.service_id,
            "invoice_id": invoice_id,
            "request_id": str(generate_timestamp())
        }

        # Add signature if secret key is provided
        if self.secret_key:
            data["sign"] = self._generate_signature(data)

        # Make request
        response = self.http_client.post(
            endpoint=f"{ClickEndpoints.MERCHANT_API}/invoice/status",
            json_data=data
        )

        return response

    @handle_exceptions
    def cancel_invoice(
        self,
        invoice_id: str,
        reason: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Cancel invoice.

        Args:
            invoice_id: Invoice ID
            reason: Optional reason for cancellation

        Returns:
            Dict containing cancellation status and details
        """
        # Prepare request data
        data = {
            "service_id": self.service_id,
            "invoice_id": invoice_id,
            "request_id": str(generate_timestamp())
        }

        # Add reason if provided
        if reason:
            data["reason"] = reason

        # Add signature if secret key is provided
        if self.secret_key:
            data["sign"] = self._generate_signature(data)

        # Make request
        response = self.http_client.post(
            endpoint=f"{ClickEndpoints.MERCHANT_API}/invoice/cancel",
            json_data=data
        )

        return response
