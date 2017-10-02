#!/usr/bin/env python

import context
from ispyb.connection import Connection, get_connection_class
from nose import with_setup
from ispyb.sp.mxacquisition import mxacquisition
from ispyb.sp.emacquisition import emacquisition
from testtools import get_connection

def test_insert_motion_correction():
    conn = get_connection()
    group_params = mxacquisition.get_data_collection_group_params()
    group_params['parentid'] = 55168
    group_id = mxacquisition.insert_data_collection_group(conn, group_params.values())
    collection_params = mxacquisition.get_data_collection_params()
    collection_params['parentid'] = group_id
    dc_id = mxacquisition.insert_data_collection(conn, collection_params.values())
    params = emacquisition.get_motion_correction_params()
    params["dataCollectionId"] = dc_id
    params["dosePerFrame"] = 20
    motion_cor_id = emacquisition.insert_motion_correction(conn, params.values())
    conn.disconnect()
    assert motion_cor_id is not None

def test_insert_ctf():
    conn = get_connection()
    group_params = mxacquisition.get_data_collection_group_params()
    group_params['parentid'] = 55168
    group_id = mxacquisition.insert_data_collection_group(conn, group_params.values())
    collection_params = mxacquisition.get_data_collection_params()
    collection_params['parentid'] = group_id
    dc_id = mxacquisition.insert_data_collection(conn, collection_params.values())

    params = emacquisition.get_motion_correction_params()
    params["dataCollectionId"] = dc_id
    params["dosePerFrame"] = 20
    motion_cor_id = emacquisition.insert_motion_correction(conn, params.values())

    params = emacquisition.get_ctf_params()
    params['motionCorrectionId'] = motion_cor_id
    ctf_id = emacquisition.insert_ctf(conn, params.values())
    conn.disconnect()
    assert ctf_id is not None
