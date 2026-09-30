import sys, commons
for q in sys.argv[1:]:
    d = commons.call(dict(action="query", list="search", srsearch=q, srnamespace=14, srlimit=15))
    print("##", q)
    for s in d["query"]["search"]: print(s["title"])
