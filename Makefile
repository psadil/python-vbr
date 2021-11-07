API ?= https://a2cps-dev.tapis.io
USERNAME ?= $(A2CPS_USERNAME)
PASSWORD ?= $(A2CPS_PASSWORD)

docs-apidoc:
	cd docs; sphinx-apidoc --maxdepth 2 -M -H "API Reference" -f -o source ../src/vbr

docs: docs-apidoc
	cd docs; make html

.SILENT:
deps:
	pip --disable-pip-version-check install -r requirements.txt

.SILENT:
pytest: deps
	python -m pytest

tests: pytest

.SILENT:
classfiles-clean:
	cd src ; python -m scripts.redcap_classfiles clean

classfiles:
	cd src ; python -m scripts.redcap_classfiles build; yapf -i --recursive vbr/tableclasses/redcap/autogenerated

definitions:
	cd src ; python -m scripts.definitions; mv -f *.json  ../files/

.SILENT:
definitions-clean:
	rm -f files/*.json

clean: definitions-clean

.SILENT:
create_tables:
	cd src ; python -m scripts.create_tables --base-url "$(API)" --username "$(USERNAME)" --password "$(PASSWORD)" $(SCRIPT_ARGS)

.SILENT:
drop_tables:
	cd src ; python -m scripts.drop_tables --base-url "$(API)" --username "$(USERNAME)" --password "$(PASSWORD)" $(SCRIPT_ARGS)

.SILENT:
bootstrap_tables:
	cd src ; python -m scripts.bootstrap_tables --base-url "$(API)" --username "$(USERNAME)" --password "$(PASSWORD)" $(SCRIPT_ARGS)

.SILENT:
dump_tables: 
	cd src ; python -m scripts.dump_tables --base-url "$(API)" --username "$(USERNAME)" --password "$(PASSWORD)" $(SCRIPT_ARGS)

.SILENT:
load_tables: 
	cd src ; python -m scripts.load_tables --base-url "$(API)" --username "$(USERNAME)" --password "$(PASSWORD)" $(SCRIPT_ARGS)

.SILENT:
dump_tables-clean:
	cd exports; rm *.csv

.SILENT:
clean_tables:
	cd src; echo "Cleaning: $(SCRIPT_ARGS)"

reset: drop_tables create_tables bootstrap_tables

.SILENT:
dbml:
	mkdir -p files-dbml; cd src; python -m scripts.dbml build --dotfile; mv -f dbml.* ../files-dbml/

.SILENT:
reformat-source:
	black src/vbr

.SILENT:
reformat-scripts:
	black src/scripts

.SILENT:
reformat-tests:
	black src/tests

reformat: reformat-source reformat-scripts reformat-tests

.SILENT:
isort-source:
	isort src/vbr

.SILENT:
isort-scripts:
	isort src/scripts

isort: isort-source isort-scripts
