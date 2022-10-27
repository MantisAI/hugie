# Contributing to hfie

Thanks for your interest to contribute to this tool 🙏🏻Here we cover
how you can get started and some processes we follow

## Code changes

If you are submitting a change based on an existing issue carry on,
otherwise it is recommended to start by opening an issue to discuss
the change you want to propose.

To setup your development environment follow the instructions in the
README in the for development section. Note that we use `pre-commit`
to enforce certain styling standards. Precommit runs those checks
and makes those changes when you commit changes, so even though
they do happen automatically, you will need to commit twice when
this happens.

Before opening a PR make sure all tests pass. You can find instructions
on how to run tests in README as well. Tests will also run automatically
as part of a Github action but if they faill, this would be the first
thing you will be requested to fix.

Add a detailed description of your change and mention the issues it affects
ideally using `Fixes #ISSUE_NUMBER` so that they close automatically once
the PR is merged.

Finally update the documentation in README or in the script as needed for
the new functionality or changes you are making.

## Issues and feature recommendations

If you are opening a bug we at the very least ask to provide us with a way
to reproduce the error. This will make the process of fixing it much easier,
otherwise it will be difficult to be sure that any change we make is succcesfully
addressing what you are experiencing.

All feature recommendations are welcome. Please describe the rationale behind the
proposal and how it affects your use case.
