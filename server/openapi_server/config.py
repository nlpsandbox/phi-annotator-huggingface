import os
from enum import Enum

defaultValues = {
    "CONFIG_NAME": "",
    "MODEL_NAME": ""
}


class ConfigName(Enum):
    BERT_BASE_NER = "bert-base-ner"
    BERT_BASE_NER_UNCASED = "bert-base-ner-uncased"
    BERT_LARGE_NER = "bert-large-ner"


class AbstractConfig(object):
    """
    Parent class containing get_property to return the environment variable or
    default value if not found.
    """
    def __init__(self):
        self._defaultValues = defaultValues

    def get_property(self, property_name):
        if os.getenv(property_name) is not None:
            return os.getenv(property_name)
        # we don't want KeyError?
        if property_name not in self._defaultValues.keys():
            return None  # No default value found
        # return default value
        return self._defaultValues[property_name]


class Config(AbstractConfig):
    """
    This class is used to provide coniguration values to the application, first
    using environment variables and if not found, defaulting to those values
    provided in the defaultValues dictionary above.
    """

    @property
    def config_name(self):
        return self.get_property('CONFIG_NAME')

    @property
    def model_name(self):
        return self.get_property('MODEL_NAME')


config = Config()
