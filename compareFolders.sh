#!/bin/bash

filestocheck=(`ls source_folder/`)
for file in ${filestocheck[@]}; do ls destination_folder/ | grep $file; done

#This will show from which files source_folder are present in destination_folder.
