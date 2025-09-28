![Github CI](https://github.com/justmars/citation-date/actions/workflows/ci.yml/badge.svg)

# Citation Date Parser

citation-date is a Python library for parsing and normalizing dates from Philippine legal citations, including dockets, reports, and other references. It handles common typos and multiple date formats with US and UK variants. It is eventually used by the dataset employed in [LawSQL](https://lawsql.com).

## Purpose

The library is designed to:

- Extract dates from text commonly found in legal documents such as Philippine Supreme Court reports (SCRA) and dockets (G.R. No. ...).
- Handle both US (Month Day, Year) and UK (Day Month Year) date formats.
- Normalize dates to standard formats (%B %d, %Y or datetime.date).
- Support dates enclosed in parentheses () or brackets [], and in raw strings.
- Provide regex patterns and utility functions for downstream processing in other citation libraries.

## Key Components

### Regex Patterns

#### US/UK Date Patterns

```py
us = rf"({month}{separator}{day}{separator}{year})"
uk = rf"({day}{separator}{month}{separator}{year})"
```

These patterns detect date-like strings and account for common separators.

#### Report Dates

- `REPORT_DATE_REGEX` matches dates in citations like 1 SCRA 200 (1Dec. 2000).
- Supports naked dates, bracketed [Dec. 1, 2000], or parenthesis (Dec. 1, 2000).

#### Docket Dates

- `DOCKET_DATE_REGEX` matches docket-specific dates such as G.R. No. 12345, Dec,1, 2000.
- `DOCKET_DATE_FORMAT` standardizes formatting to %b. %d, %Y.

## Documentation

See [documentation](https://justmars.github.io/citation-date).
