# coding: utf-8

"""
    Swagger Petstore

    This is a sample server Petstore server.  You can find out more about Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/).  For this sample, you can use the api key `special-key` to test the authorization filters.  # noqa: E501

    OpenAPI spec version: 1.0.6
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PetIdUploadImageBody(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'additional_metadata': 'str',
        'file': 'str'
    }

    attribute_map = {
        'additional_metadata': 'additionalMetadata',
        'file': 'file'
    }

    def __init__(self, additional_metadata=None, file=None):  # noqa: E501
        """PetIdUploadImageBody - a model defined in Swagger"""  # noqa: E501
        self._additional_metadata = None
        self._file = None
        self.discriminator = None
        if additional_metadata is not None:
            self.additional_metadata = additional_metadata
        if file is not None:
            self.file = file

    @property
    def additional_metadata(self):
        """Gets the additional_metadata of this PetIdUploadImageBody.  # noqa: E501

        Additional data to pass to server  # noqa: E501

        :return: The additional_metadata of this PetIdUploadImageBody.  # noqa: E501
        :rtype: str
        """
        return self._additional_metadata

    @additional_metadata.setter
    def additional_metadata(self, additional_metadata):
        """Sets the additional_metadata of this PetIdUploadImageBody.

        Additional data to pass to server  # noqa: E501

        :param additional_metadata: The additional_metadata of this PetIdUploadImageBody.  # noqa: E501
        :type: str
        """

        self._additional_metadata = additional_metadata

    @property
    def file(self):
        """Gets the file of this PetIdUploadImageBody.  # noqa: E501

        file to upload  # noqa: E501

        :return: The file of this PetIdUploadImageBody.  # noqa: E501
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this PetIdUploadImageBody.

        file to upload  # noqa: E501

        :param file: The file of this PetIdUploadImageBody.  # noqa: E501
        :type: str
        """

        self._file = file

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(PetIdUploadImageBody, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PetIdUploadImageBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
