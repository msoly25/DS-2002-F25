#!/bin/bash

# Fetch data from the Dog CEO API and save it to a file.
# We redirect standard output (1) to a file.
echo "Fetching all dog breeds..."
curl -s 'https://dog.ceo/api/breeds/list/all' > breeds.json


