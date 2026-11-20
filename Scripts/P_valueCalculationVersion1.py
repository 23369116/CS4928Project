import os
import glob
import re
import xml.etree.ElementTree as ET
import pandas as pd
from scipy.stats import spearmanr

def parse_pmd(xml_path):
    pmd_counts = {}
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
        for violation in root.findall('.//{*}violation'):
            class_name = violation.get('class')
            if class_name:
                clean_class = class_name.split('.')[-1]
                pmd_counts[clean_class] = pmd_counts.get(clean_class, 0) + 1
    except Exception as e:
        print(f"  [-] Error parsing PMD XML ({os.path.basename(xml_path)}): {e}")
    return pmd_counts

def parse_designite(csv_path):
    designite_counts = {}
    try:
        df_des = pd.read_csv(csv_path)
        class_col = None
        for col in ['Type Name', 'Class Name', 'Type name', 'Class name']:
            if col in df_des.columns:
                class_col = col
                break
                
        if class_col:
            df_counts = df_des[class_col].value_counts()
            for full_class_name, count in df_counts.items():
                clean_class = str(full_class_name).split('.')[-1]
                designite_counts[clean_class] = count
        else:
            print(f"  [-] Column missing from CSV {os.path.basename(csv_path)}.")
    except Exception as e:
        print(f"  [-] Error reading Designite CSV ({os.path.basename(csv_path)}): {e}")
    return designite_counts

def analyze_correlation(df, label="Global"):
    if len(df) > 1 and (df['PMD_Violations'].any() or df['Designite_Smells'].any()):
        coef, p_value = spearmanr(df['PMD_Violations'], df['Designite_Smells'])
        print(f"\n================ [{label} Analysis] ================")
        print(f"Total Classes Evaluated: {len(df)}")
        print(f"Spearman Correlation Coefficient: {coef:.4f}")
        print(f"P-value (Significance level): {p_value}")
        print("--------------------------------------------------")
        if coef > 0.5:
            print("Interpretation: Strong Positive Correlation! Badly formatted modules cleanly align with severe structural decay.")
        elif coef > 0.1:
            print("Interpretation: Weak Positive Correlation. The tools intersect loosely on flawed classes.")
        else:
            print("Interpretation: No clear Correlation. PMD syntax errors do not indicate architectural issues.")
        print("==================================================")
        return coef, p_value
    else:
        print(f"\n[-] Insufficient data variation in {label} to calculate correlation.")
        return None, None

# --- Main Adaptive Scanning Routine ---
base_dir = "."
all_global_data = []
current_folder_name = os.path.basename(os.getcwd())

print(f"Scanning base directory: {os.path.abspath(base_dir)}")

# 1. CHECK LOCAL ISOLATED DIRECTORY FIRST
# Look for a localized structure (e.g. if you are directly inside 'collections' or 'ant-1.8.4')
local_pmd = glob.glob("*PMD*.xml")
local_designite_csv = glob.glob("**/implementationCodeSmells.csv", recursive=True)

if local_pmd and local_designite_csv:
    print(f"\n[+] Detected localized project workspace: {current_folder_name}")
    pmd_path = local_pmd[0]
    designite_csv_path = local_designite_csv[0]
    
    pmd_counts = parse_pmd(pmd_path)
    designite_counts = parse_designite(designite_csv_path)
    
    all_classes = set(pmd_counts.keys()).union(set(designite_counts.keys()))
    for cls in all_classes:
        all_global_data.append({
            "System": current_folder_name,
            "Class": cls,
            "PMD_Violations": pmd_counts.get(cls, 0),
            "Designite_Smells": designite_counts.get(cls, 0)
        })
else:
    # 2. FALLBACK TO MULTI-PROJECT BATCH PIPELINE MODE
    pmd_files = glob.glob(os.path.join(base_dir, "*_PMD_RULESET.xml"))
    for pmd_path in pmd_files:
        filename = os.path.basename(pmd_path)
        version_match = re.match(r"(.+?)_PMD_RULESET\.xml", filename)
        if not version_match:
            continue
            
        version_key = version_match.group(1)
        designite_csv_path = os.path.join(base_dir, f"{version_key}_Designite_Output", "implementationCodeSmells.csv")
        
        if os.path.exists(designite_csv_path):
            print(f"\n[+] Found pipeline dataset pair for system: {version_key}")
            pmd_counts = parse_pmd(pmd_path)
            designite_counts = parse_designite(designite_csv_path)
            
            all_classes = set(pmd_counts.keys()).union(set(designite_counts.keys()))
            for cls in all_classes:
                all_global_data.append({
                    "System": version_key,
                    "Class": cls,
                    "PMD_Violations": pmd_counts.get(cls, 0),
                    "Designite_Smells": designite_counts.get(cls, 0)
                })

# --- Print Visual Previews and Run Statistics ---
if all_global_data:
    df_global = pd.DataFrame(all_global_data)
    
    print("\n\n##################################################")
    print("###          COMBINED METRICS LEADERBOARD      ###")
    print("##################################################")
    print(df_global.sort_values(by='PMD_Violations', ascending=False).head(15).to_string(index=False))
    
    analyze_correlation(df_global, label=current_folder_name if local_pmd and local_designite_csv else "COMBINED SYSTEM-WIDE GLOBAL")
else:
    print("\n[-] Processing complete. No synchronized data pairs could be found.")
    print("    Ensure your PMD .xml file and Designite folder are in this directory.")
