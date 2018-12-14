#!/bin/sh
pid=`netstat -ntpl | grep uwsgi | awk '{print $NF}'|awk -F'/' '{print $1}'`
echo $pid
 
while [ -n "$1" ]  
do  
case "$1" in   
    start)  
        uwsgi testtool.ini
        /etc/init.d/nginx start
        shift
        ;;  
    stop)  
        kill -9 $pid
        /etc/init.d/nginx stop
        shift  
        ;;  
    restart)  
        kill -9 $pid
        uwsgi testtool.ini
        /etc/init.d/nginx restart
        shift  
        ;;  
     *)  
         echo "use start|stop|restart to execute the bash script"  
        ;;  
esac
done
