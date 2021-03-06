# flake8: noqa
# -*- coding: utf-8 -*-
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

import json

from airflow.operators.slack_operator import SlackAPIOperator
from airflow.utils.decorators import apply_defaults


class SlackAPIPostOperator(SlackAPIOperator):
    """
    Posts messages to a slack channel

    :param slack_conn_id: Slack connection ID which its password is Slack API token
    :type slack_conn_id: str
    :param token: Slack API token (https://api.slack.com/web)
    :type token: str
    :param method: The Slack API Method to Call (https://api.slack.com/methods)
    :type method: str
    :param api_params: API Method call parameters (https://api.slack.com/methods)
    :type api_params: dict
    :param channel: channel in which to post message on slack name (#general) or
        ID (C12318391). (templated)
    :type channel: str
    :param username: Username that airflow will be posting to Slack as. (templated)
    :type username: str
    :param text: message to send to slack. (templated)
    :type text: str
    :param icon_url: url to icon used for this message
    :type icon_url: str
    :param attachments: extra formatting details. (templated)
        - see https://api.slack.com/docs/attachments.
    :type attachments: list of hashes
    :param blocks: extra block layouts. (templated)
        - see https://api.slack.com/reference/block-kit/blocks.
    :type blocks: list of hashes
    """

    template_fields = ('username', 'text', 'attachments', 'blocks', 'channel')
    ui_color = '#FFBA40'

    @apply_defaults
    def __init__(self,
                 slack_conn_id=None,
                 token=None,
                 api_params=None,
                 channel='#general',
                 username='Airflow',
                 text='No message has been set.\n'
                      'Here is a cat video instead\n'
                      'https://www.youtube.com/watch?v=J---aiyznGQ',
                 icon_url='https://raw.githubusercontent.com/apache/'
                          'airflow/master/airflow/www/static/pin_100.png',
                 attachments=None,
                 blocks=None,
                 *args, **kwargs):
        self.method = 'chat.postMessage'
        self.channel = channel
        self.username = username
        self.text = text
        self.icon_url = icon_url
        self.attachments = attachments or []
        self.blocks = blocks or []
        super(SlackAPIPostOperator, self).__init__(method=self.method,
                                                   token=token,
                                                   slack_conn_id=slack_conn_id,
                                                   api_params=api_params,
                                                   *args, **kwargs)

    def construct_api_call_params(self):
        self.api_params = {
            'channel': self.channel,
            'username': self.username,
            'text': self.text,
            'icon_url': self.icon_url,
            'attachments': json.dumps(self.attachments),
            'blocks': json.dumps(self.blocks),
        }
