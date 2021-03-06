from __future__ import division, print_function

import context
import ispyb.factory

def test_upsert_sample(testconfig):
  with ispyb.open(testconfig) as conn:
        core = ispyb.factory.create_data_area(ispyb.factory.DataAreaType.CORE, conn)
        params = core.get_sample_params()
        params['containerid'] = 1326
        params['crystalid'] = 3918
        params['name'] = 'Sample-010101'
        params['code'] = 'SAM-010101'
        id = core.upsert_sample(list(params.values()))
        assert id is not None

def test_retrieve_visit_id(testconfig):
  with ispyb.open(testconfig) as conn:
        core = ispyb.factory.create_data_area(ispyb.factory.DataAreaType.CORE, conn)
        id = core.retrieve_visit_id('cm14451-2')
        assert id == 55168

def test_retrieve_current_sessions(testconfig):
  with ispyb.open(testconfig) as conn:
        core = ispyb.factory.create_data_area(ispyb.factory.DataAreaType.CORE, conn)
        rs = core.retrieve_current_sessions('i03', 24*60*30000)
        assert len(rs) > 0

def test_retrieve_current_sessions_for_person(testconfig):
  with ispyb.open(testconfig) as conn:
        core = ispyb.factory.create_data_area(ispyb.factory.DataAreaType.CORE, conn)
        rs = core.retrieve_current_sessions_for_person('i03', 'boaty', tolerance_mins=24*60*30000)
        assert len(rs) > 0

def test_retrieve_most_recent_session(testconfig):
  with ispyb.open(testconfig) as conn:
        core = ispyb.factory.create_data_area(ispyb.factory.DataAreaType.CORE, conn)
        rs = core.retrieve_most_recent_session('i03', 'cm')
        assert len(rs) == 1

def test_retrieve_persons_for_proposal(testconfig):
  with ispyb.open(testconfig) as conn:
        core = ispyb.factory.create_data_area(ispyb.factory.DataAreaType.CORE, conn)
        rs = core.retrieve_persons_for_proposal('cm', 14451)
        assert len(rs) == 1
        login = rs[0]['login']
        assert login is not None

def test_retrieve_current_cm_sessions(testconfig):
  with ispyb.open(testconfig) as conn:
        core = ispyb.factory.create_data_area(ispyb.factory.DataAreaType.CORE, conn)
        rs = core.retrieve_current_cm_sessions('i03')
        assert len(rs) > 0

def test_retrieve_active_plates(testconfig):
  with ispyb.open(testconfig) as conn:
        core = ispyb.factory.create_data_area(ispyb.factory.DataAreaType.CORE, conn)
        rs = core.retrieve_active_plates('i02-2')
        assert len(rs) >= 0

def test_retrieve_proposal_title(testconfig):
  with ispyb.open(testconfig) as conn:
        core = ispyb.factory.create_data_area(ispyb.factory.DataAreaType.CORE, conn)
        title = core.retrieve_proposal_title('cm', 14451)
        assert title.strip() == 'I03 Commissioning Directory 2016'
