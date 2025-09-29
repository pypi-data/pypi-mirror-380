import requests
from typing import Dict, Any, Optional, Union
from dataclasses import dataclass
from datetime import datetime
import uuid

@dataclass
class PaymentRequest:
    agent_id: str
    amount: int
    currency: str = "usd"
    description: Optional[str] = None
    payment_method: str = "stripe"  # "stripe" or "braintree"
    recipient_account_id: Optional[str] = None
    recipient_business_name: Optional[str] = None
    recipient_email: Optional[str] = None


@dataclass
class PaymentResponse:
    payment_intent_id: str
    client_secret: str
    status: str
    receipt: Dict[str, Any]
    payment_method: str = "stripe"


@dataclass
class RecipientSearchResult:
    query: str
    results: list
    total_found: int

@dataclass
class Receipt:
    receipt_id: str
    agent_id: str
    amount: int
    currency: str
    timestamp: str
    signature: str
    verification_url: str

@dataclass
class SpendingLimits:
    daily_limit: int
    monthly_limit: int
    daily_spent: int
    monthly_spent: int
    daily_remaining: int
    monthly_remaining: int

# AP2 / x402 models
@dataclass
class IntentMandate:
    id: str
    status: str
    policy: Dict[str, Any]
    subject: Dict[str, Any]
    hash: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


@dataclass
class CartMandate:
    id: str
    status: str
    cart: Dict[str, Any]
    links: Dict[str, Any]
    hash: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


@dataclass
class AP2PaymentResult:
    status: str
    rail: str
    processor: str
    processor_ref: str
    receipt: Dict[str, Any]
    onchain_txid: Optional[str] = None


@dataclass
class PaymentMethodPayload:
    rail: str
    provider: Optional[str] = None
    payment_reference: Optional[str] = None
    wallet_address: Optional[str] = None
    extra: Optional[Dict[str, Any]] = None

    def to_dict(self) -> Dict[str, Any]:
        payload: Dict[str, Any] = {"rail": self.rail}
        if self.provider:
            payload["provider"] = self.provider
        if self.payment_reference:
            payload["payment_reference"] = self.payment_reference
        if self.wallet_address:
            payload["wallet_address"] = self.wallet_address
        if self.extra:
            payload["extra"] = self.extra
        return payload


def build_card_payment_method(
    *,
    provider: str = "stripe",
    payment_reference: Optional[str] = None,
    extra: Optional[Dict[str, Any]] = None,
) -> PaymentMethodPayload:
    """Helper for AP2 card payments (Stripe or Braintree)."""

    return PaymentMethodPayload(
        rail="card",
        provider=provider,
        payment_reference=payment_reference,
        extra=extra,
    )


def build_braintree_payment_method(
    *,
    customer_id: Optional[str] = None,
    merchant_account_id: Optional[str] = None,
    supplier_domain: Optional[str] = None,
    descriptor: Optional[Dict[str, Any]] = None,
) -> PaymentMethodPayload:
    """Helper for AP2 Braintree payments using stored customer IDs."""

    extra: Dict[str, Any] = {}
    if customer_id:
        extra["customer_id"] = customer_id
    if merchant_account_id:
        extra["merchant_account_id"] = merchant_account_id
    if supplier_domain:
        extra["supplier_domain"] = supplier_domain
    if descriptor:
        extra.update({
            "descriptor_name": descriptor.get("name"),
            "descriptor_phone": descriptor.get("phone"),
        })

    return PaymentMethodPayload(
        rail="braintree",
        provider="braintree",
        extra=extra or None,
    )


def build_stablecoin_payment_method(
    *,
    payer_private_key: str,
    destination_wallet: Optional[str] = None,
    network: str = "base-sepolia",
    asset: Optional[str] = None,
    max_timeout_seconds: Optional[int] = None,
    source_wallet_address: Optional[str] = None,
    additional_extra: Optional[Dict[str, Any]] = None,
) -> PaymentMethodPayload:
    """Helper for AP2 stablecoin payments via Coinbase x402."""

    extra: Dict[str, Any] = {
        "payer_private_key": payer_private_key,
        "network": network,
    }
    if asset:
        extra["asset"] = asset
    if max_timeout_seconds is not None:
        extra["max_timeout_seconds"] = max_timeout_seconds
    if source_wallet_address:
        extra["source_wallet_address"] = source_wallet_address
    if additional_extra:
        extra.update(additional_extra)

    return PaymentMethodPayload(
        rail="stablecoin",
        wallet_address=destination_wallet,
        extra=extra,
    )

# A2A Protocol Models
@dataclass
class A2APaymentRequest:
    """Agent-to-Agent payment request following the A2A protocol"""
    supplier: str  # Domain like "acme-corp.com"
    amount: int  # Amount in cents
    description: str
    currency: str = "usd"
    txn_id: Optional[str] = None  # Client-generated transaction ID
    msg: str = "PayRequest"
    version: str = "1.0"

@dataclass 
class A2APaymentResponse:
    """Agent-to-Agent payment response"""
    txn_id: str
    status: str  # "processing" | "supplier_onboarding" | "paid" | "failed"
    msg: str = "PayResponse"
    provisional_key: Optional[str] = None
    next_action_url: Optional[str] = None
    error: Optional[str] = None

@dataclass
class A2AStatusQuery:
    """Query the status of an A2A transaction"""
    txn_id: str
    msg: str = "StatusQuery"

@dataclass
class A2AStatusResponse:
    """Response to A2A status query"""
    txn_id: str
    status: str
    events: list
    msg: str = "StatusResponse"

class AgentPaymentsSDK:
    def __init__(self, api_url: str, agent_id: str, api_key: str):
        self.api_url = api_url.rstrip('/')
        self.agent_id = agent_id
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        })

    def _make_request(self, method: str, endpoint: str, **kwargs) -> Dict[str, Any]:
        """Make HTTP request to the API"""
        url = f"{self.api_url}{endpoint}"
        response = self.session.request(method, url, **kwargs)
        
        if not response.ok:
            raise Exception(f"API request failed: {response.status_code} - {response.text}")
        
        return response.json()

    def create_payment(self, request: PaymentRequest) -> PaymentResponse:
        """Create a payment for an agent"""
        data = {
            "agent_id": request.agent_id,
            "amount": request.amount,
            "currency": request.currency,
            "description": request.description,
            "payment_method": request.payment_method
        }
        
        # Add recipient information
        if request.recipient_account_id:
            data["recipient_account_id"] = request.recipient_account_id
        elif request.recipient_business_name:
            data["recipient_business_name"] = request.recipient_business_name
        elif request.recipient_email:
            data["recipient_email"] = request.recipient_email
        
        result = self._make_request("POST", "/mcp/payments", json=data)
        
        return PaymentResponse(
            payment_intent_id=result["payment_intent"]["id"] if "payment_intent" in result else result["payment"]["id"],
            client_secret=result["payment_intent"]["client_secret"] if "payment_intent" in result else "",
            status=result["payment_intent"]["status"] if "payment_intent" in result else result["payment"]["state"],
            receipt=result["receipt"],
            payment_method=result.get("payment_method", "stripe")
        )


    def search_recipients(self, query: str, payment_method: str = "all") -> RecipientSearchResult:
        """Search for recipients across all payment methods"""
        params = {"query": query, "payment_method": payment_method}
        result = self._make_request("POST", "/mcp/search-recipients", params=params)
        
        return RecipientSearchResult(
            query=result["query"],
            results=result["results"],
            total_found=result["total_found"]
        )

    def check_balance(self) -> SpendingLimits:
        """Check spending limits and current balance"""
        result = self._make_request("GET", f"/mcp/balance/{self.agent_id}")
        
        return SpendingLimits(
            daily_limit=result["daily_limit"],
            monthly_limit=result["monthly_limit"],
            daily_spent=result["daily_spent"],
            monthly_spent=result["monthly_spent"],
            daily_remaining=result["daily_remaining"],
            monthly_remaining=result["monthly_remaining"]
        )

    def verify_receipt(self, receipt_id: str) -> Dict[str, Any]:
        """Verify a payment receipt"""
        return self._make_request("GET", f"/receipts/verify/{receipt_id}")

    def create_a2a_payment(self, recipient_id: str, amount: int, 
                          currency: str = "usd", memo: Optional[str] = None) -> Dict[str, Any]:
        """Create a legacy agent-to-agent payment (deprecated - use pay_supplier instead)"""
        data = {
            "agent_id": self.agent_id,
            "recipient_id": recipient_id,
            "amount": amount,
            "currency": currency,
            "memo": memo
        }
        
        return self._make_request("POST", "/a2a/payment", json=data)
    
    def pay_supplier(self, supplier: str, amount: int, description: str, 
                    agent_owner_email: str, agent_id: str,
                    currency: str = "usd", txn_id: Optional[str] = None,
                    agent_description: Optional[str] = None,
                    company_name: Optional[str] = None) -> A2APaymentResponse:
        """
        Pay a supplier using the A2A protocol
        
        Args:
            supplier: Domain name of the supplier (e.g., "acme-corp.com")
            amount: Amount in cents
            description: Description of the payment
            agent_owner_email: REQUIRED - Email of agent owner (from SSO)
            agent_id: REQUIRED - Agent identifier (unique per owner)
            currency: Currency code (default: "usd")
            txn_id: Optional client-generated transaction ID
            agent_description: Optional agent description
            company_name: Optional company name
            
        Returns:
            A2APaymentResponse with transaction details
        """
        if txn_id is None:
            txn_id = f"agt_txn_{uuid.uuid4().hex[:12]}"
            
        data = {
            "msg": "PayRequest",
            "version": "1.0",
            "txn_id": txn_id,
            "supplier": supplier,
            "amount": amount,
            "currency": currency,
            "description": description,
            "api_key": self.api_key,
            "agent_owner_email": agent_owner_email,
            "agent_id": agent_id
        }
        
        # Add optional fields if provided
        if agent_description:
            data["agent_description"] = agent_description
        if company_name:
            data["company_name"] = company_name
        
        result = self._make_request("POST", "/a2a/pay", json=data)
        
        return A2APaymentResponse(
            txn_id=result["txn_id"],
            status=result["status"],
            msg=result.get("msg", "PayResponse"),
            provisional_key=result.get("provisional_key"),
            next_action_url=result.get("next_action_url"),
            error=result.get("error")
        )
    
    def check_a2a_status(self, txn_id: str) -> A2AStatusResponse:
        """
        Check the status of an A2A payment transaction
        
        Args:
            txn_id: Transaction ID to check
            
        Returns:
            A2AStatusResponse with current status and events
        """
        data = {
            "msg": "StatusQuery",
            "txn_id": txn_id
        }
        
        result = self._make_request("POST", "/a2a/status", json=data)
        
        return A2AStatusResponse(
            txn_id=result["txn_id"],
            status=result["status"],
            events=result.get("events", []),
            msg=result.get("msg", "StatusResponse")
        ) 

    def create_ap2_intent_mandate(
        self,
        *,
        policy: Dict[str, Any],
        agent_id: Optional[str] = None,
        constraints: Optional[Dict[str, Any]] = None,
        expires_at: Optional[Union[str, datetime]] = None,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> IntentMandate:
        """Create an AP2 intent mandate binding a policy to an agent."""

        payload: Dict[str, Any] = {
            "agent_id": agent_id or self.agent_id,
            "policy": policy,
        }
        if constraints:
            payload["constraints"] = constraints
        if metadata:
            payload["metadata"] = metadata
        if expires_at:
            payload["expires_at"] = (
                expires_at.isoformat()
                if isinstance(expires_at, datetime)
                else expires_at
            )

        result = self._make_request("POST", "/ap2/mandates/intent", json=payload)
        mandate = result.get("intent_mandate", {})
        return IntentMandate(
            id=mandate.get("id"),
            status=mandate.get("status", "unknown"),
            policy=mandate.get("policy", {}),
            subject=mandate.get("subject", {}),
            hash=mandate.get("hash"),
            metadata=mandate.get("metadata"),
        )

    def create_ap2_cart_mandate(
        self,
        *,
        intent_mandate_id: str,
        cart: Dict[str, Any],
        metadata: Optional[Dict[str, Any]] = None,
    ) -> CartMandate:
        """Create an AP2 cart mandate that links to an intent."""

        payload: Dict[str, Any] = {
            "intent_mandate_id": intent_mandate_id,
            "cart": cart,
        }
        if metadata:
            payload["metadata"] = metadata

        result = self._make_request("POST", "/ap2/mandates/cart", json=payload)
        cart_mandate = result.get("cart_mandate", {})
        return CartMandate(
            id=cart_mandate.get("id"),
            status=cart_mandate.get("status", "unknown"),
            cart=cart_mandate.get("cart", {}),
            links=cart_mandate.get("links", {}),
            hash=cart_mandate.get("hash"),
            metadata=cart_mandate.get("metadata"),
        )

    def ap2_pay(
        self,
        *,
        intent_mandate_id: str,
        cart_mandate_id: str,
        payment_method: Union[PaymentMethodPayload, Dict[str, Any]],
    ) -> AP2PaymentResult:
        """Execute an AP2 payment for the given mandates."""

        if isinstance(payment_method, PaymentMethodPayload):
            method_payload = payment_method.to_dict()
        else:
            method_payload = payment_method

        result = self._make_request(
            "POST",
            "/ap2/pay",
            json={
                "intent_mandate_id": intent_mandate_id,
                "cart_mandate_id": cart_mandate_id,
                "payment_method": method_payload,
            },
        )

        return AP2PaymentResult(
            status=result.get("status", "processing"),
            rail=result.get("rail", method_payload.get("rail", "unknown")),
            processor=result.get("processor", "unknown"),
            processor_ref=result.get("processor_ref"),
            receipt=result.get("receipt", {}),
            onchain_txid=result.get("onchain_txid"),
        )
