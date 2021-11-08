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
	jupyter-book build --builder pdfhtml --verbose --keep-going .

clean:
	git clean -xdf
	rm -rf module04_version_control_with_git/learning_git/
