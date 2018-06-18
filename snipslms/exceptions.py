class SonosActionException(Exception):
    """An exception occured with the LMS Action."""


class ServiceException(SonosActionException):
    """An exception occured within a service"""


# Device Discovery Service
class DeviceDiscoveryException(ServiceException):
    """An exception occured with the device discovery service"""


class NoReachableDeviceException(DeviceDiscoveryException):
    """No connected devices were found by the DeviceDiscovery service"""
