# Entry schema

One YAML/JSON record per entry, append-only. Files live in `entries/`, one
per entry, named for the entry `id` (e.g. `entries/FRXP-0001.json`).

## Fields

- `id` — FRXP-{seq}
- `timestamp_utc` — entry creation
- `statement` — a single resolvable claim with a binary or numeric
  outcome (e.g., "Asset X's Phase 3 readout in indication Y reports a
  statistically significant primary endpoint by DATE")
- `p` — stated probability (or interval for numeric claims)
- `method` — string; the versioned identifier of the internal procedure that
  produced `p` (e.g. `frx-cal-v0`). Fixed at entry, never rewritten; a change
  of procedure is a new version identifier on subsequent entries, not an edit
  to earlier ones. Lets scoring be partitioned by method version.
- `basis` — `open` | `confirmatory` (honest-provenance rule: claims where
  the direction was informed by existing signals are labeled confirmatory
  and EXCLUDED from headline calibration)
- `source_class` — public sources only in v1 (registry, label, docket,
  press release classes — no architecture internals, no client data)
- `resolution_criterion` — the exact observable that resolves it, named
  at entry (the register's whole discipline)
- `resolution_deadline` — date after which unresolved = `void`
- `resolution` — `pending` | `correct` | `incorrect` | `void` + date +
  citation
- `entry_hash` — SHA-256 of the canonical entry
- `prev_hash` — chain link (genesis = zeros)

## Canonical form and hashing

`entry_hash` is the SHA-256 of the canonical serialization of the entry with
the `entry_hash` key removed and every other key — `prev_hash` included —
present. Canonical serialization is UTF-8 JSON with keys sorted, `", "` and
`": "` separators, and no non-ASCII escaping.

`prev_hash` is the `entry_hash` of the preceding entry in `id` order. The
first entry's `prev_hash` is the genesis value: 64 zeros.

Both are computed by `tools/hash_chain.py`:

```
python3 tools/hash_chain.py hash entries/FRXP-0001.json   # print entry_hash
python3 tools/hash_chain.py verify                        # walk the whole chain
```

Because `entry_hash` covers `prev_hash`, rewriting any earlier entry breaks
every hash after it — which is the point. Corrections are made by appending a
new entry that references the old `id` (GOVERNANCE.md, rule 1).
