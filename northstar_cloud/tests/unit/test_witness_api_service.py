from northstar_cloud.tests import base
from northstar_cloud.common import utils as c_utils
import mock
import pytest


class TestWitnessApiService(base.BaseTest):
    def setUp(self):
        super(TestWitnessApiService, self).setUp()
        self.service = mock.Mock()

    @pytest.skip("fixing")
    def test_init_aggregate_witness_events(self):
        witness_events = [["Sample_1"], ["Sample_2"]]
        self.service.init_aggregate_witness_events(witness_events)
        wt_graph = self.service.graph
        self.assertEqual(len(wt_graph.witness_events), 2)

    @pytest.skip("fixing")
    def test_calculate_predict_witness_merge(self):
        witness_events = [["Sample_1"], ["Sample_2"]]
        self.service.init_aggregate_witness_events(witness_events)
        is_merge_possible, merge_list = self.service.calculate_witness_merge()
        self.assertEqual(
            is_merge_possible.name,
            c_utils.PossibleEvents.WITNESS_DECISION_NO_MERGE_POSSIBLE.name
        )
        self.assertEqual(merge_list, witness_events)
