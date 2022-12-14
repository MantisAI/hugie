# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Adds `ls` alias to `list` command #50
- Adds `-f` shortcut to `--force` command #50

### Changed
- Only create docs on merge to main #50

### Removed
- Removes `--no-force` option to `delete` command #50

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
