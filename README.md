# Governance
A research calibration record. Forecasts about clinical, regulatory, and coverage events, made to be scored. Not investment advice; not a solicitation.

1. Append-only. Errors are corrected by a new entry referencing the old id; nothing is edited or deleted.
2. Resolution by pre-stated criterion only, never by judgment at resolution time. Ambiguous outcomes resolve void; voids are published and counted.
3. Calibration reporting: quarterly Brier and reliability once n >= 20 resolved open entries; confirmatory entries reported separately, never blended.
4. Entries land in batches; each batch is committed and OpenTimestamps-anchored the same day. No entry references non-public information.
5. Sealed-commitment class (added 2026-09-03): an entry may publish only the SHA-256 of a salted statement, with disclosure bound to a pre-stated trigger and deadline. Temporal precedence without disclosure; scored only after disclosure.
6. Hash chain: entry_hash = SHA-256 of the canonical JSON (sorted keys, compact separators) of the entry minus entry_hash; prev_hash links entries; genesis prev is 64 zeros. tools/hash_chain.py verifies.
