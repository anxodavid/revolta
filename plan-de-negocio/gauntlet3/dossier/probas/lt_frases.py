import sys, language_tool_python as L
tool = L.LanguageTool('gl-ES')
for s in open(sys.argv[1]).read().strip().split('\n'):
    ms = [(m.rule_id, s[m.offset:m.offset+m.error_length], m.replacements[:2]) for m in tool.check(s) if not m.rule_id.startswith('HUNSPELL')]
    print('OK ' if not ms else 'MAL', s, ms if ms else '')
tool.close()
