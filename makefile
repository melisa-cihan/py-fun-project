
BUILD_ARTIFACT=py-fun-SNAPSHOT-0.1.0.tar
BUILD = build
DOCS_BUILD = docs/_build/html

# first goal is default
run:
	python main.py

# package distributable artifact after clean project build
package: clean build
	tar cvf $(BUILD)/$(BUILD_ARTIFACT) -C $(BUILD)/lib .
	@echo -e "\\\\\\\\\nartifact: \"$(BUILD)/$(BUILD_ARTIFACT)\" built"

# build runs tests and (if passing) 'setup.py' installs distributable
# content under 'build/lib' including docs
$(BUILD): tests $(DOCS_BUILD)
	mkdir -p $(BUILD)/lib
	[ ! -d $(BUILD)/lib/html ] && mkdir $(BUILD)/lib/html
	cp -R $(DOCS_BUILD) $(BUILD)/lib
	[ -f setup.py ] && python setup.py $(BUILD)

# run tests
tests: .PHONY
	python -m unittest -v tests

# build docs
$(DOCS_BUILD):
	(cd docs; make html)

# clean up artifacts created during the build process
clean:
	rm -rf $(BUILD) $(shell dirname $(DOCS_BUILD))
	find . -type d -name '__pycache__' | xargs rm -rf

# install Python dependencies from 'requirements.txt'
REQUIREMENTS="requirements.txt"
# 
install:
	@pip install -r $(REQUIREMENTS) | grep -v "already satisfied" || \
		echo "everything from \"$(REQUIREMENTS)\" is up-to-date"

# pseudo goal never created
.PHONY:
