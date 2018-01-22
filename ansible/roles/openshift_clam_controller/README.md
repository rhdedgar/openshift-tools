openshift_clam_controller
=========

Ansible role for creating and configuring the oso-clam-controller container and daemonset

Requirements
------------

Ansible Modules:

- tools_roles/lib_openshift_3.2


Role Variables
--------------

- `occ_namespace`: The project namespace in which the application should be deployed.
- `occ_aws_creds_content`: credentials of the S3 bucket to which we upload files.
- `occ_aws_config_content`: locations of various config and logfiles needed by scanlog_listener.
- `occ_nodes`: Apply the clam-controller-enabled=True label to nodes matching value of occ_nodes list.
- `occ_zagg_config`: A dictionary with config data for the ZAGG monitoring client, to populate `zagg_client.yaml`. Expected values: `hostgroups`, `url`, `user`, `password`, `ssl_verify`, `verbose` and `debug`. The value `occ_zagg_config.hostgroups` should be a list of host group names.

Dependencies
------------


Example Playbook
----------------


License
-------

Apache 2.0

Author Information
------------------

Openshift Operations
