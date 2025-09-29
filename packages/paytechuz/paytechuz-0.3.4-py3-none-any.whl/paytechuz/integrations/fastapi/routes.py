"""
FastAPI routes for PayTechUZ.
"""
import base64
import hashlib
import json
import logging
from datetime import datetime
from decimal import Decimal
from typing import Dict, Any, Optional

from fastapi import (
    APIRouter,
    HTTPException,
    Request,
    Response,
    status
)
from sqlalchemy.orm import Session

# pylint: disable=E0401,E0611
from paytechuz.core.exceptions import (
    PermissionDenied,
    InvalidAmount,
    TransactionNotFound,
    AccountNotFound,
    MethodNotFound,
    UnsupportedMethod,
    InvalidAccount
)

from .models import PaymentTransaction

logger = logging.getLogger(__name__)

router = APIRouter()


class PaymeWebhookHandler:
    """
    Base Payme webhook handler for FastAPI.

    This class handles webhook requests from the Payme payment system.
    You can extend this class and override the event methods to customize
    the behavior.

    Example:
    ```python
    from paytechuz.integrations.fastapi.routes import PaymeWebhookHandler

    class CustomPaymeWebhookHandler(PaymeWebhookHandler):
        def successfully_payment(self, params, transaction):
            # Your custom logic here
            print(f"Payment successful: {transaction.transaction_id}")

            # Update your order status
            order = db.query(Order).filter(
                Order.id == transaction.account_id
            ).first()
            order.status = 'paid'
            db.commit()
    ```
    """

    def __init__(
        self,
        db: Session,
        payme_id: str,
        payme_key: str,
        account_model: Any,
        account_field: str = 'id',
        amount_field: str = 'amount',
        one_time_payment: bool = True
    ):
        """
        Initialize the Payme webhook handler.

        Args:
            db: Database session
            payme_id: Payme merchant ID
            payme_key: Payme merchant key
            account_model: Account model class
            account_field: Account field name
            amount_field: Amount field name
            one_time_payment: Whether to validate amount
        """
        self.db = db
        self.payme_id = payme_id
        self.payme_key = payme_key
        self.account_model = account_model
        self.account_field = account_field
        self.amount_field = amount_field
        self.one_time_payment = one_time_payment

    async def handle_webhook(self, request: Request) -> Response:
        """
        Handle webhook request from Payme.

        Args:
            request: FastAPI request object

        Returns:
            Response object with JSON data
        """
        try:
            # Check authorization
            auth_header = request.headers.get('Authorization')
            self._check_auth(auth_header)

            # Parse request data
            data = await request.json()
            method = data.get('method')
            params = data.get('params', {})
            request_id = data.get('id', 0)

            # Process the request based on the method
            if method == 'CheckPerformTransaction':
                result = self._check_perform_transaction(params)
            elif method == 'CreateTransaction':
                result = self._create_transaction(params)
            elif method == 'PerformTransaction':
                result = self._perform_transaction(params)
            elif method == 'CheckTransaction':
                result = self._check_transaction(params)
            elif method == 'CancelTransaction':
                result = self._cancel_transaction(params)
            elif method == 'GetStatement':
                result = self._get_statement(params)
            else:
                return Response(
                    content=json.dumps({
                        'jsonrpc': '2.0',
                        'id': request_id,
                        'error': {
                            'code': -32601,
                            'message': f"Method not supported: {method}"
                        }
                    }),
                    media_type="application/json",
                    status_code=200  # Always return 200 for RPC-style errors
                )

            # Return the result
            return Response(
                content=json.dumps({
                    'jsonrpc': '2.0',
                    'id': request_id,
                    'result': result
                }),
                media_type="application/json",
                status_code=200
            )

        except PermissionDenied:
            return Response(
                content=json.dumps({
                    'jsonrpc': '2.0',
                    'id': request_id if 'request_id' in locals() else 0,
                    'error': {
                        'code': -32504,
                        'message': "permission denied"
                    }
                }),
                media_type="application/json",
                status_code=200  # Return 200 status code for all errors
            )

        except (MethodNotFound, UnsupportedMethod) as e:
            return Response(
                content=json.dumps({
                    'jsonrpc': '2.0',
                    'id': request_id if 'request_id' in locals() else 0,
                    'error': {
                        'code': -32601,
                        'message': str(e)
                    }
                }),
                media_type="application/json",
                status_code=200  # Return 200 status code for all errors
            )

        except AccountNotFound as e:
            return Response(
                content=json.dumps({
                    'jsonrpc': '2.0',
                    'id': request_id if 'request_id' in locals() else 0,
                    'error': {
                        'code': -31050,
                        'message': str(e)
                    }
                }),
                media_type="application/json",
                status_code=200
            )

        except InvalidAmount as e:
            return Response(
                content=json.dumps({
                    'jsonrpc': '2.0',
                    'id': request_id if 'request_id' in locals() else 0,
                    'error': {
                        'code': -31001,
                        'message': str(e)
                    }
                }),
                media_type="application/json",
                status_code=200
            )

        except InvalidAccount as e:
            return Response(
                content=json.dumps({
                    'jsonrpc': '2.0',
                    'id': request_id if 'request_id' in locals() else 0,
                    'error': {
                        'code': -31050,
                        'message': str(e)
                    }
                }),
                media_type="application/json",
                status_code=200
            )

        except TransactionNotFound as e:
            return Response(
                content=json.dumps({
                    'jsonrpc': '2.0',
                    'id': request_id if 'request_id' in locals() else 0,
                    'error': {
                        'code': -31001,
                        'message': str(e)
                    }
                }),
                media_type="application/json",
                status_code=200
            )

        except Exception as e:
            logger.exception(f"Unexpected error in Payme webhook: {e}")
            return Response(
                content=json.dumps({
                    'jsonrpc': '2.0',
                    'id': request_id if 'request_id' in locals() else 0,
                    'error': {
                        'code': -32400,
                        'message': 'Internal error'
                    }
                }),
                media_type="application/json",
                status_code=200
            )

    def _check_auth(self, auth_header: Optional[str]) -> None:
        """
        Check authorization header.
        """
        if not auth_header:
            raise PermissionDenied("Missing authentication credentials")

        try:
            auth_parts = auth_header.split()
            if len(auth_parts) != 2 or auth_parts[0].lower() != 'basic':
                raise PermissionDenied("Invalid authentication format")

            auth_decoded = base64.b64decode(auth_parts[1]).decode('utf-8')
            _, password = auth_decoded.split(':')  # We only need the password

            if password != self.payme_key:
                raise PermissionDenied("Invalid merchant key")
        except PermissionDenied:
            raise
        except Exception as e:
            logger.error(f"Authentication error: {e}")
            raise PermissionDenied("Authentication error")

    def _find_account(self, params: Dict[str, Any]) -> Any:
        """
        Find account by parameters.
        """
        account_value = params.get('account', {}).get(self.account_field)
        if not account_value:
            raise AccountNotFound("Account not found in parameters")

        lookup_field = 'id' if self.account_field == 'order_id' else (
            self.account_field
        )

        if (lookup_field == 'id' and
                isinstance(account_value, str) and
                account_value.isdigit()):
            account_value = int(account_value)

        account = self.db.query(self.account_model).filter_by(
            **{lookup_field: account_value}
        ).first()
        if not account:
            raise AccountNotFound(
                f"Account with {self.account_field}={account_value} not found"
            )

        return account

    def _validate_amount(self, account: Any, amount: int) -> bool:
        """
        Validate payment amount.
        """
        # If one_time_payment is disabled, we still validate the amount
        # but we don't require it to match exactly

        expected_amount = Decimal(getattr(account, self.amount_field)) * 100
        received_amount = Decimal(amount)

        # If one_time_payment is enabled, amount must match exactly
        if self.one_time_payment and expected_amount != received_amount:
            raise InvalidAmount(
                (f"Invalid amount. Expected: {expected_amount}, "
                 f"received: {received_amount}")
            )

        # If one_time_payment is disabled, amount must be positive
        if not self.one_time_payment and received_amount <= 0:
            raise InvalidAmount(
                (f"Invalid amount. Amount must be positive, "
                 f"received: {received_amount}")
            )

        return True

    def _check_perform_transaction(
        self, params: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Handle CheckPerformTransaction method.
        """
        account = self._find_account(params)
        self._validate_amount(account, params.get('amount'))

        # Call the event method
        self.before_check_perform_transaction(params, account)

        return {'allow': True}

    def _create_transaction(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Handle CreateTransaction method.
        """
        transaction_id = params.get('id')
        account = self._find_account(params)
        amount = params.get('amount')

        self._validate_amount(account, amount)

        # Check if there's already a transaction for this account with a
        # different transaction_id. Only check if one_time_payment is enabled
        if self.one_time_payment:
            # Check for existing transactions in non-final states
            existing_transactions = self.db.query(PaymentTransaction).filter(
                PaymentTransaction.gateway == PaymentTransaction.PAYME,
                PaymentTransaction.account_id == str(account.id)
            ).filter(
                PaymentTransaction.transaction_id != transaction_id
            ).all()

            # Filter out transactions in final states
            # (SUCCESSFULLY, CANCELLED, CANCELLED_DURING_INIT)
            non_final_transactions = [
                t for t in existing_transactions
                if t.state not in [
                    PaymentTransaction.SUCCESSFULLY,
                    PaymentTransaction.CANCELLED,
                    PaymentTransaction.CANCELLED_DURING_INIT
                ]
            ]

            if non_final_transactions:
                # If there's already a transaction for this account with a
                # different transaction_id in a non-final state, raise an error
                raise InvalidAccount(
                    (f"Account with {self.account_field}={account.id} "
                     f"already has a pending transaction")
                )

        # Check for existing transaction with the same transaction_id
        transaction = self.db.query(PaymentTransaction).filter(
            PaymentTransaction.gateway == PaymentTransaction.PAYME,
            PaymentTransaction.transaction_id == transaction_id
        ).first()

        if transaction:
            # Call the event method
            self.transaction_already_exists(params, transaction)

            # For existing transactions, use the original time from extra_data
            # This ensures the same response is returned for repeated calls
            create_time = transaction.extra_data.get(
                'create_time', params.get('time')
            )

            return {
                'transaction': transaction.transaction_id,
                'state': transaction.state,
                'create_time': create_time,
            }

        # Create new transaction
        transaction = PaymentTransaction(
            gateway=PaymentTransaction.PAYME,
            transaction_id=transaction_id,
            account_id=account.id,
            amount=Decimal(amount) / 100,  # Convert from tiyin to som
            state=PaymentTransaction.INITIATING,
            extra_data={
                'account_field': self.account_field,
                'account_value': (
                    params.get('account', {}).get(self.account_field)
                ),
                'create_time': params.get('time'),
                'raw_params': params
            }
        )

        self.db.add(transaction)
        self.db.commit()
        self.db.refresh(transaction)

        # Call the event method
        self.transaction_created(params, transaction, account)

        # Use the time from the request params
        # instead of transaction.created_at
        create_time = params.get('time')

        return {
            'transaction': transaction.transaction_id,
            'state': transaction.state,
            'create_time': create_time,
        }

    def _perform_transaction(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Handle PerformTransaction method.
        """
        transaction_id = params.get('id')

        transaction = self.db.query(PaymentTransaction).filter(
            PaymentTransaction.gateway == PaymentTransaction.PAYME,
            PaymentTransaction.transaction_id == transaction_id
        ).first()

        if not transaction:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Transaction {transaction_id} not found"
            )

        # Mark transaction as paid
        transaction.mark_as_paid(self.db)

        # Call the event method
        self.successfully_payment(params, transaction)

        return {
            'transaction': transaction.transaction_id,
            'state': transaction.state,
            'perform_time': int(
                transaction.performed_at.timestamp() * 1000
            ) if transaction.performed_at else 0,
        }

    def _check_transaction(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Handle CheckTransaction method.
        """
        transaction_id = params.get('id')

        transaction = self.db.query(PaymentTransaction).filter(
            PaymentTransaction.gateway == PaymentTransaction.PAYME,
            PaymentTransaction.transaction_id == transaction_id
        ).first()

        if not transaction:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Transaction {transaction_id} not found"
            )

        # Call the event method
        self.check_transaction(params, transaction)

        # Use the original time from extra_data for consistency
        create_time = transaction.extra_data.get(
            'create_time', int(transaction.created_at.timestamp() * 1000)
        )

        return {
            'transaction': transaction.transaction_id,
            'state': transaction.state,
            'create_time': create_time,
            'perform_time': (
                int(transaction.performed_at.timestamp() * 1000)
                if transaction.performed_at else 0
            ),
            'cancel_time': (
                int(transaction.cancelled_at.timestamp() * 1000)
                if transaction.cancelled_at else 0
            ),
            'reason': transaction.reason,
        }

    def _cancel_response(
        self, transaction: PaymentTransaction
    ) -> Dict[str, Any]:
        """
        Helper method to generate cancel transaction response.

        Args:
            transaction: Transaction object

        Returns:
            Dict containing the response
        """
        # Get reason from the transaction model
        reason = transaction.reason

        # If reason is None, use default reason
        if reason is None:
            from paytechuz.core.constants import PaymeCancelReason
            reason = PaymeCancelReason.REASON_FUND_RETURNED  # Default reason 5
            # Update the transaction with the default reason
            transaction.reason = reason
            self.db.commit()
            self.db.refresh(transaction)

        return {
            'transaction': transaction.transaction_id,
            'state': transaction.state,
            'cancel_time': (int(transaction.cancelled_at.timestamp() * 1000)
                            if transaction.cancelled_at else 0),
            'reason': reason,
        }

    def _cancel_transaction(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Handle CancelTransaction method.
        """
        transaction_id = params.get('id')
        reason = params.get('reason')

        transaction = self.db.query(PaymentTransaction).filter(
            PaymentTransaction.gateway == PaymentTransaction.PAYME,
            PaymentTransaction.transaction_id == transaction_id
        ).first()

        if not transaction:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Transaction {transaction_id} not found"
            )

        # Check if transaction is already cancelled
        cancelled_states = [
            PaymentTransaction.CANCELLED,
            PaymentTransaction.CANCELLED_DURING_INIT
        ]
        if transaction.state in cancelled_states:
            # If transaction is already cancelled, update the reason
            # if provided
            if 'reason' in params:
                reason = params.get('reason')

                # If reason is not provided, use default reason
                # from PaymeCancelReason
                if reason is None:
                    from paytechuz.core.constants import PaymeCancelReason
                    # Default reason 5
                    reason = PaymeCancelReason.REASON_FUND_RETURNED

                # Convert reason to int if it's a string
                if isinstance(reason, str) and reason.isdigit():
                    reason = int(reason)

                # Store the reason directly in the reason column
                transaction.reason = reason

                # For backward compatibility, also store in extra_data
                extra_data = transaction.extra_data or {}
                extra_data['cancel_reason'] = reason
                transaction.extra_data = extra_data

                self.db.commit()
                self.db.refresh(transaction)

            # Return the existing data
            return self._cancel_response(transaction)

        # Use mark_as_cancelled method to ensure consistent behavior
        reason = params.get('reason')
        transaction.mark_as_cancelled(self.db, reason=reason)

        # Ensure the reason is stored in extra_data
        extra_data = transaction.extra_data or {}
        if 'cancel_reason' not in extra_data:
            # Default reason 5 if none provided
            extra_data['cancel_reason'] = reason if reason is not None else 5
            transaction.extra_data = extra_data
            self.db.commit()
            self.db.refresh(transaction)

        # Call the event method
        self.cancelled_payment(params, transaction)

        # Return cancel response
        return self._cancel_response(transaction)

    def _get_statement(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Handle GetStatement method.
        """
        from_date = params.get('from')
        to_date = params.get('to')

        # Convert milliseconds to datetime objects
        if from_date:
            from_datetime = datetime.fromtimestamp(from_date / 1000)
        else:
            from_datetime = datetime.fromtimestamp(0)  # Unix epoch start

        if to_date:
            to_datetime = datetime.fromtimestamp(to_date / 1000)
        else:
            to_datetime = datetime.now()  # Current time

        # Get transactions in the date range
        transactions = self.db.query(PaymentTransaction).filter(
            PaymentTransaction.gateway == PaymentTransaction.PAYME,
            PaymentTransaction.created_at >= from_datetime,
            PaymentTransaction.created_at <= to_datetime
        ).all()

        # Format transactions for response
        result = []
        for transaction in transactions:
            result.append({
                'id': transaction.transaction_id,
                'time': int(transaction.created_at.timestamp() * 1000),
                'amount': int(transaction.amount * 100),  # Convert to tiyin
                'account': {
                    self.account_field: transaction.account_id
                },
                'state': transaction.state,
                'create_time': transaction.extra_data.get(
                    'create_time',
                    int(transaction.created_at.timestamp() * 1000)
                ),
                'perform_time': (
                    int(transaction.performed_at.timestamp() * 1000)
                    if transaction.performed_at else 0
                ),
                'cancel_time': (
                    int(transaction.cancelled_at.timestamp() * 1000)
                    if transaction.cancelled_at else 0
                ),
                'reason': transaction.reason,
            })

        # Call the event method
        self.get_statement(params, result)

        return {'transactions': result}

    # Event methods that can be overridden by subclasses

    def before_check_perform_transaction(
        self, params: Dict[str, Any], account: Any
    ) -> None:
        """
        Called before checking if a transaction can be performed.

        Args:
            params: Request parameters
            account: Account object
        """
        pass

    def transaction_already_exists(
        self, params: Dict[str, Any], transaction: PaymentTransaction
    ) -> None:
        """
        Called when a transaction already exists.

        Args:
            params: Request parameters
            transaction: Transaction object
        """
        pass

    def transaction_created(
        self,
        params: Dict[str, Any],
        transaction: PaymentTransaction,
        account: Any
    ) -> None:
        """
        Called when a transaction is created.

        Args:
            params: Request parameters
            transaction: Transaction object
            account: Account object
        """
        pass

    def successfully_payment(
        self,
        params: Dict[str, Any],
        transaction: PaymentTransaction
    ) -> None:
        """
        Called when a payment is successful.

        Args:
            params: Request parameters
            transaction: Transaction object
        """
        pass

    def check_transaction(
        self,
        params: Dict[str, Any],
        transaction: PaymentTransaction
    ) -> None:
        """
        Called when checking a transaction.

        Args:
            params: Request parameters
            transaction: Transaction object
        """
        pass

    def cancelled_payment(
        self,
        params: Dict[str, Any],
        transaction: PaymentTransaction
    ) -> None:
        """
        Called when a payment is cancelled.

        Args:
            params: Request parameters
            transaction: Transaction object
        """
        pass

    def get_statement(
        self,
        params: Dict[str, Any],
        transactions: list
    ) -> None:
        """
        Called when getting a statement.

        Args:
            params: Request parameters
            transactions: List of transactions
        """
        pass


class ClickWebhookHandler:
    """
    Base Click webhook handler for FastAPI.

    This class handles webhook requests from the Click payment system.
    You can extend this class and override the event methods to customize
    the behavior.

    Example:
    ```python
    from paytechuz.integrations.fastapi.routes import ClickWebhookHandler

    class CustomClickWebhookHandler(ClickWebhookHandler):
        def successfully_payment(self, params, transaction):
            # Your custom logic here
            print(f"Payment successful: {transaction.transaction_id}")

            # Update your order status
            order = (db.query(Order)
                     .filter(Order.id == transaction.account_id)
                     .first())
            order.status = 'paid'
            db.commit()
    ```
    """

    def __init__(
        self,
        db: Session,
        service_id: str,
        secret_key: str,
        account_model: Any,
        commission_percent: float = 0.0
    ):
        """
        Initialize the Click webhook handler.

        Args:
            db: Database session
            service_id: Click service ID
            secret_key: Click secret key
            account_model: Account model class
            commission_percent: Commission percentage
        """
        self.db = db
        self.service_id = service_id
        self.secret_key = secret_key
        self.account_model = account_model
        self.commission_percent = commission_percent

    async def handle_webhook(self, request: Request) -> Dict[str, Any]:
        """
        Handle webhook request from Click.

        Args:
            request: FastAPI request object

        Returns:
            Response data
        """
        try:
            # Get parameters from request
            form_data = await request.form()
            params = {key: form_data.get(key) for key in form_data}

            # Check authorization
            self._check_auth(params)

            # Extract parameters
            click_trans_id = params.get('click_trans_id')
            merchant_trans_id = params.get('merchant_trans_id')
            amount = float(params.get('amount', 0))
            action = int(params.get('action', -1))
            error = int(params.get('error', 0))

            # Find account
            try:
                account = self._find_account(merchant_trans_id)
            except Exception:
                logger.error(f"Account not found: {merchant_trans_id}")
                return {
                    'click_trans_id': click_trans_id,
                    'merchant_trans_id': merchant_trans_id,
                    'error': -5,
                    'error_note': "User not found"
                }

            # Validate amount
            try:
                expected = float(getattr(account, 'amount', 0))
                self._validate_amount(amount, expected)
            except Exception as e:
                logger.error(f"Invalid amount: {e}")
                return {
                    'click_trans_id': click_trans_id,
                    'merchant_trans_id': merchant_trans_id,
                    'error': -2,
                    'error_note': str(e)
                }

            # Check if transaction already exists
            transaction = self.db.query(PaymentTransaction).filter(
                PaymentTransaction.gateway == PaymentTransaction.CLICK,
                PaymentTransaction.transaction_id == click_trans_id
            ).first()

            if transaction:
                # If transaction is already completed, return success
                if transaction.state == PaymentTransaction.SUCCESSFULLY:
                    # Call the event method
                    self.transaction_already_exists(params, transaction)

                    return {
                        'click_trans_id': click_trans_id,
                        'merchant_trans_id': merchant_trans_id,
                        'merchant_prepare_id': transaction.id,
                        'error': 0,
                        'error_note': "Success"
                    }

                # If transaction is cancelled, return error
                if transaction.state == PaymentTransaction.CANCELLED:
                    return {
                        'click_trans_id': click_trans_id,
                        'merchant_trans_id': merchant_trans_id,
                        'merchant_prepare_id': transaction.id,
                        'error': -9,
                        'error_note': "Transaction cancelled"
                    }

            # Handle different actions
            if action == 0:  # Prepare
                # Create transaction
                transaction = PaymentTransaction(
                    gateway=PaymentTransaction.CLICK,
                    transaction_id=click_trans_id,
                    account_id=merchant_trans_id,
                    amount=amount,
                    state=PaymentTransaction.INITIATING,
                    extra_data={
                        'raw_params': params
                    }
                )

                self.db.add(transaction)
                self.db.commit()
                self.db.refresh(transaction)

                # Call the event method
                self.transaction_created(params, transaction, account)

                return {
                    'click_trans_id': click_trans_id,
                    'merchant_trans_id': merchant_trans_id,
                    'merchant_prepare_id': transaction.id,
                    'error': 0,
                    'error_note': "Success"
                }

            elif action == 1:  # Complete
                # Check if error is negative (payment failed)
                is_successful = error >= 0

                if not transaction:
                    # Create transaction if it doesn't exist
                    transaction = PaymentTransaction(
                        gateway=PaymentTransaction.CLICK,
                        transaction_id=click_trans_id,
                        account_id=merchant_trans_id,
                        amount=amount,
                        state=PaymentTransaction.INITIATING,
                        extra_data={
                            'raw_params': params
                        }
                    )

                    self.db.add(transaction)
                    self.db.commit()
                    self.db.refresh(transaction)

                if is_successful:
                    # Mark transaction as paid
                    transaction.mark_as_paid(self.db)

                    # Call the event method
                    self.successfully_payment(params, transaction)
                else:
                    # Mark transaction as cancelled
                    error_reason = f"Error code: {error}"
                    transaction.mark_as_cancelled(self.db, reason=error_reason)

                    # Call the event method
                    self.cancelled_payment(params, transaction)

                return {
                    'click_trans_id': click_trans_id,
                    'merchant_trans_id': merchant_trans_id,
                    'merchant_prepare_id': transaction.id,
                    'error': 0,
                    'error_note': "Success"
                }

            else:
                logger.error(f"Unsupported action: {action}")
                return {
                    'click_trans_id': click_trans_id,
                    'merchant_trans_id': merchant_trans_id,
                    'error': -3,
                    'error_note': "Action not found"
                }

        except Exception as e:
            logger.exception(f"Unexpected error in Click webhook: {e}")
            return {
                'error': -7,
                'error_note': "Internal error"
            }

    def _check_auth(self, params: Dict[str, Any]) -> None:
        """
        Check authentication using signature.
        """
        if not all([self.service_id, self.secret_key]):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Missing required settings: service_id or secret_key"
            )

        if str(params.get("service_id")) != self.service_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid service ID"
            )

        sign_string = params.get("sign_string")
        sign_time = params.get("sign_time")

        if not sign_string or not sign_time:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Missing signature parameters"
            )

        # Prepare signature components
        text_parts = [
            str(params.get("click_trans_id") or ""),
            str(params.get("service_id") or ""),
            str(self.secret_key or ""),
            str(params.get("merchant_trans_id") or ""),
            str(params.get("merchant_prepare_id") or ""),
            str(params.get("amount") or ""),
            str(params.get("action") or ""),
            str(sign_time)
        ]

        # Calculate hash
        calculated_hash = hashlib.md5("".join(text_parts).encode("utf-8")).hexdigest()

        if calculated_hash != sign_string:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid signature"
            )

    def _find_account(self, merchant_trans_id: str) -> Any:
        """
        Find account by merchant_trans_id.
        """
        # Try to convert merchant_trans_id to int if it's a string and a digit
        if isinstance(merchant_trans_id, str) and merchant_trans_id.isdigit():
            merchant_trans_id = int(merchant_trans_id)

        account = (
            self.db.query(self.account_model)
            .filter_by(id=merchant_trans_id)
            .first()
        )
        if not account:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Account with id={merchant_trans_id} not found"
            )

        return account

    def _validate_amount(
        self, received_amount: float, expected_amount: float
    ) -> None:
        """
        Validate payment amount.
        """
        # Add commission if needed
        if self.commission_percent > 0:
            commission_factor = 1 + (self.commission_percent / 100)
            expected_amount = expected_amount * commission_factor
            expected_amount = round(expected_amount, 2)

        # Allow small difference due to floating point precision
        if abs(received_amount - expected_amount) > 0.01:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=(
                    f"Incorrect amount. Expected: {expected_amount}, "
                    f"received: {received_amount}"
                )
            )

    # Event methods that can be overridden by subclasses

    def transaction_already_exists(
        self,
        params: Dict[str, Any],
        transaction: PaymentTransaction
    ) -> None:
        """
        Called when a transaction already exists.

        Args:
            params: Request parameters
            transaction: Transaction object
        """
        pass

    def transaction_created(
        self,
        params: Dict[str, Any],
        transaction: PaymentTransaction,
        account: Any
    ) -> None:
        """
        Called when a transaction is created.

        Args:
            params: Request parameters
            transaction: Transaction object
            account: Account object
        """
        pass

    def successfully_payment(
        self,
        params: Dict[str, Any],
        transaction: PaymentTransaction
    ) -> None:
        """
        Called when a payment is successful.

        Args:
            params: Request parameters
            transaction: Transaction object
        """
        pass

    def cancelled_payment(
        self,
        params: Dict[str, Any],
        transaction: PaymentTransaction
    ) -> None:
        """
        Called when a payment is cancelled.

        Args:
            params: Request parameters
            transaction: Transaction object
        """
        pass
