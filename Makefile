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
	rm -rf _build
	rm -rf _config.yml
	rm -rf _toc.yml
	rm -rf ch*/__pycache__
	rm -rf ch*/*.pyc
	rm -rf ch*/*/__pycache__
	rm -rf ch*/*/*/__pycache__
	rm -rf ch*/generated/*.png
	rm -rf ch01data/boids_1.mp4
	rm -rf ch01python/analyzer.py
	rm -rf ch01python/eight
	rm -rf ch01python/eight.py
	rm -rf ch01python/pretty.py
	rm -rf ch03tests/diffusion/.coverage
	rm -rf ch03tests/diffusion/htmlcov
	rm -rf ch03tests/DiffusionExample/
	rm -rf ch03tests/energy_example.py
	rm -rf ch03tests/saskatchewan/
	rm -rf ch04packaging/.pytest_cache
	rm -rf ch04packaging/greeter.py
	rm -rf ch04packaging/greetings/doc/output/
	rm -rf ch04packaging/map.png
	rm -rf ch05construction/anotherfile.py
	rm -rf ch05construction/config.yaml
	rm -rf ch05construction/context.py
	rm -rf ch06design/fixed.png
	rm -rf ch07dry/*.yaml
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
	rm -rf index.html
	rm -rf index.md
