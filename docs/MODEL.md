# Bahai Badi Calendar — computational and historical model

| Field | Value |
| --- | --- |
| Stable provider ID | `bahai` |
| Resource kind | `calendar` |
| Canonical compiled name | `Bahai Badi Calendar.so` |
| Intended installation | `/System/Resources/Calendars/Bahai Badi Calendar.so` |

## Maintained model

Badíʿ calendar: fixed Western 21-March rule for years 1–171 B.E.; modern Tehran equinox/sunset model from 172 B.E. within the documented Gregorian 1000–3000 astronomical range; documented fixed-rule continuation outside that range.

## Historical scope / fidelity limitation

**Implemented interpretation:** Badíʿ calendar chronology.

**Fidelity boundary:** Astronomical reconstruction is approximate; failed year-start calculation must not masquerade as the historical 1844 epoch.

This is an account of the implemented model, not a claim that a particular mathematical projection was observed or officially used in every historical period. Where the source model uses approximations, retrospective continuation or external ICU/CLDR authorities, that distinction must remain explicit.

## Observable behaviour

The provider owns fields, localized formatting, period starts and navigation. Field extraction determines the supported date domain; every other operation must reject the same invalid input. Switching calendar presentation cannot rewrite canonical instants or event ordering.

## Unsupported inputs and reproducibility

Missing providers are unavailable; consumers must not substitute a different provider with a similar name. Malformed or out-of-range inputs must return an explicit failure without modifying outputs. Module metadata must convey its true ID and kind, independent of filename ordering.

## Provenance

The model and boundary above are documented from the current resource build map, Calendar model matrix and Common historical-fidelity audit. They have not yet been independently requalified in this repository.

- [Libraries/Common temporal sources](https://github.com/Infiltrator-Projects/Libraries/tree/main/resources/temporal)
- [Current canonical build catalogue](https://github.com/Infiltrator-Projects/Libraries/blob/main/resources/temporal/Makefile)
- [Calendar chronology and clock models](https://github.com/Infiltrator-Projects/Calendar/blob/main/docs/MODELS.md)
- [Historical fidelity audit](https://github.com/Infiltrator-Projects/Libraries/blob/main/docs/TEMPORAL_HISTORICAL_FIDELITY.md)
- [Temporal discovery and executable provider ABI](https://github.com/Infiltrator-Projects/Libraries/blob/main/docs/TEMPORAL_PROVIDERS.md)
