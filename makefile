CURRENT_USE_CASE:="pytest"

git-status:
	git status

install:
	pip install .

open-readme:
	open https://github.com/quanlinguo/salesforce-scripts

publish commit-and-push:
	git pull
	git commit -m ${CURRENT_USE_CASE}
	git push
