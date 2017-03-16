#!/usr/bin/env python

import git
repo = git.Repo('/tmp/GitNote')
repo.remotes.origin.pull(refspec='master:master')
# REMOTE_URL = "https://github.com/csrgxtu/GitNote.git"
# origin = repo.create_remote('origin', REMOTE_URL)
# origin.fetch()
# origin.pull(origin.refs[0].remote_head)
print "---- DONE ----"
