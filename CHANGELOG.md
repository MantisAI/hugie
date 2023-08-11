# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.0..0.3.2] 2023-07-27

### Added
- Add endpoint config subcommand #47 (resolves #41)
- Adds `ls` alias to `list` command #50
- Adds `-f` shortcut to `--force` command #50
- Adds `poetry` for dependency management #69
- Adds `ui` command to open Hugging Face Inference Endpoint website in browser #70

### Changed
- Only create docs on merge to main #50
- Switch to poetry for dependency management #69
- Don't set `top_k` when running `hugie endpoint test` #49

### Removed
- Removes `--no-force` option to `delete` command #50

### Fixed
- Fixes error handling flows #72
- Fixes breaking changes introduced by pydantic 2.0 #68
- Fix data bug in update function #63
- Address missing token message #46
- Handle 40x responses in create #45
- Update now handles 40x codes #44
- Remove --no-json from cli #43

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

### Fixed
- Correct table column widths #16
