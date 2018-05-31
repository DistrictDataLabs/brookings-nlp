#!/bin/bash
# Execute the reveal.js slides form of a Notebook

# Make sure the first argument to this script is a notebook
if [ "$#" -ne 1 ]; then
  echo "Usage: ./slideshow.sh Notebook.ipynb"
  exit 1
fi

# Make sure the notebook exists
if [ ! -f "$1" ]; then
    echo "Please specify an existing notebook"
    exit 1
fi

# Execute the jupyter slides convert and serving
jupyter nbconvert "$1" --output-dir=slides --to slides --post serve
