# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    OpenAPI spec version: 1.1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class StopWatch(object):
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
        'created': 'datetime',
        'issue_index': 'int'
    }

    attribute_map = {
        'created': 'created',
        'issue_index': 'issue_index'
    }

    def __init__(self, created=None, issue_index=None):  # noqa: E501
        """StopWatch - a model defined in Swagger"""  # noqa: E501

        self._created = None
        self._issue_index = None
        self.discriminator = None

        if created is not None:
            self.created = created
        if issue_index is not None:
            self.issue_index = issue_index

    @property
    def created(self):
        """Gets the created of this StopWatch.  # noqa: E501


        :return: The created of this StopWatch.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this StopWatch.


        :param created: The created of this StopWatch.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def issue_index(self):
        """Gets the issue_index of this StopWatch.  # noqa: E501


        :return: The issue_index of this StopWatch.  # noqa: E501
        :rtype: int
        """
        return self._issue_index

    @issue_index.setter
    def issue_index(self, issue_index):
        """Sets the issue_index of this StopWatch.


        :param issue_index: The issue_index of this StopWatch.  # noqa: E501
        :type: int
        """

        self._issue_index = issue_index

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
        if issubclass(StopWatch, dict):
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
        if not isinstance(other, StopWatch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
