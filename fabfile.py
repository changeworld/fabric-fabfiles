from fabric.api import local

def tag(name="", message=""):
  local("git checkout master; git pull origin master; git tag -a %(n)s -m %(m)s; git push origin %(n)s" % { "n" : name, "m" : message })
