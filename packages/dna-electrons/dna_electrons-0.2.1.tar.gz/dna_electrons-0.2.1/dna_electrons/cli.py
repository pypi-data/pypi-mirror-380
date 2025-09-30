# Copyright (c) 2025 Yash Munnalal Gupta
# SPDX-License-Identifier: MIT

import argparse, sys, json, csv
from .core import compute_electrons
from .io import compute_from_fasta

def _emit_row_dict(record_id, res):
    return {
        "id": record_id,
        "length": res.sequence_length,
        "bases": res.breakdown.get("bases", 0),
        "backbone": res.breakdown.get("backbone", 0),
        "phosphate_charge": res.breakdown.get("phosphate_charge", 0),
        "total": res.total,
        "counts": res.counts,
    }

def main():
    p = argparse.ArgumentParser(description="Compute total electrons for DNA sequences.")
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--seq", help="DNA sequence (ATGC). If --double, treated as one strand of a duplex.")
    g.add_argument("--fasta", help="Path to FASTA file containing one or more sequences.")
    p.add_argument("--double", action="store_true", help="Treat as double-stranded (default if neither flag given).")
    p.add_argument("--single", action="store_true", help="Treat as single-stranded.")
    p.add_argument("--include-backbone", action="store_true", help="Include sugar-phosphate backbone electrons.")
    p.add_argument("--include-charge", action="store_true", help="Include phosphate negative-charge electrons.")
    p.add_argument("--output", choices=["text", "csv", "json"], default="text",
                   help="Output format. For FASTA, 'csv' or 'json' are convenient.")
    args = p.parse_args()

    if args.single and args.double:
        p.error("Use only one of --single / --double.")
    double = not args.single if not args.double else True

    if args.seq:
        res = compute_electrons(
            args.seq,
            double_stranded=double,
            include_backbone=args.include_backbone,
            include_phosphate_charge=args.include_charge,
        )
        if args.output == "text":
            print(f"Total electrons: {res.total}")
            print("Breakdown:", res.breakdown)
            print("Counts:", res.counts)
        else:
            row = _emit_row_dict("sequence", res)
            if args.output == "json":
                print(json.dumps(row, indent=2))
            else:  # csv
                writer = csv.DictWriter(sys.stdout, fieldnames=list(row.keys()))
                writer.writeheader()
                writer.writerow(row)
        return

    rows = compute_from_fasta(
        args.fasta,
        double_stranded=double,
        include_backbone=args.include_backbone,
        include_phosphate_charge=args.include_charge,
    )
    out_rows = [_emit_row_dict(rid, res) for rid, res in rows]

    if args.output == "text":
        for row in out_rows:
            print(f">{row['id']}  len={row['length']}  total={row['total']}")
            print(f"  bases={row['bases']} backbone={row['backbone']} charge={row['phosphate_charge']} counts={row['counts']}")
    elif args.output == "json":
        print(json.dumps(out_rows, indent=2))
    else:  # csv
        if out_rows:
            writer = csv.DictWriter(sys.stdout, fieldnames=list(out_rows[0].keys()))
            writer.writeheader()
            for row in out_rows:
                writer.writerow(row)
