# Paegents Python SDK

The official Python SDK for **Paegents** - Payment infrastructure for AI agents.

## Installation

```bash
pip install paegents
```

## Quick Start

```python
from paegents import PaegentsSDK

# Initialize the SDK
sdk = PaegentsSDK(
    api_url="https://api.paegents.com",
    agent_id="my_ai_agent",
    api_key="ak_live_your_api_key_here"
)

# Make an A2A payment to a supplier
response = sdk.pay_supplier(
    supplier="acme-corp.com",
    amount=2500,  # $25.00 in cents
    description="GPU compute credits"
)

print(f"Payment {response.status}: {response.txn_id}")

# Check payment status
status = sdk.check_a2a_status(response.txn_id)
print(f"Current status: {status.status}")
```

## AP2 Mandates & Stablecoin (x402)

Use AP2 to pre-authorize spend via intent/cart mandates and execute payments
across card, ACH, and stablecoin rails.

```python
import os
from paegents import (
    build_card_payment_method,
    build_stablecoin_payment_method,
)

# 1) Create an intent mandate for your agent
intent = sdk.create_ap2_intent_mandate(
    policy={
        "max_amount": {"value": 25_00},  # $25 ceiling
        "currency": "usd"
    }
)

# 2) Attach a cart mandate (invoice/basket)
cart = sdk.create_ap2_cart_mandate(
    intent_mandate_id=intent.id,
    cart={
        "total": 12_50,
        "currency": "usd",
        "description": "Monthly agent hosting"
    }
)

# 3a) Execute a card payment (Stripe/Braintree)
card_payment = sdk.ap2_pay(
    intent_mandate_id=intent.id,
    cart_mandate_id=cart.id,
    payment_method=build_card_payment_method(provider="stripe")
)
print(card_payment.status)

# 3b) Execute a stablecoin payment on Coinbase x402
stablecoin_payment = sdk.ap2_pay(
    intent_mandate_id=intent.id,
    cart_mandate_id=cart.id,
    payment_method=build_stablecoin_payment_method(
        payer_private_key=os.environ["STABLE_COIN_PRIVATE_KEY"],
        destination_wallet=os.environ.get("STABLE_COIN_DESTINATION"),
    )
)
print(stablecoin_payment.onchain_txid)
```

The stablecoin helper accepts optional parameters (`network`, `asset`,
`max_timeout_seconds`, etc.) so you can tune facilitator requests without
hand-crafting JSON payloads.

## A2A (Agent-to-Agent) Payments

The core feature of Paegents is seamless agent-to-agent payments using domain-based supplier resolution.

### Making a Payment

```python
# Pay a supplier by domain
response = sdk.pay_supplier(
    supplier="software-company.io",
    amount=5000,  # $50.00 in cents
    description="API usage charges",
    currency="usd"  # Optional, defaults to USD
)

# Handle different response statuses
if response.status == "paid":
    print(f"Payment successful! Transaction: {response.txn_id}")
elif response.status == "processing":
    print(f"Payment processing... Transaction: {response.txn_id}")
elif response.status == "supplier_onboarding":
    print(f"Supplier needs onboarding: {response.next_action_url}")
elif response.status == "failed":
    print(f"Payment failed: {response.error}")
```

### Checking Payment Status

```python
# Poll for status updates
status = sdk.check_a2a_status("agt_txn_123abc456def")

print(f"Status: {status.status}")
print(f"Events: {status.events}")
```

## Traditional MCP Payments

For payments to specific accounts (legacy method):

### Stripe Payments

```python
from paegents import PaymentRequest

# Pay a Stripe account
payment = PaymentRequest(
    agent_id="my_agent",
    amount=1000,  # $10.00
    currency="usd",
    description="Service payment",
    payment_method="stripe",
    recipient_account_id="acct_stripe_account_id"
)

response = sdk.create_payment(payment)
print(f"Payment intent: {response.payment_intent_id}")
```

### PayPal Payments

```python
from paegents import PayPalPaymentRequest

# Pay via PayPal email
paypal_payment = PayPalPaymentRequest(
    agent_id="my_agent",
    recipient_email="vendor@company.com",
    amount=25.00,  # PayPal uses dollars
    description="Consulting services"
)

response = sdk.create_paypal_payment(paypal_payment)
print(f"PayPal payment: {response.payment_intent_id}")
```

## Account Management

### Check Spending Limits

```python
limits = sdk.check_balance()
print(f"Daily remaining: ${limits.daily_remaining / 100:.2f}")
print(f"Monthly remaining: ${limits.monthly_remaining / 100:.2f}")
```

### Discover Recipients

```python
# Search for payment recipients
results = sdk.search_recipients("acme", payment_method="all")
for result in results.results:
    print(f"Found: {result['business_name']} ({result['payment_method']})")

# Check if email can receive PayPal
discovery = sdk.discover_paypal_email("payments@company.com")
if discovery.can_receive_paypal:
    print(f"✅ {discovery.email} can receive PayPal payments")
```

### Verify Receipts

```python
# Verify payment receipt authenticity
verification = sdk.verify_receipt("receipt_id_here")
if verification['valid']:
    print("✅ Receipt is authentic")
    print(f"Amount: ${verification['receipt']['amount'] / 100:.2f}")
else:
    print("❌ Receipt verification failed")
```

## Error Handling

```python
try:
    response = sdk.pay_supplier("unknown-company.com", 1000, "Test payment")
except Exception as e:
    print(f"Payment failed: {e}")
```

## Configuration

### Environment Variables

You can set default configuration via environment variables:

```bash
export PAEGENTS_API_URL="https://api.paegents.com"
export PAEGENTS_API_KEY="ak_live_your_key_here" 
export PAEGENTS_AGENT_ID="my_agent_id"
```

```python
import os
from paegents import PaegentsSDK

# SDK will use environment variables if not provided
sdk = PaegentsSDK(
    api_url=os.getenv("PAEGENTS_API_URL"),
    agent_id=os.getenv("PAEGENTS_AGENT_ID"),
    api_key=os.getenv("PAEGENTS_API_KEY")
)
```

## API Reference

### AgentPaymentsSDK

The main SDK class for interacting with Paegents.

#### Constructor

```python
sdk = PaegentsSDK(api_url, agent_id, api_key)
```

#### A2A Methods

- `pay_supplier(supplier, amount, description, currency="usd", txn_id=None)` → `A2APaymentResponse`
- `check_a2a_status(txn_id)` → `A2AStatusResponse`

#### Legacy MCP Methods

- `create_payment(request)` → `PaymentResponse`
- `create_paypal_payment(request)` → `PaymentResponse`
- `search_recipients(query, payment_method="all")` → `RecipientSearchResult`
- `discover_paypal_email(email)` → `EmailDiscoveryResult`
- `check_balance()` → `SpendingLimits`
- `verify_receipt(receipt_id)` → `Dict[str, Any]`

## Support

- **Documentation**: [docs.paegents.com](https://docs.paegents.com)
- **API Reference**: [docs.paegents.com/api](https://docs.paegents.com/api)  
- **Support**: [support@paegents.com](mailto:support@paegents.com)
- **Issues**: [github.com/paegents/python-sdk/issues](https://github.com/paegents/python-sdk/issues)

## License

MIT License - see [LICENSE](LICENSE) file for details.
