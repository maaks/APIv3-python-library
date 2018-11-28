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


class GetEmailEventReportEvents(object):
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
        'email': 'str',
        'date': 'datetime',
        'subject': 'str',
        'message_id': 'str',
        'event': 'str',
        'reason': 'str',
        'tag': 'str',
        'ip': 'str',
        'link': 'str',
        '_from': 'str'
    }

    attribute_map = {
        'email': 'email',
        'date': 'date',
        'subject': 'subject',
        'message_id': 'messageId',
        'event': 'event',
        'reason': 'reason',
        'tag': 'tag',
        'ip': 'ip',
        'link': 'link',
        '_from': 'from'
    }

    def __init__(self, email=None, date=None, subject=None, message_id=None, event=None, reason=None, tag=None, ip=None, link=None, _from=None):  # noqa: E501
        """GetEmailEventReportEvents - a model defined in Swagger"""  # noqa: E501

        self._email = None
        self._date = None
        self._subject = None
        self._message_id = None
        self._event = None
        self._reason = None
        self._tag = None
        self._ip = None
        self._link = None
        self.__from = None
        self.discriminator = None

        self.email = email
        self.date = date
        if subject is not None:
            self.subject = subject
        self.message_id = message_id
        self.event = event
        if reason is not None:
            self.reason = reason
        if tag is not None:
            self.tag = tag
        if ip is not None:
            self.ip = ip
        if link is not None:
            self.link = link
        if _from is not None:
            self._from = _from

    @property
    def email(self):
        """Gets the email of this GetEmailEventReportEvents.  # noqa: E501

        Email address which generates the event  # noqa: E501

        :return: The email of this GetEmailEventReportEvents.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this GetEmailEventReportEvents.

        Email address which generates the event  # noqa: E501

        :param email: The email of this GetEmailEventReportEvents.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def date(self):
        """Gets the date of this GetEmailEventReportEvents.  # noqa: E501

        UTC date-time on which the event has been generated  # noqa: E501

        :return: The date of this GetEmailEventReportEvents.  # noqa: E501
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this GetEmailEventReportEvents.

        UTC date-time on which the event has been generated  # noqa: E501

        :param date: The date of this GetEmailEventReportEvents.  # noqa: E501
        :type: datetime
        """
        if date is None:
            raise ValueError("Invalid value for `date`, must not be `None`")  # noqa: E501

        self._date = date

    @property
    def subject(self):
        """Gets the subject of this GetEmailEventReportEvents.  # noqa: E501

        Subject of the event  # noqa: E501

        :return: The subject of this GetEmailEventReportEvents.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this GetEmailEventReportEvents.

        Subject of the event  # noqa: E501

        :param subject: The subject of this GetEmailEventReportEvents.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def message_id(self):
        """Gets the message_id of this GetEmailEventReportEvents.  # noqa: E501

        Message ID which generated the event  # noqa: E501

        :return: The message_id of this GetEmailEventReportEvents.  # noqa: E501
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        """Sets the message_id of this GetEmailEventReportEvents.

        Message ID which generated the event  # noqa: E501

        :param message_id: The message_id of this GetEmailEventReportEvents.  # noqa: E501
        :type: str
        """
        if message_id is None:
            raise ValueError("Invalid value for `message_id`, must not be `None`")  # noqa: E501

        self._message_id = message_id

    @property
    def event(self):
        """Gets the event of this GetEmailEventReportEvents.  # noqa: E501

        Event which occurred  # noqa: E501

        :return: The event of this GetEmailEventReportEvents.  # noqa: E501
        :rtype: str
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this GetEmailEventReportEvents.

        Event which occurred  # noqa: E501

        :param event: The event of this GetEmailEventReportEvents.  # noqa: E501
        :type: str
        """
        if event is None:
            raise ValueError("Invalid value for `event`, must not be `None`")  # noqa: E501
        allowed_values = ["bounces", "hardBounces", "softBounces", "delivered", "spam", "requests", "opened", "clicks", "invalid", "deferred", "blocked", "unsubscribed"]  # noqa: E501
        if event not in allowed_values:
            raise ValueError(
                "Invalid value for `event` ({0}), must be one of {1}"  # noqa: E501
                .format(event, allowed_values)
            )

        self._event = event

    @property
    def reason(self):
        """Gets the reason of this GetEmailEventReportEvents.  # noqa: E501

        Reason of bounce (only available if the event is hardbounce or softbounce)  # noqa: E501

        :return: The reason of this GetEmailEventReportEvents.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this GetEmailEventReportEvents.

        Reason of bounce (only available if the event is hardbounce or softbounce)  # noqa: E501

        :param reason: The reason of this GetEmailEventReportEvents.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def tag(self):
        """Gets the tag of this GetEmailEventReportEvents.  # noqa: E501

        Tag of the email which generated the event  # noqa: E501

        :return: The tag of this GetEmailEventReportEvents.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this GetEmailEventReportEvents.

        Tag of the email which generated the event  # noqa: E501

        :param tag: The tag of this GetEmailEventReportEvents.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def ip(self):
        """Gets the ip of this GetEmailEventReportEvents.  # noqa: E501

        IP from which the user has opened the email or clicked on the link (only available if the event is opened or clicks)  # noqa: E501

        :return: The ip of this GetEmailEventReportEvents.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this GetEmailEventReportEvents.

        IP from which the user has opened the email or clicked on the link (only available if the event is opened or clicks)  # noqa: E501

        :param ip: The ip of this GetEmailEventReportEvents.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def link(self):
        """Gets the link of this GetEmailEventReportEvents.  # noqa: E501

        The link which is sent to the user (only available if the event is requests or opened or clicks)  # noqa: E501

        :return: The link of this GetEmailEventReportEvents.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this GetEmailEventReportEvents.

        The link which is sent to the user (only available if the event is requests or opened or clicks)  # noqa: E501

        :param link: The link of this GetEmailEventReportEvents.  # noqa: E501
        :type: str
        """

        self._link = link

    @property
    def _from(self):
        """Gets the _from of this GetEmailEventReportEvents.  # noqa: E501

        Sender email from which the emails are sent  # noqa: E501

        :return: The _from of this GetEmailEventReportEvents.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this GetEmailEventReportEvents.

        Sender email from which the emails are sent  # noqa: E501

        :param _from: The _from of this GetEmailEventReportEvents.  # noqa: E501
        :type: str
        """

        self.__from = _from

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
        if not isinstance(other, GetEmailEventReportEvents):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
