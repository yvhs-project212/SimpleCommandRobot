#!/usr/bin/bash

if [[ "$1" = "" || "$1" != "http"* ]]; then
  scriptname="$(basename $0)"
  cat <<EOF
Usage: $scriptname <GitHubURL of new project> [new directory name]
  GitHub project must be created first.
  By default, the new directory will have the same name as the GitHub project.

EOF
  exit 1
fi

url="$1"
project="$(basename "$1")"
repos="$(dirname $(dirname $(realpath "$0")))"
[ -n "$2" ] && project="$2"

# Confirm GitHub project
response=$(curl -sI "$url" | perl -ne '/^HTTP.*? (\d+)/ and print "$1";')
if [ "$response" != 200 ]; then
  cat <<EOF
ERROR: GitHub project doesn't appear to exist.  (HTTP response code $response)
 * Create your new project on GitHub before running this script.

EOF
  exit 1
fi

echo "Creating project $project in directory $repos..."
cd $repos
git clone "$url" "$project"

echo "Confirming that GitHub project is new..."
cd "$project"
if [ "$DANGEROUS" = "" -a "$(git log -g --oneline 2>/dev/null | wc -l)" -gt 1 ]; then
  cat <<EOF
ERROR: GitHub project "$url"
  This appears to be an existing repository with commits.  This script won't
  replace an existing repo unless the DANGEROUS environment variable is set.
  Aborting.
EOF
  exit 1
fi

echo "Downloading robotpy template..."
cd "$repos"
git clone "https://github.com/yvhs-project212/SimpleCommandRobot" JUNK-template
cd JUNK-template
git checkout template
mv .gitignore LICENSE code ../"$project"/
cd ..
rm -rf JUNK-template

echo "Adding first commit..."
cd "$project"
git add .gitignore LICENSE code
git commit -m"Create new robot project based on SimpleCommandRobot template"

echo "Pushing to GitHub..."
git push origin main

echo "New project \"$project\" created successfully."
