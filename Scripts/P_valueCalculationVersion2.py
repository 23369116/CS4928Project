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
            package_name = violation.get('package', '').strip()
            class_name = violation.get('class', '').strip()
            
            if class_name:
                # If PMD includes package info, build FQCN, otherwise use class name
                fqcn = f"{package_name}.{class_name}" if package_name else class_name
                # Standardize to short name as a universal fallback key to guarantee matching
                short_name = class_name.split('.')[-1]
                
                if short_name not in pmd_counts:
                    pmd_counts[short_name] = 0
                pmd_counts[short_name] += 1
    except Exception as e:
        print(f"  [-] Error parsing PMD XML ({os.path.basename(xml_path)}): {e}")
    return pmd_counts

def parse_designite(target_dir):
    designite_counts = {}
    smell_files = ['designCodeSmells.csv', 'architectureCodeSmells.csv']
    
    for csv_file in smell_files:
        csv_path = os.path.join(target_dir, csv_file)
        if not os.path.exists(csv_path):
            continue
            
        try:
            df_des = pd.read_csv(csv_path)
            
            # Find the type/class identifier column
            class_col = None
            for col in ['Type Name', 'Class Name', 'Type name', 'Class name']:
                if col in df_des.columns:
                    class_col = col
                    break
            
            if class_col:
                for _, row in df_des.iterrows():
                    raw_class = str(row[class_col]).strip()
                    if pd.isna(row[class_col]) or raw_class == 'nan':
                        continue
                    
                    # Extract the short name to align with PMD's fallback formatting
                    short_name = raw_class.split('.')[-1]
                    
                    if short_name not in designite_counts:
                        designite_counts[short_name] = 0
                    designite_counts[short_name] += 1
        except Exception as e:
            print(f"  [-] Error reading Designite CSV ({csv_file}): {e}")
            
    return designite_counts

def analyze_correlation(df, label="Global"):
    if len(df) > 1 and (df['PMD_Violations'].any() or df['Designite_Smells'].any()):
        coef, p_value = spearmanr(df['PMD_Violations'], df['Designite_Smells'])
        print(f"\n================ [{label} Analysis] ================")
        print(f"Total Unique Classes Aligned: {len(df)}")
        print(f"Spearman Correlation Coefficient: {coef:.4f}")
        print(f"P-value (Significance level): {p_value:.6f}")
        print("--------------------------------------------------")
        
        if p_value > 0.05:
            print("Interpretation: Not Statistically Significant (p > 0.05).")
        elif coef > 0.5:
            print("Interpretation: Strong Positive Correlation! Low-level structural tension aligns cleanly with macro-architectural decay.")
        elif coef > 0.2:
            print("Interpretation: Moderate Positive Correlation. Code complexity trends upward alongside design smells.")
        elif coef < -0.2:
            print("Interpretation: Negative Correlation. The tools have an inverse relationship on this subset.")
        else:
            print("Interpretation: Weak or Negligible Correlation.")
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
local_pmd = glob.glob("*PMD*.xml")
if local_pmd and os.path.exists(f"{current_folder_name}_Designite_Output"):
    print(f"\n[+] Detected localized project workspace: {current_folder_name}")
    pmd_counts = parse_pmd(local_pmd[0])
    designite_counts = parse_designite(f"{current_folder_name}_Designite_Output")
    
    all_classes = set(pmd_counts.keys()).union(set(designite_counts.keys()))
    for cls in all_classes:
        all_global_data.append({
            "System": current_folder_name,
            "Class": cls,
            "PMD_Violations": pmd_counts.get(cls, 0),
            "Designite_Smells": designite_counts.get(cls, 0)
        })
else:
    # 2. BATCH PIPELINE MODE
    pmd_files = glob.glob(os.path.join(base_dir, "*_PMD_COMBINED.xml")) + glob.glob(os.path.join(base_dir, "*_PMD_DESIGN.xml"))
    
    for pmd_path in pmd_files:
        filename = os.path.basename(pmd_path)
        version_match = re.match(r"(.+?)_PMD_(COMBINED|DESIGN)\.xml", filename)
        if not version_match:
            continue
            
        version_key = version_match.group(1)
        designite_dir = os.path.join(base_dir, f"{version_key}_Designite_Output")
        
        if os.path.exists(designite_dir):
            print(f"[+] Syncing metrics for system: {version_key}")
            pmd_counts = parse_pmd(pmd_path)
            designite_counts = parse_designite(designite_dir)
            
            all_classes = set(pmd_counts.keys()).union(set(designite_counts.keys()))
            for cls in all_classes:
                all_global_data.append({
                    "System": version_key,
                    "Class": cls,
                    "PMD_Violations": pmd_counts.get(cls, 0),
                    "Designite_Smells": designite_counts.get(cls, 0)
                })

# --- Run Statistics ---
if all_global_data:
    df_global = pd.DataFrame(all_global_data)
    df_global.to_csv("final_study_correlation_matrix.csv", index=False)
    
    print("\n##################################################")
    print("###          CORRECTED COMBINED LEADERBOARD    ###")
    print("##################################################")
    print(df_global.sort_values(by='PMD_Violations', ascending=False).head(10).to_string(index=False))
    
    print("\n🔬 Running Flawed-Only Subset Sensitivity Check...")
    df_flawed = df_global[(df_global['PMD_Violations'] > 0) & (df_global['Designite_Smells'] > 0)]
    if len(df_flawed) > 1:
        analyze_correlation(df_flawed, label="FLAWED SUBSET ONLY")
    else:
        print("  -> Not enough overlapping flawed classes to run subset math.")
    print("--------------------------------------------------\n")

    # Call your original global analysis function
    analyze_correlation(df_global, label="COMBINED SYSTEM-WIDE GLOBAL")
else:
    print("\n[-] No data synchronized. Check filenames.")

