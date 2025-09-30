#!/bin/bash
set -e

for file in *.stl; do
    [ -e "$file" ] || continue

    base=$(basename "$file" .stl)
    tmpfile="${file}.tmp"

    awk -v name="$base" '
        # Match "solid" with optional whitespace, but not if already named
        /^[[:space:]]*solid[[:space:]]*$/          { print "solid " name; next }
        /^[[:space:]]*solid[[:space:]]+"name"$/    { print; next }

        # Match "solid something", but only if it’s not the correct name
        /^[[:space:]]*solid[[:space:]]+/ && $2 != name {
            print "solid " name; next
        }

        # Same logic for endsolid
        /^[[:space:]]*endsolid[[:space:]]*$/        { print "endsolid " name; next }
        /^[[:space:]]*endsolid[[:space:]]+"name"$/  { print; next }

        /^[[:space:]]*endsolid[[:space:]]+/ && $2 != name {
            print "endsolid " name; next
        }

        { print }
    ' "$file" > "$tmpfile"

    mv "$tmpfile" "$file"
    echo "✅ Verified or updated: $file"
done

