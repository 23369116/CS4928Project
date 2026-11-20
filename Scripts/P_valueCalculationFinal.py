from collections import Counter, defaultdict
import glob
import math
import os
import re
import xml.etree.ElementTree as ET
import pandas as pd
from scipy.stats import spearmanr


def parse_pmd(xml_path):
    """Parses PMD XML and returns:

    1. Total violation counts per class
    2. Violation counts broken down by specific PMD rule per class
    """
    total_counts = Counter()
    rule_counts = defaultdict(Counter)  # {rule_name: Counter({class_id: count})}

    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
        for violation in root.findall('.//{*}violation'):
            pkg = violation.get('package', '').strip()
            cls = violation.get('class', '').strip()
            rule = violation.get('rule', 'UnknownRule').strip()

            if cls:
                identifier = f'{pkg}.{cls}'.replace('$', '.') if pkg else cls.replace('$', '.')
                total_counts[identifier] += 1
                rule_counts[rule][identifier] += 1
    except Exception as e:
        print(f' [-] Error parsing PMD XML ({os.path.basename(xml_path)}): {e}')

    return total_counts, rule_counts


def parse_designite(target_dir):
    """Parses Designite CSVs and returns smell counts keyed by FQCN."""
    designite_counts = Counter()
    smell_files = ['designCodeSmells.csv', 'architectureCodeSmells.csv']

    for csv_file in smell_files:
        csv_path = os.path.join(target_dir, csv_file)
        if not os.path.exists(csv_path):
            continue

        try:
            df_des = pd.read_csv(csv_path)
            pkg_col = next((c for c in ['Package Name', 'Package name'] if c in df_des.columns), None)
            cls_col = next((c for c in ['Type Name', 'Class Name', 'Type name', 'Class name'] if c in df_des.columns), None)

            if not cls_col:
                continue

            df_valid = df_des.dropna(subset=[cls_col]).copy()
            cls_series = df_valid[cls_col].astype(str).str.strip().str.replace('$', '.', regex=False)

            if pkg_col:
                pkg_series = df_valid[pkg_col].fillna('').astype(str).str.strip()

                identifiers = [
                    f'{p}.{c}' if (p and not c.startswith(f'{p}.')) else c
                    for p, c in zip(pkg_series, cls_series)
                ]

            else:
                identifiers = cls_series.tolist()

            designite_counts.update(identifiers)
        except Exception as e:
            print(f' [-] Error reading Designite CSV ({csv_file}): {e}')

    return designite_counts


def analyze_rule_correlations(df_global, all_rule_keys):
    """Calculates Spearman correlation and p-values for every individual PMD warning rule."""
    results = []
    num_rules = len(all_rule_keys)

    for rule in all_rule_keys:
        col_name = f'RULE_{rule}'
        # Skip rules that appear in fewer than 3 classes or have zero variance
        if df_global[col_name].nunique() <= 1 or (df_global[col_name] > 0).sum() < 3:
            continue

        coef, p_val = spearmanr(df_global[col_name], df_global['Designite_Smells'])
        if math.isnan(coef) or math.isnan(p_val):
            continue

        # Bonferroni correction adjusts p-value for multiple hypothesis testing
        bonferroni_p = min(p_val * num_rules, 1.0)

        results.append({
            'PMD_Rule': rule,
            'Classes_Affected': int((df_global[col_name] > 0).sum()),
            'Total_Occurrences': int(df_global[col_name].sum()),
            'Spearman_R': round(coef, 4),
            'Raw_P_Value': p_val,
            'Bonferroni_P_Value': bonferroni_p,
            'Significant_Strict': bonferroni_p < 0.05
        })

    if not results:
        print('\n[-] Not enough rule variance to compute per-warning correlations.')
        return

    df_rules = pd.DataFrame(results).sort_values(by='Raw_P_Value', ascending=True)
    df_rules.to_csv('pmd_rule_correlations.csv', index=False)

    print('\n########################################################################')
    print('### TOP PMD WARNINGS CORRELATED WITH DESIGNITE SMELLS (BY P-VALUE)   ###')
    print('########################################################################')
    # Format p-values cleanly for console display
    display_df = df_rules.head(15).copy()
    display_df['Raw_P_Value'] = display_df['Raw_P_Value'].map(lambda x: f'{x:.2e}')
    display_df['Bonferroni_P_Value'] = display_df['Bonferroni_P_Value'].map(lambda x: f'{x:.2e}')
    print(display_df.to_string(index=False))
    print('\n[+] Full rule-by-rule p-value table saved to: pmd_rule_correlations.csv')


def sync_project(system_name, pmd_path, designite_dir):
    """Aligns total counts and per-rule counts for a single project."""
    print(f'[+] Syncing metrics for system: {system_name}')
    total_pmd, rule_pmd = parse_pmd(pmd_path)
    designite_counts = parse_designite(designite_dir)

    all_classes = set(total_pmd.keys()).union(designite_counts.keys())
    rows = []

    for cls in all_classes:
        row = {
            'System': system_name,
            'Class': cls,
            'PMD_Violations': total_pmd[cls],
            'Designite_Smells': designite_counts[cls],
        }
        # Attach individual rule counts for this class
        for rule, counts_dict in rule_pmd.items():
            row[f'RULE_{rule}'] = counts_dict[cls]
        rows.append(row)

    return rows, set(rule_pmd.keys())


def main():
    base_dir = '.'
    all_global_data = []
    all_rules_discovered = set()
    current_folder_name = os.path.basename(os.getcwd())

    local_pmd = glob.glob('*PMD*.xml')
    local_des_dir = f'{current_folder_name}_Designite_Output'

    if local_pmd and os.path.exists(local_des_dir):
        rows, rules = sync_project(current_folder_name, local_pmd[0], local_des_dir)
        all_global_data.extend(rows)
        all_rules_discovered.update(rules)
    else:
        project_files = {}
        for pmd_path in sorted(glob.glob(os.path.join(base_dir, '*_PMD_*.xml'))):
            match = re.match(r'(.+?)_PMD_(COMBINED|DESIGN)\.xml$', os.path.basename(pmd_path))
            if match:
                version_key, report_type = match.groups()
                if version_key not in project_files or report_type == 'COMBINED':
                    project_files[version_key] = pmd_path

        for version_key, pmd_path in project_files.items():
            designite_dir = os.path.join(base_dir, f'{version_key}_Designite_Output')
            if os.path.exists(designite_dir):
                rows, rules = sync_project(version_key, pmd_path, designite_dir)
                all_global_data.extend(rows)
                all_rules_discovered.update(rules)

    if not all_global_data:
        print('\n[-] No data synchronized. Check filenames.')
        return

    # Fill missing rule columns with 0 for classes/projects that didn't trigger a specific rule
    df_global = pd.DataFrame(all_global_data).fillna(0)

    # Save main matrix (excluding the dynamic RULE_ columns to keep it clean)
    core_cols = ['System', 'Class', 'PMD_Violations', 'Designite_Smells']
    df_global[core_cols].to_csv('final_study_correlation_matrix.csv', index=False)

    # Run rule-by-rule p-value analysis
    analyze_rule_correlations(df_global, sorted(all_rules_discovered))


if __name__ == '__main__':
    main()
