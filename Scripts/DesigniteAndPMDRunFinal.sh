#!/bin/bash
set -u  # Catch uninitialized variables

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR" || exit 1

PMD_BIN="/C/Users/donag/Downloads/pmd-bin-6.23.0/pmd-bin-6.23.0/bin/run.sh"
DESIGNITE_JAR="./DesigniteJava.jar"
RULESETS="category/java/design.xml,category/java/bestpractices.xml,category/java/codestyle.xml,category/java/documentation.xml"

# Automatically pick whichever Python interpreter has pandas/scipy installed
if python -c "import pandas, scipy" >/dev/null 2>&1; then
    PYTHON_CMD="python"
elif python3 -c "import pandas, scipy" >/dev/null 2>&1; then
    PYTHON_CMD="python3"
else
    echo "❌ Error: Neither 'python' nor 'python3' has pandas and scipy installed."
    echo "   Run: python -m pip install pandas scipy"
    exit 1
fi

if [ ! -f "projectList.txt" ]; then
    echo "❌ Error: projectList.txt not found in $SCRIPT_DIR"
    exit 1
fi

while IFS= read -r in || [ -n "$in" ]; do
    # Strip Windows carriage returns (\r) and trailing slashes
    in=$(echo "$in" | tr -d '\r' | sed 's:/*$::')
    [ -z "$in" ] && continue

    if [ ! -d "$in" ]; then
        echo "⚠️  Skipping '$in': Directory does not exist."
        continue
    fi

    # Flatten nested paths (e.g., repos/freemind-0.9.0 -> freemind-0.9.0) so p.py finds them
    PROJECT_KEY=$(basename "$in")

    echo "=================================================="
    echo "🚀 Recreating Study for Project: $PROJECT_KEY ($in)"
    echo "=================================================="

    # 1. RUN PMD (Recursively scans all subfolders inside $in)
    PMD_OUTPUT="${PROJECT_KEY}_PMD_COMBINED.xml"
    echo "🔍 Running PMD Analysis..."
    "$PMD_BIN" pmd \
        -d "$in" \
        -f xml \
        -R "$RULESETS" \
        -threads 1 > "$PMD_OUTPUT"
    PMD_EXIT=$?

    # PMD exits with 0 (no violations) or 4 (violations found). Any other code is an error.
    if [ $PMD_EXIT -ne 0 ] && [ $PMD_EXIT -ne 4 ]; then
        echo "❌ PMD failed with exit code $PMD_EXIT for $PROJECT_KEY. Removing corrupt XML."
        rm -f "$PMD_OUTPUT"
        continue
    fi
    echo "✅ PMD Completed: $PMD_OUTPUT"

    # 2. RUN DESIGNITEJAVA (Recursively scans all subfolders inside $in)
    echo "📐 Running Designite analysis..."
    DESIGNITE_DIR="${PROJECT_KEY}_Designite_Output"
    mkdir -p "$DESIGNITE_DIR"
    java -jar "$DESIGNITE_JAR" -i "$in" -o "$DESIGNITE_DIR"
    echo "✅ Designite Completed: $DESIGNITE_DIR/"

done < projectList.txt

# 3. RUN CORRELATION SCRIPT
echo "=================================================="
echo "📊 Running Statistical Correlation Script (p.py) using $PYTHON_CMD..."
echo "=================================================="
"$PYTHON_CMD" P_valueCalculationFinal.py

