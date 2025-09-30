import unittest
from dna_electrons.core import compute_electrons

class TestDNACalc(unittest.TestCase):
    def test_at_pair_example(self):
        res = compute_electrons("A", double_stranded=True, include_backbone=True, include_phosphate_charge=True)
        assert res.sequence_length == 1
        assert res.breakdown["bases"] == 136
        assert res.breakdown["backbone"] == 238
        assert res.breakdown["phosphate_charge"] == 2
        assert res.total == 136+238+2

    def test_double_no_backbone(self):
        res = compute_electrons("AT", double_stranded=True, include_backbone=False, include_phosphate_charge=False)
        assert res.total == 2*136

    def test_single_with_backbone_and_charge(self):
        res = compute_electrons("ATGC", double_stranded=False, include_backbone=True, include_phosphate_charge=True)
        assert res.total == 272 + 119*4 + 1*4
