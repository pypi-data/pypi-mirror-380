import unittest, os, tempfile
from dna_electrons.io import compute_from_fasta

FASTA = ">seq1\nATGC\n>seq2\nA\n"

class TestIO(unittest.TestCase):
    def test_fasta(self):
        with tempfile.TemporaryDirectory() as d:
            fp = os.path.join(d, "x.fasta")
            with open(fp, "w") as f:
                f.write(FASTA)
            rows = compute_from_fasta(fp, double_stranded=True, include_backbone=True, include_phosphate_charge=True)
            assert len(rows) == 2
            ids = [rid for rid, _ in rows]
            assert ids == ["seq1", "seq2"]
