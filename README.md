# braintree-tutorial
Playing around with Braintree. When making a payment, you can use card numbers found here: https://developers.braintreepayments.com/reference/general/testing/python

**Important**: This was only used in development mode.

## Setup the server
1. Setup environment variables. You can find these on the BrainTree dashboard after logging in.
```bash
BRAINTREE_MERCHANT_ID="..."
BRAINTREE_PUBLIC_KEY="..."
BRAINTREE_PRIVATE_KEY="..."
```

1. Start the server.
```bash
cd myapp
python manage.py runserver 0.0.0.0:8000
```

## Serve the client files

```bash
cd client
python -m http.server 8001
```

You can now access the files on http://localhost:8001/.
