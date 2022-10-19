#################################################################################
# GLOBALS                                                                       #
#################################################################################

PYTHON_VERSION = python3.8
VIRTUALENV := .venv

#################################################################################
# COMMANDS                                                                      #
#################################################################################

# Set the default location for the virtualenv to be stored
# Create the virtualenv by installing the requirements and test requirements

.PHONY: virtualenv
virtualenv:
	@if [ -d $(VIRTUALENV) ]; then rm -rf $(VIRTUALENV); fi
	@mkdir -p $(VIRTUALENV)
	virtualenv --python $(PYTHON_VERSION) $(VIRTUALENV)
	$(VIRTUALENV)/bin/pip3 install -e .[dev]
	${VIRTUALENV}/bin/pre-commit install --hook-type pre-push --hook-type post-checkout --hook-type pre-commit
	touch $@

# Delete all compiled Python files
.PHONY: clean
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
