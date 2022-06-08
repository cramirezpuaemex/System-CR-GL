#!/bin/bash
cd /home/carlos/Escritorio/Resultados/2006/

FILES=`ls -1d *`


for  FILES in $FILES
do
	echo $FILES
    cd $FILES
    FILES2=`ls -1d *`
    for FILES2 in $FILES2
    do
        echo $FILES2
    done
    cd ..


done
