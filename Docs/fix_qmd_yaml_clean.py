# File: fix_qmd_yaml_clean.py

input_path = "data_analysis.qmd"
output_path = "data_analysis_fixed.qmd"

with open(input_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

yaml_started = False
yaml_ended = False
yaml_lines = []
body_lines = []

for line in lines:
    if line.strip() == "---":
        if not yaml_started:
            yaml_started = True
            yaml_lines.append(line)
        elif not yaml_ended:
            yaml_ended = True
            yaml_lines.append(line)
        else:
            # Extra YAML block — treat it as normal text
            body_lines.append("\n# --- (was extra YAML)\n")
    elif yaml_started and not yaml_ended:
        yaml_lines.append(line)
    else:
        body_lines.append(line)

# Final file creation
with open(output_path, "w", encoding="utf-8") as file:
    if not yaml_ended:
        # If YAML was never properly closed, just wrap it up
        yaml_lines.append("---\n")
    file.writelines(yaml_lines)
    file.write("\n")
    file.writelines(body_lines)

print(f"✅ Fixed file written to: {output_path}")
