#!/bin/sh
pid=`netstat -ntpl | grep uwsgi | awk '{print $NF}'|awk -F'/' '{print $1}'`
echo $pid
kill -9 $pid
uwsgi testtool.ini
newpid=`netstat -ntpl | grep uwsgi | awk '{print $NF}'|awk -F'/' '{print $1}'`
echo 'success new pid is '${newpid}
