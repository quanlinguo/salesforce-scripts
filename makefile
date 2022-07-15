CURRENT_USE_CASE:="Get access token using Salesforce CLI"

git-status:
	git status

open-readme:
	open https://github.com/quanlinguo/salesforce-scripts

publish commit-and-push:
	git pull
	git commit -m ${CURRENT_USE_CASE}
	git push
