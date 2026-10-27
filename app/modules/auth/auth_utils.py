from app.core.security import hash_password

# Verified against when the email is unknown, so a miss costs the same as a wrong password
# and response timing doesn't reveal which emails are registered.
DUMMY_PASSWORD_HASH = hash_password("dummy-password-for-timing-parity")
