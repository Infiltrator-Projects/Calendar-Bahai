# Bahai Badi Calendar — validation requirements

**Evidence status:** No independent executable, standalone CI, installer or released artifact is established by these documents. All checkboxes are future gates, not claims of passing tests.

## Qualification checklist

- [ ] Establish exact original Common revision, licensed source provenance, direct and shared dependencies.
- [ ] Keep the implementation limited to stable ID `bahai`; do not embed another independent resource's algorithm.
- [ ] Produce the directly named portable shared object `Bahai Badi Calendar.so`.
- [ ] Verify metadata version, name, ID, kind, loadability and executable ABI through Common.
- [ ] Verify model-specific computation and historical-reference dates/times against evidence independent of self-round-tripping.
- [ ] Reject malformed, out-of-range and unsupported inputs with bounded work and no caller-owned output mutation.
- [ ] Verify bad/missing/different-kind resources cannot silently fall back or break other installed resources.
- [ ] Test the actual installed package bytes through the native resource directory.
- [ ] Verify clean installation, upgrade, removal and recovery without conflicting with the combined Common package.
- [ ] Record reproducibility, package/hash, build environment and release commit.
- [ ] Confirm consumer discovery in Calendar, Files and System Settings without embedding duplicate implementations.

## Model-specific reference qualification

Distinguish valid 1844 epoch data from year-start calculation failures; check modern Tehran equinox/sunset boundaries.

**Documented model:** Badíʿ calendar: fixed Western 21-March rule for years 1–171 B.E.; modern Tehran equinox/sunset model from 172 B.E. within the documented Gregorian 1000–3000 astronomical range; documented fixed-rule continuation outside that range.

**Fidelity boundary:** Astronomical reconstruction is approximate; failed year-start calculation must not masquerade as the historical 1844 epoch.

Also test period start/end, forward/backward navigation, localized output, extreme Julian-day values and consistency of supported-domain rejection across all operations.

## Prior evidence versus independent release evidence

The existing Common suite (`resources/temporal/tests/test-calendars.c`) supplies the starting contract, but a passing Common pack does not prove a standalone package or this repository's release. Attach specific commits, test runs, environments and artifacts before marking any item complete.

- [Libraries/Common temporal sources](https://github.com/Infiltrator-Projects/Libraries/tree/main/resources/temporal)
- [Current canonical build catalogue](https://github.com/Infiltrator-Projects/Libraries/blob/main/resources/temporal/Makefile)
- [Calendar chronology and clock models](https://github.com/Infiltrator-Projects/Calendar/blob/main/docs/MODELS.md)
- [Historical fidelity audit](https://github.com/Infiltrator-Projects/Libraries/blob/main/docs/TEMPORAL_HISTORICAL_FIDELITY.md)
- [Temporal discovery and executable provider ABI](https://github.com/Infiltrator-Projects/Libraries/blob/main/docs/TEMPORAL_PROVIDERS.md)
