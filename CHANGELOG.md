# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0]

✨ Renamed to Hugie 🐻

### Added
- Add endpoint subcommand
- Add endpoint test command

### Changed
- Add error handling
- Abstract json loading to `load_json` function
- Allow test command to take an input JSON containing queries
- Make create output more human readable #26
- Make delete error messsage more informative #25
- Add tests and CI/CD

### Bug fixes
- Correct table column widths #16
