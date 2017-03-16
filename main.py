#!/usr/bin/env python
# coding=utf-8
# Author: Archer
# Date: 16/March/2017
# File: main.py
# Desc: use gitpython index, commit, push to github, a little demo
# Produced By Shopee
import git
import sys

# init the repo object from existing git repo
repo = git.Repo('.')

# untracked files
PushFiles = list()
for f in repo.untracked_files:
    PushFiles.append(f)

# changed files
for f in [item.a_path for item in repo.index.diff(None)]:
    PushFiles.append(f)

for f in PushFiles:
    print f

# git add --a
repo.index.add(PushFiles)


# git commit -m 'msg'
repo.index.commit(sys.argv[1])

# git config credential.helper store
cr = repo.config_reader()
# cw = repo.config_writer()
if cr.has_section('credential') and cr.get_value('credential', 'helper') == u'store':
    pass
else:
    # cw.add_section('credential')
    try:
        cr.set_value('credential', 'helper', 'store')
    except:
        pass

# git push
repo.remotes.origin.push(refspec='master:master')
