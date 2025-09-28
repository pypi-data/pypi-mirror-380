# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_payment_cryptography_data import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class CurrentPinAttributes:
    boto3_raw_data: "type_defs.CurrentPinAttributesTypeDef" = dataclasses.field()

    CurrentPinPekIdentifier = field("CurrentPinPekIdentifier")
    CurrentEncryptedPinBlock = field("CurrentEncryptedPinBlock")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CurrentPinAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CurrentPinAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AmexCardSecurityCodeVersion1:
    boto3_raw_data: "type_defs.AmexCardSecurityCodeVersion1TypeDef" = (
        dataclasses.field()
    )

    CardExpiryDate = field("CardExpiryDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AmexCardSecurityCodeVersion1TypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AmexCardSecurityCodeVersion1TypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AmexCardSecurityCodeVersion2:
    boto3_raw_data: "type_defs.AmexCardSecurityCodeVersion2TypeDef" = (
        dataclasses.field()
    )

    CardExpiryDate = field("CardExpiryDate")
    ServiceCode = field("ServiceCode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AmexCardSecurityCodeVersion2TypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AmexCardSecurityCodeVersion2TypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AsymmetricEncryptionAttributes:
    boto3_raw_data: "type_defs.AsymmetricEncryptionAttributesTypeDef" = (
        dataclasses.field()
    )

    PaddingType = field("PaddingType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AsymmetricEncryptionAttributesTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AsymmetricEncryptionAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CardHolderVerificationValue:
    boto3_raw_data: "type_defs.CardHolderVerificationValueTypeDef" = dataclasses.field()

    UnpredictableNumber = field("UnpredictableNumber")
    PanSequenceNumber = field("PanSequenceNumber")
    ApplicationTransactionCounter = field("ApplicationTransactionCounter")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CardHolderVerificationValueTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CardHolderVerificationValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CardVerificationValue1:
    boto3_raw_data: "type_defs.CardVerificationValue1TypeDef" = dataclasses.field()

    CardExpiryDate = field("CardExpiryDate")
    ServiceCode = field("ServiceCode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CardVerificationValue1TypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CardVerificationValue1TypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CardVerificationValue2:
    boto3_raw_data: "type_defs.CardVerificationValue2TypeDef" = dataclasses.field()

    CardExpiryDate = field("CardExpiryDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CardVerificationValue2TypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CardVerificationValue2TypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DynamicCardVerificationCode:
    boto3_raw_data: "type_defs.DynamicCardVerificationCodeTypeDef" = dataclasses.field()

    UnpredictableNumber = field("UnpredictableNumber")
    PanSequenceNumber = field("PanSequenceNumber")
    ApplicationTransactionCounter = field("ApplicationTransactionCounter")
    TrackData = field("TrackData")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DynamicCardVerificationCodeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DynamicCardVerificationCodeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DynamicCardVerificationValue:
    boto3_raw_data: "type_defs.DynamicCardVerificationValueTypeDef" = (
        dataclasses.field()
    )

    PanSequenceNumber = field("PanSequenceNumber")
    CardExpiryDate = field("CardExpiryDate")
    ServiceCode = field("ServiceCode")
    ApplicationTransactionCounter = field("ApplicationTransactionCounter")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DynamicCardVerificationValueTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DynamicCardVerificationValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DiscoverDynamicCardVerificationCode:
    boto3_raw_data: "type_defs.DiscoverDynamicCardVerificationCodeTypeDef" = (
        dataclasses.field()
    )

    CardExpiryDate = field("CardExpiryDate")
    UnpredictableNumber = field("UnpredictableNumber")
    ApplicationTransactionCounter = field("ApplicationTransactionCounter")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DiscoverDynamicCardVerificationCodeTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DiscoverDynamicCardVerificationCodeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CryptogramVerificationArpcMethod1:
    boto3_raw_data: "type_defs.CryptogramVerificationArpcMethod1TypeDef" = (
        dataclasses.field()
    )

    AuthResponseCode = field("AuthResponseCode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CryptogramVerificationArpcMethod1TypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CryptogramVerificationArpcMethod1TypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CryptogramVerificationArpcMethod2:
    boto3_raw_data: "type_defs.CryptogramVerificationArpcMethod2TypeDef" = (
        dataclasses.field()
    )

    CardStatusUpdate = field("CardStatusUpdate")
    ProprietaryAuthenticationData = field("ProprietaryAuthenticationData")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CryptogramVerificationArpcMethod2TypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CryptogramVerificationArpcMethod2TypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseMetadata:
    boto3_raw_data: "type_defs.ResponseMetadataTypeDef" = dataclasses.field()

    RequestId = field("RequestId")
    HTTPStatusCode = field("HTTPStatusCode")
    HTTPHeaders = field("HTTPHeaders")
    RetryAttempts = field("RetryAttempts")
    HostId = field("HostId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResponseMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Emv2000Attributes:
    boto3_raw_data: "type_defs.Emv2000AttributesTypeDef" = dataclasses.field()

    MajorKeyDerivationMode = field("MajorKeyDerivationMode")
    PrimaryAccountNumber = field("PrimaryAccountNumber")
    PanSequenceNumber = field("PanSequenceNumber")
    ApplicationTransactionCounter = field("ApplicationTransactionCounter")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.Emv2000AttributesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Emv2000AttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmvCommonAttributes:
    boto3_raw_data: "type_defs.EmvCommonAttributesTypeDef" = dataclasses.field()

    MajorKeyDerivationMode = field("MajorKeyDerivationMode")
    PrimaryAccountNumber = field("PrimaryAccountNumber")
    PanSequenceNumber = field("PanSequenceNumber")
    ApplicationCryptogram = field("ApplicationCryptogram")
    Mode = field("Mode")
    PinBlockPaddingType = field("PinBlockPaddingType")
    PinBlockLengthPosition = field("PinBlockLengthPosition")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EmvCommonAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmvCommonAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MasterCardAttributes:
    boto3_raw_data: "type_defs.MasterCardAttributesTypeDef" = dataclasses.field()

    MajorKeyDerivationMode = field("MajorKeyDerivationMode")
    PrimaryAccountNumber = field("PrimaryAccountNumber")
    PanSequenceNumber = field("PanSequenceNumber")
    ApplicationCryptogram = field("ApplicationCryptogram")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MasterCardAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MasterCardAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DukptAttributes:
    boto3_raw_data: "type_defs.DukptAttributesTypeDef" = dataclasses.field()

    KeySerialNumber = field("KeySerialNumber")
    DukptDerivationType = field("DukptDerivationType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DukptAttributesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DukptAttributesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DukptDerivationAttributes:
    boto3_raw_data: "type_defs.DukptDerivationAttributesTypeDef" = dataclasses.field()

    KeySerialNumber = field("KeySerialNumber")
    DukptKeyDerivationType = field("DukptKeyDerivationType")
    DukptKeyVariant = field("DukptKeyVariant")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DukptDerivationAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DukptDerivationAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DukptEncryptionAttributes:
    boto3_raw_data: "type_defs.DukptEncryptionAttributesTypeDef" = dataclasses.field()

    KeySerialNumber = field("KeySerialNumber")
    Mode = field("Mode")
    DukptKeyDerivationType = field("DukptKeyDerivationType")
    DukptKeyVariant = field("DukptKeyVariant")
    InitializationVector = field("InitializationVector")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DukptEncryptionAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DukptEncryptionAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EcdhDerivationAttributes:
    boto3_raw_data: "type_defs.EcdhDerivationAttributesTypeDef" = dataclasses.field()

    CertificateAuthorityPublicKeyIdentifier = field(
        "CertificateAuthorityPublicKeyIdentifier"
    )
    PublicKeyCertificate = field("PublicKeyCertificate")
    KeyAlgorithm = field("KeyAlgorithm")
    KeyDerivationFunction = field("KeyDerivationFunction")
    KeyDerivationHashAlgorithm = field("KeyDerivationHashAlgorithm")
    SharedInformation = field("SharedInformation")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EcdhDerivationAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EcdhDerivationAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmvEncryptionAttributes:
    boto3_raw_data: "type_defs.EmvEncryptionAttributesTypeDef" = dataclasses.field()

    MajorKeyDerivationMode = field("MajorKeyDerivationMode")
    PrimaryAccountNumber = field("PrimaryAccountNumber")
    PanSequenceNumber = field("PanSequenceNumber")
    SessionDerivationData = field("SessionDerivationData")
    Mode = field("Mode")
    InitializationVector = field("InitializationVector")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EmvEncryptionAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmvEncryptionAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SymmetricEncryptionAttributes:
    boto3_raw_data: "type_defs.SymmetricEncryptionAttributesTypeDef" = (
        dataclasses.field()
    )

    Mode = field("Mode")
    InitializationVector = field("InitializationVector")
    PaddingType = field("PaddingType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SymmetricEncryptionAttributesTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SymmetricEncryptionAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VisaAmexDerivationOutputs:
    boto3_raw_data: "type_defs.VisaAmexDerivationOutputsTypeDef" = dataclasses.field()

    AuthorizationRequestKeyArn = field("AuthorizationRequestKeyArn")
    AuthorizationRequestKeyCheckValue = field("AuthorizationRequestKeyCheckValue")
    CurrentPinPekArn = field("CurrentPinPekArn")
    CurrentPinPekKeyCheckValue = field("CurrentPinPekKeyCheckValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VisaAmexDerivationOutputsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VisaAmexDerivationOutputsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PinData:
    boto3_raw_data: "type_defs.PinDataTypeDef" = dataclasses.field()

    PinOffset = field("PinOffset")
    VerificationValue = field("VerificationValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PinDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PinDataTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Ibm3624NaturalPin:
    boto3_raw_data: "type_defs.Ibm3624NaturalPinTypeDef" = dataclasses.field()

    DecimalizationTable = field("DecimalizationTable")
    PinValidationDataPadCharacter = field("PinValidationDataPadCharacter")
    PinValidationData = field("PinValidationData")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.Ibm3624NaturalPinTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Ibm3624NaturalPinTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Ibm3624PinFromOffset:
    boto3_raw_data: "type_defs.Ibm3624PinFromOffsetTypeDef" = dataclasses.field()

    DecimalizationTable = field("DecimalizationTable")
    PinValidationDataPadCharacter = field("PinValidationDataPadCharacter")
    PinValidationData = field("PinValidationData")
    PinOffset = field("PinOffset")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.Ibm3624PinFromOffsetTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Ibm3624PinFromOffsetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Ibm3624PinOffset:
    boto3_raw_data: "type_defs.Ibm3624PinOffsetTypeDef" = dataclasses.field()

    EncryptedPinBlock = field("EncryptedPinBlock")
    DecimalizationTable = field("DecimalizationTable")
    PinValidationDataPadCharacter = field("PinValidationDataPadCharacter")
    PinValidationData = field("PinValidationData")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.Ibm3624PinOffsetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Ibm3624PinOffsetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Ibm3624PinVerification:
    boto3_raw_data: "type_defs.Ibm3624PinVerificationTypeDef" = dataclasses.field()

    DecimalizationTable = field("DecimalizationTable")
    PinValidationDataPadCharacter = field("PinValidationDataPadCharacter")
    PinValidationData = field("PinValidationData")
    PinOffset = field("PinOffset")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.Ibm3624PinVerificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Ibm3624PinVerificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Ibm3624RandomPin:
    boto3_raw_data: "type_defs.Ibm3624RandomPinTypeDef" = dataclasses.field()

    DecimalizationTable = field("DecimalizationTable")
    PinValidationDataPadCharacter = field("PinValidationDataPadCharacter")
    PinValidationData = field("PinValidationData")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.Ibm3624RandomPinTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.Ibm3624RandomPinTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MacAlgorithmDukpt:
    boto3_raw_data: "type_defs.MacAlgorithmDukptTypeDef" = dataclasses.field()

    KeySerialNumber = field("KeySerialNumber")
    DukptKeyVariant = field("DukptKeyVariant")
    DukptDerivationType = field("DukptDerivationType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MacAlgorithmDukptTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MacAlgorithmDukptTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SessionKeyDerivationValue:
    boto3_raw_data: "type_defs.SessionKeyDerivationValueTypeDef" = dataclasses.field()

    ApplicationCryptogram = field("ApplicationCryptogram")
    ApplicationTransactionCounter = field("ApplicationTransactionCounter")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SessionKeyDerivationValueTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SessionKeyDerivationValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VisaPin:
    boto3_raw_data: "type_defs.VisaPinTypeDef" = dataclasses.field()

    PinVerificationKeyIndex = field("PinVerificationKeyIndex")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VisaPinTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VisaPinTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VisaPinVerificationValue:
    boto3_raw_data: "type_defs.VisaPinVerificationValueTypeDef" = dataclasses.field()

    EncryptedPinBlock = field("EncryptedPinBlock")
    PinVerificationKeyIndex = field("PinVerificationKeyIndex")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VisaPinVerificationValueTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VisaPinVerificationValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VisaPinVerification:
    boto3_raw_data: "type_defs.VisaPinVerificationTypeDef" = dataclasses.field()

    PinVerificationKeyIndex = field("PinVerificationKeyIndex")
    VerificationValue = field("VerificationValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VisaPinVerificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VisaPinVerificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SessionKeyAmex:
    boto3_raw_data: "type_defs.SessionKeyAmexTypeDef" = dataclasses.field()

    PrimaryAccountNumber = field("PrimaryAccountNumber")
    PanSequenceNumber = field("PanSequenceNumber")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SessionKeyAmexTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SessionKeyAmexTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SessionKeyEmv2000:
    boto3_raw_data: "type_defs.SessionKeyEmv2000TypeDef" = dataclasses.field()

    PrimaryAccountNumber = field("PrimaryAccountNumber")
    PanSequenceNumber = field("PanSequenceNumber")
    ApplicationTransactionCounter = field("ApplicationTransactionCounter")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SessionKeyEmv2000TypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SessionKeyEmv2000TypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SessionKeyEmvCommon:
    boto3_raw_data: "type_defs.SessionKeyEmvCommonTypeDef" = dataclasses.field()

    PrimaryAccountNumber = field("PrimaryAccountNumber")
    PanSequenceNumber = field("PanSequenceNumber")
    ApplicationTransactionCounter = field("ApplicationTransactionCounter")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SessionKeyEmvCommonTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SessionKeyEmvCommonTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SessionKeyMastercard:
    boto3_raw_data: "type_defs.SessionKeyMastercardTypeDef" = dataclasses.field()

    PrimaryAccountNumber = field("PrimaryAccountNumber")
    PanSequenceNumber = field("PanSequenceNumber")
    ApplicationTransactionCounter = field("ApplicationTransactionCounter")
    UnpredictableNumber = field("UnpredictableNumber")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SessionKeyMastercardTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SessionKeyMastercardTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SessionKeyVisa:
    boto3_raw_data: "type_defs.SessionKeyVisaTypeDef" = dataclasses.field()

    PrimaryAccountNumber = field("PrimaryAccountNumber")
    PanSequenceNumber = field("PanSequenceNumber")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SessionKeyVisaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SessionKeyVisaTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TranslationPinDataIsoFormat034:
    boto3_raw_data: "type_defs.TranslationPinDataIsoFormat034TypeDef" = (
        dataclasses.field()
    )

    PrimaryAccountNumber = field("PrimaryAccountNumber")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TranslationPinDataIsoFormat034TypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TranslationPinDataIsoFormat034TypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AmexAttributes:
    boto3_raw_data: "type_defs.AmexAttributesTypeDef" = dataclasses.field()

    MajorKeyDerivationMode = field("MajorKeyDerivationMode")
    PrimaryAccountNumber = field("PrimaryAccountNumber")
    PanSequenceNumber = field("PanSequenceNumber")
    ApplicationTransactionCounter = field("ApplicationTransactionCounter")
    AuthorizationRequestKeyIdentifier = field("AuthorizationRequestKeyIdentifier")

    @cached_property
    def CurrentPinAttributes(self):  # pragma: no cover
        return CurrentPinAttributes.make_one(
            self.boto3_raw_data["CurrentPinAttributes"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AmexAttributesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AmexAttributesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VisaAttributes:
    boto3_raw_data: "type_defs.VisaAttributesTypeDef" = dataclasses.field()

    MajorKeyDerivationMode = field("MajorKeyDerivationMode")
    PrimaryAccountNumber = field("PrimaryAccountNumber")
    PanSequenceNumber = field("PanSequenceNumber")
    ApplicationTransactionCounter = field("ApplicationTransactionCounter")
    AuthorizationRequestKeyIdentifier = field("AuthorizationRequestKeyIdentifier")

    @cached_property
    def CurrentPinAttributes(self):  # pragma: no cover
        return CurrentPinAttributes.make_one(
            self.boto3_raw_data["CurrentPinAttributes"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VisaAttributesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VisaAttributesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CardGenerationAttributes:
    boto3_raw_data: "type_defs.CardGenerationAttributesTypeDef" = dataclasses.field()

    @cached_property
    def AmexCardSecurityCodeVersion1(self):  # pragma: no cover
        return AmexCardSecurityCodeVersion1.make_one(
            self.boto3_raw_data["AmexCardSecurityCodeVersion1"]
        )

    @cached_property
    def AmexCardSecurityCodeVersion2(self):  # pragma: no cover
        return AmexCardSecurityCodeVersion2.make_one(
            self.boto3_raw_data["AmexCardSecurityCodeVersion2"]
        )

    @cached_property
    def CardVerificationValue1(self):  # pragma: no cover
        return CardVerificationValue1.make_one(
            self.boto3_raw_data["CardVerificationValue1"]
        )

    @cached_property
    def CardVerificationValue2(self):  # pragma: no cover
        return CardVerificationValue2.make_one(
            self.boto3_raw_data["CardVerificationValue2"]
        )

    @cached_property
    def CardHolderVerificationValue(self):  # pragma: no cover
        return CardHolderVerificationValue.make_one(
            self.boto3_raw_data["CardHolderVerificationValue"]
        )

    @cached_property
    def DynamicCardVerificationCode(self):  # pragma: no cover
        return DynamicCardVerificationCode.make_one(
            self.boto3_raw_data["DynamicCardVerificationCode"]
        )

    @cached_property
    def DynamicCardVerificationValue(self):  # pragma: no cover
        return DynamicCardVerificationValue.make_one(
            self.boto3_raw_data["DynamicCardVerificationValue"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CardGenerationAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CardGenerationAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CardVerificationAttributes:
    boto3_raw_data: "type_defs.CardVerificationAttributesTypeDef" = dataclasses.field()

    @cached_property
    def AmexCardSecurityCodeVersion1(self):  # pragma: no cover
        return AmexCardSecurityCodeVersion1.make_one(
            self.boto3_raw_data["AmexCardSecurityCodeVersion1"]
        )

    @cached_property
    def AmexCardSecurityCodeVersion2(self):  # pragma: no cover
        return AmexCardSecurityCodeVersion2.make_one(
            self.boto3_raw_data["AmexCardSecurityCodeVersion2"]
        )

    @cached_property
    def CardVerificationValue1(self):  # pragma: no cover
        return CardVerificationValue1.make_one(
            self.boto3_raw_data["CardVerificationValue1"]
        )

    @cached_property
    def CardVerificationValue2(self):  # pragma: no cover
        return CardVerificationValue2.make_one(
            self.boto3_raw_data["CardVerificationValue2"]
        )

    @cached_property
    def CardHolderVerificationValue(self):  # pragma: no cover
        return CardHolderVerificationValue.make_one(
            self.boto3_raw_data["CardHolderVerificationValue"]
        )

    @cached_property
    def DynamicCardVerificationCode(self):  # pragma: no cover
        return DynamicCardVerificationCode.make_one(
            self.boto3_raw_data["DynamicCardVerificationCode"]
        )

    @cached_property
    def DynamicCardVerificationValue(self):  # pragma: no cover
        return DynamicCardVerificationValue.make_one(
            self.boto3_raw_data["DynamicCardVerificationValue"]
        )

    @cached_property
    def DiscoverDynamicCardVerificationCode(self):  # pragma: no cover
        return DiscoverDynamicCardVerificationCode.make_one(
            self.boto3_raw_data["DiscoverDynamicCardVerificationCode"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CardVerificationAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CardVerificationAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CryptogramAuthResponse:
    boto3_raw_data: "type_defs.CryptogramAuthResponseTypeDef" = dataclasses.field()

    @cached_property
    def ArpcMethod1(self):  # pragma: no cover
        return CryptogramVerificationArpcMethod1.make_one(
            self.boto3_raw_data["ArpcMethod1"]
        )

    @cached_property
    def ArpcMethod2(self):  # pragma: no cover
        return CryptogramVerificationArpcMethod2.make_one(
            self.boto3_raw_data["ArpcMethod2"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CryptogramAuthResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CryptogramAuthResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DecryptDataOutput:
    boto3_raw_data: "type_defs.DecryptDataOutputTypeDef" = dataclasses.field()

    KeyArn = field("KeyArn")
    KeyCheckValue = field("KeyCheckValue")
    PlainText = field("PlainText")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DecryptDataOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DecryptDataOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EncryptDataOutput:
    boto3_raw_data: "type_defs.EncryptDataOutputTypeDef" = dataclasses.field()

    KeyArn = field("KeyArn")
    KeyCheckValue = field("KeyCheckValue")
    CipherText = field("CipherText")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EncryptDataOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EncryptDataOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerateCardValidationDataOutput:
    boto3_raw_data: "type_defs.GenerateCardValidationDataOutputTypeDef" = (
        dataclasses.field()
    )

    KeyArn = field("KeyArn")
    KeyCheckValue = field("KeyCheckValue")
    ValidationData = field("ValidationData")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GenerateCardValidationDataOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerateCardValidationDataOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerateMacOutput:
    boto3_raw_data: "type_defs.GenerateMacOutputTypeDef" = dataclasses.field()

    KeyArn = field("KeyArn")
    KeyCheckValue = field("KeyCheckValue")
    Mac = field("Mac")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GenerateMacOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerateMacOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReEncryptDataOutput:
    boto3_raw_data: "type_defs.ReEncryptDataOutputTypeDef" = dataclasses.field()

    KeyArn = field("KeyArn")
    KeyCheckValue = field("KeyCheckValue")
    CipherText = field("CipherText")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReEncryptDataOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReEncryptDataOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TranslatePinDataOutput:
    boto3_raw_data: "type_defs.TranslatePinDataOutputTypeDef" = dataclasses.field()

    PinBlock = field("PinBlock")
    KeyArn = field("KeyArn")
    KeyCheckValue = field("KeyCheckValue")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TranslatePinDataOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TranslatePinDataOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VerifyAuthRequestCryptogramOutput:
    boto3_raw_data: "type_defs.VerifyAuthRequestCryptogramOutputTypeDef" = (
        dataclasses.field()
    )

    KeyArn = field("KeyArn")
    KeyCheckValue = field("KeyCheckValue")
    AuthResponseValue = field("AuthResponseValue")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.VerifyAuthRequestCryptogramOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VerifyAuthRequestCryptogramOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VerifyCardValidationDataOutput:
    boto3_raw_data: "type_defs.VerifyCardValidationDataOutputTypeDef" = (
        dataclasses.field()
    )

    KeyArn = field("KeyArn")
    KeyCheckValue = field("KeyCheckValue")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.VerifyCardValidationDataOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VerifyCardValidationDataOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VerifyMacOutput:
    boto3_raw_data: "type_defs.VerifyMacOutputTypeDef" = dataclasses.field()

    KeyArn = field("KeyArn")
    KeyCheckValue = field("KeyCheckValue")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VerifyMacOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VerifyMacOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VerifyPinDataOutput:
    boto3_raw_data: "type_defs.VerifyPinDataOutputTypeDef" = dataclasses.field()

    VerificationKeyArn = field("VerificationKeyArn")
    VerificationKeyCheckValue = field("VerificationKeyCheckValue")
    EncryptionKeyArn = field("EncryptionKeyArn")
    EncryptionKeyCheckValue = field("EncryptionKeyCheckValue")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VerifyPinDataOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VerifyPinDataOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WrappedKeyMaterial:
    boto3_raw_data: "type_defs.WrappedKeyMaterialTypeDef" = dataclasses.field()

    Tr31KeyBlock = field("Tr31KeyBlock")

    @cached_property
    def DiffieHellmanSymmetricKey(self):  # pragma: no cover
        return EcdhDerivationAttributes.make_one(
            self.boto3_raw_data["DiffieHellmanSymmetricKey"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WrappedKeyMaterialTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WrappedKeyMaterialTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EncryptionDecryptionAttributes:
    boto3_raw_data: "type_defs.EncryptionDecryptionAttributesTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Symmetric(self):  # pragma: no cover
        return SymmetricEncryptionAttributes.make_one(self.boto3_raw_data["Symmetric"])

    @cached_property
    def Asymmetric(self):  # pragma: no cover
        return AsymmetricEncryptionAttributes.make_one(
            self.boto3_raw_data["Asymmetric"]
        )

    @cached_property
    def Dukpt(self):  # pragma: no cover
        return DukptEncryptionAttributes.make_one(self.boto3_raw_data["Dukpt"])

    @cached_property
    def Emv(self):  # pragma: no cover
        return EmvEncryptionAttributes.make_one(self.boto3_raw_data["Emv"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EncryptionDecryptionAttributesTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EncryptionDecryptionAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReEncryptionAttributes:
    boto3_raw_data: "type_defs.ReEncryptionAttributesTypeDef" = dataclasses.field()

    @cached_property
    def Symmetric(self):  # pragma: no cover
        return SymmetricEncryptionAttributes.make_one(self.boto3_raw_data["Symmetric"])

    @cached_property
    def Dukpt(self):  # pragma: no cover
        return DukptEncryptionAttributes.make_one(self.boto3_raw_data["Dukpt"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReEncryptionAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReEncryptionAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerateMacEmvPinChangeOutput:
    boto3_raw_data: "type_defs.GenerateMacEmvPinChangeOutputTypeDef" = (
        dataclasses.field()
    )

    NewPinPekArn = field("NewPinPekArn")
    SecureMessagingIntegrityKeyArn = field("SecureMessagingIntegrityKeyArn")
    SecureMessagingConfidentialityKeyArn = field("SecureMessagingConfidentialityKeyArn")
    Mac = field("Mac")
    EncryptedPinBlock = field("EncryptedPinBlock")
    NewPinPekKeyCheckValue = field("NewPinPekKeyCheckValue")
    SecureMessagingIntegrityKeyCheckValue = field(
        "SecureMessagingIntegrityKeyCheckValue"
    )
    SecureMessagingConfidentialityKeyCheckValue = field(
        "SecureMessagingConfidentialityKeyCheckValue"
    )

    @cached_property
    def VisaAmexDerivationOutputs(self):  # pragma: no cover
        return VisaAmexDerivationOutputs.make_one(
            self.boto3_raw_data["VisaAmexDerivationOutputs"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GenerateMacEmvPinChangeOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerateMacEmvPinChangeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GeneratePinDataOutput:
    boto3_raw_data: "type_defs.GeneratePinDataOutputTypeDef" = dataclasses.field()

    GenerationKeyArn = field("GenerationKeyArn")
    GenerationKeyCheckValue = field("GenerationKeyCheckValue")
    EncryptionKeyArn = field("EncryptionKeyArn")
    EncryptionKeyCheckValue = field("EncryptionKeyCheckValue")
    EncryptedPinBlock = field("EncryptedPinBlock")

    @cached_property
    def PinData(self):  # pragma: no cover
        return PinData.make_one(self.boto3_raw_data["PinData"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GeneratePinDataOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GeneratePinDataOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MacAlgorithmEmv:
    boto3_raw_data: "type_defs.MacAlgorithmEmvTypeDef" = dataclasses.field()

    MajorKeyDerivationMode = field("MajorKeyDerivationMode")
    PrimaryAccountNumber = field("PrimaryAccountNumber")
    PanSequenceNumber = field("PanSequenceNumber")
    SessionKeyDerivationMode = field("SessionKeyDerivationMode")

    @cached_property
    def SessionKeyDerivationValue(self):  # pragma: no cover
        return SessionKeyDerivationValue.make_one(
            self.boto3_raw_data["SessionKeyDerivationValue"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MacAlgorithmEmvTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MacAlgorithmEmvTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PinGenerationAttributes:
    boto3_raw_data: "type_defs.PinGenerationAttributesTypeDef" = dataclasses.field()

    @cached_property
    def VisaPin(self):  # pragma: no cover
        return VisaPin.make_one(self.boto3_raw_data["VisaPin"])

    @cached_property
    def VisaPinVerificationValue(self):  # pragma: no cover
        return VisaPinVerificationValue.make_one(
            self.boto3_raw_data["VisaPinVerificationValue"]
        )

    @cached_property
    def Ibm3624PinOffset(self):  # pragma: no cover
        return Ibm3624PinOffset.make_one(self.boto3_raw_data["Ibm3624PinOffset"])

    @cached_property
    def Ibm3624NaturalPin(self):  # pragma: no cover
        return Ibm3624NaturalPin.make_one(self.boto3_raw_data["Ibm3624NaturalPin"])

    @cached_property
    def Ibm3624RandomPin(self):  # pragma: no cover
        return Ibm3624RandomPin.make_one(self.boto3_raw_data["Ibm3624RandomPin"])

    @cached_property
    def Ibm3624PinFromOffset(self):  # pragma: no cover
        return Ibm3624PinFromOffset.make_one(
            self.boto3_raw_data["Ibm3624PinFromOffset"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PinGenerationAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PinGenerationAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PinVerificationAttributes:
    boto3_raw_data: "type_defs.PinVerificationAttributesTypeDef" = dataclasses.field()

    @cached_property
    def VisaPin(self):  # pragma: no cover
        return VisaPinVerification.make_one(self.boto3_raw_data["VisaPin"])

    @cached_property
    def Ibm3624Pin(self):  # pragma: no cover
        return Ibm3624PinVerification.make_one(self.boto3_raw_data["Ibm3624Pin"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PinVerificationAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PinVerificationAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SessionKeyDerivation:
    boto3_raw_data: "type_defs.SessionKeyDerivationTypeDef" = dataclasses.field()

    @cached_property
    def EmvCommon(self):  # pragma: no cover
        return SessionKeyEmvCommon.make_one(self.boto3_raw_data["EmvCommon"])

    @cached_property
    def Mastercard(self):  # pragma: no cover
        return SessionKeyMastercard.make_one(self.boto3_raw_data["Mastercard"])

    @cached_property
    def Emv2000(self):  # pragma: no cover
        return SessionKeyEmv2000.make_one(self.boto3_raw_data["Emv2000"])

    @cached_property
    def Amex(self):  # pragma: no cover
        return SessionKeyAmex.make_one(self.boto3_raw_data["Amex"])

    @cached_property
    def Visa(self):  # pragma: no cover
        return SessionKeyVisa.make_one(self.boto3_raw_data["Visa"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SessionKeyDerivationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SessionKeyDerivationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TranslationIsoFormats:
    boto3_raw_data: "type_defs.TranslationIsoFormatsTypeDef" = dataclasses.field()

    @cached_property
    def IsoFormat0(self):  # pragma: no cover
        return TranslationPinDataIsoFormat034.make_one(
            self.boto3_raw_data["IsoFormat0"]
        )

    IsoFormat1 = field("IsoFormat1")

    @cached_property
    def IsoFormat3(self):  # pragma: no cover
        return TranslationPinDataIsoFormat034.make_one(
            self.boto3_raw_data["IsoFormat3"]
        )

    @cached_property
    def IsoFormat4(self):  # pragma: no cover
        return TranslationPinDataIsoFormat034.make_one(
            self.boto3_raw_data["IsoFormat4"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TranslationIsoFormatsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TranslationIsoFormatsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DerivationMethodAttributes:
    boto3_raw_data: "type_defs.DerivationMethodAttributesTypeDef" = dataclasses.field()

    @cached_property
    def EmvCommon(self):  # pragma: no cover
        return EmvCommonAttributes.make_one(self.boto3_raw_data["EmvCommon"])

    @cached_property
    def Amex(self):  # pragma: no cover
        return AmexAttributes.make_one(self.boto3_raw_data["Amex"])

    @cached_property
    def Visa(self):  # pragma: no cover
        return VisaAttributes.make_one(self.boto3_raw_data["Visa"])

    @cached_property
    def Emv2000(self):  # pragma: no cover
        return Emv2000Attributes.make_one(self.boto3_raw_data["Emv2000"])

    @cached_property
    def Mastercard(self):  # pragma: no cover
        return MasterCardAttributes.make_one(self.boto3_raw_data["Mastercard"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DerivationMethodAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DerivationMethodAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerateCardValidationDataInput:
    boto3_raw_data: "type_defs.GenerateCardValidationDataInputTypeDef" = (
        dataclasses.field()
    )

    KeyIdentifier = field("KeyIdentifier")
    PrimaryAccountNumber = field("PrimaryAccountNumber")

    @cached_property
    def GenerationAttributes(self):  # pragma: no cover
        return CardGenerationAttributes.make_one(
            self.boto3_raw_data["GenerationAttributes"]
        )

    ValidationDataLength = field("ValidationDataLength")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GenerateCardValidationDataInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerateCardValidationDataInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VerifyCardValidationDataInput:
    boto3_raw_data: "type_defs.VerifyCardValidationDataInputTypeDef" = (
        dataclasses.field()
    )

    KeyIdentifier = field("KeyIdentifier")
    PrimaryAccountNumber = field("PrimaryAccountNumber")

    @cached_property
    def VerificationAttributes(self):  # pragma: no cover
        return CardVerificationAttributes.make_one(
            self.boto3_raw_data["VerificationAttributes"]
        )

    ValidationData = field("ValidationData")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.VerifyCardValidationDataInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VerifyCardValidationDataInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WrappedKey:
    boto3_raw_data: "type_defs.WrappedKeyTypeDef" = dataclasses.field()

    @cached_property
    def WrappedKeyMaterial(self):  # pragma: no cover
        return WrappedKeyMaterial.make_one(self.boto3_raw_data["WrappedKeyMaterial"])

    KeyCheckValueAlgorithm = field("KeyCheckValueAlgorithm")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WrappedKeyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WrappedKeyTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MacAttributes:
    boto3_raw_data: "type_defs.MacAttributesTypeDef" = dataclasses.field()

    Algorithm = field("Algorithm")

    @cached_property
    def EmvMac(self):  # pragma: no cover
        return MacAlgorithmEmv.make_one(self.boto3_raw_data["EmvMac"])

    @cached_property
    def DukptIso9797Algorithm1(self):  # pragma: no cover
        return MacAlgorithmDukpt.make_one(self.boto3_raw_data["DukptIso9797Algorithm1"])

    @cached_property
    def DukptIso9797Algorithm3(self):  # pragma: no cover
        return MacAlgorithmDukpt.make_one(self.boto3_raw_data["DukptIso9797Algorithm3"])

    @cached_property
    def DukptCmac(self):  # pragma: no cover
        return MacAlgorithmDukpt.make_one(self.boto3_raw_data["DukptCmac"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MacAttributesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MacAttributesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VerifyAuthRequestCryptogramInput:
    boto3_raw_data: "type_defs.VerifyAuthRequestCryptogramInputTypeDef" = (
        dataclasses.field()
    )

    KeyIdentifier = field("KeyIdentifier")
    TransactionData = field("TransactionData")
    AuthRequestCryptogram = field("AuthRequestCryptogram")
    MajorKeyDerivationMode = field("MajorKeyDerivationMode")

    @cached_property
    def SessionKeyDerivationAttributes(self):  # pragma: no cover
        return SessionKeyDerivation.make_one(
            self.boto3_raw_data["SessionKeyDerivationAttributes"]
        )

    @cached_property
    def AuthResponseAttributes(self):  # pragma: no cover
        return CryptogramAuthResponse.make_one(
            self.boto3_raw_data["AuthResponseAttributes"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.VerifyAuthRequestCryptogramInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VerifyAuthRequestCryptogramInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerateMacEmvPinChangeInput:
    boto3_raw_data: "type_defs.GenerateMacEmvPinChangeInputTypeDef" = (
        dataclasses.field()
    )

    NewPinPekIdentifier = field("NewPinPekIdentifier")
    NewEncryptedPinBlock = field("NewEncryptedPinBlock")
    PinBlockFormat = field("PinBlockFormat")
    SecureMessagingIntegrityKeyIdentifier = field(
        "SecureMessagingIntegrityKeyIdentifier"
    )
    SecureMessagingConfidentialityKeyIdentifier = field(
        "SecureMessagingConfidentialityKeyIdentifier"
    )
    MessageData = field("MessageData")

    @cached_property
    def DerivationMethodAttributes(self):  # pragma: no cover
        return DerivationMethodAttributes.make_one(
            self.boto3_raw_data["DerivationMethodAttributes"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GenerateMacEmvPinChangeInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerateMacEmvPinChangeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DecryptDataInput:
    boto3_raw_data: "type_defs.DecryptDataInputTypeDef" = dataclasses.field()

    KeyIdentifier = field("KeyIdentifier")
    CipherText = field("CipherText")

    @cached_property
    def DecryptionAttributes(self):  # pragma: no cover
        return EncryptionDecryptionAttributes.make_one(
            self.boto3_raw_data["DecryptionAttributes"]
        )

    @cached_property
    def WrappedKey(self):  # pragma: no cover
        return WrappedKey.make_one(self.boto3_raw_data["WrappedKey"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DecryptDataInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DecryptDataInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EncryptDataInput:
    boto3_raw_data: "type_defs.EncryptDataInputTypeDef" = dataclasses.field()

    KeyIdentifier = field("KeyIdentifier")
    PlainText = field("PlainText")

    @cached_property
    def EncryptionAttributes(self):  # pragma: no cover
        return EncryptionDecryptionAttributes.make_one(
            self.boto3_raw_data["EncryptionAttributes"]
        )

    @cached_property
    def WrappedKey(self):  # pragma: no cover
        return WrappedKey.make_one(self.boto3_raw_data["WrappedKey"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EncryptDataInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EncryptDataInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GeneratePinDataInput:
    boto3_raw_data: "type_defs.GeneratePinDataInputTypeDef" = dataclasses.field()

    GenerationKeyIdentifier = field("GenerationKeyIdentifier")
    EncryptionKeyIdentifier = field("EncryptionKeyIdentifier")

    @cached_property
    def GenerationAttributes(self):  # pragma: no cover
        return PinGenerationAttributes.make_one(
            self.boto3_raw_data["GenerationAttributes"]
        )

    PrimaryAccountNumber = field("PrimaryAccountNumber")
    PinBlockFormat = field("PinBlockFormat")
    PinDataLength = field("PinDataLength")

    @cached_property
    def EncryptionWrappedKey(self):  # pragma: no cover
        return WrappedKey.make_one(self.boto3_raw_data["EncryptionWrappedKey"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GeneratePinDataInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GeneratePinDataInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReEncryptDataInput:
    boto3_raw_data: "type_defs.ReEncryptDataInputTypeDef" = dataclasses.field()

    IncomingKeyIdentifier = field("IncomingKeyIdentifier")
    OutgoingKeyIdentifier = field("OutgoingKeyIdentifier")
    CipherText = field("CipherText")

    @cached_property
    def IncomingEncryptionAttributes(self):  # pragma: no cover
        return ReEncryptionAttributes.make_one(
            self.boto3_raw_data["IncomingEncryptionAttributes"]
        )

    @cached_property
    def OutgoingEncryptionAttributes(self):  # pragma: no cover
        return ReEncryptionAttributes.make_one(
            self.boto3_raw_data["OutgoingEncryptionAttributes"]
        )

    @cached_property
    def IncomingWrappedKey(self):  # pragma: no cover
        return WrappedKey.make_one(self.boto3_raw_data["IncomingWrappedKey"])

    @cached_property
    def OutgoingWrappedKey(self):  # pragma: no cover
        return WrappedKey.make_one(self.boto3_raw_data["OutgoingWrappedKey"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReEncryptDataInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReEncryptDataInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TranslatePinDataInput:
    boto3_raw_data: "type_defs.TranslatePinDataInputTypeDef" = dataclasses.field()

    IncomingKeyIdentifier = field("IncomingKeyIdentifier")
    OutgoingKeyIdentifier = field("OutgoingKeyIdentifier")

    @cached_property
    def IncomingTranslationAttributes(self):  # pragma: no cover
        return TranslationIsoFormats.make_one(
            self.boto3_raw_data["IncomingTranslationAttributes"]
        )

    @cached_property
    def OutgoingTranslationAttributes(self):  # pragma: no cover
        return TranslationIsoFormats.make_one(
            self.boto3_raw_data["OutgoingTranslationAttributes"]
        )

    EncryptedPinBlock = field("EncryptedPinBlock")

    @cached_property
    def IncomingDukptAttributes(self):  # pragma: no cover
        return DukptDerivationAttributes.make_one(
            self.boto3_raw_data["IncomingDukptAttributes"]
        )

    @cached_property
    def OutgoingDukptAttributes(self):  # pragma: no cover
        return DukptDerivationAttributes.make_one(
            self.boto3_raw_data["OutgoingDukptAttributes"]
        )

    @cached_property
    def IncomingWrappedKey(self):  # pragma: no cover
        return WrappedKey.make_one(self.boto3_raw_data["IncomingWrappedKey"])

    @cached_property
    def OutgoingWrappedKey(self):  # pragma: no cover
        return WrappedKey.make_one(self.boto3_raw_data["OutgoingWrappedKey"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TranslatePinDataInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TranslatePinDataInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VerifyPinDataInput:
    boto3_raw_data: "type_defs.VerifyPinDataInputTypeDef" = dataclasses.field()

    VerificationKeyIdentifier = field("VerificationKeyIdentifier")
    EncryptionKeyIdentifier = field("EncryptionKeyIdentifier")

    @cached_property
    def VerificationAttributes(self):  # pragma: no cover
        return PinVerificationAttributes.make_one(
            self.boto3_raw_data["VerificationAttributes"]
        )

    EncryptedPinBlock = field("EncryptedPinBlock")
    PrimaryAccountNumber = field("PrimaryAccountNumber")
    PinBlockFormat = field("PinBlockFormat")
    PinDataLength = field("PinDataLength")

    @cached_property
    def DukptAttributes(self):  # pragma: no cover
        return DukptAttributes.make_one(self.boto3_raw_data["DukptAttributes"])

    @cached_property
    def EncryptionWrappedKey(self):  # pragma: no cover
        return WrappedKey.make_one(self.boto3_raw_data["EncryptionWrappedKey"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VerifyPinDataInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VerifyPinDataInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerateMacInput:
    boto3_raw_data: "type_defs.GenerateMacInputTypeDef" = dataclasses.field()

    KeyIdentifier = field("KeyIdentifier")
    MessageData = field("MessageData")

    @cached_property
    def GenerationAttributes(self):  # pragma: no cover
        return MacAttributes.make_one(self.boto3_raw_data["GenerationAttributes"])

    MacLength = field("MacLength")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GenerateMacInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerateMacInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VerifyMacInput:
    boto3_raw_data: "type_defs.VerifyMacInputTypeDef" = dataclasses.field()

    KeyIdentifier = field("KeyIdentifier")
    MessageData = field("MessageData")
    Mac = field("Mac")

    @cached_property
    def VerificationAttributes(self):  # pragma: no cover
        return MacAttributes.make_one(self.boto3_raw_data["VerificationAttributes"])

    MacLength = field("MacLength")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VerifyMacInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VerifyMacInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
