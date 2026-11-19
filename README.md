# Foster Rx Prediction Register

> *"A research calibration record. Forecasts about clinical, regulatory, and
> coverage events, made to be scored. Not investment advice; not a
> solicitation."*

This repository is a public register of forecasts. Each forecast is entered
with a stated probability and a resolution rule before the outcome is known.
Entries are hash-chained and timestamped, then scored when the outcome lands,
misses included.

## What an entry is

An entry is a single claim that can be resolved, about a clinical, regulatory
or coverage event. It carries a stated probability, the exact observable that
will resolve it, and a deadline. Entries are append-only: nothing is edited or
deleted after it is entered.

Entries cover drug assets, regulatory decisions and coverage decisions. They
rest on public sources only. The register does not carry forecasts about
Foster Rx itself.

Nothing here is investment advice.

## Entry schema (one JSON record per entry, append-only)

- `id`: FRXP-{seq}
- `timestamp_utc`: when the entry was created
- `statement`: a single resolvable claim with a binary or numeric outcome
  (e.g., "Asset X's Phase 3 readout in indication Y reports a statistically
  significant primary endpoint by DATE")
- `p`: the stated probability (or an interval for numeric claims)
- `method`: the versioned identifier of the procedure that produced `p`
- `basis`: `open` | `confirmatory`. Claims where the direction was informed
  by existing signals are labelled confirmatory and excluded from headline
  calibration.
- `source_class`: the class of public source the entry rests on (registry,
  label, docket, press release)
- `resolution_criterion`: the exact observable that resolves the entry,
  named at entry
- `resolution_deadline`: the date after which an unresolved entry is `void`
- `resolution`: `pending` | `correct` | `incorrect` | `void`, with date and
  citation
- `entry_hash`: SHA-256 of the canonical entry
- `prev_hash`: the chain link (the first entry links to 64 zeros)

This is a summary. The normative schema is [`schema.md`](schema.md).

## Governance

1. **Append-only.** Errors are corrected by a new entry that references the
   old id. Nothing is edited or deleted.
2. **Resolution by the pre-stated criterion only**, never by a judgment call
   at resolution time. Ambiguous outcomes resolve `void`, and voids are
   published and counted.
3. **Calibration reporting.** A quarterly Brier score and reliability summary
   once 20 or more `open` entries have resolved. Confirmatory entries are
   reported separately and never blended.
4. **Cadence.** Entries are made in batches, and each batch is committed and
   anchored the same day. No entry references non-public information.
5. **Sealed commitments.** An entry may publish only the SHA-256 of a salted
   statement, with disclosure bound to a trigger and deadline stated at
   entry. It is scored only after disclosure.
6. **Hash chain.** Each entry carries its own hash and the hash of the entry
   before it.

This is a summary. The governing text is [`GOVERNANCE.md`](GOVERNANCE.md).

## Method
Probabilities are produced by a versioned, deterministic internal method (frx-cal-v0) over public inputs. Method commitment: SHA-256 50feac6451f5028b84cb97c9fe72a66e49246200dbcabad185ce979ff046f842. The method is validated by this register's published scoring.

## Anchoring

Three layers show that an entry existed when it says it did, and that it has
not changed since.

- **Git history.** Entries are files in this public repository. The commit
  history is the first timestamp.
- **OpenTimestamps.** The commit hash of each batch is stamped with
  OpenTimestamps, which gives a Bitcoin-anchored proof of existence that does
  not depend on Foster Rx or on GitHub. For the first batch,
  `BATCH-0001.commit` holds the commit hash and `BATCH-0001.commit.ots` holds
  the proof.
- **Hash chain.** Each entry includes the hash of the entry before it, so
  changing an earlier entry breaks every hash after it.

## Repository layout
```
README.md              this file: disclaimer, scope, summaries, method
GOVERNANCE.md          the six governance rules, in force
schema.md              the entry schema, field by field
entries/               one file per entry, append-only (two entries in the first batch)
BATCH-0001.commit      commit hash of the first batch
BATCH-0001.commit.ots  OpenTimestamps proof for that commit hash
tools/hash_chain.py    walks the hash chain and checks every entry
```

## Checking the chain

From the repository root:

```
python3 tools/hash_chain.py verify
```

The tool recomputes every entry hash, checks each link to the entry before
it, and prints one line per entry.

## Contact

info@fosterrx.com
