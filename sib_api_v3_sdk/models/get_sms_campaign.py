# coding: utf-8

"""
    SendinBlue API

    SendinBlue provide a RESTFul API that can be used with any languages. With this API, you will be able to :   - Manage your campaigns and get the statistics   - Manage your contacts   - Send transactional Emails and SMS   - and much more...  You can download our wrappers at https://github.com/orgs/sendinblue  **Possible responses**   | Code | Message |   | :-------------: | ------------- |   | 200  | OK. Successful Request  |   | 201  | OK. Successful Creation |   | 202  | OK. Request accepted |   | 204  | OK. Successful Update/Deletion  |   | 400  | Error. Bad Request  |   | 401  | Error. Authentication Needed  |   | 402  | Error. Not enough credit, plan upgrade needed  |   | 403  | Error. Permission denied  |   | 404  | Error. Object does not exist |   | 405  | Error. Method not allowed  |   # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: contact@sendinblue.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from sib_api_v3_sdk.models.get_sms_campaign_overview import GetSmsCampaignOverview  # noqa: F401,E501


class GetSmsCampaign(object):
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
        'id': 'int',
        'name': 'str',
        'status': 'str',
        'content': 'str',
        'scheduled_at': 'datetime',
        'sender': 'str',
        'created_at': 'datetime',
        'modified_at': 'datetime',
        'recipients': 'object',
        'statistics': 'object'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'content': 'content',
        'scheduled_at': 'scheduledAt',
        'sender': 'sender',
        'created_at': 'createdAt',
        'modified_at': 'modifiedAt',
        'recipients': 'recipients',
        'statistics': 'statistics'
    }

    def __init__(self, id=None, name=None, status=None, content=None, scheduled_at=None, sender=None, created_at=None, modified_at=None, recipients=None, statistics=None):  # noqa: E501
        """GetSmsCampaign - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._status = None
        self._content = None
        self._scheduled_at = None
        self._sender = None
        self._created_at = None
        self._modified_at = None
        self._recipients = None
        self._statistics = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.status = status
        self.content = content
        self.scheduled_at = scheduled_at
        self.sender = sender
        self.created_at = created_at
        self.modified_at = modified_at
        self.recipients = recipients
        self.statistics = statistics

    @property
    def id(self):
        """Gets the id of this GetSmsCampaign.  # noqa: E501

        ID of the SMS Campaign  # noqa: E501

        :return: The id of this GetSmsCampaign.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetSmsCampaign.

        ID of the SMS Campaign  # noqa: E501

        :param id: The id of this GetSmsCampaign.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this GetSmsCampaign.  # noqa: E501

        Name of the SMS Campaign  # noqa: E501

        :return: The name of this GetSmsCampaign.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetSmsCampaign.

        Name of the SMS Campaign  # noqa: E501

        :param name: The name of this GetSmsCampaign.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def status(self):
        """Gets the status of this GetSmsCampaign.  # noqa: E501

        Status of the SMS Campaign  # noqa: E501

        :return: The status of this GetSmsCampaign.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GetSmsCampaign.

        Status of the SMS Campaign  # noqa: E501

        :param status: The status of this GetSmsCampaign.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["draft", "sent", "archive", "queued", "suspended", "inProcess"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def content(self):
        """Gets the content of this GetSmsCampaign.  # noqa: E501

        Content of the SMS Campaign  # noqa: E501

        :return: The content of this GetSmsCampaign.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this GetSmsCampaign.

        Content of the SMS Campaign  # noqa: E501

        :param content: The content of this GetSmsCampaign.  # noqa: E501
        :type: str
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

    @property
    def scheduled_at(self):
        """Gets the scheduled_at of this GetSmsCampaign.  # noqa: E501

        UTC date-time on which SMS campaign is scheduled. Should be in YYYY-MM-DDTHH:mm:ss.SSSZ format  # noqa: E501

        :return: The scheduled_at of this GetSmsCampaign.  # noqa: E501
        :rtype: datetime
        """
        return self._scheduled_at

    @scheduled_at.setter
    def scheduled_at(self, scheduled_at):
        """Sets the scheduled_at of this GetSmsCampaign.

        UTC date-time on which SMS campaign is scheduled. Should be in YYYY-MM-DDTHH:mm:ss.SSSZ format  # noqa: E501

        :param scheduled_at: The scheduled_at of this GetSmsCampaign.  # noqa: E501
        :type: datetime
        """
        if scheduled_at is None:
            raise ValueError("Invalid value for `scheduled_at`, must not be `None`")  # noqa: E501

        self._scheduled_at = scheduled_at

    @property
    def sender(self):
        """Gets the sender of this GetSmsCampaign.  # noqa: E501

        Sender of the SMS Campaign  # noqa: E501

        :return: The sender of this GetSmsCampaign.  # noqa: E501
        :rtype: str
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """Sets the sender of this GetSmsCampaign.

        Sender of the SMS Campaign  # noqa: E501

        :param sender: The sender of this GetSmsCampaign.  # noqa: E501
        :type: str
        """
        if sender is None:
            raise ValueError("Invalid value for `sender`, must not be `None`")  # noqa: E501

        self._sender = sender

    @property
    def created_at(self):
        """Gets the created_at of this GetSmsCampaign.  # noqa: E501

        Creation UTC date-time of the SMS campaign (YYYY-MM-DDTHH:mm:ss.SSSZ)  # noqa: E501

        :return: The created_at of this GetSmsCampaign.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this GetSmsCampaign.

        Creation UTC date-time of the SMS campaign (YYYY-MM-DDTHH:mm:ss.SSSZ)  # noqa: E501

        :param created_at: The created_at of this GetSmsCampaign.  # noqa: E501
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def modified_at(self):
        """Gets the modified_at of this GetSmsCampaign.  # noqa: E501

        UTC date-time of last modification of the SMS campaign (YYYY-MM-DDTHH:mm:ss.SSSZ)  # noqa: E501

        :return: The modified_at of this GetSmsCampaign.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this GetSmsCampaign.

        UTC date-time of last modification of the SMS campaign (YYYY-MM-DDTHH:mm:ss.SSSZ)  # noqa: E501

        :param modified_at: The modified_at of this GetSmsCampaign.  # noqa: E501
        :type: datetime
        """
        if modified_at is None:
            raise ValueError("Invalid value for `modified_at`, must not be `None`")  # noqa: E501

        self._modified_at = modified_at

    @property
    def recipients(self):
        """Gets the recipients of this GetSmsCampaign.  # noqa: E501


        :return: The recipients of this GetSmsCampaign.  # noqa: E501
        :rtype: object
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        """Sets the recipients of this GetSmsCampaign.


        :param recipients: The recipients of this GetSmsCampaign.  # noqa: E501
        :type: object
        """
        if recipients is None:
            raise ValueError("Invalid value for `recipients`, must not be `None`")  # noqa: E501

        self._recipients = recipients

    @property
    def statistics(self):
        """Gets the statistics of this GetSmsCampaign.  # noqa: E501


        :return: The statistics of this GetSmsCampaign.  # noqa: E501
        :rtype: object
        """
        return self._statistics

    @statistics.setter
    def statistics(self, statistics):
        """Sets the statistics of this GetSmsCampaign.


        :param statistics: The statistics of this GetSmsCampaign.  # noqa: E501
        :type: object
        """
        if statistics is None:
            raise ValueError("Invalid value for `statistics`, must not be `None`")  # noqa: E501

        self._statistics = statistics

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GetSmsCampaign):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
