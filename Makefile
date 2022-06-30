SITE_PACKAGES_DIR=$(shell python3 -c "import site; print(site.getsitepackages()[0])")

default: html

_config.yml:
	cp docs/_config.yml .

_toc.yml:
	cp docs/_toc.yml .

index.md:
	cp docs/index.md .

html: _config.yml _toc.yml index.md
	jupyter-book build --verbose --keep-going .

pdf: _config.yml _toc.yml index.md
	# Extend the default pyppeteer timeout to 999s
	sed -i'' -e "s/self._defaultNavigationTimeout = .*/self._defaultNavigationTimeout = 999000 # milliseconds/" $(SITE_PACKAGES_DIR)/pyppeteer/page.py
	jupyter-book build --builder pdfhtml --verbose --keep-going .

clean:
	git clean -xdf
	rm -rf module04_version_control_with_git/learning_git/
