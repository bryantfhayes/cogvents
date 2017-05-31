# File: buildinfo.py
# Info: Basic functions for getting build-related info.
#       Really not-cool and lame but useful maybe.

idString = "$Id$"
def getRevision():
  global idString
  return idString.replace("$", "").replace("Id:", "").strip()
