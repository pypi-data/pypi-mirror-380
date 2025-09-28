# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_payment_cryptography_data import type_defs as bs_td


class PAYMENT_CRYPTOGRAPHY_DATACaster:

    def decrypt_data(
        self,
        res: "bs_td.DecryptDataOutputTypeDef",
    ) -> "dc_td.DecryptDataOutput":
        return dc_td.DecryptDataOutput.make_one(res)

    def encrypt_data(
        self,
        res: "bs_td.EncryptDataOutputTypeDef",
    ) -> "dc_td.EncryptDataOutput":
        return dc_td.EncryptDataOutput.make_one(res)

    def generate_card_validation_data(
        self,
        res: "bs_td.GenerateCardValidationDataOutputTypeDef",
    ) -> "dc_td.GenerateCardValidationDataOutput":
        return dc_td.GenerateCardValidationDataOutput.make_one(res)

    def generate_mac(
        self,
        res: "bs_td.GenerateMacOutputTypeDef",
    ) -> "dc_td.GenerateMacOutput":
        return dc_td.GenerateMacOutput.make_one(res)

    def generate_mac_emv_pin_change(
        self,
        res: "bs_td.GenerateMacEmvPinChangeOutputTypeDef",
    ) -> "dc_td.GenerateMacEmvPinChangeOutput":
        return dc_td.GenerateMacEmvPinChangeOutput.make_one(res)

    def generate_pin_data(
        self,
        res: "bs_td.GeneratePinDataOutputTypeDef",
    ) -> "dc_td.GeneratePinDataOutput":
        return dc_td.GeneratePinDataOutput.make_one(res)

    def re_encrypt_data(
        self,
        res: "bs_td.ReEncryptDataOutputTypeDef",
    ) -> "dc_td.ReEncryptDataOutput":
        return dc_td.ReEncryptDataOutput.make_one(res)

    def translate_pin_data(
        self,
        res: "bs_td.TranslatePinDataOutputTypeDef",
    ) -> "dc_td.TranslatePinDataOutput":
        return dc_td.TranslatePinDataOutput.make_one(res)

    def verify_auth_request_cryptogram(
        self,
        res: "bs_td.VerifyAuthRequestCryptogramOutputTypeDef",
    ) -> "dc_td.VerifyAuthRequestCryptogramOutput":
        return dc_td.VerifyAuthRequestCryptogramOutput.make_one(res)

    def verify_card_validation_data(
        self,
        res: "bs_td.VerifyCardValidationDataOutputTypeDef",
    ) -> "dc_td.VerifyCardValidationDataOutput":
        return dc_td.VerifyCardValidationDataOutput.make_one(res)

    def verify_mac(
        self,
        res: "bs_td.VerifyMacOutputTypeDef",
    ) -> "dc_td.VerifyMacOutput":
        return dc_td.VerifyMacOutput.make_one(res)

    def verify_pin_data(
        self,
        res: "bs_td.VerifyPinDataOutputTypeDef",
    ) -> "dc_td.VerifyPinDataOutput":
        return dc_td.VerifyPinDataOutput.make_one(res)


payment_cryptography_data_caster = PAYMENT_CRYPTOGRAPHY_DATACaster()
