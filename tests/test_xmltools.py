#!/usr/bin/env python

import context
from nose import with_setup
import sys
import os
from xml.etree import ElementTree
from datetime import datetime
from ispyb.connection import Connection, get_connection_class
from ispyb.xmltools import XmlDictConfig, mx_data_reduction_xml_to_ispyb
from testtools import get_connection

def test_mx_data_reduction_xml_to_ispyb():
    conn = get_connection()
    cursor = conn.get_cursor()

    xml_file = 'data/mx_data_reduction_pipeline_results.xml'
    # Convert the XML to a dictionary
    tree = ElementTree.parse(xml_file)
    xmldict = XmlDictConfig( tree.getroot() )

    # Find the datacollection associated with this data reduction run
    xml_dir = os.path.split(xml_file)[0]
    try:
        dc_id = int(open(os.path.join(xml_dir, '.dc_id'), 'r').read())
        print 'Got DC ID %d from file system' % dc_id
    except:
        dc_id = None

    (app_id, ap_id, scaling_id, integration_id) = mx_data_reduction_xml_to_ispyb(xmldict, dc_id, cursor)

    # Output results xml
    xml = '<?xml version="1.0" encoding="ISO-8859-1"?>'\
            '<dbstatus><autoProcProgramId>%d</autoProcProgramId>'\
            '<autoProcId>%d</autoProcId>'\
            '<autoProcScalingId>%d</autoProcScalingId>'\
            '<autoProcIntegrationId>%d</autoProcIntegrationId>'\
            '<code>ok</code></dbstatus>' % (app_id, ap_id, scaling_id, integration_id)
    print(xml)
    conn.disconnect()
