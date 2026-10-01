import yaml, sys, language_tool_python as L
d = yaml.safe_load(open(sys.argv[1]))
tool = L.LanguageTool('gl-ES')
n = 0
for f in d['feitos']:
    for m in tool.check(f['feito']):
        pal = f['feito'][m.offset:m.offset+m.error_length]
        n += 1
        print(f"{f['id']} [{m.rule_id}] «{pal}» -> {m.replacements[:3]} :: {m.message[:100]}")
tool.close()
print('total avisos', n)
