from github import Github

acces_token ="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"
g=Github(access_token)

user=g.get_user()
print(user.login)
