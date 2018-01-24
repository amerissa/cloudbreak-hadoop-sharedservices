# Hadoop Shared Services On The Cloud

## Introduction:
The concept is to centralize the management layer of running clusters while allowing clients to spin up their own clusters and focus solely on compute. The following components will be centralized:
1. Hive Metastore: All table and database definitions will be centralized and managed. Creating a table on S3 in one cluster will result in other current and future clusters knowing about that table and being able to use it.
2. S3 Storage: The blueprints will contain S3 keys and allow Hive to use tables on S3. The data does not need to be duplicated per cluster.
3. Ranger: A centralized Ranger with one Hive repository will manage the permissions to Hive across all clusters. Operational teams will ensure security is respected across the client clusters
4. Ambari-Infra: All logs and audit information will be centralized with an identifier of which user is accessing which tables on which cluster.
5. Atlas: Metadata data and tags will be tracked centrally.

Cloudbreak is the chosen solution to deploy the clusters.

The generator script will generate both parent cluster blueprint and client cluster blueprint. The script will pause until the parent cluster is generated so you can provide it with the hostnames of the specific host groups


## Features:

1. Namenode HA out of the box
2. Resource Manager HA out of the Box
3. Ambari Infra HA
4. Scalability of worker nodes
5. Kerberos integration can be done using https://github.com/amerissa/cloudbreak-krb-recipe


## Requirements:
* Python 2.7
* Jinja2

## Usage:

> git clone git@github.com:amerissa/cloudbreak-hadoop-sharedservices.git
>
> cd cloudbreak-hadoop-sharedservices
>
> ./generator.py
