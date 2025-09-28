# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1] - 2025-09-27

### Added
- Calendar period grouping helpers for date fields, including friendly month/quarter/week labels and smarter filter links when drilling into grouped data
- Example project updates demonstrating time-period groupings and duration aggregations on cat nap durations

### Fixed
- Aggregations over `DurationField` values now treat timedeltas safely, so group-by sum and average operations work for `DurationField` columns without raising `TypeError`
- Average values keep numeric `floatformat` rendering only for real numbers, so duration aggregates display their native Django formatting

## [1.0.1] - 2025-06-24

### Fixed
- Fixed display of nullable boolean fields in group by view - now shows '?' icon instead of red X for None values
- Fixed filtering for nullable boolean fields - clicking on None values now correctly filters with `field__isnull=True`

## [1.0.0] - 2025-05-27

### Added
- Initial stable release of django-admin-groupby
- Group by functionality for Django admin with SQL-style aggregations
- Support for Count, Sum, Avg aggregations
- Custom PostProcess aggregations for calculated fields
- Integration with Django admin filters, search, and permissions
- Example project demonstrating usage with a Cat model
- Support for Django 3.2 through 5.2
- Python 3.8 through 3.12 support
