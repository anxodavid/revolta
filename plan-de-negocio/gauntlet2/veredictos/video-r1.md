# video · ronda 1

### Crítico visual ciego: PIERDE/NO APRUEBA

Image 2 relies on repetitive, faceless landscape B-roll with a uniform green haze, and at least 3 of its 12 frames catch a crossfade mid-dissolve and show double exposure. It lacks characters and dramatic scenes that could carry the story, while Image 1 shows clear historical scenes with people doing things.

I viewed both contact sheets. Image 1 is a low-resolution YouTube storyboard (160x90 upscaled), so it looks soft, yet it still holds up well as a history video. It shows varied baroque interiors (a gilded salon, a hall of mirrors, a banquet, a study, a chapel) and ends in formal gardens. The characters wear consistent period costume and each shot shows an action (reading a decree, a handshake, laying a table, a night arrest with torches). The golden palette stays coherent throughout, and at this resolution I see no obvious deformed faces or hands. Image 2 has a very consistent and evocative look (Atlantic mist, stone, moss, a desaturated green wash) and good individual frames (the old man by the fire, the hands with the mortar). Its narrative content is poor, though. About 8 of the 12 frames are landscapes or empty B-roll (hills, walls, villages, castle seen from far away), and the few people shown are hooded figures from behind with no faces. At least 3 frames (1:10, 2:30, 3:30) catch a crossfade mid-dissolve and show double exposure, with ghost figures overlaid on the castle and village. The green haze makes everything look alike, and the castle-and-road shot is repeated. Image 2 is more atmospheric and has fewer anatomical risks, but Image 1 does much more to carry a historical story with characters and scenes.

### Operador de canales faceless con IA: PIERDE/NO APRUEBA

The sample was not produced by an automatic, open-source pipeline. Script, correction and shot list (the LLM stages) were written by Claude Opus 5.5 in `manual` mode. The pipeline stopped (exit 3), the answers were placed in llm_cache/ by hand, and the pipeline was re-run to read them. No local LLM (Carballo/Carvalho via llama.cpp) has been run in the pipeline, so neither the script quality nor the CPU time of a truly unattended run has been measured.

Fix: rerun `pipeline.py temas/irmandinos-apertura.yaml --llm openai` in an empty working directory against a local Galician LLM (e.g. proxectonos/Llama-3.1-Carballo-Instr3 in Q4 on llama-server). Publish that MP4 and its qa.md with the real times, together with an ASR/LanguageTool comparison against the current script.

In the same run, add a gate that reviews each image automatically and regenerates with a new seed on failure. It could use an open vision-language model or a hand detector plus an anachronism checklist. It must catch cases like the current closing shot: four hands, one pair with no body, at 3:46-4:00, which the QA passed as PUBLICABLE. Across the 240 images of a 60-min episode, with no human review, that kind of defect will be frequent.

Errores factuales: qa.md and README.md say there is no human intervention between the topic YAML and the MP4 ('un solo comando, sin intervención humana'). In fact the three LLM stages were answered by an outside agent (Claude in manual mode) after the pipeline stopped with exit code 3, so it was not one unattended command. | The automatic verdict 'PUBLICABLE 9/9' covers up a visible visual defect: the closing shot (3:46-4:00) has four hands, one pair with no arm or body. The builder's notes only mention minor anachronisms. | qa.md says the 0:00-0:22 image shows a green hill (outeiro verde). It shows a steep rocky slope with cypress-like trees; this is minor.

I checked the real MP4, /home/user/revolta/plan-de-negocio/gauntlet2/video/ejemplo.mp4. It decodes fully with ffmpeg and no process is writing to it. It is 240.79 s long, 1920x1080 at 24 fps, with AAC stereo and a mov_text subtitle track tagged glg. The file is 36.6 MB. There are no dead silences: under the voice the rain sits at about -44 dBFS.

I ran my own ASR with word timestamps using the Nós Whisper turbo model on the final mix. In the full-file pass, some words appeared that are not in the script: 'as.', 'en Europa', 'dixo' and 'E' at the start of some sentences. Every one of them falls at the edge of a 30-second window. I re-transcribed those passages as short clips and the individual sentence WAVs, and they came out clean, so these are ASR artifacts and the audio is fine. Audio start matches the subtitle timings within about 0.1-0.3 s. Loudness is -20 LUFS with a true peak of -5 dBTP, which is right for sleep content.

The frames (the automatic contact sheet plus a grid of 40 frames I extracted, one every 6 s) are consistent in style: misty, green, 'period film'. They hold up at the level of the reference channel.

But the footage has visible defects the automatic QA does not detect. The closing shot, 3:46-4:00, shows four hands: the woman has two on the jar, and a second pair with no arm or body comes in from the right. The village at 1:15 looks modern, with glass windows, balconies and red tile roofs. The crowd at 1:10 carries pikes and crosses. The QA only measures brightness, contrast and similarity, so it gave 9/9 PUBLICABLE.

The subtitles split lines into orphan fragments of about 0.5-0.7 s ('moito tempo.', 'no chan.'). Every pause is the same fixed 1.4 s / 2.4 s, which makes the cadence mechanical.

The sample is also only 4 min long; the reference averages 33 min and the target is 60 min. Long-form behaviour is only extrapolated [S].

Is the pipeline really automatic? The code (pipeline.py, llm.py, README.md) confirms that the three LLM stages (script, correction, shot list) were written by Claude Opus 5.5 in 'manual' mode. In that mode the pipeline stops with exit code 3, writes the prompt to llm_pending/, and an outside agent writes the answer into llm_cache/. The pipeline was then re-run and read those answers from the cache. So the text of the video (its best-looking part) is not what the open-source pipeline would produce unattended. The local LLMs it names (Carballo, Carvalho) have never been tested here. That goes against D5 and the brief's 'best open source software' requirement, and it means the sample does not prove the pipeline 'dé el pego'.

The video is close to the reference's level, but I am not convinced by what matters: an unattended run with an open model, and a gate that catches malformed images.
