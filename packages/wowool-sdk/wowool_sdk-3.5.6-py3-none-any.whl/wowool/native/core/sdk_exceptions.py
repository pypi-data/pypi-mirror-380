from wowool.error import Error as WowoolError


class SDKError(WowoolError):
    pass


class SDKLicenseError(SDKError):
    pass


class SDKProcessingError(SDKError):
    pass
