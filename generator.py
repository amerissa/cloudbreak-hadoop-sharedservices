#!/usr/bin/env python
import os
import jinja2


def render(tpl_path, context):
    path, filename = os.path.split(tpl_path)
    return(jinja2.Environment(loader=jinja2.FileSystemLoader(path or './')).get_template(filename).render(context))


s3key = raw_input('S3 Key: ')
s3secret = raw_input('S3 Secret: ')

hivedbhost = raw_input('Hive Metastore DB Host: ')
hivedbname = raw_input('Hive Metastore DB Name: ')
hivedbuser = raw_input('Hive Metastore DB User: ')
hivedbpassword = raw_input('Hive Metastore DB Password: ')

rangerdbhost = raw_input('Ranger DB Host: ')
rangerdbname = raw_input('Ranger DB Name: ')
rangerdbuser = raw_input('Ranger DB User: ')
rangerdbpassword = raw_input('Ranger DB Password: ')


rangeradminpassword = raw_input('Ranger Ambari Admin Password: ')

context = { 's3key' : s3key, 's3secret' : s3secret, 'hivedbname' : hivedbname, 'hivedbhost' : hivedbhost, 'hivedbuser' : hivedbuser, 'hivedbpassword' : hivedbpassword, 'rangerdbhost' : rangerdbhost, 'rangerdbname' : rangerdbname, 'rangerdbuser' : rangerdbuser, 'rangerdbpassword' : rangerdbpassword, 'rangeradminpassword' : rangeradminpassword }


parent = render('./parentcluster.template', context)
parentjson = open('./parentblueprint.json', 'w')
parentjson.write(parent)
parentjson.close()
print('Parent Blueprint has been generated at ./parentblueprint.json. Wait until the cluster is up and input the hostname of the following host groups.')

master1 = raw_input('Master1 Server form Parent Cluster: ')
master2 = raw_input('Master2 Server form Parent Cluster: ')
master3 = raw_input('Master3 Server form Parent Cluster: ')

context = { 's3key' : s3key, 's3secret' : s3secret, 'master1' : master1, "master2" : master2, "master3" : master3, 'rangeradminpassword' : rangeradminpassword, 'hivedbname' : hivedbname, 'hivedbhost' : hivedbhost, 'hivedbuser' : hivedbuser, 'hivedbpassword' : hivedbpassword }
child = render('./clientcluster.template', context)
childjson = open('./childblueprint.json', 'w')
childjson.write(child)
childjson.close()
