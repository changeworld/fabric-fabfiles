from fabric.api import env, local, run

def tag(name="", message=""):
  local("git checkout master; git pull origin master; git tag -a %(n)s -m %(m)s; git push origin %(n)s" % { "n" : name, "m" : message })

def develop():
  # TODO: Change host name
  env.hosts = ['develop-server']

def production():
  # TODO: Change host name
  env.hosts = ['production-server']

def deploy(target="master"):
  # TODO: Change user name and repository, rollout scripts
  run("sudo -i -u [user_name] mv [repository] [repository_backup]")
  run("sudo -i -u [user_name] [rollout scripts] %s" % target)
