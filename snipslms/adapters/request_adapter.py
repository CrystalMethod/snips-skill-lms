from snipslms.use_cases.request_objects import MuteRequestObject, SpeakerInterruptRequestObject, VolumeDownRequestObject, VolumeUpRequestObject


class VolumeUpRequestAdapter(object):

    @classmethod
    def from_intent_message(cls, intentMessage):
        slots_dict = cls.extract_slots_dictionary(intentMessage)
        return VolumeUpRequestObject.from_dict(slots_dict)

    @staticmethod
    def extract_slots_dictionary(intentMessage):
        slots_dict = dict()
        if len(intentMessage.slots.indicator_room):
            slots_dict.update({'room': intentMessage.slots.indicator_room.first().value})
        return slots_dict


class VolumeDownRequestAdapter(object):

    @classmethod
    def from_intent_message(cls, intentMessage):
        slots_dict = cls.extract_slots_dictionary(intentMessage)
        return VolumeDownRequestObject.from_dict(slots_dict)

    @staticmethod
    def extract_slots_dictionary(intentMessage):
        slots_dict = dict()
        if len(intentMessage.slots.indicator_room):
            slots_dict.update({'room': intentMessage.slots.indicator_room.first().value})
        return slots_dict


class MuteRequestAdapter(object):

    @classmethod
    def from_intent_message(cls, intentMessage):
        slots_dict = cls.extract_slots_dictionary(intentMessage)
        return MuteRequestObject.from_dict(slots_dict)

    @staticmethod
    def extract_slots_dictionary(intentMessage):
        slots_dict = dict()
        if len(intentMessage.slots.indicator_room):
            slots_dict.update({'room': intentMessage.slots.indicator_room.first().value})
        return slots_dict


class SpeakerInterruptRequestAdapter(object):

    @classmethod
    def from_intent_message(cls, intentMessage):
        slots_dict = cls.extract_slots_dictionary(intentMessage)
        return SpeakerInterruptRequestObject.from_dict(slots_dict)

    @staticmethod
    def extract_slots_dictionary(intentMessage):
        slots_dict = dict()
        if len(intentMessage.slots.indicator_room):
            slots_dict.update({'room': intentMessage.slots.indicator_room.first().value})
        return slots_dict
