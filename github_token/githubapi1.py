from github import Github

access_token="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"
g =Github(access_token)

user=g.get_user()
print(user.login)
