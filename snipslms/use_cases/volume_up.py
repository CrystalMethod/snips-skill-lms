from snipslms.shared.use_case import UseCase
from snipslms.shared.response_object import ResponseSuccess, ResponseFailure
from snipslms.exceptions import NoReachableDeviceException


class VolumeUpUseCase(UseCase):

    DEFAULT_VOLUME_INCREMENT = 10

    def __init__(self, server, player):
        self.server = server
        self.player = player

    def process_request(self, request_object):
        #device = self.device_discovery_service.get()
        volume_increase = request_object.volume_increase
        if volume_increase:
            #device.increase_volume(request_object.volume_increase)
            self.player.volume_up(volume_increase)
        else:
            #device.increase_volume(self.DEFAULT_VOLUME_INCREMENT)
            self.player.volume_up(self.DEFAULT_VOLUME_INCREMENT)
        return ResponseSuccess()
