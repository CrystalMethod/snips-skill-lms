#!/usr/bin/env python2
# -*-: coding utf-8 -*-

import ConfigParser
import io
import os

from hermes_python.hermes import Hermes
from hermes_python.ontology import *

from LMSTools import LMSDiscovery, LMSServer, LMSPlayer

from snipslms.use_cases.mute import MuteUseCase
from snipslms.use_cases.speaker_interrupt import SpeakerInterruptUseCase
from snipslms.use_cases.volume_down import VolumeDownUseCase
from snipslms.use_cases.volume_up import VolumeUpUseCase
from snipslms.adapters.request_adapter import MuteRequestAdapter, SpeakerInterruptRequestAdapter, \
    VolumeDownRequestAdapter, VolumeUpRequestAdapter

# Utils functions
CONFIGURATION_ENCODING_FORMAT = "utf-8"
CONFIG_INI = "config.ini"

HOSTNAME = "192.168.1.114"

HERMES_HOST = "{}:1883".format(HOSTNAME)

class SnipsConfigParser(ConfigParser.SafeConfigParser):
    def to_dict(self):
        return {section: {option_name: option for option_name, option in self.items(section)} for section in
                self.sections()}


def read_configuration_file(configuration_file):
    try:
        with io.open(configuration_file, encoding=CONFIGURATION_ENCODING_FORMAT) as f:
            conf_parser = SnipsConfigParser()
            conf_parser.readfp(f)
            return conf_parser.to_dict()
    except (IOError, ConfigParser.Error) as e:
        return dict()


def hotword_detected_callack(hermes, intentMessage):
    #nur muten, wenn player spielt?
    #player.mute()
    h.player.pause()
    pass


def session_ended_callback(hermes, intentMessage):
    # nur unmuten, wenn player spielt?
    #player.unmute()
    h.player.unpause()
    pass


def volumeDown_callback(hermes, intentMessage):
    usecase = VolumeDownUseCase(hermes.server, hermes.player)
    volume_down_request = VolumeDownRequestAdapter.from_intent_message(intentMessage)

    response = usecase.execute(volume_down_request)
    if not response:
        print response.value
        hermes.publish_end_session(intentMessage.session_id, "An error occured.")
    else:
        print response
        hermes.publish_end_session(intentMessage.session_id, "")


def volumeUp_callback(hermes, intentMessage):
    usecase = VolumeUpUseCase(hermes.server, hermes.player)
    volume_up_request = VolumeUpRequestAdapter.from_intent_message(intentMessage)

    response = usecase.execute(volume_up_request)
    if not response:
        print response.value
        hermes.publish_end_session(intentMessage.session_id, "An error occured.")
    else:
        print response
        hermes.publish_end_session(intentMessage.session_id, "")


def mute_callback(hermes, intentMessage):
    usecase = MuteUseCase()
    mute_request = MuteRequestAdapter.from_intent_message(intentMessage)

    response = usecase.execute(mute_request)
    if not response:
        print response.value
        hermes.publish_end_session(intentMessage.session_id, "An error occured.")
    else:
        print response
        hermes.publish_end_session(intentMessage.session_id, "")


def getEthName():
    # Get name of the Ethernet interface
    interface = "None"
    try:
        for root, dirs, files in os.walk('/sys/class/net'):
            for dir in dirs:
                if dir[:3] == 'enx' or dir[:3] == 'eth':
                    interface = dir
    except:
        pass
    return interface


def getMAC(interface='eth0'):
    # Return the MAC address of the specified interface
    try:
        str = open('/sys/class/net/%s/address' % interface).read()
    except:
        str = "00:00:00:00:00:00"
    return str[0:17]


def speakerInterrupt_callback(hermes, intentMessage):
    usecase = SpeakerInterruptUseCase(hermes.server, hermes.player)
    speaker_interrupt_request = SpeakerInterruptRequestAdapter.from_intent_message(intentMessage)

    response = usecase.execute(speaker_interrupt_request)
    if not response:
        print response.value
        hermes.publish_end_session(intentMessage.session_id, "An error occured.")
    else:
        print response
        hermes.publish_end_session(intentMessage.session_id, "")


if __name__ == "__main__":
    configuration = read_configuration_file("config.ini")
    #client_id = configuration['secret']['client_id']
    #client_secret = configuration['secret']['client_secret']

    #ethName = getEthName()
    #ethMAC = getMAC(ethName)
    #print(ethMAC)

    with Hermes(HERMES_HOST) as h:
        servers = LMSDiscovery().all()
        h.server = LMSServer(servers[0]["host"], servers[0]["port"])
        h.player = h.server.get_player_from_ref(ref="b8:27:eb:cb:f0:d7")

        print(h.player.name)

        h \
            .subscribe_session_started(hotword_detected_callack) \
            .subscribe_session_ended(session_ended_callback) \
            .subscribe_intent("CrystalMethod:volumeUp2", volumeUp_callback) \
            .subscribe_intent("CrystalMethod:volumeDown2", volumeDown_callback) \
            .subscribe_intent("CrystalMethod:muteSound2", mute_callback) \
            .subscribe_intent("CrystalMethod:speakerInterrupt2", speakerInterrupt_callback) \
            .loop_forever()
