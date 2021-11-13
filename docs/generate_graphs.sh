#!/usr/bin/env bash

WORKING_DIR=$(pwd)
IMG_DIR=$WORKING_DIR/img
GRAPH_DIR=$WORKING_DIR/graph

if [[ ! -d $IMG_DIR  || ! -d $GRAPH_DIR ]]
then 
	echo "Exiting -- Run this from the correct directory." 
	exit 1
fi

files_todo=""
for file in $GRAPH_DIR/*
do 
	name=${file##*/} 			# /path/to/graph.uml -> graph.uml
	base=${name%%.*}			# graph.uml -> graph

	if [[ ! -e "$IMG_DIR/$base.png" ]]  	# img doesn't exist for this graph
	then
		echo "+ $name has no rendered image."
		files_todo+=" $file"
	fi
done


if [[ -n $files_todo ]] 
then
	echo "Generating images..." 
	plantuml $files_todo -o $IMG_DIR
else
	echo "All images are present. Nothing to do." 
fi

exit 0
