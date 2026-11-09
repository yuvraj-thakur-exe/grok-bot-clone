# GROKBOT-RE: Authentication Architecture

- **Client Authentication**: Hardware passkey / WebAuthn signature proxy via `sand-webauthn-signer.exe`.
- **API Token Security**: Provider keys stored encrypted in local SQLite database or operating system credential vault.
- **Session Tokens**: Redacted and isolated from diagnostic traces.
