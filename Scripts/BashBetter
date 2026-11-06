#!/bin/bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

while IFS= read -r in || [ -n "$in" ]; do
    in=$(echo "$in" | tr -d '\r')
    if [ -n "$in" ]; then
        echo "=================================================="
        echo "🚀 Recreating Study for Project: $in"
        echo "=================================================="

        # 1. RUN PMD WITH BUILT-IN STRUCTURAL DESIGN RULES ONLY
        # This eliminates formatting noise and extracts true design metrics
        RULESETS="category/java/design.xml"
        PMD_OUTPUT="${in}_PMD_DESIGN.xml"
        
        echo "🔍 Running PMD Design Analysis..."
        /C/Users/donag/Downloads/pmd-bin-6.23.0/pmd-bin-6.23.0/bin/run.sh pmd \
            -d "$in" \
            -f xml \
            -R "$RULESETS" \
            -threads 1 > "$PMD_OUTPUT"
        
        echo "✅ PMD Design Completed."

        # 2. RUN DESIGNITE
        echo "📐 Running Designite analysis..."
        DESIGNITE_DIR="${in}_Designite_Output"
        mkdir -p "$DESIGNITE_DIR"
        java -jar ./DesigniteJava.jar -i "$in" -o "$DESIGNITE_DIR"
        echo "✅ Designite Completed."

        # 3. ACADEMIC CORRELATION PARSER
        echo "📊 Computing Package-Level Correlation Matrix..."
        
        python3 -c "
import xml.etree.ElementTree as ET
import csv
import os

pmd_xml = '$PMD_OUTPUT'
designite_dir = '$DESIGNITE_DIR'
project_name = '$in'

# Structure: { package_name: {'pmd_count': 0, 'arch_smells': 0, 'pmd_rules': set(), 'smells': set()} }
package_metrics = {}

def get_package_from_path(filepath):
    # Extracts a generic package structure from file paths to align both tools
    normalized = os.path.normpath(filepath)
    parts = normalized.split(os.sep)
    if 'src' in parts:
        src_index = parts.index('src')
        return '.'.join(parts[src_index+1:-1])
    return '.'.join(parts[-3:-1]) if len(parts) > 2 else 'root'

# Parse PMD Design Warnings
if os.path.exists(pmd_xml):
    try:
        tree = ET.parse(pmd_xml)
        root = tree.getroot()
        for file_elem in root.findall('.//file'):
            filepath = file_elem.get('name', '')
            pkg = get_package_from_path(filepath)
            
            if pkg not in package_metrics:
                package_metrics[pkg] = {'pmd_count': 0, 'arch_smells': 0, 'pmd_rules': set(), 'smells': set()}
                
            for viol in file_elem.findall('violation'):
                package_metrics[pkg]['pmd_count'] += 1
                package_metrics[pkg]['pmd_rules'].add(viol.get('rule'))
    except Exception as e:
        print(f'Error parsing PMD: {e}')

# Parse Designite Architecture/Design Smells
code_smells_path = os.path.join(designite_dir, 'CodeSmells.csv')
if os.path.exists(code_smells_path):
    try:
        with open(code_smells_path, mode='r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Target 'Package Name' if Designite lists it, fallback to path extraction
                pkg = row.get('Package Name', get_package_from_path(row.get('File Name', '')))
                if not pkg or pkg == '': 
                    pkg = 'root'
                
                if pkg not in package_metrics:
                    package_metrics[pkg] = {'pmd_count': 0, 'arch_smells': 0, 'pmd_rules': set(), 'smells': set()}
                
                package_metrics[pkg]['arch_smells'] += 1
                package_metrics[pkg]['smells'].add(row.get('Code Smell', row.get('Code Smell Type', 'Unknown')))
    except Exception as e:
        print(f'Error reading Designite: {e}')

# Output Academic Summary Matrix
output_csv = f'{project_name}_Correlation_Matrix.csv'
print(f'\n🏫 Package Structural Density Correlation:')
print(f'{\"Package Scope\":<40} | {\"PMD Design Flags\":<16} | {\"Arch Smells\":<12}')
print('-' * 75)

with open(output_csv, mode='w', newline='', encoding='utf-8') as out_f:
    writer = csv.writer(out_f)
    writer.writerow(['Package', 'PMD Design Warnings', 'Architectural Smells', 'Triggered PMD Rules', 'Triggered Smells'])
    
    for pkg, data in sorted(package_metrics.items()):
        writer.writerow([pkg, data['pmd_count'], data['arch_smells'], ', '.join(data['pmd_rules']), ', '.join(data['smells'])])
        if data['pmd_count'] > 0 or data['arch_smells'] > 0:
            print(f'{pkg[:40]:<40} | {data[\"pmd_count\"]:<16} | {data[\"arch_smells\"]:<12}')

print(f'\n💾 Correlation Matrix successfully exported to: {output_csv}\n')
"
    fi
done < projectList.txt
