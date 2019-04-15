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

from sib_api_v3_sdk.models.send_email_attachment import SendEmailAttachment  # noqa: F401,E501


class SendEmail(object):
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
        'email_to': 'list[str]',
        'email_bcc': 'list[str]',
        'email_cc': 'list[str]',
        'reply_to': 'str',
        'attachment_url': 'str',
        'attachment': 'list[SendEmailAttachment]',
        'headers': 'object',
        'attributes': 'object',
        'tags': 'list[str]'
    }

    attribute_map = {
        'email_to': 'emailTo',
        'email_bcc': 'emailBcc',
        'email_cc': 'emailCc',
        'reply_to': 'replyTo',
        'attachment_url': 'attachmentUrl',
        'attachment': 'attachment',
        'headers': 'headers',
        'attributes': 'attributes',
        'tags': 'tags'
    }

    def __init__(self, email_to=None, email_bcc=None, email_cc=None, reply_to=None, attachment_url=None, attachment=None, headers=None, attributes=None, tags=None):  # noqa: E501
        """SendEmail - a model defined in Swagger"""  # noqa: E501

        self._email_to = None
        self._email_bcc = None
        self._email_cc = None
        self._reply_to = None
        self._attachment_url = None
        self._attachment = None
        self._headers = None
        self._attributes = None
        self._tags = None
        self.discriminator = None

        self.email_to = email_to
        if email_bcc is not None:
            self.email_bcc = email_bcc
        if email_cc is not None:
            self.email_cc = email_cc
        if reply_to is not None:
            self.reply_to = reply_to
        if attachment_url is not None:
            self.attachment_url = attachment_url
        if attachment is not None:
            self.attachment = attachment
        if headers is not None:
            self.headers = headers
        if attributes is not None:
            self.attributes = attributes
        if tags is not None:
            self.tags = tags

    @property
    def email_to(self):
        """Gets the email_to of this SendEmail.  # noqa: E501

        List of the email addresses of the recipients. For example, ['abc@example.com', 'asd@example.com'].  # noqa: E501

        :return: The email_to of this SendEmail.  # noqa: E501
        :rtype: list[str]
        """
        return self._email_to

    @email_to.setter
    def email_to(self, email_to):
        """Sets the email_to of this SendEmail.

        List of the email addresses of the recipients. For example, ['abc@example.com', 'asd@example.com'].  # noqa: E501

        :param email_to: The email_to of this SendEmail.  # noqa: E501
        :type: list[str]
        """
        if email_to is None:
            raise ValueError("Invalid value for `email_to`, must not be `None`")  # noqa: E501

        self._email_to = email_to

    @property
    def email_bcc(self):
        """Gets the email_bcc of this SendEmail.  # noqa: E501

        List of the email addresses of the recipients in bcc  # noqa: E501

        :return: The email_bcc of this SendEmail.  # noqa: E501
        :rtype: list[str]
        """
        return self._email_bcc

    @email_bcc.setter
    def email_bcc(self, email_bcc):
        """Sets the email_bcc of this SendEmail.

        List of the email addresses of the recipients in bcc  # noqa: E501

        :param email_bcc: The email_bcc of this SendEmail.  # noqa: E501
        :type: list[str]
        """

        self._email_bcc = email_bcc

    @property
    def email_cc(self):
        """Gets the email_cc of this SendEmail.  # noqa: E501

        List of the email addresses of the recipients in cc  # noqa: E501

        :return: The email_cc of this SendEmail.  # noqa: E501
        :rtype: list[str]
        """
        return self._email_cc

    @email_cc.setter
    def email_cc(self, email_cc):
        """Sets the email_cc of this SendEmail.

        List of the email addresses of the recipients in cc  # noqa: E501

        :param email_cc: The email_cc of this SendEmail.  # noqa: E501
        :type: list[str]
        """

        self._email_cc = email_cc

    @property
    def reply_to(self):
        """Gets the reply_to of this SendEmail.  # noqa: E501

        Email address which shall be used by campaign recipients to reply back  # noqa: E501

        :return: The reply_to of this SendEmail.  # noqa: E501
        :rtype: str
        """
        return self._reply_to

    @reply_to.setter
    def reply_to(self, reply_to):
        """Sets the reply_to of this SendEmail.

        Email address which shall be used by campaign recipients to reply back  # noqa: E501

        :param reply_to: The reply_to of this SendEmail.  # noqa: E501
        :type: str
        """

        self._reply_to = reply_to

    @property
    def attachment_url(self):
        """Gets the attachment_url of this SendEmail.  # noqa: E501

        Absolute url of the attachment (no local file). Extension allowed: xlsx, xls, ods, docx, docm, doc, csv, pdf, txt, gif, jpg, jpeg, png, tif, tiff, rtf, bmp, cgm, css, shtml, html, htm, zip, xml, ppt, pptx, tar, ez, ics, mobi, msg, pub and eps  # noqa: E501

        :return: The attachment_url of this SendEmail.  # noqa: E501
        :rtype: str
        """
        return self._attachment_url

    @attachment_url.setter
    def attachment_url(self, attachment_url):
        """Sets the attachment_url of this SendEmail.

        Absolute url of the attachment (no local file). Extension allowed: xlsx, xls, ods, docx, docm, doc, csv, pdf, txt, gif, jpg, jpeg, png, tif, tiff, rtf, bmp, cgm, css, shtml, html, htm, zip, xml, ppt, pptx, tar, ez, ics, mobi, msg, pub and eps  # noqa: E501

        :param attachment_url: The attachment_url of this SendEmail.  # noqa: E501
        :type: str
        """

        self._attachment_url = attachment_url

    @property
    def attachment(self):
        """Gets the attachment of this SendEmail.  # noqa: E501

        Pass the list of content (base64 encoded) and name of the attachment. For example, [{'content':'base64 encoded content 1', 'name':'attcahment1'}, {'content':'base64 encoded content 2', 'name':'attcahment2'}].  # noqa: E501

        :return: The attachment of this SendEmail.  # noqa: E501
        :rtype: list[SendEmailAttachment]
        """
        return self._attachment

    @attachment.setter
    def attachment(self, attachment):
        """Sets the attachment of this SendEmail.

        Pass the list of content (base64 encoded) and name of the attachment. For example, [{'content':'base64 encoded content 1', 'name':'attcahment1'}, {'content':'base64 encoded content 2', 'name':'attcahment2'}].  # noqa: E501

        :param attachment: The attachment of this SendEmail.  # noqa: E501
        :type: list[SendEmailAttachment]
        """

        self._attachment = attachment

    @property
    def headers(self):
        """Gets the headers of this SendEmail.  # noqa: E501

        Pass the set of headers that shall be sent along the mail headers in the original email. 'sender.ip' header can be set (only for dedicated ip users) to mention the IP to be used for sending transactional emails. For example, {'Content-Type':'text/html', 'charset':'iso-8859-1', 'sender.ip':'1.2.3.4'}  # noqa: E501

        :return: The headers of this SendEmail.  # noqa: E501
        :rtype: object
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this SendEmail.

        Pass the set of headers that shall be sent along the mail headers in the original email. 'sender.ip' header can be set (only for dedicated ip users) to mention the IP to be used for sending transactional emails. For example, {'Content-Type':'text/html', 'charset':'iso-8859-1', 'sender.ip':'1.2.3.4'}  # noqa: E501

        :param headers: The headers of this SendEmail.  # noqa: E501
        :type: object
        """

        self._headers = headers

    @property
    def attributes(self):
        """Gets the attributes of this SendEmail.  # noqa: E501

        Pass the set of attributes to customize the template. For example, {'FNAME':'Joe', 'LNAME':'Doe'}  # noqa: E501

        :return: The attributes of this SendEmail.  # noqa: E501
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this SendEmail.

        Pass the set of attributes to customize the template. For example, {'FNAME':'Joe', 'LNAME':'Doe'}  # noqa: E501

        :param attributes: The attributes of this SendEmail.  # noqa: E501
        :type: object
        """

        self._attributes = attributes

    @property
    def tags(self):
        """Gets the tags of this SendEmail.  # noqa: E501

        Tag your emails to find them more easily  # noqa: E501

        :return: The tags of this SendEmail.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this SendEmail.

        Tag your emails to find them more easily  # noqa: E501

        :param tags: The tags of this SendEmail.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

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
        if not isinstance(other, SendEmail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
