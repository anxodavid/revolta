"""Lanza las consultas a Commons por concepto y vuelca metadatos (sin descargar imágenes) en JSONL."""
import json, sys, commons
C = "Category:"
JOBS = {
 "01-horreo": dict(cats=["Quality images of Hórreos in Galicia (Spain)","Hórreos in the province of Lugo","Hórreos in the province of Ourense","Hórreos in the province of Pontevedra","Hórreos in the province of A Coruña","Hórreos in Combarro","Hórreos, Folgoso do Courel","Hórreo de Carnota","Hórreo de Lira","Hórreos in Galicia (Spain)"], finds=["hórreo granito Galicia"]),
 "02-carro-bois": dict(cats=["Carts in Galicia (Spain)","Carros de bois","Yokes in Galicia (Spain)","Rubia Gallega"], finds=["carro do país Galicia bois","carro de bois Galicia rodas macizas","Galician ox cart"]),
 "03-palloza-casa": dict(cats=["Pallozas","Pallozas in Piornedo","Pallozas in Cervantes","Pallozas in Cervantes (Lugo)","Pallozas in Balouta","Pallozas in Campo del Agua","Pallozas in Pedrafita do Cebreiro"], finds=["casa rural granito lousa Galicia","aldea Galicia casa de pedra tejado pizarra"]),
 "04-pazo": dict(cats=["Pazos in Galicia (Spain)","Pazo de Oca","Patio of the Pazo de Oca","Pazo Baión","Pazos in the province of Pontevedra"], finds=["pazo galego fachada","pazo galicia palomar capilla","Pazo de Fefiñáns","Pazo de Mariñán"]),
 "05-cruceiro-peto": dict(cats=["Wayside crosses in Galicia (Spain)","Cruceiro de Mañufe","Cruceiro do Berbés","Cruceiro da Costa","Cruceiro dos Maios","Wayside shrines in Galicia (Spain)","Petos de ánimas"], finds=["peto de ánimas Galicia","cruceiro Galicia granito"]),
 "06-cocina": dict(cats=["Lareiras","Kitchens in Galicia (Spain)","Hearths in Galicia (Spain)"], finds=["lareira cociña tradicional galega","escano lareira Galicia","pote de ferro lareira","gramalleira","lacena cociña galega","cunca de barro Galicia"]),
 "07-queimada": dict(cats=["Queimada (drink)","Queimada"], finds=["queimada Galicia pota barro"]),
 "08-traje": dict(cats=["Traditional clothing of Galicia (Spain)","Clogs of Galicia (Spain)"], finds=["traxe tradicional galego","coroza Galicia capa de xunco","refaixo dengue mantelo","montera galega traxe"]),
 "09-herramientas": dict(cats=["Agricultural tools in Galicia (Spain)","Ploughs in Galicia (Spain)","Spinning wheels in Galicia (Spain)","Looms in Galicia (Spain)","Museo do Pobo Galego"], finds=["arado romano Galicia","mallo debullar Galicia","roca fuso fiar Galicia","tear tradicional Galicia","fouce sacho Galicia ferramenta","grade arado madeira Galicia"]),
 "10-muino-fonte": dict(cats=["Watermills in Galicia (Spain)","Interiors of watermills in Galicia (Spain)","Fulling stocks in Galicia (Spain)","Wash houses in Galicia (Spain)","Fountains in Galicia (Spain)","Water wheels in Galicia (Spain)"], finds=["muíño de auga Galicia","batán Galicia"]),
 "11-barcos-costa": dict(cats=["Dornas","Boats of Galicia (Spain)","Quality images of Rías Baixas","Costa da Morte"], finds=["dorna barco tradicional Galicia","gamela embarcación Galicia","traiñeira Galicia","barco tradicional ría Arousa"]),
 "12-iconografia": dict(cats=["Romanesque corbels in Galicia","Romanesque capitals in Santiago de Compostela","Castle of Pambre","Castle of Sobroso","Castle of Monterrei","Castle of Ribadavia","Sculptures in Santa María de Oseira"], finds=["Tumbo A catedral Santiago miniatura","Cantigas de Santa Maria miniatura","grabado Santiago de Compostela siglo XVII","Compostela grabado siglo XVI"]),
 "13-armas-ropa": dict(cats=["Spanish armour","Spanish swords"], finds=["armadura española siglo XVI","Spanish arquebus 16th century","escribano siglo XVII grabado","Spanish 16th century costume engraving"]),
 "14-samos-antiguo": dict(cats=["Monastery of San Xulián de Samos","Quality images of Mosteiro de San Xulián de Samos","Ruth Matilda Anderson","Cloisters of the Mosteiro of Santa María de Oseira"], finds=["Galicia fotografía antigua 1910","Samos claustro","aldea gallega fotografía 1920 Anderson"]),
}
only = sys.argv[1:] 
for k, j in JOBS.items():
    if only and k not in only: continue
    seen = set()
    with open(f"datos/{k}.jsonl", "w") as f:
        for c in j["cats"]:
            for r in commons.cat_files(C + c, 120):
                if r["page"] in seen: continue
                seen.add(r["page"]); r["origen"] = "cat:" + c; f.write(json.dumps(r, ensure_ascii=False) + "\n")
            f.flush()
        for q in j["finds"]:
            for r in commons.find(q, 60):
                if r["page"] in seen: continue
                seen.add(r["page"]); r["origen"] = "find:" + q; f.write(json.dumps(r, ensure_ascii=False) + "\n")
            f.flush()
    print("listo", k, len(seen), flush=True)
