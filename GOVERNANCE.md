# Governance

These four rules govern the Foster Rx Prediction Register. They are published
beside the register and are in force from the genesis batch.

1. **Append-only.** Errors are corrected by a new entry referencing the
   old id; nothing is edited or deleted.
2. **Resolution by pre-stated criterion only** — never by judgment call
   at resolution time. Ambiguous outcomes resolve `void`, and voids are
   published and counted.
3. **Calibration reporting:** quarterly Brier score and reliability
   summary once n ≥ 20 resolved `open` entries; confirmatory entries
   reported separately, never blended.
4. **Cadence:** entries in batches, each batch committed and anchored
   same day. No entry references non-public information, ever.

---

*A research calibration record. Not investment advice; not a solicitation.*
5. Sealed-commitment class (added 2026-09-03): an entry may publish only the SHA-256 of a salted statement, with disclosure bound to a pre-stated trigger and deadline. Temporal precedence without disclosure; scored only after disclosure.
6. Hash chain: entry_hash = SHA-256 of the canonical JSON (sorted keys, compact separators) of the entry minus entry_hash; prev_hash links entries; genesis prev is 64 zeros. tools/hash_chain.py verifies.
