#!/bin/bash

# Check if commit message was provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <commit-message>"
    exit 1
fi

# Variables
COMMIT_MESSAGE="$1"

# Adding all changes to git
git add .

# Committing changes
git commit -m "$COMMIT_MESSAGE"

# Pushing to the remote repository
git push

