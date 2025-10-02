# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html)[^1].

<!---
Types of changes

- Added for new features.
- Changed for changes in existing functionality.
- Deprecated for soon-to-be removed features.
- Removed for now removed features.
- Fixed for any bug fixes.
- Security in case of vulnerabilities.

-->

## [Unreleased]


## [1.0.0] - 2025-10-01

### Added

* An action to initialize a Krita :
    * It create an `.kra` file 
* Setup the krita file outside krita with `kritarunner` command:
    * Create a `kritarunner` folder on the data directory folder (AppData, Share or Application Support)
    * Copy and paste the script `krita_setup_file.py` into the `kritarunner` folder
    * Find resolution, frame rate for the project and the frame count for the shot and add them to the arguments of the `kritarunner` command.




