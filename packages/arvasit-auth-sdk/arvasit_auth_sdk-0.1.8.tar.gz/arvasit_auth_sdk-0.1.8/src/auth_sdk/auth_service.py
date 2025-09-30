import hashlib
import hmac
from datetime import datetime
from typing import Optional, Dict, Any, List

import requests
from pydantic import BaseModel

from .auth_types import (
    AuthServiceConfig,
    AuthHeaders,
    SignupRequest,
    SignupResponse,
    LoginRequest,
    LoginResponse,
    OtpLoginRequest,
    RecoveryCodeLoginRequest,
    TwoFALoginRequest,
    CheckCredentialRequest,
    CheckCredentialResponse,
    SuggestUsernameRequest,
    CheckUserNameRequest,
    CredentialForForgotPasswordRequest,
    EnterCredentialForForgotPasswordResponse,
    ForgotPasswordSendOTPRequest,
    VerifyForgotPasswordOTPRequest,
    ValidateForgetPasswordTokenRequest,
    VerifyTokenSetupPasswordRequest,
    UpdatePasswordRequest,
    GenerateRecoveryCodesRequest,
    RefreshAccessTokenRequest,
    RefreshTokenResponse,
    GenerateQRCodeAndSecretFor2FARequest,
    GenerateQrCodeAndSecretFor2FAResponse,
    VerifyQRCodeAndSecretFor2FARequest,
    ListOfSecretKeysRequest,
    ListOfSecretKeysResponse,
    ListOfRecoveryCodeRequest,
    ListOfRecoveryCodeResponse,
    RemoveTwoFADeviceRequest,
    DisableTwoFARequest,
    LogoutRequest,
    LoginActivityCountsRequest,
    LoginActivityCountResponse,
    LoginActivityDetailsRequest,
    LoginActivityDetailsResponse,
    MagicLinkResponse,
    VerifyMagicLinkRequest,
)


class AuthService:
    def __init__(self, config: AuthServiceConfig):
        self.config = config
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Content-Type": "application/json",
                "X-Public-Key": config.public_key,
                "X-Secret-Key": config.secret_key,
            }
        )
        self.base_url = config.url

    def _get_auth_headers(self, access_token: Optional[str] = None) -> Dict[str, str]:
        timestamp = str(int(datetime.now().timestamp() * 1000))
        signature_data = f"{self.config.public_key}{timestamp}"
        signature = hmac.new(
            self.config.secret_key.encode(), signature_data.encode(), hashlib.sha256
        ).hexdigest()

        headers = {
            "public-key": self.config.public_key,
            "timestamp": timestamp,
            "signature": signature,
        }

        if access_token:
            headers["Authorization"] = f"Bearer {access_token}"

        return headers

    def _handle_error(self, error: Exception) -> Exception:
        if isinstance(error, requests.exceptions.RequestException):
            message = (
                error.response.json().get("message", str(error))
                if error.response
                else str(error)
            )
            return Exception(f"Auth Service Error: {message}")
        return error

    def signup(self, params: SignupRequest) -> SignupResponse:
        """Signup a new user."""
        path = "/auth/signup"
        headers = self._get_auth_headers()

        try:
            response = self.session.post(
                f"{self.base_url}{path}", json=params.model_dump(), headers=headers
            )
            response.raise_for_status()
            return SignupResponse(**response.json())
        except Exception as e:
            raise self._handle_error(e)

    def suggest_username(self, first_name: str, last_name: str) -> List[str]:
        """Suggest available usernames based on first and last name."""
        path = "/user/usernames"
        headers = self._get_auth_headers()

        try:
            response = self.session.get(
                f"{self.base_url}{path}",
                params={"firstName": first_name, "lastName": last_name},
                headers=headers,
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            raise self._handle_error(e)

    def check_available_username(self, username: str) -> bool:
        """Check if a username is available."""
        path = "/user/checkUsername"
        headers = self._get_auth_headers()

        try:
            response = self.session.get(
                f"{self.base_url}{path}",
                params={"username": username},
                headers=headers,
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            raise self._handle_error(e)

    def check_credential(self, credential: str) -> CheckCredentialResponse:
        """Check the type of credential (email or phone)."""
        path = "/auth/checkCredential"
        headers = self._get_auth_headers()

        try:
            response = self.session.get(
                f"{self.base_url}{path}",
                params={"credential": credential},
                headers=headers,
            )
            response.raise_for_status()
            return CheckCredentialResponse(**response.json())
        except Exception as e:
            raise self._handle_error(e)

    def login_with_password(self, params: LoginRequest) -> LoginResponse:
        """Login using password."""
        path = "/auth/loginWithPassword"
        headers = self._get_auth_headers()

        try:
            response = self.session.post(
                f"{self.base_url}{path}", json=params.model_dump(), headers=headers
            )
            response.raise_for_status()
            return LoginResponse(**response.json())
        except Exception as e:
            raise self._handle_error(e)

    def login_with_otp(self, params: OtpLoginRequest) -> LoginResponse:
        """Login using OTP."""
        path = "/auth/loginWithOtp"
        headers = self._get_auth_headers()

        try:
            response = self.session.post(
                f"{self.base_url}{path}", json=params.model_dump(), headers=headers
            )
            response.raise_for_status()
            return LoginResponse(**response.json())
        except Exception as e:
            raise self._handle_error(e)

    def login_with_recovery_code(
        self, params: RecoveryCodeLoginRequest
    ) -> LoginResponse:
        """Login using recovery code."""
        path = "/auth/recoveryCodeToLogin"
        headers = self._get_auth_headers()

        try:
            response = self.session.post(
                f"{self.base_url}{path}", json=params.model_dump(), headers=headers
            )
            response.raise_for_status()
            return LoginResponse(**response.json())
        except Exception as e:
            raise self._handle_error(e)

    def verify_magic_link(self, params: VerifyMagicLinkRequest) -> MagicLinkResponse:
        """Verify magic link for authentication."""
        path = "/auth/verify-magic-link"
        headers = self._get_auth_headers()

        try:
            response = self.session.get(
                f"{self.base_url}{path}",
                params=params.model_dump(),
                headers=headers,
            )
            response.raise_for_status()
            return MagicLinkResponse(**response.json())
        except Exception as e:
            raise self._handle_error(e)

    def send_otp_for_login(self, credential: str) -> CheckCredentialResponse:
        """Send OTP for login."""
        path = "/auth/sendOtpForLogin"
        headers = self._get_auth_headers()

        try:
            response = self.session.get(
                f"{self.base_url}{path}",
                params={"credential": credential},
                headers=headers,
            )
            response.raise_for_status()
            return CheckCredentialResponse(**response.json())
        except Exception as e:
            raise self._handle_error(e)

    def verify_two_factor_authentication(
        self, params: TwoFALoginRequest
    ) -> LoginResponse:
        """Verify two factor authentication."""
        path = "/auth/verifyTwoFactorAuthToken"
        headers = self._get_auth_headers()

        try:
            response = self.session.post(
                f"{self.base_url}{path}", json=params.model_dump(), headers=headers
            )
            response.raise_for_status()
            return LoginResponse(**response.json())
        except Exception as e:
            raise self._handle_error(e)

    def logout(self, params: LogoutRequest) -> str:
        """Logout user."""
        path = "/auth/userLogout"
        headers = self._get_auth_headers()

        try:
            response = self.session.post(
                f"{self.base_url}{path}", json=params.model_dump(), headers=headers
            )
            response.raise_for_status()
            return response.text
        except Exception as e:
            raise self._handle_error(e)

    def enter_credential_for_forgot_password(
        self, credential: str
    ) -> EnterCredentialForForgotPasswordResponse:
        """Enter credential for forgot password to get type email or phone."""
        path = "/auth/enterCredentialForForgotPassword"
        headers = self._get_auth_headers()

        try:
            response = self.session.get(
                f"{self.base_url}{path}",
                params={"credential": credential},
                headers=headers,
            )
            response.raise_for_status()
            return EnterCredentialForForgotPasswordResponse(**response.json())
        except Exception as e:
            raise self._handle_error(e)

    def forgot_password_send_otp(self, credential: str, otp_type: str) -> str:
        """Send OTP for forgot password authorization."""
        path = "/auth/forgotPasswordSendOTP"
        headers = self._get_auth_headers()

        try:
            response = self.session.post(
                f"{self.base_url}{path}",
                json={"credential": credential, "type": otp_type},
                headers=headers,
            )
            response.raise_for_status()
            return response.text
        except Exception as e:
            raise self._handle_error(e)

    def verify_forgot_password_otp(self, credential: str, otp: str) -> str:
        """Verify OTP for forgot password reset."""
        path = "/auth/verifyForgotPasswordOtp"
        headers = self._get_auth_headers()

        try:
            response = self.session.post(
                f"{self.base_url}{path}",
                json={"credential": credential, "otp": otp},
                headers=headers,
            )
            response.raise_for_status()
            return response.text
        except Exception as e:
            raise self._handle_error(e)

    def validate_forget_password_token(self, token: str) -> bool:
        """Check if forgot password generated token is valid."""
        path = "/auth/validateForgetPasswordToken"
        headers = self._get_auth_headers()

        try:
            response = self.session.get(
                f"{self.base_url}{path}",
                params={"token": token},
                headers=headers,
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            raise self._handle_error(e)

    def verify_token_setup_password(self, token: str, password: str) -> bool:
        """Verify token and set new password."""
        path = "/auth/verifyTokenSetupPassword"
        headers = self._get_auth_headers()

        try:
            response = self.session.post(
                f"{self.base_url}{path}",
                json={"token": token, "password": password},
                headers=headers,
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            raise self._handle_error(e)

    def update_password(
        self, credential: str, old_password: str, new_password: str
    ) -> bool:
        """Update password with old password verification."""
        path = "/auth/updatePassword"
        headers = self._get_auth_headers()

        try:
            response = self.session.put(
                f"{self.base_url}{path}",
                json={
                    "credential": credential,
                    "oldPassword": old_password,
                    "newPassword": new_password,
                },
                headers=headers,
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            raise self._handle_error(e)

    def refresh_access_token(
        self, params: RefreshAccessTokenRequest
    ) -> RefreshTokenResponse:
        """Refresh access token."""
        path = "/auth/refreshAccessToken"
        headers = self._get_auth_headers()

        try:
            response = self.session.get(
                f"{self.base_url}{path}", params=params.model_dump(), headers=headers
            )
            response.raise_for_status()
            return RefreshTokenResponse(**response.json())
        except Exception as e:
            raise self._handle_error(e)

    def generate_recovery_codes(self, access_token: str) -> LoginResponse:
        """Generate recovery codes."""
        path = "/secret-keys/generateRecoveryCodes"
        headers = self._get_auth_headers(access_token)

        try:
            response = self.session.post(f"{self.base_url}{path}", headers=headers)
            response.raise_for_status()
            return LoginResponse(**response.json())
        except Exception as e:
            raise self._handle_error(e)

    def generate_qr_code_and_secret_for_2fa(
        self, access_token: str
    ) -> GenerateQrCodeAndSecretFor2FAResponse:
        """Generate QR code and secret for 2FA."""
        path = "/secret-keys/generateQRCodeAndSecretFor2FA"
        headers = self._get_auth_headers(access_token)

        try:
            response = self.session.post(f"{self.base_url}{path}", headers=headers)
            response.raise_for_status()
            return GenerateQrCodeAndSecretFor2FAResponse(**response.json())
        except Exception as e:
            raise self._handle_error(e)

    def verify_qr_code_and_secret_for_2fa(
        self, params: VerifyQRCodeAndSecretFor2FARequest
    ) -> GenerateQrCodeAndSecretFor2FAResponse:
        """Verify QR code and secret for 2FA."""
        path = "/secret-keys/verifyQrCodeAndSecretFor2FA"
        access_token = params.accessToken
        request_data = {"totp": params.totp, "secretKey": params.secretKey}
        headers = self._get_auth_headers(access_token)

        try:
            response = self.session.post(
                f"{self.base_url}{path}", json=request_data, headers=headers
            )
            response.raise_for_status()
            return GenerateQrCodeAndSecretFor2FAResponse(**response.json())
        except Exception as e:
            raise self._handle_error(e)

    def list_of_two_fa_secrets(self, access_token: str) -> ListOfSecretKeysResponse:
        """List of 2FA secrets."""
        path = "/secret-keys/listOfTwoFASecrets"
        headers = self._get_auth_headers(access_token)

        try:
            response = self.session.get(f"{self.base_url}{path}", headers=headers)
            response.raise_for_status()
            return ListOfSecretKeysResponse(**response.json())
        except Exception as e:
            raise self._handle_error(e)

    def remove_two_fa_device(self, access_token: str, key: str) -> List[str]:
        """Remove 2FA device."""
        path = "/secret-keys/removeTwoFADevice"
        headers = self._get_auth_headers(access_token)

        try:
            response = self.session.delete(
                f"{self.base_url}{path}", params={"key": key}, headers=headers
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            raise self._handle_error(e)

    def disable_two_fa(self, access_token: str) -> bool:
        """Disable 2FA."""
        path = "/auth/disableTwoFA"
        headers = self._get_auth_headers(access_token)

        try:
            response = self.session.post(f"{self.base_url}{path}", headers=headers)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            raise self._handle_error(e)

    def list_of_recovery_code(self, access_token: str) -> ListOfRecoveryCodeResponse:
        """List of recovery codes."""
        path = "/secret-keys/listOfRecoveryCode"
        headers = self._get_auth_headers(access_token)

        try:
            response = self.session.get(f"{self.base_url}{path}", headers=headers)
            response.raise_for_status()
            return ListOfRecoveryCodeResponse(**response.json())
        except Exception as e:
            raise self._handle_error(e)

    def login_activity_counts(
        self, access_token: str, start_date: str, end_date: str, **kwargs
    ) -> LoginActivityCountResponse:
        """Get login activity counts."""
        path = "/logging-events/loginActivityCount"
        headers = self._get_auth_headers(access_token)

        params = {"startDate": start_date, "endDate": end_date}
        params.update(kwargs)

        try:
            response = self.session.get(
                f"{self.base_url}{path}", params=params, headers=headers
            )
            response.raise_for_status()
            return LoginActivityCountResponse(**response.json())
        except Exception as e:
            raise self._handle_error(e)

    def login_activity_details(
        self, access_token: str, start_date: str, end_date: str, **kwargs
    ) -> LoginActivityDetailsResponse:
        """Get login activity details."""
        path = "/logging-events/loginActivityDetails"
        headers = self._get_auth_headers(access_token)

        params = {"startDate": start_date, "endDate": end_date}
        params.update(kwargs)

        try:
            response = self.session.get(
                f"{self.base_url}{path}", params=params, headers=headers
            )
            response.raise_for_status()
            return LoginActivityDetailsResponse(**response.json())
        except Exception as e:
            raise self._handle_error(e)
