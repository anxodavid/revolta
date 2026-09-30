# video · ronda 3

### Crítico visual ciego: PIERDE/NO APRUEBA (mejora marginal)

Image 1 can only be judged from low-resolution 160x90 thumbnails, so hands and faces can't be checked, and some frames look blurry or oddly posed (6, 11). Image 2 is flat and monotonous, with the same grey light and the 'walking away down the path' shot repeated many times.

Image 1 wins, but only by a small margin. It looks photoreal and cinematic, like a costume drama. The lighting varies from shot to shot: backlit windows, candlelit gold interiors, a dark corridor lit by a torch, a bright garden, and a wide final shot of formal gardens. The shots also vary in type (close-ups, groups, medium shots, wide establishing shots) and the palette stays consistent throughout, which is what a history video needs to feel like a premium documentary. Its frames are 160x90 YouTube storyboard thumbnails, so artifacts can't be ruled out. Frame 6 has blurry, shapeless figures, and frame 11 has odd scale and poses in the kneeling group. Image 2 is very consistent. It keeps the same oil-painting style across all 12 frames, and at high resolution it shows no glaring artifacts or junk text. Its weaknesses are a flat grey overcast light in almost every shot, a muted and monotonous palette, and repeated compositions. The 'figures in cloaks walking away down a path' shot appears 3-4 times (frames 1, 6, 12, and partly 8). Faces in the crowds (frames 7, 10, 11) are generic and repetitive. It reads as a generic 'AI oil painting' and has less emotional and dramatic range. On atmosphere and ability to carry a story, Image 1 is stronger. On technical consistency that can actually be checked, Image 2 is stronger.

### Operador de canales faceless con IA: PIERDE/NO APRUEBA

The script is not narration: the local LLM failed in almost every block, and the video strings dossier facts together literally, with repetitions (5 times 'botou abaixo moitas fortalezas', 'os señores regresaron' twice in a row) and a hook with no referent. Action: switch pipeline.py/llm.py to the API backend already decided (a strong LLM) for the gancho, resumo and paragraphs, keeping veracidade/LanguageTool as a safety net. Add a blocking coherence gate: no repeated n-grams of 4 or more words, every referent introduced before use, strict chronological order. Regenerate the video at a length that makes sense for sleep (at least 10-15 min as a sample).

Errores factuales: The script says 'douscentas catro testemuñas' in the Tabera-Fonseca case. The Concello de Santiago's Rocha Forte project site gives declarations from 183 people. Sources disagree, so the dossier should flag the conflict or leave the figure out. | qa.md declares 13/13 gates passed and PUBLICABLE, even though the LLM text was rejected in almost every block. The verdict hides that the script is literal fallback text.

Checked on the real MP4 (/home/user/revolta/plan-de-negocio/gauntlet2/video/ejemplo.mp4). It decodes completely, and no ffmpeg or python process is writing to it. It runs 3:11 at 1080p24, with AAC 48k and a gl mov_text subtitle track. Loudness is -17.2 LUFS with LRA 7.9, matching qa.md. The QA reports A/V offset 0.01 s, WER 0.037 on the mix and 99.7 % subtitle alignment. Scene detection at 0.3 finds no hard cuts, so the transitions are soft.

Images and sound pass the bar. The 25-frame contact sheet shows a coherent painterly style with no obvious deformed hands, faces or text. The Nós voice also works.

The script does not pass. qa.md shows that almost every block written by the local LLM (EuroLLM-9B) was rejected. The resumo was omitted, and about 17 of 18 paragraphs fell back to literal or mixed dossier text. So what you hear is a chain of dossier facts read one after another, not a story. Concrete faults a listener would notice:
- The hook 'Dicían que eran refuxios de malfeitores' has no subject or referent.
- There is no curiosity or 'picante' in the first 60-120 s, so the promoter's request is not met.
- 'botou abaixo moitas fortalezas' is repeated about 5 times, twice in the same sentence ('Botáronse abaixo moitas fortalezas por mandato dunha irmandade que... botou abaixo moitas fortalezas').
- The chronology jumps: fortresses are torn down before the irmandade is even introduced.
- 'Os veciños da cidade' appears without naming the city, and the Rocha Forte is introduced without explaining what it is.
- 'houbo unha reacción armada dos señores, que regresaron. Os señores regresaron...' repeats itself back to back.

Further issues:
- A 3-minute piece is far from the long running time of the reference and of the sleep format.
- The pipeline is genuinely automatic in one command, with caches and gates. But it still uses the local LLM for the script, against the promoter's 30-09 decision to write it with an LLM via API.
- The 13/13 PUBLICABLE gates measure truthfulness and language, not narrative coherence or repetition, so they approve something a viewer would find odd.

Web check: the Tabera-Fonseca case (1526-27) and the Rocha Forte are confirmed by the Concello de Santiago's Rocha Forte project site (https://rochaforte.santiagodecompostela.gal/relatos/timeline/preito-tavera-fonseca/?lang=es) and by Galipedia (https://gl.wikipedia.org/wiki/Gran_Guerra_Irmandi%C3%B1a).
