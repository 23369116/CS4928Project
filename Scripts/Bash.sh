#!/bin/bash
while IFS= read -r in || [ -n "$in" ]; do
    in=$(echo "$in" | tr -d '\r')
    if [ -n "$in" ]; then
        echo "=================================================="
        echo "🚀 Processing project: $in"
        echo "=================================================="

        # 1. RUN PMD (Outputs matching suffix expected by Python)
        echo "🔍 Running PMD analysis..."
        /C/Users/donag/Downloads/pmd-bin-6.23.0/pmd-bin-6.23.0/bin/run.sh pmd \
            -d "$in" \
            -f xml \
            -R rulesets/java/quickstart.xml > "${in}_PMD_RULESET.xml"
        echo "✅ PMD completed. Saved to: ${in}_PMD_RULESET.xml"

        # 2. RUN DESIGNITE
        echo "📐 Running Designite analysis..."
        mkdir -p "${in}_Designite_Output"
        
        java -jar ./DesigniteJava.jar -i "$in" -o "${in}_Designite_Output"
            
        echo "✅ Designite completed. Saved to folder: ${in}_Designite_Output/"
    fi
done < projectList.txt
