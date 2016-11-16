#!/bin/env python
# vim: expandtab:tabstop=4:shiftwidth=4

"""
 This script is used to test basic SSO services and report to Zabbix.
 It tries to get a temporary token from the IDP host, and use it to authenticate to each
 of our ops-manged AWS accounts as found in ~/etc/openshift_tools/aws_accounts.txt.
 It will run an IAM command and report an issue to Zabbix if any received HTTP status codes != 200.
"""


import os
import yaml

# Reason: disable pylint import-error because our modules aren't loaded on jenkins.
# pylint: disable=import-error
import boto3

import saml_aws_creds
from openshift_tools.monitoring.zagg_sender import ZaggSender


class CheckIam(object):
    """ Class to check HTTP return codes of IAM commands. """


    def __init__(self):
        self.client = None


    @staticmethod
    def check_accounts():
        """ Retrieves a list of the config-managed ops AWS accounts.

        Returns:
            A list containing each of the lines found in the aws accounts file

        Raises:
            A ValueError if the path does not exist
        """

        config_path = '/etc/openshift_tools/sso-config.yaml'
        if os.path.isfile(config_path):
            with open(config_path, 'r') as sso_config:
                yaml_config = yaml.load(sso_config)

                if yaml_config["aws_account_file"]:
                    path = yaml_config["aws_account_file"]

        accounts_list = []

        if os.path.isfile(path):
            with open(path) as open_file:
                stripped_line = list([line.rstrip() for line in open_file.readlines()])
                for line in stripped_line:
                    if line is not None:
                        accounts_list.append(line)
                return accounts_list
        else:
            raise ValueError(path + ' does not exist.')


    @staticmethod
    def get_token(aws_account):
        """ Generate temporary SSO access credentials.

        Requires the config file containing the IDP hostname.

        Returns:
            A temporary boto3 client created with a session token provided by the IDP host.

        Raises:
            A ValueError if the config path can not be found.
        """

        sso_config_path = '/etc/openshift_tools/sso-config.yaml'

        if os.path.isfile(sso_config_path):
            with open(sso_config_path, 'r') as sso_config:
                yaml_config = yaml.load(sso_config)

                if yaml_config["idp_host"]:
                    ops_idp_host = yaml_config["idp_host"]

                creds = saml_aws_creds.get_temp_credentials(
                    metadata_id='urn:amazon:webservices:%s' % aws_account,
                    idp_host=ops_idp_host
                    )

                client = boto3.client(
                    'iam',
                    aws_access_key_id=creds['AccessKeyId'],
                    aws_secret_access_key=creds['SecretAccessKey'],
                    aws_session_token=creds['SessionToken']
                    )

                return client

        else:
            raise ValueError(sso_config_path + 'does not exist.')


    def main(self):
        """ Main function. """

        zag = ZaggSender()
        ops_accounts = self.check_accounts()
        zabbix_key = "sso.iam.not.reachable"
        key_value = 0

        for account in ops_accounts:
            account_number = account[0].split(':')[1]
            temp_client = CHECK.get_token(account_number)
            acc_status = temp_client.get_role(RoleName='iam_monitoring')

            if acc_status['ResponseMetadata']['HTTPStatusCode'] != 200:
                key_value += 1

        # or have if key_status > 0 send a 1 to zabbix
        zag.add_zabbix_keys({zabbix_key: key_value})
        zag.send_metrics()

if __name__ == '__main__':
    CHECK = CheckIam()
    CHECK.main()
