clean: ; \
    rm -fr bin eggs develop-eggs parts .installed.cfg; \
    rm -fr cbtop/cbtop.egg-info; \
    rm -f MemcachedSource-*.json cbtop.log; \
    rm -fr priority15/priority15.egg-info; \
    rm -fr collectors/cbagent.egg-info collectors/dist collectors/build; \
    rm -f `find . -name *.pyc`

buildout: ; \
    buildout -t 120 -q;

pep8: ; \
    ./bin/pep8 --ignore=E501 collectors cbtop priority15 webapp

jshint: ; \
    jshint webapp/cbmonitor/static/scripts

test_webapp: ; \
    ./bin/django test_coverage cbmonitor

start_webapp: ; \
    ./bin/django syncdb --noinput; \
    ./bin/django runserver --nothreading --traceback &

stop_webapp: ; \
    kill -9 `ps -ef | grep django | grep -v grep | awk '{print $$2}'` 2>/dev/null; \
    rm -fr cbmonitor.db

test_collectors: ; \
    ./bin/nosetests collectors

test: buildout pep8 jshint test_webapp start_webapp test_collectors stop_webapp;
