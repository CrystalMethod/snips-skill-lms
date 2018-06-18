from snipslms.shared.use_case import UseCase
from snipslms.shared.response_object import ResponseSuccess, ResponseFailure
from snipslms.exceptions import NoReachableDeviceException


class VolumeDownUseCase(UseCase):

    DEFAULT_VOLUME_DECREMENT = 10

    def __init__(self, server, player):
        """

        :param server:
        :param player:
        """
        self.server = server
        self.player = player

    def process_request(self, request_object):
        #device = self.device_discovery_service.get()
        volume_decrease = request_object.volume_decrease
        if volume_decrease:
            #device.decrease_volume(volume_decrease)
            r = self.player.volume_down(volume_decrease)
        else:
            #device.decrease_volume(self.DEFAULT_VOLUME_DECREMENT)
            r = self.player.volume_down(self.DEFAULT_VOLUME_DECREMENT)
        return ResponseSuccess()
