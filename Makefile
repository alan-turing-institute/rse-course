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
	rm -f _config.yml
	rm -f _toc.yml
	rm -f ch*/*.pyc
	rm -f ch*/generated/*.png
	rm -f ch01data/boids_1.mp4
	rm -f ch01python/analyzer.py
	rm -f ch01python/eight
	rm -f ch01python/eight.py
	rm -f ch01python/pretty.py
	rm -f ch04packaging/greeter.py
	rm -f ch04packaging/map.png
	rm -f ch05construction/anotherfile.py
	rm -f ch05construction/config.yaml
	rm -f ch05construction/context.py
	rm -f ch06design/fixed.png
	rm -f ch07dry/*.yaml
	rm -f index.html
	rm -f index.md
	rm -rf _build
	rm -rf ch*/__pycache__
	rm -rf ch*/*/__pycache__
	rm -rf ch*/*/*/__pycache__
	rm -rf ch*/*/*/*/__pycache__
	rm -rf ch03tests/diffusion/.pytest_cache
	rm -rf ch03tests/DiffusionExample/.pytest_cache
	rm -rf ch04packaging/.pytest_cache
	rm -rf ch04packaging/greetings/doc/output/
	rm -rf ch09*/*.csv
	rm -rf ch09*/*.db
	rm -rf ch09*/*.hdf5
	rm -rf ch09*/*.mko
	rm -rf ch09*/*.mol
	rm -rf ch09*/*.out
	rm -rf ch09*/*.py
	rm -rf ch09*/*.tex
	rm -rf ch09*/*.ttl
	rm -rf ch09*/*.xml
	rm -rf ch09*/*.xsd
	rm -rf ch09*/*.xsl
	rm -rf combined*
