# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_iotwireless import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class SessionKeysAbpV10X:
    boto3_raw_data: "type_defs.SessionKeysAbpV10XTypeDef" = dataclasses.field()

    NwkSKey = field("NwkSKey")
    AppSKey = field("AppSKey")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SessionKeysAbpV10XTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SessionKeysAbpV10XTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SessionKeysAbpV11:
    boto3_raw_data: "type_defs.SessionKeysAbpV11TypeDef" = dataclasses.field()

    FNwkSIntKey = field("FNwkSIntKey")
    SNwkSIntKey = field("SNwkSIntKey")
    NwkSEncKey = field("NwkSEncKey")
    AppSKey = field("AppSKey")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SessionKeysAbpV11TypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SessionKeysAbpV11TypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Accuracy:
    boto3_raw_data: "type_defs.AccuracyTypeDef" = dataclasses.field()

    HorizontalAccuracy = field("HorizontalAccuracy")
    VerticalAccuracy = field("VerticalAccuracy")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccuracyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccuracyTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationConfig:
    boto3_raw_data: "type_defs.ApplicationConfigTypeDef" = dataclasses.field()

    FPort = field("FPort")
    Type = field("Type")
    DestinationName = field("DestinationName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ApplicationConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SidewalkAccountInfo:
    boto3_raw_data: "type_defs.SidewalkAccountInfoTypeDef" = dataclasses.field()

    AmazonId = field("AmazonId")
    AppServerPrivateKey = field("AppServerPrivateKey")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SidewalkAccountInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SidewalkAccountInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Tag:
    boto3_raw_data: "type_defs.TagTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagTypeDef"]]
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
class AssociateMulticastGroupWithFuotaTaskRequest:
    boto3_raw_data: "type_defs.AssociateMulticastGroupWithFuotaTaskRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    MulticastGroupId = field("MulticastGroupId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateMulticastGroupWithFuotaTaskRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateMulticastGroupWithFuotaTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateWirelessDeviceWithFuotaTaskRequest:
    boto3_raw_data: "type_defs.AssociateWirelessDeviceWithFuotaTaskRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    WirelessDeviceId = field("WirelessDeviceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateWirelessDeviceWithFuotaTaskRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateWirelessDeviceWithFuotaTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateWirelessDeviceWithMulticastGroupRequest:
    boto3_raw_data: (
        "type_defs.AssociateWirelessDeviceWithMulticastGroupRequestTypeDef"
    ) = dataclasses.field()

    Id = field("Id")
    WirelessDeviceId = field("WirelessDeviceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateWirelessDeviceWithMulticastGroupRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.AssociateWirelessDeviceWithMulticastGroupRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateWirelessDeviceWithThingRequest:
    boto3_raw_data: "type_defs.AssociateWirelessDeviceWithThingRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    ThingArn = field("ThingArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateWirelessDeviceWithThingRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateWirelessDeviceWithThingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateWirelessGatewayWithCertificateRequest:
    boto3_raw_data: (
        "type_defs.AssociateWirelessGatewayWithCertificateRequestTypeDef"
    ) = dataclasses.field()

    Id = field("Id")
    IotCertificateId = field("IotCertificateId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateWirelessGatewayWithCertificateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.AssociateWirelessGatewayWithCertificateRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateWirelessGatewayWithThingRequest:
    boto3_raw_data: "type_defs.AssociateWirelessGatewayWithThingRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    ThingArn = field("ThingArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateWirelessGatewayWithThingRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateWirelessGatewayWithThingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BeaconingOutput:
    boto3_raw_data: "type_defs.BeaconingOutputTypeDef" = dataclasses.field()

    DataRate = field("DataRate")
    Frequencies = field("Frequencies")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BeaconingOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BeaconingOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Beaconing:
    boto3_raw_data: "type_defs.BeaconingTypeDef" = dataclasses.field()

    DataRate = field("DataRate")
    Frequencies = field("Frequencies")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BeaconingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BeaconingTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelMulticastGroupSessionRequest:
    boto3_raw_data: "type_defs.CancelMulticastGroupSessionRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CancelMulticastGroupSessionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelMulticastGroupSessionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CdmaLocalId:
    boto3_raw_data: "type_defs.CdmaLocalIdTypeDef" = dataclasses.field()

    PnOffset = field("PnOffset")
    CdmaChannel = field("CdmaChannel")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CdmaLocalIdTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CdmaLocalIdTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CdmaNmrObj:
    boto3_raw_data: "type_defs.CdmaNmrObjTypeDef" = dataclasses.field()

    PnOffset = field("PnOffset")
    CdmaChannel = field("CdmaChannel")
    PilotPower = field("PilotPower")
    BaseStationId = field("BaseStationId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CdmaNmrObjTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CdmaNmrObjTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CertificateList:
    boto3_raw_data: "type_defs.CertificateListTypeDef" = dataclasses.field()

    SigningAlg = field("SigningAlg")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CertificateListTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CertificateListTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoRaWANConnectionStatusEventNotificationConfigurations:
    boto3_raw_data: (
        "type_defs.LoRaWANConnectionStatusEventNotificationConfigurationsTypeDef"
    ) = dataclasses.field()

    GatewayEuiEventTopic = field("GatewayEuiEventTopic")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LoRaWANConnectionStatusEventNotificationConfigurationsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.LoRaWANConnectionStatusEventNotificationConfigurationsTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoRaWANConnectionStatusResourceTypeEventConfiguration:
    boto3_raw_data: (
        "type_defs.LoRaWANConnectionStatusResourceTypeEventConfigurationTypeDef"
    ) = dataclasses.field()

    WirelessGatewayEventTopic = field("WirelessGatewayEventTopic")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LoRaWANConnectionStatusResourceTypeEventConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.LoRaWANConnectionStatusResourceTypeEventConfigurationTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoRaWANFuotaTask:
    boto3_raw_data: "type_defs.LoRaWANFuotaTaskTypeDef" = dataclasses.field()

    RfRegion = field("RfRegion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LoRaWANFuotaTaskTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoRaWANFuotaTaskTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TraceContent:
    boto3_raw_data: "type_defs.TraceContentTypeDef" = dataclasses.field()

    WirelessDeviceFrameInfo = field("WirelessDeviceFrameInfo")
    LogLevel = field("LogLevel")
    MulticastFrameInfo = field("MulticastFrameInfo")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TraceContentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TraceContentTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoRaWANServiceProfile:
    boto3_raw_data: "type_defs.LoRaWANServiceProfileTypeDef" = dataclasses.field()

    AddGwMetadata = field("AddGwMetadata")
    DrMin = field("DrMin")
    DrMax = field("DrMax")
    PrAllowed = field("PrAllowed")
    RaAllowed = field("RaAllowed")
    TxPowerIndexMin = field("TxPowerIndexMin")
    TxPowerIndexMax = field("TxPowerIndexMax")
    NbTransMin = field("NbTransMin")
    NbTransMax = field("NbTransMax")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LoRaWANServiceProfileTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoRaWANServiceProfileTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SidewalkCreateWirelessDevice:
    boto3_raw_data: "type_defs.SidewalkCreateWirelessDeviceTypeDef" = (
        dataclasses.field()
    )

    DeviceProfileId = field("DeviceProfileId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SidewalkCreateWirelessDeviceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SidewalkCreateWirelessDeviceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWirelessGatewayTaskRequest:
    boto3_raw_data: "type_defs.CreateWirelessGatewayTaskRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    WirelessGatewayTaskDefinitionId = field("WirelessGatewayTaskDefinitionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateWirelessGatewayTaskRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWirelessGatewayTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DakCertificateMetadata:
    boto3_raw_data: "type_defs.DakCertificateMetadataTypeDef" = dataclasses.field()

    CertificateId = field("CertificateId")
    MaxAllowedSignature = field("MaxAllowedSignature")
    FactorySupport = field("FactorySupport")
    ApId = field("ApId")
    DeviceTypeId = field("DeviceTypeId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DakCertificateMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DakCertificateMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDestinationRequest:
    boto3_raw_data: "type_defs.DeleteDestinationRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDestinationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDestinationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDeviceProfileRequest:
    boto3_raw_data: "type_defs.DeleteDeviceProfileRequestTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDeviceProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDeviceProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFuotaTaskRequest:
    boto3_raw_data: "type_defs.DeleteFuotaTaskRequestTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteFuotaTaskRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFuotaTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMulticastGroupRequest:
    boto3_raw_data: "type_defs.DeleteMulticastGroupRequestTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteMulticastGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMulticastGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteNetworkAnalyzerConfigurationRequest:
    boto3_raw_data: "type_defs.DeleteNetworkAnalyzerConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationName = field("ConfigurationName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteNetworkAnalyzerConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteNetworkAnalyzerConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteQueuedMessagesRequest:
    boto3_raw_data: "type_defs.DeleteQueuedMessagesRequestTypeDef" = dataclasses.field()

    Id = field("Id")
    MessageId = field("MessageId")
    WirelessDeviceType = field("WirelessDeviceType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteQueuedMessagesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteQueuedMessagesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteServiceProfileRequest:
    boto3_raw_data: "type_defs.DeleteServiceProfileRequestTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteServiceProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteServiceProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteWirelessDeviceImportTaskRequest:
    boto3_raw_data: "type_defs.DeleteWirelessDeviceImportTaskRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteWirelessDeviceImportTaskRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteWirelessDeviceImportTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteWirelessDeviceRequest:
    boto3_raw_data: "type_defs.DeleteWirelessDeviceRequestTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteWirelessDeviceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteWirelessDeviceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteWirelessGatewayRequest:
    boto3_raw_data: "type_defs.DeleteWirelessGatewayRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteWirelessGatewayRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteWirelessGatewayRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteWirelessGatewayTaskDefinitionRequest:
    boto3_raw_data: "type_defs.DeleteWirelessGatewayTaskDefinitionRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteWirelessGatewayTaskDefinitionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteWirelessGatewayTaskDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteWirelessGatewayTaskRequest:
    boto3_raw_data: "type_defs.DeleteWirelessGatewayTaskRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteWirelessGatewayTaskRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteWirelessGatewayTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterWirelessDeviceRequest:
    boto3_raw_data: "type_defs.DeregisterWirelessDeviceRequestTypeDef" = (
        dataclasses.field()
    )

    Identifier = field("Identifier")
    WirelessDeviceType = field("WirelessDeviceType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeregisterWirelessDeviceRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterWirelessDeviceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Destinations:
    boto3_raw_data: "type_defs.DestinationsTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Name = field("Name")
    ExpressionType = field("ExpressionType")
    Expression = field("Expression")
    Description = field("Description")
    RoleArn = field("RoleArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DestinationsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DestinationsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeviceProfile:
    boto3_raw_data: "type_defs.DeviceProfileTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Name = field("Name")
    Id = field("Id")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeviceProfileTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeviceProfileTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SidewalkEventNotificationConfigurations:
    boto3_raw_data: "type_defs.SidewalkEventNotificationConfigurationsTypeDef" = (
        dataclasses.field()
    )

    AmazonIdEventTopic = field("AmazonIdEventTopic")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SidewalkEventNotificationConfigurationsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SidewalkEventNotificationConfigurationsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SidewalkResourceTypeEventConfiguration:
    boto3_raw_data: "type_defs.SidewalkResourceTypeEventConfigurationTypeDef" = (
        dataclasses.field()
    )

    WirelessDeviceEventTopic = field("WirelessDeviceEventTopic")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SidewalkResourceTypeEventConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SidewalkResourceTypeEventConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Dimension:
    boto3_raw_data: "type_defs.DimensionTypeDef" = dataclasses.field()

    name = field("name")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DimensionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DimensionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateAwsAccountFromPartnerAccountRequest:
    boto3_raw_data: (
        "type_defs.DisassociateAwsAccountFromPartnerAccountRequestTypeDef"
    ) = dataclasses.field()

    PartnerAccountId = field("PartnerAccountId")
    PartnerType = field("PartnerType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateAwsAccountFromPartnerAccountRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.DisassociateAwsAccountFromPartnerAccountRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateMulticastGroupFromFuotaTaskRequest:
    boto3_raw_data: (
        "type_defs.DisassociateMulticastGroupFromFuotaTaskRequestTypeDef"
    ) = dataclasses.field()

    Id = field("Id")
    MulticastGroupId = field("MulticastGroupId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateMulticastGroupFromFuotaTaskRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.DisassociateMulticastGroupFromFuotaTaskRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateWirelessDeviceFromFuotaTaskRequest:
    boto3_raw_data: (
        "type_defs.DisassociateWirelessDeviceFromFuotaTaskRequestTypeDef"
    ) = dataclasses.field()

    Id = field("Id")
    WirelessDeviceId = field("WirelessDeviceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateWirelessDeviceFromFuotaTaskRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.DisassociateWirelessDeviceFromFuotaTaskRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateWirelessDeviceFromMulticastGroupRequest:
    boto3_raw_data: (
        "type_defs.DisassociateWirelessDeviceFromMulticastGroupRequestTypeDef"
    ) = dataclasses.field()

    Id = field("Id")
    WirelessDeviceId = field("WirelessDeviceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateWirelessDeviceFromMulticastGroupRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.DisassociateWirelessDeviceFromMulticastGroupRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateWirelessDeviceFromThingRequest:
    boto3_raw_data: "type_defs.DisassociateWirelessDeviceFromThingRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateWirelessDeviceFromThingRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateWirelessDeviceFromThingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateWirelessGatewayFromCertificateRequest:
    boto3_raw_data: (
        "type_defs.DisassociateWirelessGatewayFromCertificateRequestTypeDef"
    ) = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateWirelessGatewayFromCertificateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.DisassociateWirelessGatewayFromCertificateRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateWirelessGatewayFromThingRequest:
    boto3_raw_data: "type_defs.DisassociateWirelessGatewayFromThingRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateWirelessGatewayFromThingRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateWirelessGatewayFromThingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Positioning:
    boto3_raw_data: "type_defs.PositioningTypeDef" = dataclasses.field()

    ClockSync = field("ClockSync")
    Stream = field("Stream")
    Gnss = field("Gnss")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PositioningTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PositioningTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FuotaTaskEventLogOption:
    boto3_raw_data: "type_defs.FuotaTaskEventLogOptionTypeDef" = dataclasses.field()

    Event = field("Event")
    LogLevel = field("LogLevel")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FuotaTaskEventLogOptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FuotaTaskEventLogOptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FuotaTask:
    boto3_raw_data: "type_defs.FuotaTaskTypeDef" = dataclasses.field()

    Id = field("Id")
    Arn = field("Arn")
    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FuotaTaskTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FuotaTaskTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GatewayListItem:
    boto3_raw_data: "type_defs.GatewayListItemTypeDef" = dataclasses.field()

    GatewayId = field("GatewayId")
    DownlinkFrequency = field("DownlinkFrequency")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GatewayListItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GatewayListItemTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDestinationRequest:
    boto3_raw_data: "type_defs.GetDestinationRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDestinationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDestinationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeviceProfileRequest:
    boto3_raw_data: "type_defs.GetDeviceProfileRequestTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDeviceProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeviceProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoRaWANDeviceProfileOutput:
    boto3_raw_data: "type_defs.LoRaWANDeviceProfileOutputTypeDef" = dataclasses.field()

    SupportsClassB = field("SupportsClassB")
    ClassBTimeout = field("ClassBTimeout")
    PingSlotPeriod = field("PingSlotPeriod")
    PingSlotDr = field("PingSlotDr")
    PingSlotFreq = field("PingSlotFreq")
    SupportsClassC = field("SupportsClassC")
    ClassCTimeout = field("ClassCTimeout")
    MacVersion = field("MacVersion")
    RegParamsRevision = field("RegParamsRevision")
    RxDelay1 = field("RxDelay1")
    RxDrOffset1 = field("RxDrOffset1")
    RxDataRate2 = field("RxDataRate2")
    RxFreq2 = field("RxFreq2")
    FactoryPresetFreqsList = field("FactoryPresetFreqsList")
    MaxEirp = field("MaxEirp")
    MaxDutyCycle = field("MaxDutyCycle")
    RfRegion = field("RfRegion")
    SupportsJoin = field("SupportsJoin")
    Supports32BitFCnt = field("Supports32BitFCnt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LoRaWANDeviceProfileOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoRaWANDeviceProfileOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFuotaTaskRequest:
    boto3_raw_data: "type_defs.GetFuotaTaskRequestTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFuotaTaskRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFuotaTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoRaWANFuotaTaskGetInfo:
    boto3_raw_data: "type_defs.LoRaWANFuotaTaskGetInfoTypeDef" = dataclasses.field()

    RfRegion = field("RfRegion")
    StartTime = field("StartTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LoRaWANFuotaTaskGetInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoRaWANFuotaTaskGetInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SummaryMetricConfiguration:
    boto3_raw_data: "type_defs.SummaryMetricConfigurationTypeDef" = dataclasses.field()

    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SummaryMetricConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SummaryMetricConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMulticastGroupRequest:
    boto3_raw_data: "type_defs.GetMulticastGroupRequestTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMulticastGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMulticastGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMulticastGroupSessionRequest:
    boto3_raw_data: "type_defs.GetMulticastGroupSessionRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetMulticastGroupSessionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMulticastGroupSessionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoRaWANMulticastSessionOutput:
    boto3_raw_data: "type_defs.LoRaWANMulticastSessionOutputTypeDef" = (
        dataclasses.field()
    )

    DlDr = field("DlDr")
    DlFreq = field("DlFreq")
    SessionStartTime = field("SessionStartTime")
    SessionTimeout = field("SessionTimeout")
    PingSlotPeriod = field("PingSlotPeriod")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.LoRaWANMulticastSessionOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoRaWANMulticastSessionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetNetworkAnalyzerConfigurationRequest:
    boto3_raw_data: "type_defs.GetNetworkAnalyzerConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationName = field("ConfigurationName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetNetworkAnalyzerConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetNetworkAnalyzerConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPartnerAccountRequest:
    boto3_raw_data: "type_defs.GetPartnerAccountRequestTypeDef" = dataclasses.field()

    PartnerAccountId = field("PartnerAccountId")
    PartnerType = field("PartnerType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPartnerAccountRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPartnerAccountRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SidewalkAccountInfoWithFingerprint:
    boto3_raw_data: "type_defs.SidewalkAccountInfoWithFingerprintTypeDef" = (
        dataclasses.field()
    )

    AmazonId = field("AmazonId")
    Fingerprint = field("Fingerprint")
    Arn = field("Arn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SidewalkAccountInfoWithFingerprintTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SidewalkAccountInfoWithFingerprintTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPositionConfigurationRequest:
    boto3_raw_data: "type_defs.GetPositionConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceIdentifier = field("ResourceIdentifier")
    ResourceType = field("ResourceType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetPositionConfigurationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPositionConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Gnss:
    boto3_raw_data: "type_defs.GnssTypeDef" = dataclasses.field()

    Payload = field("Payload")
    CaptureTime = field("CaptureTime")
    CaptureTimeAccuracy = field("CaptureTimeAccuracy")
    AssistPosition = field("AssistPosition")
    AssistAltitude = field("AssistAltitude")
    Use2DSolver = field("Use2DSolver")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GnssTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GnssTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Ip:
    boto3_raw_data: "type_defs.IpTypeDef" = dataclasses.field()

    IpAddress = field("IpAddress")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IpTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IpTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WiFiAccessPoint:
    boto3_raw_data: "type_defs.WiFiAccessPointTypeDef" = dataclasses.field()

    MacAddress = field("MacAddress")
    Rss = field("Rss")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WiFiAccessPointTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WiFiAccessPointTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPositionRequest:
    boto3_raw_data: "type_defs.GetPositionRequestTypeDef" = dataclasses.field()

    ResourceIdentifier = field("ResourceIdentifier")
    ResourceType = field("ResourceType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPositionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPositionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourceEventConfigurationRequest:
    boto3_raw_data: "type_defs.GetResourceEventConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    Identifier = field("Identifier")
    IdentifierType = field("IdentifierType")
    PartnerType = field("PartnerType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetResourceEventConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourceEventConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourceLogLevelRequest:
    boto3_raw_data: "type_defs.GetResourceLogLevelRequestTypeDef" = dataclasses.field()

    ResourceIdentifier = field("ResourceIdentifier")
    ResourceType = field("ResourceType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourceLogLevelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourceLogLevelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourcePositionRequest:
    boto3_raw_data: "type_defs.GetResourcePositionRequestTypeDef" = dataclasses.field()

    ResourceIdentifier = field("ResourceIdentifier")
    ResourceType = field("ResourceType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourcePositionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourcePositionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceEndpointRequest:
    boto3_raw_data: "type_defs.GetServiceEndpointRequestTypeDef" = dataclasses.field()

    ServiceType = field("ServiceType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetServiceEndpointRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServiceEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceProfileRequest:
    boto3_raw_data: "type_defs.GetServiceProfileRequestTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetServiceProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServiceProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoRaWANGetServiceProfileInfo:
    boto3_raw_data: "type_defs.LoRaWANGetServiceProfileInfoTypeDef" = (
        dataclasses.field()
    )

    UlRate = field("UlRate")
    UlBucketSize = field("UlBucketSize")
    UlRatePolicy = field("UlRatePolicy")
    DlRate = field("DlRate")
    DlBucketSize = field("DlBucketSize")
    DlRatePolicy = field("DlRatePolicy")
    AddGwMetadata = field("AddGwMetadata")
    DevStatusReqFreq = field("DevStatusReqFreq")
    ReportDevStatusBattery = field("ReportDevStatusBattery")
    ReportDevStatusMargin = field("ReportDevStatusMargin")
    DrMin = field("DrMin")
    DrMax = field("DrMax")
    ChannelMask = field("ChannelMask")
    PrAllowed = field("PrAllowed")
    HrAllowed = field("HrAllowed")
    RaAllowed = field("RaAllowed")
    NwkGeoLoc = field("NwkGeoLoc")
    TargetPer = field("TargetPer")
    MinGwDiversity = field("MinGwDiversity")
    TxPowerIndexMin = field("TxPowerIndexMin")
    TxPowerIndexMax = field("TxPowerIndexMax")
    NbTransMin = field("NbTransMin")
    NbTransMax = field("NbTransMax")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LoRaWANGetServiceProfileInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoRaWANGetServiceProfileInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWirelessDeviceImportTaskRequest:
    boto3_raw_data: "type_defs.GetWirelessDeviceImportTaskRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetWirelessDeviceImportTaskRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWirelessDeviceImportTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SidewalkGetStartImportInfo:
    boto3_raw_data: "type_defs.SidewalkGetStartImportInfoTypeDef" = dataclasses.field()

    DeviceCreationFileList = field("DeviceCreationFileList")
    Role = field("Role")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SidewalkGetStartImportInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SidewalkGetStartImportInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWirelessDeviceRequest:
    boto3_raw_data: "type_defs.GetWirelessDeviceRequestTypeDef" = dataclasses.field()

    Identifier = field("Identifier")
    IdentifierType = field("IdentifierType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetWirelessDeviceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWirelessDeviceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWirelessDeviceStatisticsRequest:
    boto3_raw_data: "type_defs.GetWirelessDeviceStatisticsRequestTypeDef" = (
        dataclasses.field()
    )

    WirelessDeviceId = field("WirelessDeviceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetWirelessDeviceStatisticsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWirelessDeviceStatisticsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SidewalkDeviceMetadata:
    boto3_raw_data: "type_defs.SidewalkDeviceMetadataTypeDef" = dataclasses.field()

    Rssi = field("Rssi")
    BatteryLevel = field("BatteryLevel")
    Event = field("Event")
    DeviceState = field("DeviceState")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SidewalkDeviceMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SidewalkDeviceMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWirelessGatewayCertificateRequest:
    boto3_raw_data: "type_defs.GetWirelessGatewayCertificateRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetWirelessGatewayCertificateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWirelessGatewayCertificateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWirelessGatewayFirmwareInformationRequest:
    boto3_raw_data: "type_defs.GetWirelessGatewayFirmwareInformationRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetWirelessGatewayFirmwareInformationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWirelessGatewayFirmwareInformationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWirelessGatewayRequest:
    boto3_raw_data: "type_defs.GetWirelessGatewayRequestTypeDef" = dataclasses.field()

    Identifier = field("Identifier")
    IdentifierType = field("IdentifierType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetWirelessGatewayRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWirelessGatewayRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWirelessGatewayStatisticsRequest:
    boto3_raw_data: "type_defs.GetWirelessGatewayStatisticsRequestTypeDef" = (
        dataclasses.field()
    )

    WirelessGatewayId = field("WirelessGatewayId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetWirelessGatewayStatisticsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWirelessGatewayStatisticsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWirelessGatewayTaskDefinitionRequest:
    boto3_raw_data: "type_defs.GetWirelessGatewayTaskDefinitionRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetWirelessGatewayTaskDefinitionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWirelessGatewayTaskDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWirelessGatewayTaskRequest:
    boto3_raw_data: "type_defs.GetWirelessGatewayTaskRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetWirelessGatewayTaskRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWirelessGatewayTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GlobalIdentity:
    boto3_raw_data: "type_defs.GlobalIdentityTypeDef" = dataclasses.field()

    Lac = field("Lac")
    GeranCid = field("GeranCid")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GlobalIdentityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GlobalIdentityTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GsmLocalId:
    boto3_raw_data: "type_defs.GsmLocalIdTypeDef" = dataclasses.field()

    Bsic = field("Bsic")
    Bcch = field("Bcch")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GsmLocalIdTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GsmLocalIdTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportedSidewalkDevice:
    boto3_raw_data: "type_defs.ImportedSidewalkDeviceTypeDef" = dataclasses.field()

    SidewalkManufacturingSn = field("SidewalkManufacturingSn")
    OnboardingStatus = field("OnboardingStatus")
    OnboardingStatusReason = field("OnboardingStatusReason")
    LastUpdateTime = field("LastUpdateTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportedSidewalkDeviceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportedSidewalkDeviceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoRaWANJoinEventNotificationConfigurations:
    boto3_raw_data: "type_defs.LoRaWANJoinEventNotificationConfigurationsTypeDef" = (
        dataclasses.field()
    )

    DevEuiEventTopic = field("DevEuiEventTopic")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LoRaWANJoinEventNotificationConfigurationsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoRaWANJoinEventNotificationConfigurationsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoRaWANJoinResourceTypeEventConfiguration:
    boto3_raw_data: "type_defs.LoRaWANJoinResourceTypeEventConfigurationTypeDef" = (
        dataclasses.field()
    )

    WirelessDeviceEventTopic = field("WirelessDeviceEventTopic")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LoRaWANJoinResourceTypeEventConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoRaWANJoinResourceTypeEventConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDestinationsRequest:
    boto3_raw_data: "type_defs.ListDestinationsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDestinationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDestinationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDeviceProfilesRequest:
    boto3_raw_data: "type_defs.ListDeviceProfilesRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    DeviceProfileType = field("DeviceProfileType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDeviceProfilesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDeviceProfilesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDevicesForWirelessDeviceImportTaskRequest:
    boto3_raw_data: "type_defs.ListDevicesForWirelessDeviceImportTaskRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    Status = field("Status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDevicesForWirelessDeviceImportTaskRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDevicesForWirelessDeviceImportTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEventConfigurationsRequest:
    boto3_raw_data: "type_defs.ListEventConfigurationsRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceType = field("ResourceType")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListEventConfigurationsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEventConfigurationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFuotaTasksRequest:
    boto3_raw_data: "type_defs.ListFuotaTasksRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFuotaTasksRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFuotaTasksRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMulticastGroupsByFuotaTaskRequest:
    boto3_raw_data: "type_defs.ListMulticastGroupsByFuotaTaskRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListMulticastGroupsByFuotaTaskRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMulticastGroupsByFuotaTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MulticastGroupByFuotaTask:
    boto3_raw_data: "type_defs.MulticastGroupByFuotaTaskTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MulticastGroupByFuotaTaskTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MulticastGroupByFuotaTaskTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMulticastGroupsRequest:
    boto3_raw_data: "type_defs.ListMulticastGroupsRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMulticastGroupsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMulticastGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MulticastGroup:
    boto3_raw_data: "type_defs.MulticastGroupTypeDef" = dataclasses.field()

    Id = field("Id")
    Arn = field("Arn")
    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MulticastGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MulticastGroupTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNetworkAnalyzerConfigurationsRequest:
    boto3_raw_data: "type_defs.ListNetworkAnalyzerConfigurationsRequestTypeDef" = (
        dataclasses.field()
    )

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListNetworkAnalyzerConfigurationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNetworkAnalyzerConfigurationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkAnalyzerConfigurations:
    boto3_raw_data: "type_defs.NetworkAnalyzerConfigurationsTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    Name = field("Name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.NetworkAnalyzerConfigurationsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkAnalyzerConfigurationsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPartnerAccountsRequest:
    boto3_raw_data: "type_defs.ListPartnerAccountsRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPartnerAccountsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPartnerAccountsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPositionConfigurationsRequest:
    boto3_raw_data: "type_defs.ListPositionConfigurationsRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceType = field("ResourceType")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPositionConfigurationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPositionConfigurationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQueuedMessagesRequest:
    boto3_raw_data: "type_defs.ListQueuedMessagesRequestTypeDef" = dataclasses.field()

    Id = field("Id")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    WirelessDeviceType = field("WirelessDeviceType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListQueuedMessagesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQueuedMessagesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceProfilesRequest:
    boto3_raw_data: "type_defs.ListServiceProfilesRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListServiceProfilesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServiceProfilesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceProfile:
    boto3_raw_data: "type_defs.ServiceProfileTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Name = field("Name")
    Id = field("Id")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServiceProfileTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ServiceProfileTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceRequest:
    boto3_raw_data: "type_defs.ListTagsForResourceRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWirelessDeviceImportTasksRequest:
    boto3_raw_data: "type_defs.ListWirelessDeviceImportTasksRequestTypeDef" = (
        dataclasses.field()
    )

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListWirelessDeviceImportTasksRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWirelessDeviceImportTasksRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWirelessDevicesRequest:
    boto3_raw_data: "type_defs.ListWirelessDevicesRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    DestinationName = field("DestinationName")
    DeviceProfileId = field("DeviceProfileId")
    ServiceProfileId = field("ServiceProfileId")
    WirelessDeviceType = field("WirelessDeviceType")
    FuotaTaskId = field("FuotaTaskId")
    MulticastGroupId = field("MulticastGroupId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWirelessDevicesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWirelessDevicesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWirelessGatewayTaskDefinitionsRequest:
    boto3_raw_data: "type_defs.ListWirelessGatewayTaskDefinitionsRequestTypeDef" = (
        dataclasses.field()
    )

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    TaskDefinitionType = field("TaskDefinitionType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListWirelessGatewayTaskDefinitionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWirelessGatewayTaskDefinitionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWirelessGatewaysRequest:
    boto3_raw_data: "type_defs.ListWirelessGatewaysRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWirelessGatewaysRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWirelessGatewaysRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoRaWANGatewayMetadata:
    boto3_raw_data: "type_defs.LoRaWANGatewayMetadataTypeDef" = dataclasses.field()

    GatewayEui = field("GatewayEui")
    Snr = field("Snr")
    Rssi = field("Rssi")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LoRaWANGatewayMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoRaWANGatewayMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoRaWANPublicGatewayMetadata:
    boto3_raw_data: "type_defs.LoRaWANPublicGatewayMetadataTypeDef" = (
        dataclasses.field()
    )

    ProviderNetId = field("ProviderNetId")
    Id = field("Id")
    Rssi = field("Rssi")
    Snr = field("Snr")
    RfRegion = field("RfRegion")
    DlAllowed = field("DlAllowed")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LoRaWANPublicGatewayMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoRaWANPublicGatewayMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OtaaV10X:
    boto3_raw_data: "type_defs.OtaaV10XTypeDef" = dataclasses.field()

    AppKey = field("AppKey")
    AppEui = field("AppEui")
    JoinEui = field("JoinEui")
    GenAppKey = field("GenAppKey")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OtaaV10XTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OtaaV10XTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OtaaV11:
    boto3_raw_data: "type_defs.OtaaV11TypeDef" = dataclasses.field()

    AppKey = field("AppKey")
    NwkKey = field("NwkKey")
    JoinEui = field("JoinEui")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OtaaV11TypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OtaaV11TypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoRaWANDeviceProfile:
    boto3_raw_data: "type_defs.LoRaWANDeviceProfileTypeDef" = dataclasses.field()

    SupportsClassB = field("SupportsClassB")
    ClassBTimeout = field("ClassBTimeout")
    PingSlotPeriod = field("PingSlotPeriod")
    PingSlotDr = field("PingSlotDr")
    PingSlotFreq = field("PingSlotFreq")
    SupportsClassC = field("SupportsClassC")
    ClassCTimeout = field("ClassCTimeout")
    MacVersion = field("MacVersion")
    RegParamsRevision = field("RegParamsRevision")
    RxDelay1 = field("RxDelay1")
    RxDrOffset1 = field("RxDrOffset1")
    RxDataRate2 = field("RxDataRate2")
    RxFreq2 = field("RxFreq2")
    FactoryPresetFreqsList = field("FactoryPresetFreqsList")
    MaxEirp = field("MaxEirp")
    MaxDutyCycle = field("MaxDutyCycle")
    RfRegion = field("RfRegion")
    SupportsJoin = field("SupportsJoin")
    Supports32BitFCnt = field("Supports32BitFCnt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LoRaWANDeviceProfileTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoRaWANDeviceProfileTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoRaWANGatewayVersion:
    boto3_raw_data: "type_defs.LoRaWANGatewayVersionTypeDef" = dataclasses.field()

    PackageVersion = field("PackageVersion")
    Model = field("Model")
    Station = field("Station")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LoRaWANGatewayVersionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoRaWANGatewayVersionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoRaWANListDevice:
    boto3_raw_data: "type_defs.LoRaWANListDeviceTypeDef" = dataclasses.field()

    DevEui = field("DevEui")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LoRaWANListDeviceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoRaWANListDeviceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParticipatingGatewaysMulticastOutput:
    boto3_raw_data: "type_defs.ParticipatingGatewaysMulticastOutputTypeDef" = (
        dataclasses.field()
    )

    GatewayList = field("GatewayList")
    TransmissionInterval = field("TransmissionInterval")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ParticipatingGatewaysMulticastOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParticipatingGatewaysMulticastOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoRaWANMulticastMetadata:
    boto3_raw_data: "type_defs.LoRaWANMulticastMetadataTypeDef" = dataclasses.field()

    FPort = field("FPort")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LoRaWANMulticastMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoRaWANMulticastMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAbpV10X:
    boto3_raw_data: "type_defs.UpdateAbpV10XTypeDef" = dataclasses.field()

    FCntStart = field("FCntStart")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateAbpV10XTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UpdateAbpV10XTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAbpV11:
    boto3_raw_data: "type_defs.UpdateAbpV11TypeDef" = dataclasses.field()

    FCntStart = field("FCntStart")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateAbpV11TypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UpdateAbpV11TypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LteLocalId:
    boto3_raw_data: "type_defs.LteLocalIdTypeDef" = dataclasses.field()

    Pci = field("Pci")
    Earfcn = field("Earfcn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LteLocalIdTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LteLocalIdTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LteNmrObj:
    boto3_raw_data: "type_defs.LteNmrObjTypeDef" = dataclasses.field()

    Pci = field("Pci")
    Earfcn = field("Earfcn")
    EutranCid = field("EutranCid")
    Rsrp = field("Rsrp")
    Rsrq = field("Rsrq")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LteNmrObjTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LteNmrObjTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricQueryValue:
    boto3_raw_data: "type_defs.MetricQueryValueTypeDef" = dataclasses.field()

    Min = field("Min")
    Max = field("Max")
    Sum = field("Sum")
    Avg = field("Avg")
    Std = field("Std")
    P90 = field("P90")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricQueryValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricQueryValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParticipatingGatewaysMulticast:
    boto3_raw_data: "type_defs.ParticipatingGatewaysMulticastTypeDef" = (
        dataclasses.field()
    )

    GatewayList = field("GatewayList")
    TransmissionInterval = field("TransmissionInterval")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ParticipatingGatewaysMulticastTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParticipatingGatewaysMulticastTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SemtechGnssConfiguration:
    boto3_raw_data: "type_defs.SemtechGnssConfigurationTypeDef" = dataclasses.field()

    Status = field("Status")
    Fec = field("Fec")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SemtechGnssConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SemtechGnssConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SemtechGnssDetail:
    boto3_raw_data: "type_defs.SemtechGnssDetailTypeDef" = dataclasses.field()

    Provider = field("Provider")
    Type = field("Type")
    Status = field("Status")
    Fec = field("Fec")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SemtechGnssDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SemtechGnssDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutResourceLogLevelRequest:
    boto3_raw_data: "type_defs.PutResourceLogLevelRequestTypeDef" = dataclasses.field()

    ResourceIdentifier = field("ResourceIdentifier")
    ResourceType = field("ResourceType")
    LogLevel = field("LogLevel")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutResourceLogLevelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutResourceLogLevelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResetResourceLogLevelRequest:
    boto3_raw_data: "type_defs.ResetResourceLogLevelRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceIdentifier = field("ResourceIdentifier")
    ResourceType = field("ResourceType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResetResourceLogLevelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResetResourceLogLevelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SidewalkSendDataToDevice:
    boto3_raw_data: "type_defs.SidewalkSendDataToDeviceTypeDef" = dataclasses.field()

    Seq = field("Seq")
    MessageType = field("MessageType")
    AckModeRetryDurationSecs = field("AckModeRetryDurationSecs")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SidewalkSendDataToDeviceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SidewalkSendDataToDeviceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SidewalkSingleStartImportInfo:
    boto3_raw_data: "type_defs.SidewalkSingleStartImportInfoTypeDef" = (
        dataclasses.field()
    )

    SidewalkManufacturingSn = field("SidewalkManufacturingSn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SidewalkSingleStartImportInfoTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SidewalkSingleStartImportInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SidewalkStartImportInfo:
    boto3_raw_data: "type_defs.SidewalkStartImportInfoTypeDef" = dataclasses.field()

    DeviceCreationFile = field("DeviceCreationFile")
    Role = field("Role")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SidewalkStartImportInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SidewalkStartImportInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SidewalkUpdateAccount:
    boto3_raw_data: "type_defs.SidewalkUpdateAccountTypeDef" = dataclasses.field()

    AppServerPrivateKey = field("AppServerPrivateKey")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SidewalkUpdateAccountTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SidewalkUpdateAccountTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SidewalkUpdateImportInfo:
    boto3_raw_data: "type_defs.SidewalkUpdateImportInfoTypeDef" = dataclasses.field()

    DeviceCreationFile = field("DeviceCreationFile")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SidewalkUpdateImportInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SidewalkUpdateImportInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TdscdmaLocalId:
    boto3_raw_data: "type_defs.TdscdmaLocalIdTypeDef" = dataclasses.field()

    Uarfcn = field("Uarfcn")
    CellParams = field("CellParams")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TdscdmaLocalIdTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TdscdmaLocalIdTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TdscdmaNmrObj:
    boto3_raw_data: "type_defs.TdscdmaNmrObjTypeDef" = dataclasses.field()

    Uarfcn = field("Uarfcn")
    CellParams = field("CellParams")
    UtranCid = field("UtranCid")
    Rscp = field("Rscp")
    PathLoss = field("PathLoss")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TdscdmaNmrObjTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TdscdmaNmrObjTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestWirelessDeviceRequest:
    boto3_raw_data: "type_defs.TestWirelessDeviceRequestTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestWirelessDeviceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestWirelessDeviceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagResourceRequest:
    boto3_raw_data: "type_defs.UntagResourceRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    TagKeys = field("TagKeys")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UntagResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UntagResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDestinationRequest:
    boto3_raw_data: "type_defs.UpdateDestinationRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    ExpressionType = field("ExpressionType")
    Expression = field("Expression")
    Description = field("Description")
    RoleArn = field("RoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDestinationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDestinationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePositionRequest:
    boto3_raw_data: "type_defs.UpdatePositionRequestTypeDef" = dataclasses.field()

    ResourceIdentifier = field("ResourceIdentifier")
    ResourceType = field("ResourceType")
    Position = field("Position")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePositionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePositionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWirelessGatewayRequest:
    boto3_raw_data: "type_defs.UpdateWirelessGatewayRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    Name = field("Name")
    Description = field("Description")
    JoinEuiFilters = field("JoinEuiFilters")
    NetIdFilters = field("NetIdFilters")
    MaxEirp = field("MaxEirp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateWirelessGatewayRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWirelessGatewayRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WcdmaLocalId:
    boto3_raw_data: "type_defs.WcdmaLocalIdTypeDef" = dataclasses.field()

    Uarfcndl = field("Uarfcndl")
    Psc = field("Psc")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WcdmaLocalIdTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WcdmaLocalIdTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WcdmaNmrObj:
    boto3_raw_data: "type_defs.WcdmaNmrObjTypeDef" = dataclasses.field()

    Uarfcndl = field("Uarfcndl")
    Psc = field("Psc")
    UtranCid = field("UtranCid")
    Rscp = field("Rscp")
    PathLoss = field("PathLoss")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WcdmaNmrObjTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WcdmaNmrObjTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WirelessDeviceEventLogOption:
    boto3_raw_data: "type_defs.WirelessDeviceEventLogOptionTypeDef" = (
        dataclasses.field()
    )

    Event = field("Event")
    LogLevel = field("LogLevel")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WirelessDeviceEventLogOptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WirelessDeviceEventLogOptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WirelessGatewayEventLogOption:
    boto3_raw_data: "type_defs.WirelessGatewayEventLogOptionTypeDef" = (
        dataclasses.field()
    )

    Event = field("Event")
    LogLevel = field("LogLevel")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.WirelessGatewayEventLogOptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WirelessGatewayEventLogOptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AbpV10X:
    boto3_raw_data: "type_defs.AbpV10XTypeDef" = dataclasses.field()

    DevAddr = field("DevAddr")

    @cached_property
    def SessionKeys(self):  # pragma: no cover
        return SessionKeysAbpV10X.make_one(self.boto3_raw_data["SessionKeys"])

    FCntStart = field("FCntStart")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AbpV10XTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AbpV10XTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AbpV11:
    boto3_raw_data: "type_defs.AbpV11TypeDef" = dataclasses.field()

    DevAddr = field("DevAddr")

    @cached_property
    def SessionKeys(self):  # pragma: no cover
        return SessionKeysAbpV11.make_one(self.boto3_raw_data["SessionKeys"])

    FCntStart = field("FCntStart")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AbpV11TypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AbpV11TypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateAwsAccountWithPartnerAccountRequest:
    boto3_raw_data: "type_defs.AssociateAwsAccountWithPartnerAccountRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Sidewalk(self):  # pragma: no cover
        return SidewalkAccountInfo.make_one(self.boto3_raw_data["Sidewalk"])

    ClientRequestToken = field("ClientRequestToken")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateAwsAccountWithPartnerAccountRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateAwsAccountWithPartnerAccountRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDestinationRequest:
    boto3_raw_data: "type_defs.CreateDestinationRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    ExpressionType = field("ExpressionType")
    Expression = field("Expression")
    RoleArn = field("RoleArn")
    Description = field("Description")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDestinationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDestinationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartBulkAssociateWirelessDeviceWithMulticastGroupRequest:
    boto3_raw_data: (
        "type_defs.StartBulkAssociateWirelessDeviceWithMulticastGroupRequestTypeDef"
    ) = dataclasses.field()

    Id = field("Id")
    QueryString = field("QueryString")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartBulkAssociateWirelessDeviceWithMulticastGroupRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.StartBulkAssociateWirelessDeviceWithMulticastGroupRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartBulkDisassociateWirelessDeviceFromMulticastGroupRequest:
    boto3_raw_data: (
        "type_defs.StartBulkDisassociateWirelessDeviceFromMulticastGroupRequestTypeDef"
    ) = dataclasses.field()

    Id = field("Id")
    QueryString = field("QueryString")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartBulkDisassociateWirelessDeviceFromMulticastGroupRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.StartBulkDisassociateWirelessDeviceFromMulticastGroupRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagResourceRequest:
    boto3_raw_data: "type_defs.TagResourceRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TagResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateAwsAccountWithPartnerAccountResponse:
    boto3_raw_data: "type_defs.AssociateAwsAccountWithPartnerAccountResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Sidewalk(self):  # pragma: no cover
        return SidewalkAccountInfo.make_one(self.boto3_raw_data["Sidewalk"])

    Arn = field("Arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateAwsAccountWithPartnerAccountResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateAwsAccountWithPartnerAccountResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateWirelessGatewayWithCertificateResponse:
    boto3_raw_data: (
        "type_defs.AssociateWirelessGatewayWithCertificateResponseTypeDef"
    ) = dataclasses.field()

    IotCertificateId = field("IotCertificateId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateWirelessGatewayWithCertificateResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.AssociateWirelessGatewayWithCertificateResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDestinationResponse:
    boto3_raw_data: "type_defs.CreateDestinationResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Name = field("Name")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDestinationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDestinationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDeviceProfileResponse:
    boto3_raw_data: "type_defs.CreateDeviceProfileResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Id = field("Id")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDeviceProfileResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDeviceProfileResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFuotaTaskResponse:
    boto3_raw_data: "type_defs.CreateFuotaTaskResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Id = field("Id")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFuotaTaskResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFuotaTaskResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMulticastGroupResponse:
    boto3_raw_data: "type_defs.CreateMulticastGroupResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    Id = field("Id")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateMulticastGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMulticastGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateNetworkAnalyzerConfigurationResponse:
    boto3_raw_data: "type_defs.CreateNetworkAnalyzerConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    Name = field("Name")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateNetworkAnalyzerConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateNetworkAnalyzerConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateServiceProfileResponse:
    boto3_raw_data: "type_defs.CreateServiceProfileResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    Id = field("Id")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateServiceProfileResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateServiceProfileResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWirelessDeviceResponse:
    boto3_raw_data: "type_defs.CreateWirelessDeviceResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    Id = field("Id")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWirelessDeviceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWirelessDeviceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWirelessGatewayResponse:
    boto3_raw_data: "type_defs.CreateWirelessGatewayResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    Id = field("Id")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateWirelessGatewayResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWirelessGatewayResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWirelessGatewayTaskDefinitionResponse:
    boto3_raw_data: "type_defs.CreateWirelessGatewayTaskDefinitionResponseTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    Arn = field("Arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateWirelessGatewayTaskDefinitionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWirelessGatewayTaskDefinitionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWirelessGatewayTaskResponse:
    boto3_raw_data: "type_defs.CreateWirelessGatewayTaskResponseTypeDef" = (
        dataclasses.field()
    )

    WirelessGatewayTaskDefinitionId = field("WirelessGatewayTaskDefinitionId")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateWirelessGatewayTaskResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWirelessGatewayTaskResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDestinationResponse:
    boto3_raw_data: "type_defs.GetDestinationResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Name = field("Name")
    Expression = field("Expression")
    ExpressionType = field("ExpressionType")
    Description = field("Description")
    RoleArn = field("RoleArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDestinationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDestinationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPositionEstimateResponse:
    boto3_raw_data: "type_defs.GetPositionEstimateResponseTypeDef" = dataclasses.field()

    GeoJsonPayload = field("GeoJsonPayload")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPositionEstimateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPositionEstimateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPositionResponse:
    boto3_raw_data: "type_defs.GetPositionResponseTypeDef" = dataclasses.field()

    Position = field("Position")

    @cached_property
    def Accuracy(self):  # pragma: no cover
        return Accuracy.make_one(self.boto3_raw_data["Accuracy"])

    SolverType = field("SolverType")
    SolverProvider = field("SolverProvider")
    SolverVersion = field("SolverVersion")
    Timestamp = field("Timestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPositionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPositionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourceLogLevelResponse:
    boto3_raw_data: "type_defs.GetResourceLogLevelResponseTypeDef" = dataclasses.field()

    LogLevel = field("LogLevel")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourceLogLevelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourceLogLevelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourcePositionResponse:
    boto3_raw_data: "type_defs.GetResourcePositionResponseTypeDef" = dataclasses.field()

    GeoJsonPayload = field("GeoJsonPayload")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourcePositionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourcePositionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceEndpointResponse:
    boto3_raw_data: "type_defs.GetServiceEndpointResponseTypeDef" = dataclasses.field()

    ServiceType = field("ServiceType")
    ServiceEndpoint = field("ServiceEndpoint")
    ServerTrust = field("ServerTrust")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetServiceEndpointResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServiceEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWirelessGatewayCertificateResponse:
    boto3_raw_data: "type_defs.GetWirelessGatewayCertificateResponseTypeDef" = (
        dataclasses.field()
    )

    IotCertificateId = field("IotCertificateId")
    LoRaWANNetworkServerCertificateId = field("LoRaWANNetworkServerCertificateId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetWirelessGatewayCertificateResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWirelessGatewayCertificateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWirelessGatewayStatisticsResponse:
    boto3_raw_data: "type_defs.GetWirelessGatewayStatisticsResponseTypeDef" = (
        dataclasses.field()
    )

    WirelessGatewayId = field("WirelessGatewayId")
    LastUplinkReceivedAt = field("LastUplinkReceivedAt")
    ConnectionStatus = field("ConnectionStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetWirelessGatewayStatisticsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWirelessGatewayStatisticsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWirelessGatewayTaskResponse:
    boto3_raw_data: "type_defs.GetWirelessGatewayTaskResponseTypeDef" = (
        dataclasses.field()
    )

    WirelessGatewayId = field("WirelessGatewayId")
    WirelessGatewayTaskDefinitionId = field("WirelessGatewayTaskDefinitionId")
    LastUplinkReceivedAt = field("LastUplinkReceivedAt")
    TaskCreatedAt = field("TaskCreatedAt")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetWirelessGatewayTaskResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWirelessGatewayTaskResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceResponse:
    boto3_raw_data: "type_defs.ListTagsForResourceResponseTypeDef" = dataclasses.field()

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendDataToMulticastGroupResponse:
    boto3_raw_data: "type_defs.SendDataToMulticastGroupResponseTypeDef" = (
        dataclasses.field()
    )

    MessageId = field("MessageId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SendDataToMulticastGroupResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendDataToMulticastGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendDataToWirelessDeviceResponse:
    boto3_raw_data: "type_defs.SendDataToWirelessDeviceResponseTypeDef" = (
        dataclasses.field()
    )

    MessageId = field("MessageId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SendDataToWirelessDeviceResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendDataToWirelessDeviceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSingleWirelessDeviceImportTaskResponse:
    boto3_raw_data: "type_defs.StartSingleWirelessDeviceImportTaskResponseTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    Arn = field("Arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartSingleWirelessDeviceImportTaskResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSingleWirelessDeviceImportTaskResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartWirelessDeviceImportTaskResponse:
    boto3_raw_data: "type_defs.StartWirelessDeviceImportTaskResponseTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    Arn = field("Arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartWirelessDeviceImportTaskResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartWirelessDeviceImportTaskResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestWirelessDeviceResponse:
    boto3_raw_data: "type_defs.TestWirelessDeviceResponseTypeDef" = dataclasses.field()

    Result = field("Result")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestWirelessDeviceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestWirelessDeviceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoRaWANGatewayOutput:
    boto3_raw_data: "type_defs.LoRaWANGatewayOutputTypeDef" = dataclasses.field()

    GatewayEui = field("GatewayEui")
    RfRegion = field("RfRegion")
    JoinEuiFilters = field("JoinEuiFilters")
    NetIdFilters = field("NetIdFilters")
    SubBands = field("SubBands")

    @cached_property
    def Beaconing(self):  # pragma: no cover
        return BeaconingOutput.make_one(self.boto3_raw_data["Beaconing"])

    MaxEirp = field("MaxEirp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LoRaWANGatewayOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoRaWANGatewayOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoRaWANGateway:
    boto3_raw_data: "type_defs.LoRaWANGatewayTypeDef" = dataclasses.field()

    GatewayEui = field("GatewayEui")
    RfRegion = field("RfRegion")
    JoinEuiFilters = field("JoinEuiFilters")
    NetIdFilters = field("NetIdFilters")
    SubBands = field("SubBands")

    @cached_property
    def Beaconing(self):  # pragma: no cover
        return Beaconing.make_one(self.boto3_raw_data["Beaconing"])

    MaxEirp = field("MaxEirp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LoRaWANGatewayTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LoRaWANGatewayTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateResourcePositionRequest:
    boto3_raw_data: "type_defs.UpdateResourcePositionRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceIdentifier = field("ResourceIdentifier")
    ResourceType = field("ResourceType")
    GeoJsonPayload = field("GeoJsonPayload")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateResourcePositionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateResourcePositionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CdmaObj:
    boto3_raw_data: "type_defs.CdmaObjTypeDef" = dataclasses.field()

    SystemId = field("SystemId")
    NetworkId = field("NetworkId")
    BaseStationId = field("BaseStationId")
    RegistrationZone = field("RegistrationZone")

    @cached_property
    def CdmaLocalId(self):  # pragma: no cover
        return CdmaLocalId.make_one(self.boto3_raw_data["CdmaLocalId"])

    PilotPower = field("PilotPower")
    BaseLat = field("BaseLat")
    BaseLng = field("BaseLng")

    @cached_property
    def CdmaNmr(self):  # pragma: no cover
        return CdmaNmrObj.make_many(self.boto3_raw_data["CdmaNmr"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CdmaObjTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CdmaObjTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SidewalkDevice:
    boto3_raw_data: "type_defs.SidewalkDeviceTypeDef" = dataclasses.field()

    AmazonId = field("AmazonId")
    SidewalkId = field("SidewalkId")
    SidewalkManufacturingSn = field("SidewalkManufacturingSn")

    @cached_property
    def DeviceCertificates(self):  # pragma: no cover
        return CertificateList.make_many(self.boto3_raw_data["DeviceCertificates"])

    @cached_property
    def PrivateKeys(self):  # pragma: no cover
        return CertificateList.make_many(self.boto3_raw_data["PrivateKeys"])

    DeviceProfileId = field("DeviceProfileId")
    CertificateId = field("CertificateId")
    Status = field("Status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SidewalkDeviceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SidewalkDeviceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SidewalkListDevice:
    boto3_raw_data: "type_defs.SidewalkListDeviceTypeDef" = dataclasses.field()

    AmazonId = field("AmazonId")
    SidewalkId = field("SidewalkId")
    SidewalkManufacturingSn = field("SidewalkManufacturingSn")

    @cached_property
    def DeviceCertificates(self):  # pragma: no cover
        return CertificateList.make_many(self.boto3_raw_data["DeviceCertificates"])

    DeviceProfileId = field("DeviceProfileId")
    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SidewalkListDeviceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SidewalkListDeviceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectionStatusEventConfiguration:
    boto3_raw_data: "type_defs.ConnectionStatusEventConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def LoRaWAN(self):  # pragma: no cover
        return LoRaWANConnectionStatusEventNotificationConfigurations.make_one(
            self.boto3_raw_data["LoRaWAN"]
        )

    WirelessGatewayIdEventTopic = field("WirelessGatewayIdEventTopic")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConnectionStatusEventConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectionStatusEventConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectionStatusResourceTypeEventConfiguration:
    boto3_raw_data: (
        "type_defs.ConnectionStatusResourceTypeEventConfigurationTypeDef"
    ) = dataclasses.field()

    @cached_property
    def LoRaWAN(self):  # pragma: no cover
        return LoRaWANConnectionStatusResourceTypeEventConfiguration.make_one(
            self.boto3_raw_data["LoRaWAN"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConnectionStatusResourceTypeEventConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.ConnectionStatusResourceTypeEventConfigurationTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFuotaTaskRequest:
    boto3_raw_data: "type_defs.CreateFuotaTaskRequestTypeDef" = dataclasses.field()

    FirmwareUpdateImage = field("FirmwareUpdateImage")
    FirmwareUpdateRole = field("FirmwareUpdateRole")
    Name = field("Name")
    Description = field("Description")
    ClientRequestToken = field("ClientRequestToken")

    @cached_property
    def LoRaWAN(self):  # pragma: no cover
        return LoRaWANFuotaTask.make_one(self.boto3_raw_data["LoRaWAN"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    RedundancyPercent = field("RedundancyPercent")
    FragmentSizeBytes = field("FragmentSizeBytes")
    FragmentIntervalMS = field("FragmentIntervalMS")
    Descriptor = field("Descriptor")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFuotaTaskRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFuotaTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFuotaTaskRequest:
    boto3_raw_data: "type_defs.UpdateFuotaTaskRequestTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")
    Description = field("Description")

    @cached_property
    def LoRaWAN(self):  # pragma: no cover
        return LoRaWANFuotaTask.make_one(self.boto3_raw_data["LoRaWAN"])

    FirmwareUpdateImage = field("FirmwareUpdateImage")
    FirmwareUpdateRole = field("FirmwareUpdateRole")
    RedundancyPercent = field("RedundancyPercent")
    FragmentSizeBytes = field("FragmentSizeBytes")
    FragmentIntervalMS = field("FragmentIntervalMS")
    Descriptor = field("Descriptor")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFuotaTaskRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFuotaTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateNetworkAnalyzerConfigurationRequest:
    boto3_raw_data: "type_defs.CreateNetworkAnalyzerConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")

    @cached_property
    def TraceContent(self):  # pragma: no cover
        return TraceContent.make_one(self.boto3_raw_data["TraceContent"])

    WirelessDevices = field("WirelessDevices")
    WirelessGateways = field("WirelessGateways")
    Description = field("Description")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    ClientRequestToken = field("ClientRequestToken")
    MulticastGroups = field("MulticastGroups")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateNetworkAnalyzerConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateNetworkAnalyzerConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetNetworkAnalyzerConfigurationResponse:
    boto3_raw_data: "type_defs.GetNetworkAnalyzerConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TraceContent(self):  # pragma: no cover
        return TraceContent.make_one(self.boto3_raw_data["TraceContent"])

    WirelessDevices = field("WirelessDevices")
    WirelessGateways = field("WirelessGateways")
    Description = field("Description")
    Arn = field("Arn")
    Name = field("Name")
    MulticastGroups = field("MulticastGroups")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetNetworkAnalyzerConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetNetworkAnalyzerConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateNetworkAnalyzerConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateNetworkAnalyzerConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationName = field("ConfigurationName")

    @cached_property
    def TraceContent(self):  # pragma: no cover
        return TraceContent.make_one(self.boto3_raw_data["TraceContent"])

    WirelessDevicesToAdd = field("WirelessDevicesToAdd")
    WirelessDevicesToRemove = field("WirelessDevicesToRemove")
    WirelessGatewaysToAdd = field("WirelessGatewaysToAdd")
    WirelessGatewaysToRemove = field("WirelessGatewaysToRemove")
    Description = field("Description")
    MulticastGroupsToAdd = field("MulticastGroupsToAdd")
    MulticastGroupsToRemove = field("MulticastGroupsToRemove")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateNetworkAnalyzerConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateNetworkAnalyzerConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateServiceProfileRequest:
    boto3_raw_data: "type_defs.CreateServiceProfileRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def LoRaWAN(self):  # pragma: no cover
        return LoRaWANServiceProfile.make_one(self.boto3_raw_data["LoRaWAN"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateServiceProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateServiceProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SidewalkGetDeviceProfile:
    boto3_raw_data: "type_defs.SidewalkGetDeviceProfileTypeDef" = dataclasses.field()

    ApplicationServerPublicKey = field("ApplicationServerPublicKey")
    QualificationStatus = field("QualificationStatus")

    @cached_property
    def DakCertificateMetadata(self):  # pragma: no cover
        return DakCertificateMetadata.make_many(
            self.boto3_raw_data["DakCertificateMetadata"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SidewalkGetDeviceProfileTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SidewalkGetDeviceProfileTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDestinationsResponse:
    boto3_raw_data: "type_defs.ListDestinationsResponseTypeDef" = dataclasses.field()

    @cached_property
    def DestinationList(self):  # pragma: no cover
        return Destinations.make_many(self.boto3_raw_data["DestinationList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDestinationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDestinationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDeviceProfilesResponse:
    boto3_raw_data: "type_defs.ListDeviceProfilesResponseTypeDef" = dataclasses.field()

    @cached_property
    def DeviceProfileList(self):  # pragma: no cover
        return DeviceProfile.make_many(self.boto3_raw_data["DeviceProfileList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDeviceProfilesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDeviceProfilesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeviceRegistrationStateEventConfiguration:
    boto3_raw_data: "type_defs.DeviceRegistrationStateEventConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Sidewalk(self):  # pragma: no cover
        return SidewalkEventNotificationConfigurations.make_one(
            self.boto3_raw_data["Sidewalk"]
        )

    WirelessDeviceIdEventTopic = field("WirelessDeviceIdEventTopic")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeviceRegistrationStateEventConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeviceRegistrationStateEventConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MessageDeliveryStatusEventConfiguration:
    boto3_raw_data: "type_defs.MessageDeliveryStatusEventConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Sidewalk(self):  # pragma: no cover
        return SidewalkEventNotificationConfigurations.make_one(
            self.boto3_raw_data["Sidewalk"]
        )

    WirelessDeviceIdEventTopic = field("WirelessDeviceIdEventTopic")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MessageDeliveryStatusEventConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MessageDeliveryStatusEventConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProximityEventConfiguration:
    boto3_raw_data: "type_defs.ProximityEventConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def Sidewalk(self):  # pragma: no cover
        return SidewalkEventNotificationConfigurations.make_one(
            self.boto3_raw_data["Sidewalk"]
        )

    WirelessDeviceIdEventTopic = field("WirelessDeviceIdEventTopic")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProximityEventConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProximityEventConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeviceRegistrationStateResourceTypeEventConfiguration:
    boto3_raw_data: (
        "type_defs.DeviceRegistrationStateResourceTypeEventConfigurationTypeDef"
    ) = dataclasses.field()

    @cached_property
    def Sidewalk(self):  # pragma: no cover
        return SidewalkResourceTypeEventConfiguration.make_one(
            self.boto3_raw_data["Sidewalk"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeviceRegistrationStateResourceTypeEventConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.DeviceRegistrationStateResourceTypeEventConfigurationTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MessageDeliveryStatusResourceTypeEventConfiguration:
    boto3_raw_data: (
        "type_defs.MessageDeliveryStatusResourceTypeEventConfigurationTypeDef"
    ) = dataclasses.field()

    @cached_property
    def Sidewalk(self):  # pragma: no cover
        return SidewalkResourceTypeEventConfiguration.make_one(
            self.boto3_raw_data["Sidewalk"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MessageDeliveryStatusResourceTypeEventConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.MessageDeliveryStatusResourceTypeEventConfigurationTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProximityResourceTypeEventConfiguration:
    boto3_raw_data: "type_defs.ProximityResourceTypeEventConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Sidewalk(self):  # pragma: no cover
        return SidewalkResourceTypeEventConfiguration.make_one(
            self.boto3_raw_data["Sidewalk"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ProximityResourceTypeEventConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProximityResourceTypeEventConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FPortsOutput:
    boto3_raw_data: "type_defs.FPortsOutputTypeDef" = dataclasses.field()

    Fuota = field("Fuota")
    Multicast = field("Multicast")
    ClockSync = field("ClockSync")

    @cached_property
    def Positioning(self):  # pragma: no cover
        return Positioning.make_one(self.boto3_raw_data["Positioning"])

    @cached_property
    def Applications(self):  # pragma: no cover
        return ApplicationConfig.make_many(self.boto3_raw_data["Applications"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FPortsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FPortsOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FPorts:
    boto3_raw_data: "type_defs.FPortsTypeDef" = dataclasses.field()

    Fuota = field("Fuota")
    Multicast = field("Multicast")
    ClockSync = field("ClockSync")

    @cached_property
    def Positioning(self):  # pragma: no cover
        return Positioning.make_one(self.boto3_raw_data["Positioning"])

    @cached_property
    def Applications(self):  # pragma: no cover
        return ApplicationConfig.make_many(self.boto3_raw_data["Applications"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FPortsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FPortsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFPorts:
    boto3_raw_data: "type_defs.UpdateFPortsTypeDef" = dataclasses.field()

    @cached_property
    def Positioning(self):  # pragma: no cover
        return Positioning.make_one(self.boto3_raw_data["Positioning"])

    @cached_property
    def Applications(self):  # pragma: no cover
        return ApplicationConfig.make_many(self.boto3_raw_data["Applications"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateFPortsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UpdateFPortsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FuotaTaskLogOptionOutput:
    boto3_raw_data: "type_defs.FuotaTaskLogOptionOutputTypeDef" = dataclasses.field()

    Type = field("Type")
    LogLevel = field("LogLevel")

    @cached_property
    def Events(self):  # pragma: no cover
        return FuotaTaskEventLogOption.make_many(self.boto3_raw_data["Events"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FuotaTaskLogOptionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FuotaTaskLogOptionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FuotaTaskLogOption:
    boto3_raw_data: "type_defs.FuotaTaskLogOptionTypeDef" = dataclasses.field()

    Type = field("Type")
    LogLevel = field("LogLevel")

    @cached_property
    def Events(self):  # pragma: no cover
        return FuotaTaskEventLogOption.make_many(self.boto3_raw_data["Events"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FuotaTaskLogOptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FuotaTaskLogOptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFuotaTasksResponse:
    boto3_raw_data: "type_defs.ListFuotaTasksResponseTypeDef" = dataclasses.field()

    @cached_property
    def FuotaTaskList(self):  # pragma: no cover
        return FuotaTask.make_many(self.boto3_raw_data["FuotaTaskList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFuotaTasksResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFuotaTasksResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParticipatingGatewaysOutput:
    boto3_raw_data: "type_defs.ParticipatingGatewaysOutputTypeDef" = dataclasses.field()

    DownlinkMode = field("DownlinkMode")

    @cached_property
    def GatewayList(self):  # pragma: no cover
        return GatewayListItem.make_many(self.boto3_raw_data["GatewayList"])

    TransmissionInterval = field("TransmissionInterval")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ParticipatingGatewaysOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParticipatingGatewaysOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParticipatingGateways:
    boto3_raw_data: "type_defs.ParticipatingGatewaysTypeDef" = dataclasses.field()

    DownlinkMode = field("DownlinkMode")

    @cached_property
    def GatewayList(self):  # pragma: no cover
        return GatewayListItem.make_many(self.boto3_raw_data["GatewayList"])

    TransmissionInterval = field("TransmissionInterval")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ParticipatingGatewaysTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParticipatingGatewaysTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFuotaTaskResponse:
    boto3_raw_data: "type_defs.GetFuotaTaskResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Id = field("Id")
    Status = field("Status")
    Name = field("Name")
    Description = field("Description")

    @cached_property
    def LoRaWAN(self):  # pragma: no cover
        return LoRaWANFuotaTaskGetInfo.make_one(self.boto3_raw_data["LoRaWAN"])

    FirmwareUpdateImage = field("FirmwareUpdateImage")
    FirmwareUpdateRole = field("FirmwareUpdateRole")
    CreatedAt = field("CreatedAt")
    RedundancyPercent = field("RedundancyPercent")
    FragmentSizeBytes = field("FragmentSizeBytes")
    FragmentIntervalMS = field("FragmentIntervalMS")
    Descriptor = field("Descriptor")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetFuotaTaskResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFuotaTaskResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMetricConfigurationResponse:
    boto3_raw_data: "type_defs.GetMetricConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SummaryMetric(self):  # pragma: no cover
        return SummaryMetricConfiguration.make_one(self.boto3_raw_data["SummaryMetric"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetMetricConfigurationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMetricConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMetricConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateMetricConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SummaryMetric(self):  # pragma: no cover
        return SummaryMetricConfiguration.make_one(self.boto3_raw_data["SummaryMetric"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateMetricConfigurationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMetricConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMulticastGroupSessionResponse:
    boto3_raw_data: "type_defs.GetMulticastGroupSessionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def LoRaWAN(self):  # pragma: no cover
        return LoRaWANMulticastSessionOutput.make_one(self.boto3_raw_data["LoRaWAN"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetMulticastGroupSessionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMulticastGroupSessionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPartnerAccountResponse:
    boto3_raw_data: "type_defs.GetPartnerAccountResponseTypeDef" = dataclasses.field()

    @cached_property
    def Sidewalk(self):  # pragma: no cover
        return SidewalkAccountInfoWithFingerprint.make_one(
            self.boto3_raw_data["Sidewalk"]
        )

    AccountLinked = field("AccountLinked")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPartnerAccountResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPartnerAccountResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPartnerAccountsResponse:
    boto3_raw_data: "type_defs.ListPartnerAccountsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Sidewalk(self):  # pragma: no cover
        return SidewalkAccountInfoWithFingerprint.make_many(
            self.boto3_raw_data["Sidewalk"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPartnerAccountsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPartnerAccountsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoRaWANMulticastSession:
    boto3_raw_data: "type_defs.LoRaWANMulticastSessionTypeDef" = dataclasses.field()

    DlDr = field("DlDr")
    DlFreq = field("DlFreq")
    SessionStartTime = field("SessionStartTime")
    SessionTimeout = field("SessionTimeout")
    PingSlotPeriod = field("PingSlotPeriod")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LoRaWANMulticastSessionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoRaWANMulticastSessionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoRaWANStartFuotaTask:
    boto3_raw_data: "type_defs.LoRaWANStartFuotaTaskTypeDef" = dataclasses.field()

    StartTime = field("StartTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LoRaWANStartFuotaTaskTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoRaWANStartFuotaTaskTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SummaryMetricQuery:
    boto3_raw_data: "type_defs.SummaryMetricQueryTypeDef" = dataclasses.field()

    QueryId = field("QueryId")
    MetricName = field("MetricName")

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return Dimension.make_many(self.boto3_raw_data["Dimensions"])

    AggregationPeriod = field("AggregationPeriod")
    StartTimestamp = field("StartTimestamp")
    EndTimestamp = field("EndTimestamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SummaryMetricQueryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SummaryMetricQueryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServiceProfileResponse:
    boto3_raw_data: "type_defs.GetServiceProfileResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Name = field("Name")
    Id = field("Id")

    @cached_property
    def LoRaWAN(self):  # pragma: no cover
        return LoRaWANGetServiceProfileInfo.make_one(self.boto3_raw_data["LoRaWAN"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetServiceProfileResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServiceProfileResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWirelessDeviceImportTaskResponse:
    boto3_raw_data: "type_defs.GetWirelessDeviceImportTaskResponseTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    Arn = field("Arn")
    DestinationName = field("DestinationName")

    @cached_property
    def Sidewalk(self):  # pragma: no cover
        return SidewalkGetStartImportInfo.make_one(self.boto3_raw_data["Sidewalk"])

    CreationTime = field("CreationTime")
    Status = field("Status")
    StatusReason = field("StatusReason")
    InitializedImportedDeviceCount = field("InitializedImportedDeviceCount")
    PendingImportedDeviceCount = field("PendingImportedDeviceCount")
    OnboardedImportedDeviceCount = field("OnboardedImportedDeviceCount")
    FailedImportedDeviceCount = field("FailedImportedDeviceCount")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetWirelessDeviceImportTaskResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWirelessDeviceImportTaskResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WirelessDeviceImportTask:
    boto3_raw_data: "type_defs.WirelessDeviceImportTaskTypeDef" = dataclasses.field()

    Id = field("Id")
    Arn = field("Arn")
    DestinationName = field("DestinationName")

    @cached_property
    def Sidewalk(self):  # pragma: no cover
        return SidewalkGetStartImportInfo.make_one(self.boto3_raw_data["Sidewalk"])

    CreationTime = field("CreationTime")
    Status = field("Status")
    StatusReason = field("StatusReason")
    InitializedImportedDeviceCount = field("InitializedImportedDeviceCount")
    PendingImportedDeviceCount = field("PendingImportedDeviceCount")
    OnboardedImportedDeviceCount = field("OnboardedImportedDeviceCount")
    FailedImportedDeviceCount = field("FailedImportedDeviceCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WirelessDeviceImportTaskTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WirelessDeviceImportTaskTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GsmNmrObj:
    boto3_raw_data: "type_defs.GsmNmrObjTypeDef" = dataclasses.field()

    Bsic = field("Bsic")
    Bcch = field("Bcch")
    RxLevel = field("RxLevel")

    @cached_property
    def GlobalIdentity(self):  # pragma: no cover
        return GlobalIdentity.make_one(self.boto3_raw_data["GlobalIdentity"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GsmNmrObjTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GsmNmrObjTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportedWirelessDevice:
    boto3_raw_data: "type_defs.ImportedWirelessDeviceTypeDef" = dataclasses.field()

    @cached_property
    def Sidewalk(self):  # pragma: no cover
        return ImportedSidewalkDevice.make_one(self.boto3_raw_data["Sidewalk"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportedWirelessDeviceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportedWirelessDeviceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JoinEventConfiguration:
    boto3_raw_data: "type_defs.JoinEventConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def LoRaWAN(self):  # pragma: no cover
        return LoRaWANJoinEventNotificationConfigurations.make_one(
            self.boto3_raw_data["LoRaWAN"]
        )

    WirelessDeviceIdEventTopic = field("WirelessDeviceIdEventTopic")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JoinEventConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JoinEventConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JoinResourceTypeEventConfiguration:
    boto3_raw_data: "type_defs.JoinResourceTypeEventConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def LoRaWAN(self):  # pragma: no cover
        return LoRaWANJoinResourceTypeEventConfiguration.make_one(
            self.boto3_raw_data["LoRaWAN"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.JoinResourceTypeEventConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JoinResourceTypeEventConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMulticastGroupsByFuotaTaskResponse:
    boto3_raw_data: "type_defs.ListMulticastGroupsByFuotaTaskResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MulticastGroupList(self):  # pragma: no cover
        return MulticastGroupByFuotaTask.make_many(
            self.boto3_raw_data["MulticastGroupList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListMulticastGroupsByFuotaTaskResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMulticastGroupsByFuotaTaskResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMulticastGroupsResponse:
    boto3_raw_data: "type_defs.ListMulticastGroupsResponseTypeDef" = dataclasses.field()

    @cached_property
    def MulticastGroupList(self):  # pragma: no cover
        return MulticastGroup.make_many(self.boto3_raw_data["MulticastGroupList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMulticastGroupsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMulticastGroupsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNetworkAnalyzerConfigurationsResponse:
    boto3_raw_data: "type_defs.ListNetworkAnalyzerConfigurationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def NetworkAnalyzerConfigurationList(self):  # pragma: no cover
        return NetworkAnalyzerConfigurations.make_many(
            self.boto3_raw_data["NetworkAnalyzerConfigurationList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListNetworkAnalyzerConfigurationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNetworkAnalyzerConfigurationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListServiceProfilesResponse:
    boto3_raw_data: "type_defs.ListServiceProfilesResponseTypeDef" = dataclasses.field()

    @cached_property
    def ServiceProfileList(self):  # pragma: no cover
        return ServiceProfile.make_many(self.boto3_raw_data["ServiceProfileList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListServiceProfilesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListServiceProfilesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoRaWANDeviceMetadata:
    boto3_raw_data: "type_defs.LoRaWANDeviceMetadataTypeDef" = dataclasses.field()

    DevEui = field("DevEui")
    FPort = field("FPort")
    DataRate = field("DataRate")
    Frequency = field("Frequency")
    Timestamp = field("Timestamp")

    @cached_property
    def Gateways(self):  # pragma: no cover
        return LoRaWANGatewayMetadata.make_many(self.boto3_raw_data["Gateways"])

    @cached_property
    def PublicGateways(self):  # pragma: no cover
        return LoRaWANPublicGatewayMetadata.make_many(
            self.boto3_raw_data["PublicGateways"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LoRaWANDeviceMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoRaWANDeviceMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoRaWANGatewayCurrentVersion:
    boto3_raw_data: "type_defs.LoRaWANGatewayCurrentVersionTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CurrentVersion(self):  # pragma: no cover
        return LoRaWANGatewayVersion.make_one(self.boto3_raw_data["CurrentVersion"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LoRaWANGatewayCurrentVersionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoRaWANGatewayCurrentVersionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoRaWANUpdateGatewayTaskCreate:
    boto3_raw_data: "type_defs.LoRaWANUpdateGatewayTaskCreateTypeDef" = (
        dataclasses.field()
    )

    UpdateSignature = field("UpdateSignature")
    SigKeyCrc = field("SigKeyCrc")

    @cached_property
    def CurrentVersion(self):  # pragma: no cover
        return LoRaWANGatewayVersion.make_one(self.boto3_raw_data["CurrentVersion"])

    @cached_property
    def UpdateVersion(self):  # pragma: no cover
        return LoRaWANGatewayVersion.make_one(self.boto3_raw_data["UpdateVersion"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.LoRaWANUpdateGatewayTaskCreateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoRaWANUpdateGatewayTaskCreateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoRaWANUpdateGatewayTaskEntry:
    boto3_raw_data: "type_defs.LoRaWANUpdateGatewayTaskEntryTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CurrentVersion(self):  # pragma: no cover
        return LoRaWANGatewayVersion.make_one(self.boto3_raw_data["CurrentVersion"])

    @cached_property
    def UpdateVersion(self):  # pragma: no cover
        return LoRaWANGatewayVersion.make_one(self.boto3_raw_data["UpdateVersion"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.LoRaWANUpdateGatewayTaskEntryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoRaWANUpdateGatewayTaskEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoRaWANMulticastGet:
    boto3_raw_data: "type_defs.LoRaWANMulticastGetTypeDef" = dataclasses.field()

    RfRegion = field("RfRegion")
    DlClass = field("DlClass")
    NumberOfDevicesRequested = field("NumberOfDevicesRequested")
    NumberOfDevicesInGroup = field("NumberOfDevicesInGroup")

    @cached_property
    def ParticipatingGateways(self):  # pragma: no cover
        return ParticipatingGatewaysMulticastOutput.make_one(
            self.boto3_raw_data["ParticipatingGateways"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LoRaWANMulticastGetTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoRaWANMulticastGetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MulticastWirelessMetadata:
    boto3_raw_data: "type_defs.MulticastWirelessMetadataTypeDef" = dataclasses.field()

    @cached_property
    def LoRaWAN(self):  # pragma: no cover
        return LoRaWANMulticastMetadata.make_one(self.boto3_raw_data["LoRaWAN"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MulticastWirelessMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MulticastWirelessMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LteObj:
    boto3_raw_data: "type_defs.LteObjTypeDef" = dataclasses.field()

    Mcc = field("Mcc")
    Mnc = field("Mnc")
    EutranCid = field("EutranCid")
    Tac = field("Tac")

    @cached_property
    def LteLocalId(self):  # pragma: no cover
        return LteLocalId.make_one(self.boto3_raw_data["LteLocalId"])

    LteTimingAdvance = field("LteTimingAdvance")
    Rsrp = field("Rsrp")
    Rsrq = field("Rsrq")
    NrCapable = field("NrCapable")

    @cached_property
    def LteNmr(self):  # pragma: no cover
        return LteNmrObj.make_many(self.boto3_raw_data["LteNmr"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LteObjTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LteObjTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SummaryMetricQueryResult:
    boto3_raw_data: "type_defs.SummaryMetricQueryResultTypeDef" = dataclasses.field()

    QueryId = field("QueryId")
    QueryStatus = field("QueryStatus")
    Error = field("Error")
    MetricName = field("MetricName")

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return Dimension.make_many(self.boto3_raw_data["Dimensions"])

    AggregationPeriod = field("AggregationPeriod")
    StartTimestamp = field("StartTimestamp")
    EndTimestamp = field("EndTimestamp")
    Timestamps = field("Timestamps")

    @cached_property
    def Values(self):  # pragma: no cover
        return MetricQueryValue.make_many(self.boto3_raw_data["Values"])

    Unit = field("Unit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SummaryMetricQueryResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SummaryMetricQueryResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PositionSolverConfigurations:
    boto3_raw_data: "type_defs.PositionSolverConfigurationsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SemtechGnss(self):  # pragma: no cover
        return SemtechGnssConfiguration.make_one(self.boto3_raw_data["SemtechGnss"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PositionSolverConfigurationsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PositionSolverConfigurationsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PositionSolverDetails:
    boto3_raw_data: "type_defs.PositionSolverDetailsTypeDef" = dataclasses.field()

    @cached_property
    def SemtechGnss(self):  # pragma: no cover
        return SemtechGnssDetail.make_one(self.boto3_raw_data["SemtechGnss"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PositionSolverDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PositionSolverDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartSingleWirelessDeviceImportTaskRequest:
    boto3_raw_data: "type_defs.StartSingleWirelessDeviceImportTaskRequestTypeDef" = (
        dataclasses.field()
    )

    DestinationName = field("DestinationName")

    @cached_property
    def Sidewalk(self):  # pragma: no cover
        return SidewalkSingleStartImportInfo.make_one(self.boto3_raw_data["Sidewalk"])

    ClientRequestToken = field("ClientRequestToken")
    DeviceName = field("DeviceName")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartSingleWirelessDeviceImportTaskRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartSingleWirelessDeviceImportTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartWirelessDeviceImportTaskRequest:
    boto3_raw_data: "type_defs.StartWirelessDeviceImportTaskRequestTypeDef" = (
        dataclasses.field()
    )

    DestinationName = field("DestinationName")

    @cached_property
    def Sidewalk(self):  # pragma: no cover
        return SidewalkStartImportInfo.make_one(self.boto3_raw_data["Sidewalk"])

    ClientRequestToken = field("ClientRequestToken")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartWirelessDeviceImportTaskRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartWirelessDeviceImportTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePartnerAccountRequest:
    boto3_raw_data: "type_defs.UpdatePartnerAccountRequestTypeDef" = dataclasses.field()

    @cached_property
    def Sidewalk(self):  # pragma: no cover
        return SidewalkUpdateAccount.make_one(self.boto3_raw_data["Sidewalk"])

    PartnerAccountId = field("PartnerAccountId")
    PartnerType = field("PartnerType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePartnerAccountRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePartnerAccountRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWirelessDeviceImportTaskRequest:
    boto3_raw_data: "type_defs.UpdateWirelessDeviceImportTaskRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @cached_property
    def Sidewalk(self):  # pragma: no cover
        return SidewalkUpdateImportInfo.make_one(self.boto3_raw_data["Sidewalk"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateWirelessDeviceImportTaskRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWirelessDeviceImportTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TdscdmaObj:
    boto3_raw_data: "type_defs.TdscdmaObjTypeDef" = dataclasses.field()

    Mcc = field("Mcc")
    Mnc = field("Mnc")
    UtranCid = field("UtranCid")
    Lac = field("Lac")

    @cached_property
    def TdscdmaLocalId(self):  # pragma: no cover
        return TdscdmaLocalId.make_one(self.boto3_raw_data["TdscdmaLocalId"])

    TdscdmaTimingAdvance = field("TdscdmaTimingAdvance")
    Rscp = field("Rscp")
    PathLoss = field("PathLoss")

    @cached_property
    def TdscdmaNmr(self):  # pragma: no cover
        return TdscdmaNmrObj.make_many(self.boto3_raw_data["TdscdmaNmr"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TdscdmaObjTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TdscdmaObjTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WcdmaObj:
    boto3_raw_data: "type_defs.WcdmaObjTypeDef" = dataclasses.field()

    Mcc = field("Mcc")
    Mnc = field("Mnc")
    UtranCid = field("UtranCid")
    Lac = field("Lac")

    @cached_property
    def WcdmaLocalId(self):  # pragma: no cover
        return WcdmaLocalId.make_one(self.boto3_raw_data["WcdmaLocalId"])

    Rscp = field("Rscp")
    PathLoss = field("PathLoss")

    @cached_property
    def WcdmaNmr(self):  # pragma: no cover
        return WcdmaNmrObj.make_many(self.boto3_raw_data["WcdmaNmr"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WcdmaObjTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WcdmaObjTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WirelessDeviceLogOptionOutput:
    boto3_raw_data: "type_defs.WirelessDeviceLogOptionOutputTypeDef" = (
        dataclasses.field()
    )

    Type = field("Type")
    LogLevel = field("LogLevel")

    @cached_property
    def Events(self):  # pragma: no cover
        return WirelessDeviceEventLogOption.make_many(self.boto3_raw_data["Events"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.WirelessDeviceLogOptionOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WirelessDeviceLogOptionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WirelessDeviceLogOption:
    boto3_raw_data: "type_defs.WirelessDeviceLogOptionTypeDef" = dataclasses.field()

    Type = field("Type")
    LogLevel = field("LogLevel")

    @cached_property
    def Events(self):  # pragma: no cover
        return WirelessDeviceEventLogOption.make_many(self.boto3_raw_data["Events"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WirelessDeviceLogOptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WirelessDeviceLogOptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WirelessGatewayLogOptionOutput:
    boto3_raw_data: "type_defs.WirelessGatewayLogOptionOutputTypeDef" = (
        dataclasses.field()
    )

    Type = field("Type")
    LogLevel = field("LogLevel")

    @cached_property
    def Events(self):  # pragma: no cover
        return WirelessGatewayEventLogOption.make_many(self.boto3_raw_data["Events"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.WirelessGatewayLogOptionOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WirelessGatewayLogOptionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WirelessGatewayLogOption:
    boto3_raw_data: "type_defs.WirelessGatewayLogOptionTypeDef" = dataclasses.field()

    Type = field("Type")
    LogLevel = field("LogLevel")

    @cached_property
    def Events(self):  # pragma: no cover
        return WirelessGatewayEventLogOption.make_many(self.boto3_raw_data["Events"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WirelessGatewayLogOptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WirelessGatewayLogOptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWirelessGatewayResponse:
    boto3_raw_data: "type_defs.GetWirelessGatewayResponseTypeDef" = dataclasses.field()

    Name = field("Name")
    Id = field("Id")
    Description = field("Description")

    @cached_property
    def LoRaWAN(self):  # pragma: no cover
        return LoRaWANGatewayOutput.make_one(self.boto3_raw_data["LoRaWAN"])

    Arn = field("Arn")
    ThingName = field("ThingName")
    ThingArn = field("ThingArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetWirelessGatewayResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWirelessGatewayResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WirelessGatewayStatistics:
    boto3_raw_data: "type_defs.WirelessGatewayStatisticsTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Id = field("Id")
    Name = field("Name")
    Description = field("Description")

    @cached_property
    def LoRaWAN(self):  # pragma: no cover
        return LoRaWANGatewayOutput.make_one(self.boto3_raw_data["LoRaWAN"])

    LastUplinkReceivedAt = field("LastUplinkReceivedAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WirelessGatewayStatisticsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WirelessGatewayStatisticsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WirelessDeviceStatistics:
    boto3_raw_data: "type_defs.WirelessDeviceStatisticsTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Id = field("Id")
    Type = field("Type")
    Name = field("Name")
    DestinationName = field("DestinationName")
    LastUplinkReceivedAt = field("LastUplinkReceivedAt")

    @cached_property
    def LoRaWAN(self):  # pragma: no cover
        return LoRaWANListDevice.make_one(self.boto3_raw_data["LoRaWAN"])

    @cached_property
    def Sidewalk(self):  # pragma: no cover
        return SidewalkListDevice.make_one(self.boto3_raw_data["Sidewalk"])

    FuotaDeviceStatus = field("FuotaDeviceStatus")
    MulticastDeviceStatus = field("MulticastDeviceStatus")
    McGroupId = field("McGroupId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WirelessDeviceStatisticsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WirelessDeviceStatisticsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeviceProfileResponse:
    boto3_raw_data: "type_defs.GetDeviceProfileResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Name = field("Name")
    Id = field("Id")

    @cached_property
    def LoRaWAN(self):  # pragma: no cover
        return LoRaWANDeviceProfileOutput.make_one(self.boto3_raw_data["LoRaWAN"])

    @cached_property
    def Sidewalk(self):  # pragma: no cover
        return SidewalkGetDeviceProfile.make_one(self.boto3_raw_data["Sidewalk"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDeviceProfileResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeviceProfileResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoRaWANDeviceOutput:
    boto3_raw_data: "type_defs.LoRaWANDeviceOutputTypeDef" = dataclasses.field()

    DevEui = field("DevEui")
    DeviceProfileId = field("DeviceProfileId")
    ServiceProfileId = field("ServiceProfileId")

    @cached_property
    def OtaaV1_1(self):  # pragma: no cover
        return OtaaV11.make_one(self.boto3_raw_data["OtaaV1_1"])

    @cached_property
    def OtaaV1_0_x(self):  # pragma: no cover
        return OtaaV10X.make_one(self.boto3_raw_data["OtaaV1_0_x"])

    @cached_property
    def AbpV1_1(self):  # pragma: no cover
        return AbpV11.make_one(self.boto3_raw_data["AbpV1_1"])

    @cached_property
    def AbpV1_0_x(self):  # pragma: no cover
        return AbpV10X.make_one(self.boto3_raw_data["AbpV1_0_x"])

    @cached_property
    def FPorts(self):  # pragma: no cover
        return FPortsOutput.make_one(self.boto3_raw_data["FPorts"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LoRaWANDeviceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoRaWANDeviceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoRaWANDevice:
    boto3_raw_data: "type_defs.LoRaWANDeviceTypeDef" = dataclasses.field()

    DevEui = field("DevEui")
    DeviceProfileId = field("DeviceProfileId")
    ServiceProfileId = field("ServiceProfileId")

    @cached_property
    def OtaaV1_1(self):  # pragma: no cover
        return OtaaV11.make_one(self.boto3_raw_data["OtaaV1_1"])

    @cached_property
    def OtaaV1_0_x(self):  # pragma: no cover
        return OtaaV10X.make_one(self.boto3_raw_data["OtaaV1_0_x"])

    @cached_property
    def AbpV1_1(self):  # pragma: no cover
        return AbpV11.make_one(self.boto3_raw_data["AbpV1_1"])

    @cached_property
    def AbpV1_0_x(self):  # pragma: no cover
        return AbpV10X.make_one(self.boto3_raw_data["AbpV1_0_x"])

    @cached_property
    def FPorts(self):  # pragma: no cover
        return FPorts.make_one(self.boto3_raw_data["FPorts"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LoRaWANDeviceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LoRaWANDeviceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoRaWANUpdateDevice:
    boto3_raw_data: "type_defs.LoRaWANUpdateDeviceTypeDef" = dataclasses.field()

    DeviceProfileId = field("DeviceProfileId")
    ServiceProfileId = field("ServiceProfileId")

    @cached_property
    def AbpV1_1(self):  # pragma: no cover
        return UpdateAbpV11.make_one(self.boto3_raw_data["AbpV1_1"])

    @cached_property
    def AbpV1_0_x(self):  # pragma: no cover
        return UpdateAbpV10X.make_one(self.boto3_raw_data["AbpV1_0_x"])

    @cached_property
    def FPorts(self):  # pragma: no cover
        return UpdateFPorts.make_one(self.boto3_raw_data["FPorts"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LoRaWANUpdateDeviceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoRaWANUpdateDeviceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoRaWANSendDataToDeviceOutput:
    boto3_raw_data: "type_defs.LoRaWANSendDataToDeviceOutputTypeDef" = (
        dataclasses.field()
    )

    FPort = field("FPort")

    @cached_property
    def ParticipatingGateways(self):  # pragma: no cover
        return ParticipatingGatewaysOutput.make_one(
            self.boto3_raw_data["ParticipatingGateways"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.LoRaWANSendDataToDeviceOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoRaWANSendDataToDeviceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartFuotaTaskRequest:
    boto3_raw_data: "type_defs.StartFuotaTaskRequestTypeDef" = dataclasses.field()

    Id = field("Id")

    @cached_property
    def LoRaWAN(self):  # pragma: no cover
        return LoRaWANStartFuotaTask.make_one(self.boto3_raw_data["LoRaWAN"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartFuotaTaskRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartFuotaTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMetricsRequest:
    boto3_raw_data: "type_defs.GetMetricsRequestTypeDef" = dataclasses.field()

    @cached_property
    def SummaryMetricQueries(self):  # pragma: no cover
        return SummaryMetricQuery.make_many(self.boto3_raw_data["SummaryMetricQueries"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetMetricsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMetricsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWirelessDeviceImportTasksResponse:
    boto3_raw_data: "type_defs.ListWirelessDeviceImportTasksResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def WirelessDeviceImportTaskList(self):  # pragma: no cover
        return WirelessDeviceImportTask.make_many(
            self.boto3_raw_data["WirelessDeviceImportTaskList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListWirelessDeviceImportTasksResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWirelessDeviceImportTasksResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GsmObj:
    boto3_raw_data: "type_defs.GsmObjTypeDef" = dataclasses.field()

    Mcc = field("Mcc")
    Mnc = field("Mnc")
    Lac = field("Lac")
    GeranCid = field("GeranCid")

    @cached_property
    def GsmLocalId(self):  # pragma: no cover
        return GsmLocalId.make_one(self.boto3_raw_data["GsmLocalId"])

    GsmTimingAdvance = field("GsmTimingAdvance")
    RxLevel = field("RxLevel")

    @cached_property
    def GsmNmr(self):  # pragma: no cover
        return GsmNmrObj.make_many(self.boto3_raw_data["GsmNmr"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GsmObjTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GsmObjTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDevicesForWirelessDeviceImportTaskResponse:
    boto3_raw_data: (
        "type_defs.ListDevicesForWirelessDeviceImportTaskResponseTypeDef"
    ) = dataclasses.field()

    DestinationName = field("DestinationName")

    @cached_property
    def ImportedWirelessDeviceList(self):  # pragma: no cover
        return ImportedWirelessDevice.make_many(
            self.boto3_raw_data["ImportedWirelessDeviceList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDevicesForWirelessDeviceImportTaskResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.ListDevicesForWirelessDeviceImportTaskResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventNotificationItemConfigurations:
    boto3_raw_data: "type_defs.EventNotificationItemConfigurationsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DeviceRegistrationState(self):  # pragma: no cover
        return DeviceRegistrationStateEventConfiguration.make_one(
            self.boto3_raw_data["DeviceRegistrationState"]
        )

    @cached_property
    def Proximity(self):  # pragma: no cover
        return ProximityEventConfiguration.make_one(self.boto3_raw_data["Proximity"])

    @cached_property
    def Join(self):  # pragma: no cover
        return JoinEventConfiguration.make_one(self.boto3_raw_data["Join"])

    @cached_property
    def ConnectionStatus(self):  # pragma: no cover
        return ConnectionStatusEventConfiguration.make_one(
            self.boto3_raw_data["ConnectionStatus"]
        )

    @cached_property
    def MessageDeliveryStatus(self):  # pragma: no cover
        return MessageDeliveryStatusEventConfiguration.make_one(
            self.boto3_raw_data["MessageDeliveryStatus"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EventNotificationItemConfigurationsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventNotificationItemConfigurationsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourceEventConfigurationResponse:
    boto3_raw_data: "type_defs.GetResourceEventConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DeviceRegistrationState(self):  # pragma: no cover
        return DeviceRegistrationStateEventConfiguration.make_one(
            self.boto3_raw_data["DeviceRegistrationState"]
        )

    @cached_property
    def Proximity(self):  # pragma: no cover
        return ProximityEventConfiguration.make_one(self.boto3_raw_data["Proximity"])

    @cached_property
    def Join(self):  # pragma: no cover
        return JoinEventConfiguration.make_one(self.boto3_raw_data["Join"])

    @cached_property
    def ConnectionStatus(self):  # pragma: no cover
        return ConnectionStatusEventConfiguration.make_one(
            self.boto3_raw_data["ConnectionStatus"]
        )

    @cached_property
    def MessageDeliveryStatus(self):  # pragma: no cover
        return MessageDeliveryStatusEventConfiguration.make_one(
            self.boto3_raw_data["MessageDeliveryStatus"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetResourceEventConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourceEventConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateResourceEventConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateResourceEventConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    Identifier = field("Identifier")
    IdentifierType = field("IdentifierType")
    PartnerType = field("PartnerType")

    @cached_property
    def DeviceRegistrationState(self):  # pragma: no cover
        return DeviceRegistrationStateEventConfiguration.make_one(
            self.boto3_raw_data["DeviceRegistrationState"]
        )

    @cached_property
    def Proximity(self):  # pragma: no cover
        return ProximityEventConfiguration.make_one(self.boto3_raw_data["Proximity"])

    @cached_property
    def Join(self):  # pragma: no cover
        return JoinEventConfiguration.make_one(self.boto3_raw_data["Join"])

    @cached_property
    def ConnectionStatus(self):  # pragma: no cover
        return ConnectionStatusEventConfiguration.make_one(
            self.boto3_raw_data["ConnectionStatus"]
        )

    @cached_property
    def MessageDeliveryStatus(self):  # pragma: no cover
        return MessageDeliveryStatusEventConfiguration.make_one(
            self.boto3_raw_data["MessageDeliveryStatus"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateResourceEventConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateResourceEventConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEventConfigurationByResourceTypesResponse:
    boto3_raw_data: "type_defs.GetEventConfigurationByResourceTypesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DeviceRegistrationState(self):  # pragma: no cover
        return DeviceRegistrationStateResourceTypeEventConfiguration.make_one(
            self.boto3_raw_data["DeviceRegistrationState"]
        )

    @cached_property
    def Proximity(self):  # pragma: no cover
        return ProximityResourceTypeEventConfiguration.make_one(
            self.boto3_raw_data["Proximity"]
        )

    @cached_property
    def Join(self):  # pragma: no cover
        return JoinResourceTypeEventConfiguration.make_one(self.boto3_raw_data["Join"])

    @cached_property
    def ConnectionStatus(self):  # pragma: no cover
        return ConnectionStatusResourceTypeEventConfiguration.make_one(
            self.boto3_raw_data["ConnectionStatus"]
        )

    @cached_property
    def MessageDeliveryStatus(self):  # pragma: no cover
        return MessageDeliveryStatusResourceTypeEventConfiguration.make_one(
            self.boto3_raw_data["MessageDeliveryStatus"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetEventConfigurationByResourceTypesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEventConfigurationByResourceTypesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEventConfigurationByResourceTypesRequest:
    boto3_raw_data: (
        "type_defs.UpdateEventConfigurationByResourceTypesRequestTypeDef"
    ) = dataclasses.field()

    @cached_property
    def DeviceRegistrationState(self):  # pragma: no cover
        return DeviceRegistrationStateResourceTypeEventConfiguration.make_one(
            self.boto3_raw_data["DeviceRegistrationState"]
        )

    @cached_property
    def Proximity(self):  # pragma: no cover
        return ProximityResourceTypeEventConfiguration.make_one(
            self.boto3_raw_data["Proximity"]
        )

    @cached_property
    def Join(self):  # pragma: no cover
        return JoinResourceTypeEventConfiguration.make_one(self.boto3_raw_data["Join"])

    @cached_property
    def ConnectionStatus(self):  # pragma: no cover
        return ConnectionStatusResourceTypeEventConfiguration.make_one(
            self.boto3_raw_data["ConnectionStatus"]
        )

    @cached_property
    def MessageDeliveryStatus(self):  # pragma: no cover
        return MessageDeliveryStatusResourceTypeEventConfiguration.make_one(
            self.boto3_raw_data["MessageDeliveryStatus"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateEventConfigurationByResourceTypesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.UpdateEventConfigurationByResourceTypesRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWirelessDeviceStatisticsResponse:
    boto3_raw_data: "type_defs.GetWirelessDeviceStatisticsResponseTypeDef" = (
        dataclasses.field()
    )

    WirelessDeviceId = field("WirelessDeviceId")
    LastUplinkReceivedAt = field("LastUplinkReceivedAt")

    @cached_property
    def LoRaWAN(self):  # pragma: no cover
        return LoRaWANDeviceMetadata.make_one(self.boto3_raw_data["LoRaWAN"])

    @cached_property
    def Sidewalk(self):  # pragma: no cover
        return SidewalkDeviceMetadata.make_one(self.boto3_raw_data["Sidewalk"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetWirelessDeviceStatisticsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWirelessDeviceStatisticsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDeviceProfileRequest:
    boto3_raw_data: "type_defs.CreateDeviceProfileRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    LoRaWAN = field("LoRaWAN")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    ClientRequestToken = field("ClientRequestToken")
    Sidewalk = field("Sidewalk")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDeviceProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDeviceProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWirelessGatewayFirmwareInformationResponse:
    boto3_raw_data: "type_defs.GetWirelessGatewayFirmwareInformationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def LoRaWAN(self):  # pragma: no cover
        return LoRaWANGatewayCurrentVersion.make_one(self.boto3_raw_data["LoRaWAN"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetWirelessGatewayFirmwareInformationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWirelessGatewayFirmwareInformationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWirelessGatewayTaskCreate:
    boto3_raw_data: "type_defs.UpdateWirelessGatewayTaskCreateTypeDef" = (
        dataclasses.field()
    )

    UpdateDataSource = field("UpdateDataSource")
    UpdateDataRole = field("UpdateDataRole")

    @cached_property
    def LoRaWAN(self):  # pragma: no cover
        return LoRaWANUpdateGatewayTaskCreate.make_one(self.boto3_raw_data["LoRaWAN"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateWirelessGatewayTaskCreateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWirelessGatewayTaskCreateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWirelessGatewayTaskEntry:
    boto3_raw_data: "type_defs.UpdateWirelessGatewayTaskEntryTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @cached_property
    def LoRaWAN(self):  # pragma: no cover
        return LoRaWANUpdateGatewayTaskEntry.make_one(self.boto3_raw_data["LoRaWAN"])

    Arn = field("Arn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateWirelessGatewayTaskEntryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWirelessGatewayTaskEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMulticastGroupResponse:
    boto3_raw_data: "type_defs.GetMulticastGroupResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Id = field("Id")
    Name = field("Name")
    Description = field("Description")
    Status = field("Status")

    @cached_property
    def LoRaWAN(self):  # pragma: no cover
        return LoRaWANMulticastGet.make_one(self.boto3_raw_data["LoRaWAN"])

    CreatedAt = field("CreatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMulticastGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMulticastGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendDataToMulticastGroupRequest:
    boto3_raw_data: "type_defs.SendDataToMulticastGroupRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    PayloadData = field("PayloadData")

    @cached_property
    def WirelessMetadata(self):  # pragma: no cover
        return MulticastWirelessMetadata.make_one(
            self.boto3_raw_data["WirelessMetadata"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SendDataToMulticastGroupRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendDataToMulticastGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMetricsResponse:
    boto3_raw_data: "type_defs.GetMetricsResponseTypeDef" = dataclasses.field()

    @cached_property
    def SummaryMetricQueryResults(self):  # pragma: no cover
        return SummaryMetricQueryResult.make_many(
            self.boto3_raw_data["SummaryMetricQueryResults"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMetricsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMetricsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoRaWANMulticast:
    boto3_raw_data: "type_defs.LoRaWANMulticastTypeDef" = dataclasses.field()

    RfRegion = field("RfRegion")
    DlClass = field("DlClass")
    ParticipatingGateways = field("ParticipatingGateways")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LoRaWANMulticastTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoRaWANMulticastTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutPositionConfigurationRequest:
    boto3_raw_data: "type_defs.PutPositionConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceIdentifier = field("ResourceIdentifier")
    ResourceType = field("ResourceType")

    @cached_property
    def Solvers(self):  # pragma: no cover
        return PositionSolverConfigurations.make_one(self.boto3_raw_data["Solvers"])

    Destination = field("Destination")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutPositionConfigurationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutPositionConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPositionConfigurationResponse:
    boto3_raw_data: "type_defs.GetPositionConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Solvers(self):  # pragma: no cover
        return PositionSolverDetails.make_one(self.boto3_raw_data["Solvers"])

    Destination = field("Destination")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetPositionConfigurationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPositionConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PositionConfigurationItem:
    boto3_raw_data: "type_defs.PositionConfigurationItemTypeDef" = dataclasses.field()

    ResourceIdentifier = field("ResourceIdentifier")
    ResourceType = field("ResourceType")

    @cached_property
    def Solvers(self):  # pragma: no cover
        return PositionSolverDetails.make_one(self.boto3_raw_data["Solvers"])

    Destination = field("Destination")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PositionConfigurationItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PositionConfigurationItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLogLevelsByResourceTypesResponse:
    boto3_raw_data: "type_defs.GetLogLevelsByResourceTypesResponseTypeDef" = (
        dataclasses.field()
    )

    DefaultLogLevel = field("DefaultLogLevel")

    @cached_property
    def WirelessGatewayLogOptions(self):  # pragma: no cover
        return WirelessGatewayLogOptionOutput.make_many(
            self.boto3_raw_data["WirelessGatewayLogOptions"]
        )

    @cached_property
    def WirelessDeviceLogOptions(self):  # pragma: no cover
        return WirelessDeviceLogOptionOutput.make_many(
            self.boto3_raw_data["WirelessDeviceLogOptions"]
        )

    @cached_property
    def FuotaTaskLogOptions(self):  # pragma: no cover
        return FuotaTaskLogOptionOutput.make_many(
            self.boto3_raw_data["FuotaTaskLogOptions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetLogLevelsByResourceTypesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLogLevelsByResourceTypesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWirelessGatewaysResponse:
    boto3_raw_data: "type_defs.ListWirelessGatewaysResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def WirelessGatewayList(self):  # pragma: no cover
        return WirelessGatewayStatistics.make_many(
            self.boto3_raw_data["WirelessGatewayList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWirelessGatewaysResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWirelessGatewaysResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWirelessGatewayRequest:
    boto3_raw_data: "type_defs.CreateWirelessGatewayRequestTypeDef" = (
        dataclasses.field()
    )

    LoRaWAN = field("LoRaWAN")
    Name = field("Name")
    Description = field("Description")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWirelessGatewayRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWirelessGatewayRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWirelessDevicesResponse:
    boto3_raw_data: "type_defs.ListWirelessDevicesResponseTypeDef" = dataclasses.field()

    @cached_property
    def WirelessDeviceList(self):  # pragma: no cover
        return WirelessDeviceStatistics.make_many(
            self.boto3_raw_data["WirelessDeviceList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWirelessDevicesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWirelessDevicesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWirelessDeviceResponse:
    boto3_raw_data: "type_defs.GetWirelessDeviceResponseTypeDef" = dataclasses.field()

    Type = field("Type")
    Name = field("Name")
    Description = field("Description")
    DestinationName = field("DestinationName")
    Id = field("Id")
    Arn = field("Arn")
    ThingName = field("ThingName")
    ThingArn = field("ThingArn")

    @cached_property
    def LoRaWAN(self):  # pragma: no cover
        return LoRaWANDeviceOutput.make_one(self.boto3_raw_data["LoRaWAN"])

    @cached_property
    def Sidewalk(self):  # pragma: no cover
        return SidewalkDevice.make_one(self.boto3_raw_data["Sidewalk"])

    Positioning = field("Positioning")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetWirelessDeviceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWirelessDeviceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateWirelessDeviceRequest:
    boto3_raw_data: "type_defs.UpdateWirelessDeviceRequestTypeDef" = dataclasses.field()

    Id = field("Id")
    DestinationName = field("DestinationName")
    Name = field("Name")
    Description = field("Description")

    @cached_property
    def LoRaWAN(self):  # pragma: no cover
        return LoRaWANUpdateDevice.make_one(self.boto3_raw_data["LoRaWAN"])

    Positioning = field("Positioning")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateWirelessDeviceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateWirelessDeviceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DownlinkQueueMessage:
    boto3_raw_data: "type_defs.DownlinkQueueMessageTypeDef" = dataclasses.field()

    MessageId = field("MessageId")
    TransmitMode = field("TransmitMode")
    ReceivedAt = field("ReceivedAt")

    @cached_property
    def LoRaWAN(self):  # pragma: no cover
        return LoRaWANSendDataToDeviceOutput.make_one(self.boto3_raw_data["LoRaWAN"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DownlinkQueueMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DownlinkQueueMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoRaWANSendDataToDevice:
    boto3_raw_data: "type_defs.LoRaWANSendDataToDeviceTypeDef" = dataclasses.field()

    FPort = field("FPort")
    ParticipatingGateways = field("ParticipatingGateways")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LoRaWANSendDataToDeviceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoRaWANSendDataToDeviceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMulticastGroupSessionRequest:
    boto3_raw_data: "type_defs.StartMulticastGroupSessionRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    LoRaWAN = field("LoRaWAN")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartMulticastGroupSessionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMulticastGroupSessionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CellTowers:
    boto3_raw_data: "type_defs.CellTowersTypeDef" = dataclasses.field()

    @cached_property
    def Gsm(self):  # pragma: no cover
        return GsmObj.make_many(self.boto3_raw_data["Gsm"])

    @cached_property
    def Wcdma(self):  # pragma: no cover
        return WcdmaObj.make_many(self.boto3_raw_data["Wcdma"])

    @cached_property
    def Tdscdma(self):  # pragma: no cover
        return TdscdmaObj.make_many(self.boto3_raw_data["Tdscdma"])

    @cached_property
    def Lte(self):  # pragma: no cover
        return LteObj.make_many(self.boto3_raw_data["Lte"])

    @cached_property
    def Cdma(self):  # pragma: no cover
        return CdmaObj.make_many(self.boto3_raw_data["Cdma"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CellTowersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CellTowersTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventConfigurationItem:
    boto3_raw_data: "type_defs.EventConfigurationItemTypeDef" = dataclasses.field()

    Identifier = field("Identifier")
    IdentifierType = field("IdentifierType")
    PartnerType = field("PartnerType")

    @cached_property
    def Events(self):  # pragma: no cover
        return EventNotificationItemConfigurations.make_one(
            self.boto3_raw_data["Events"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EventConfigurationItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventConfigurationItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWirelessGatewayTaskDefinitionRequest:
    boto3_raw_data: "type_defs.CreateWirelessGatewayTaskDefinitionRequestTypeDef" = (
        dataclasses.field()
    )

    AutoCreateTasks = field("AutoCreateTasks")
    Name = field("Name")

    @cached_property
    def Update(self):  # pragma: no cover
        return UpdateWirelessGatewayTaskCreate.make_one(self.boto3_raw_data["Update"])

    ClientRequestToken = field("ClientRequestToken")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateWirelessGatewayTaskDefinitionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWirelessGatewayTaskDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWirelessGatewayTaskDefinitionResponse:
    boto3_raw_data: "type_defs.GetWirelessGatewayTaskDefinitionResponseTypeDef" = (
        dataclasses.field()
    )

    AutoCreateTasks = field("AutoCreateTasks")
    Name = field("Name")

    @cached_property
    def Update(self):  # pragma: no cover
        return UpdateWirelessGatewayTaskCreate.make_one(self.boto3_raw_data["Update"])

    Arn = field("Arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetWirelessGatewayTaskDefinitionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWirelessGatewayTaskDefinitionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWirelessGatewayTaskDefinitionsResponse:
    boto3_raw_data: "type_defs.ListWirelessGatewayTaskDefinitionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TaskDefinitions(self):  # pragma: no cover
        return UpdateWirelessGatewayTaskEntry.make_many(
            self.boto3_raw_data["TaskDefinitions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListWirelessGatewayTaskDefinitionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWirelessGatewayTaskDefinitionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMulticastGroupRequest:
    boto3_raw_data: "type_defs.CreateMulticastGroupRequestTypeDef" = dataclasses.field()

    @cached_property
    def LoRaWAN(self):  # pragma: no cover
        return LoRaWANMulticast.make_one(self.boto3_raw_data["LoRaWAN"])

    Name = field("Name")
    Description = field("Description")
    ClientRequestToken = field("ClientRequestToken")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateMulticastGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMulticastGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMulticastGroupRequest:
    boto3_raw_data: "type_defs.UpdateMulticastGroupRequestTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")
    Description = field("Description")

    @cached_property
    def LoRaWAN(self):  # pragma: no cover
        return LoRaWANMulticast.make_one(self.boto3_raw_data["LoRaWAN"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateMulticastGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMulticastGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPositionConfigurationsResponse:
    boto3_raw_data: "type_defs.ListPositionConfigurationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PositionConfigurationList(self):  # pragma: no cover
        return PositionConfigurationItem.make_many(
            self.boto3_raw_data["PositionConfigurationList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPositionConfigurationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPositionConfigurationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateLogLevelsByResourceTypesRequest:
    boto3_raw_data: "type_defs.UpdateLogLevelsByResourceTypesRequestTypeDef" = (
        dataclasses.field()
    )

    DefaultLogLevel = field("DefaultLogLevel")
    FuotaTaskLogOptions = field("FuotaTaskLogOptions")
    WirelessDeviceLogOptions = field("WirelessDeviceLogOptions")
    WirelessGatewayLogOptions = field("WirelessGatewayLogOptions")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateLogLevelsByResourceTypesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLogLevelsByResourceTypesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateWirelessDeviceRequest:
    boto3_raw_data: "type_defs.CreateWirelessDeviceRequestTypeDef" = dataclasses.field()

    Type = field("Type")
    DestinationName = field("DestinationName")
    Name = field("Name")
    Description = field("Description")
    ClientRequestToken = field("ClientRequestToken")
    LoRaWAN = field("LoRaWAN")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    Positioning = field("Positioning")

    @cached_property
    def Sidewalk(self):  # pragma: no cover
        return SidewalkCreateWirelessDevice.make_one(self.boto3_raw_data["Sidewalk"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateWirelessDeviceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateWirelessDeviceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQueuedMessagesResponse:
    boto3_raw_data: "type_defs.ListQueuedMessagesResponseTypeDef" = dataclasses.field()

    @cached_property
    def DownlinkQueueMessagesList(self):  # pragma: no cover
        return DownlinkQueueMessage.make_many(
            self.boto3_raw_data["DownlinkQueueMessagesList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListQueuedMessagesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQueuedMessagesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPositionEstimateRequest:
    boto3_raw_data: "type_defs.GetPositionEstimateRequestTypeDef" = dataclasses.field()

    @cached_property
    def WiFiAccessPoints(self):  # pragma: no cover
        return WiFiAccessPoint.make_many(self.boto3_raw_data["WiFiAccessPoints"])

    @cached_property
    def CellTowers(self):  # pragma: no cover
        return CellTowers.make_one(self.boto3_raw_data["CellTowers"])

    @cached_property
    def Ip(self):  # pragma: no cover
        return Ip.make_one(self.boto3_raw_data["Ip"])

    @cached_property
    def Gnss(self):  # pragma: no cover
        return Gnss.make_one(self.boto3_raw_data["Gnss"])

    Timestamp = field("Timestamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPositionEstimateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPositionEstimateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEventConfigurationsResponse:
    boto3_raw_data: "type_defs.ListEventConfigurationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EventConfigurationsList(self):  # pragma: no cover
        return EventConfigurationItem.make_many(
            self.boto3_raw_data["EventConfigurationsList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListEventConfigurationsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEventConfigurationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WirelessMetadata:
    boto3_raw_data: "type_defs.WirelessMetadataTypeDef" = dataclasses.field()

    LoRaWAN = field("LoRaWAN")

    @cached_property
    def Sidewalk(self):  # pragma: no cover
        return SidewalkSendDataToDevice.make_one(self.boto3_raw_data["Sidewalk"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WirelessMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WirelessMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SendDataToWirelessDeviceRequest:
    boto3_raw_data: "type_defs.SendDataToWirelessDeviceRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    TransmitMode = field("TransmitMode")
    PayloadData = field("PayloadData")

    @cached_property
    def WirelessMetadata(self):  # pragma: no cover
        return WirelessMetadata.make_one(self.boto3_raw_data["WirelessMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SendDataToWirelessDeviceRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SendDataToWirelessDeviceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
