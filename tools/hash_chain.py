#!/usr/bin/env python3
"""Entry hashing and chain verification for the Foster Rx Prediction Register.

Usage:
    hash_chain.py hash <entry.json>   print the entry_hash of one entry
    hash_chain.py verify [entries/]   walk entries in id order, check the chain
"""
import hashlib
import json
import pathlib
import sys

GENESIS = "0" * 64
ENTRIES = pathlib.Path(__file__).resolve().parent.parent / "entries"


def canonical(entry):
    """UTF-8 JSON, keys sorted, entry_hash excluded — prev_hash is covered."""
    body = {k: v for k, v in entry.items() if k != "entry_hash"}
    return json.dumps(body, sort_keys=True, ensure_ascii=False).encode("utf-8")


def entry_hash(entry):
    return hashlib.sha256(canonical(entry)).hexdigest()


def load(directory):
    """Every *.json entry in the directory, in id order."""
    entries = [(p, json.loads(p.read_text())) for p in directory.glob("*.json")]
    return sorted(entries, key=lambda pe: pe[1]["id"])


def verify(directory):
    entries = load(directory)
    prev = GENESIS
    failures = 0
    for path, entry in entries:
        # prev is the recomputed hash, not the stored one, so a rewrite of any
        # entry breaks every entry after it.
        for want, got, label in (
            (prev, entry.get("prev_hash"), "prev_hash"),
            (entry_hash(entry), entry.get("entry_hash"), "entry_hash"),
        ):
            if want != got:
                print(f"FAIL {path.name}: {label} is {got}, expected {want}")
                failures += 1
        prev = entry_hash(entry)
    print(f"{'FAIL' if failures else 'OK'}: {len(entries)} entries, "
          f"{failures} problem(s)")
    return 1 if failures else 0


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[:1] == ["hash"] and len(args) == 2:
        print(entry_hash(json.loads(pathlib.Path(args[1]).read_text())))
    elif args[:1] == ["verify"]:
        sys.exit(verify(pathlib.Path(args[1]) if len(args) > 1 else ENTRIES))
    else:
        sys.exit(__doc__)
