#!/bin/bash

# Specify the number of scripts you want to create
num_scripts=10

# Loop to create scripts
for ((i = 1; i <= num_scripts; i++)); do
	# Generate the filename
	filename="${i}-script.js"

	# Create the script
	echo -e "#!/usr/bin/env node\nconsole.log('This is script ${i}');" >"$filename"

	# Make the script executable
	chmod +x "$filename"

	echo "Created ${filename}"
done
