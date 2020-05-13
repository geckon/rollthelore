init:
	pip install poetry
	poetry install

bandit:
	bandit -r rollnpc.py loreroll

pycodestyle:
	pycodestyle --filename="*.py" .

pylint:
	pylint --reports=n rollnpc.py loreroll

pylint-error:
	pylint --reports=n --disable=C,R,W rollnpc.py loreroll

test:
	python -m pytest tests

travis: bandit pycodestyle pylint-error #test

