# Foster Rx Prediction Register

> *"A research calibration record. Forecasts about clinical, regulatory, and
> coverage events, made to be scored. Not investment advice; not a
> solicitation."*

## Why this exists (and why now)
A calibration track record cannot be backdated. Every entry made this
year becomes, by the time the calibrated transition model ships (Layer
3.E), evidence no competitor and no later Foster Rx could manufacture.
The register is also the company's method performed in public: stated
criteria before outcomes, provenance labeled, zeros published. It costs
an afternoon now and is impossible at any price later.

## What it is NOT — stated on the register itself
Not ML-1. Not a model output (until one exists, and then labeled as
such). Not investment advice — header disclaimer: *"A research
calibration record. Forecasts about clinical, regulatory, and coverage
events, made to be scored. Not investment advice; not a solicitation."*
Not a company-ops feed: v1 entries are DOMAIN predictions only (assets,
regulatory decisions, coverage decisions) — never company gates,
pipeline, or traction, which would leak strategy through the register.

## Entry schema (one YAML/JSON record per entry, append-only)
- `id` — FRXP-{seq}
- `timestamp_utc` — entry creation
- `statement` — a single resolvable claim with a binary or numeric
  outcome (e.g., "Asset X's Phase 3 readout in indication Y reports a
  statistically significant primary endpoint by DATE")
- `p` — stated probability (or interval for numeric claims)
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

The register's normative schema, including the `method` field, is
[`schema.md`](schema.md).

## Governance (published beside the register)
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

The governing text is [`GOVERNANCE.md`](GOVERNANCE.md).

## Method
Probabilities are produced by a versioned, deterministic internal method (frx-cal-v0) over public inputs. Method commitment: SHA-256 50feac6451f5028b84cb97c9fe72a66e49246200dbcabad185ce979ff046f842. The method is validated by this register's published scoring.

## Anchoring (the "cannot be re-created" mechanics)
- Public GitHub repo `fosterrx-prediction-register`: entries as files;
  git history is the first timestamp layer.
- **OpenTimestamps** stamp on each batch commit hash — Bitcoin-anchored
  proof of existence, independent of Foster Rx and of GitHub.
- Hash chain inside the entries (schema above) — internal integrity.
- Later (post-B4): merkle-sd integration for selective disclosure, and a
  credential-less `/register` page on foster-rx-domain in the same rail
  family as /verify. Neither blocks v1 — git + OTS ships this week.

## Repository layout
```
README.md          this file — disclaimer, scope, governance summary, method
GOVERNANCE.md      the four governance rules, in force
schema.md          the entry schema, field by field
entries/           one file per entry, append-only (empty until the first batch)
tools/hash_chain.py  entry hashing and chain verification
```

## Verifying the chain
```
python3 tools/hash_chain.py verify
```

---

*Foster Rx Systems Inc. · Patent Pending No. 19/459,855*
