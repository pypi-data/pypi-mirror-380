# Auto-generated Python Pydantic models from JSON schema
# Do not edit manually - regenerate from schemas/auth-types.json

from typing import Optional, List, Dict, Any
from pydantic import BaseModel

class AuthServiceConfig(BaseModel):
    url: str
    public_key: str
    secret_key: str

class AuthHeaders(BaseModel):
    public_key: str
    timestamp: str
    signature: str
    Authorization: Optional[str] = None

class CheckCredentialResponse(BaseModel):
    isValid: bool
    type: str

class SignupResponse(BaseModel):
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    email: Optional[str] = None
    username: Optional[str] = None
    isTwoFactorAuthenticationEnabled: Optional[bool] = None
    avatarUrl: Optional[str] = None
    authId: str
    role: Optional[str] = None
    defaultClient: Optional[bool] = None
    recoveryEmail: Optional[str] = None
    clientId: Optional[str] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None
    phoneNumber: Optional[str] = None
    alternatePhoneNumber: Optional[List[str]] = []
    alternateEmail: Optional[List[str]] = []

class LoginResponse(BaseModel):
    type: str
    message: str
    accessToken: str
    refreshToken: str
    deviceId: str
    userResponse: Dict[str, Any]

class DeviceRegistry(BaseModel):
    deviceId: Optional[str] = None
    deviceName: Optional[str] = None
    os: Optional[str] = None
    browserName: Optional[str] = None
    deviceType: Optional[str] = None
    deviceIp: Optional[str] = None
    rememberThisDevice: Optional[bool] = None

class LoginRequest(BaseModel):
    credential: str
    password: str
    expireSessionAt: Optional[str] = None
    tokenMetadata: Optional[Dict[str, Any]] = None
    deviceRegistry: Optional[Any] = None

class OtpLoginRequest(BaseModel):
    credential: str
    otp: str
    deviceRegistry: Optional[Any] = None

class TwoFALoginRequest(BaseModel):
    credential: str
    totp: str
    deviceRegistry: Optional[Any] = None

class RecoveryCodeLoginRequest(BaseModel):
    credential: str
    recoveryCode: str
    deviceRegistry: Optional[Any] = None

class SignupRequest(BaseModel):
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    username: Optional[str] = None
    phoneNumber: Optional[str] = None
    email: Optional[str] = None
    avatarUrl: Optional[str] = None
    password: str
    alternatePhoneNumber: Optional[List[str]] = []
    alternateEmail: Optional[List[str]] = []
    role: Optional[str] = None
    recoveryEmail: Optional[str] = None

class SuggestUsernameRequest(BaseModel):
    firstName: str
    lastName: str

class CheckUserNameRequest(BaseModel):
    username: str

class ForgotPasswordSendOTPRequest(BaseModel):
    credential: str
    type: str

class ValidateForgetPasswordTokenRequest(BaseModel):
    token: str

class VerifyTokenSetupPasswordRequest(BaseModel):
    token: str
    password: str

class VerifyForgotPasswordOTPRequest(BaseModel):
    credential: str
    otp: str

class UpdatePasswordRequest(BaseModel):
    credential: str
    oldPassword: str
    newPassword: str

class GenerateRecoveryCodesRequest(BaseModel):
    accessToken: str

class GenerateRecoveryCodeRequest(BaseModel):
    authId: str

class RefreshAccessTokenRequest(BaseModel):
    token: str

class RefreshTokenResponse(BaseModel):
    accessToken: str
    refreshToken: str

class GenerateQRCodeAndSecretFor2FARequest(BaseModel):
    accessToken: str

class GenerateQrCodeAndSecretFor2FAResponse(BaseModel):
    secret: str
    qrCode: str

class VerifyQRCodeAndSecretFor2FARequest(BaseModel):
    accessToken: str
    totp: str
    secretKey: str

class ListOfSecretKeysRequest(BaseModel):
    accessToken: str

class ListOfSecretKeysResponse(BaseModel):
    isTwoFactorEnabled: bool
    listOfSecret: List[Dict[str, Any]]

class ListOfRecoveryCodeRequest(BaseModel):
    accessToken: str

class ListOfRecoveryCodeResponse(BaseModel):
    createdOn: str
    listOfRecoveryCode: List[Dict[str, Any]]

class RemoveTwoFADeviceRequest(BaseModel):
    accessToken: str
    key: str

class DisableTwoFARequest(BaseModel):
    accessToken: str

class LogoutRequest(BaseModel):
    token: str

class EnterCredentialForForgotPasswordResponse(BaseModel):
    maskedEmail: Optional[str] = None
    maskedPhone: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None

class LoginActivityCountsRequest(BaseModel):
    accessToken: str
    startDate: str
    endDate: str
    page: Optional[int] = None
    limit: Optional[int] = None
    sortBy: Optional[str] = None
    sortOrder: Optional[str] = None
    searchField: Optional[str] = None
    searchValue: Optional[str] = None

class LoginActivityDetailsRequest(BaseModel):
    authId: Optional[str] = None
    accessToken: str
    startDate: str
    endDate: str
    page: Optional[int] = None
    limit: Optional[int] = None
    sortBy: Optional[str] = None
    sortOrder: Optional[str] = None
    searchField: Optional[str] = None
    searchValue: Optional[str] = None

class LoginActivityCountResponse(BaseModel):
    totalCount: int
    data: List[Dict[str, Any]]

class LoginActivityDetailsResponse(BaseModel):
    totalCount: int
    data: List[Dict[str, Any]]

class CheckCredentialRequest(BaseModel):
    credential: str

class CredentialForForgotPasswordRequest(BaseModel):
    credential: str

class VerifyMagicLinkRequest(BaseModel):
    token: str
    credential: str

class MagicLinkResponse(BaseModel):
    type: str
    message: str
    accessToken: str
    refreshToken: str
    deviceId: str
    userResponse: Dict[str, Any]
