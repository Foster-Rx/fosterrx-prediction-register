"""Verify the register's hash chain. Usage: python3 tools/hash_chain.py"""
import json, hashlib, pathlib
GENESIS = "0" * 64
entries = sorted(pathlib.Path("entries").glob("FRXP-*.json"))
prev = GENESIS
for p in entries:
    e = json.loads(p.read_text())
    assert e["prev_hash"] == prev, "chain break at " + e["id"]
    body = {k: v for k, v in e.items() if k != "entry_hash"}
    h = hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert h == e["entry_hash"], "hash mismatch at " + e["id"]
    prev = e["entry_hash"]
    print("ok", e["id"], e["entry_hash"][:16])
print("chain verified:", len(entries), "entries")
