
test:
	@echo "Running tests..."
	@python3 tests/iloger_test.py

.PHONY: test


dist:
	@echo "Building distribution..."
	@python3 setup.py sdist bdist_wheel

.PHONY: dist


upload: clean test dist
	@echo "Uploading distribution..."
	@twine upload dist/* --verbose

.PHONY: upload


clean:
	@echo "Cleaning up..."
	@rm -rf build dist *.egg-info

.PHONY: clean