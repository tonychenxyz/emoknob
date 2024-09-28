html = '''<html><head><link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@100..900&display=swap" rel="stylesheet">
<link rel="stylesheet" type="text/css" href="styles.css"><script src="scripts.js"></script></head><body>'''

neutral_file_selection = {
    'original': ['angry_0.0_1_neutraltext0_MSP', 'angry_0.0_1_neutraltext1_MSP', 'angry_0.0_1_neutraltext2_MSP', 'angry_0.0_1_neutraltext3_MSP'],


    'angry': ['angry_0.5_1_neutraltext0_MSP', 'angry_0.5_1_neutraltext1_MSP', 'angry_0.5_1_neutraltext2_MSP',0],
    'disgust': ['disgust_0.6_1_neutraltext0_MSP', 0, 'disgust_0.6_1_neutraltext2_MSP', 0],
    'happy': ['happy_0.4_1_neutraltext0_MSP', 'happy_0.4_1_neutraltext1_MSP', 'happy_0.4_1_neutraltext2_MSP', 0],
    'sad': [0, 'sad_0.5_5_neutraltext1_MSP', 'sad_0.5_5_neutraltext2_MSP', 'sad_0.5_5_neutraltext3_MSP'],
    'surprise': ['surprise_0.4_5_neutraltext0_MSP', 0, 'surprise_0.4_5_neutraltext3_MSP', 0],
    'contempt': [0, 'contempt_0.4_1_neutraltext1_MSP', 'contempt_0.4_1_neutraltext1_MSP', 0, 'contempt_0.4_1_neutraltext3_MSP'],

    'empathy': ['empathy_0.5_neutraltext0_complex', 0, 'empathy_0.5_neutraltext2_complex', 0],
    'charisma': ['charisma_0.4_neutraltext0_complex', 0, 'charisma_0.4_neutraltext2_complex', 0],
                 

    'romance': [0, 'romance_0.4_neutraltext1_synthetic', 'romance_0.4_neutraltext2_synthetic', 0],
    'desire': ['desire_0.5_neutraltext0_synthetic', 0, 'desire_0.5_neutraltext2_synthetic', 0],
    'sarcasm': ['sarcasm_0.5_neutraltext0_synthetic', 0, 0, 'sarcasm_0.5_neutraltext3_synthetic'],
    'envy': [0, 'envy_0.4_neutraltext1_synthetic',0,0, 'envy_0.4_neutraltext3_synthetic'],


    'curious, intrigued': ['curious, intrigued_0.4_neutraltext0_retrieval', 'curious, intrigued_0.5_neutraltext1_retrieval', 0, 0],
    'blaming': ['blaming_0.5_neutraltext0_retrieval', 0, 0,'blaming_0.4_neutraltext3_retrieval',],
    'grateful, appreciative, thankful, indebted, blessed': [0, 0, 'grateful, appreciative, thankful, indebted, blessed_0.5_neutraltext3_retrieval','grateful, appreciative, thankful, indebted, blessed_0.5_neutraltext3_retrieval'],               
    'desire and excitement': ['desire and excitement_0.6_neutraltext0_retrieval', 0, 0, 'desire and excitement_0.6_neutraltext3_retrieval']
}


html += '<h1 class="page-title">Audio Samples for <span class="emo-knob-title">🎛️ EmoKnob</span></h1>'

html += '<h1 class="section-title">Source Audio</h1>'
html += '<p class="section-desc" style="text-align:center">All of voice clone and voice clone enhaned with emotion control on this page are obtained from cloning this clip.</p>'

html += '<div class="source-audio-play"><span class="cursor-pointer"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" class="w-5 h-5"><path fill-rule="evenodd" d="M4.5 5.653c0-1.426 1.529-2.33 2.779-1.643l11.54 6.348c1.295.712 1.295 2.573 0 3.285L7.28 19.991c-1.25.687-2.779-.217-2.779-1.643V5.653z" clip-rule="evenodd"></path></svg></span>'
html += '</div>'
html += f'<audio src="audios/bria.mp3"></audio>'
html += '</div>'

html += '<h1 class="section-title">Emotion Enhancement (Simple Emotions)</h1>'

html += '<p class="section-desc">This section shows examples of enhancing an <b> emotional text </b> with fine-grained emotion control of the corresponding emotion on simple emotions. Number in parentheses is the <b> strength </b> of the emotion control. All emotion direction vectors are obtained with <b> single-shot </b> (one pair of emotional and neutral clip). </p>'

emotions_cap = ['Angry', 'Happy', 'Sad', 'Surprise', 'Contempt', 'Disgust']


for emotion_cap in emotions_cap:

    emotion = emotion_cap.lower()
    table = '''<div class="simple-emo-grid grid grid-rows-5 lg:grid-rows-5 gap-5" style="grid-template-columns: auto repeat(6, 1fr);">'''
    # Add column titles
    strengths = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]
    col_titles = ['Original <br> Clone'] + [f'{emotion_cap} <br> ({strength:.1f})' for strength in strengths[1:]]
    table += '<div class="col-span-1"></div>'  # empty cell for the top-left corner
    for title in col_titles:
        table += f'<div class="col-title p-2 rounded-lg bg-[#CFDFFF] font-bold text-center">{title}</div>'

    # Add row titles and cells
    row_titles = ['Sentence 1', 'Sentence 2', 'Sentence 3', 'Sentence 4']
    for sentence_idx, row_title in enumerate(row_titles):
        table += f'<div class="row-title p-2 rounded-lg bg-[#CFDFFF] font-bold text-center">{row_title}</div>'
        for display_beta_idx, beta in enumerate(strengths):
            table += f'<div class="cell p-2 rounded-lg flex flex-col space-y-2 bg-[#CFDFFF] items-center h-full" data-row="{row_title}" data-col="{display_beta_idx}">'
            table += '<div class="flex space-x-2 items-center justify-center">'
            table += '<span class="cursor-pointer"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" class="w-5 h-5"><path fill-rule="evenodd" d="M4.5 5.653c0-1.426 1.529-2.33 2.779-1.643l11.54 6.348c1.295.712 1.295 2.573 0 3.285L7.28 19.991c-1.25.687-2.779-.217-2.779-1.643V5.653z" clip-rule="evenodd"></path></svg></span>'
            table += '</div>'
            table += f'<audio src="audios/simple_emotion_emotext/{emotion}_{beta}_1_emotext{sentence_idx}_MSP.wav"></audio>'
            table += '</div>'

    table += '</div>'
    html += table






html += '<h1 class="section-title">Emotion Selection (Simple Emotions)</h1>'

html += '<p class="section-desc">This section shows examples of selecting emotions for a <b> neutral text </b> with simple emotions. While usual TTS frameworks speech emotions is entirely decided by text All emotion direction vectors are obtained with <b> single-shot </b> (One pairs of emotional and neutral clip). </p>'



table = '''<div class="simple-emo-grid grid grid-rows-3 lg:grid-rows-3 gap-5" style="grid-template-columns: repeat(7, 1fr);">'''

emotions_cap = ['Original', 'Happy', 'Sad', 'Surprise', 'Contempt', 'Disgust']

row_titles = ['Sentence 1', 'Sentence 2', 'Sentence 3', 'Sentence 4']
col_titles = ['Original', 'Happy', 'Sad', 'Surprise', 'Contempt', 'Disgust']

table = '''<div class="simple-emo-grid grid grid-rows-5 lg:grid-rows-5 gap-5" style="grid-template-columns: auto repeat(6, 1fr);">'''
table += '<div class="col-span-1"></div>'  # empty cell for the top-left corner

# Add column titles
for title in col_titles:
    table += f'<div class="col-title p-2 rounded-lg bg-[#CFDFFF] font-bold text-center">{title}</div>'

# Add row titles and cells
for row_idx, row_title in enumerate(row_titles):
    table += f'<div class="row-title p-2 rounded-lg bg-[#CFDFFF] font-bold text-center">{row_title}</div>'
    for col_idx, col_title in enumerate(col_titles):
        table += f'<div class="cell p-2 rounded-lg flex flex-col space-y-2 bg-[#CFDFFF] items-center h-full" data-row="{row_idx+1}" data-col="{col_idx+1}">'
        table += '<div class="flex space-x-2 items-center justify-center">'
        table += '<span class="cursor-pointer"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" class="w-5 h-5"><path fill-rule="evenodd" d="M4.5 5.653c0-1.426 1.529-2.33 2.779-1.643l11.54 6.348c1.295.712 1.295 2.573 0 3.285L7.28 19.991c-1.25.687-2.779-.217-2.779-1.643V5.653z" clip-rule="evenodd"></path></svg></span>'
        table += '</div>'
        table += f'<audio src="audios/neutral_audios/{emotions_cap[col_idx].lower()}_{row_idx}.wav"></audio>'
        table += '</div>'

table += '</div>'
html += table





html += '<h1 class="section-title">Emotion Enhancement (Complex Emotions)</h1>'

html += '<p class="section-desc">This section shows examples of enhancing an <b> emotional text </b> with fine-grained emotion control of the corresponding emotion on more complex emotions. Number in parentheses is the <b> strength </b> of the emotion control. All emotion direction vectors are obtained with <b> two-shot </b> (Two pairs of emotional and neutral clip). </p>'

emotions_cap = ['Empathy', 'Charisma']


for emotion_cap in emotions_cap:

    emotion = emotion_cap.lower()
    table = '''<div class="complex-emo-enhance grid grid-rows-5 lg:grid-rows-5 gap-5" style="grid-template-columns: auto repeat(7, 1fr);">'''
    # Add column titles
    strengths = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
    col_titles = ['Original <br> Clone'] + [f'{emotion_cap} <br> ({strength:.1f})' for strength in strengths[1:]]
    table += '<div class="col-span-1"></div>'  # empty cell for the top-left corner
    for title in col_titles:
        table += f'<div class="col-title p-2 rounded-lg bg-[#CFDFFF] font-bold text-center">{title}</div>'

    # Add row titles and cells
    row_titles = ['Sentence 1', 'Sentence 2', 'Sentence 3', 'Sentence 4']
    for sentence_idx, row_title in enumerate(row_titles):
        table += f'<div class="row-title p-2 rounded-lg bg-[#CFDFFF] font-bold text-center">{row_title}</div>'
        for display_beta_idx, beta in enumerate(strengths):
            table += f'<div class="cell p-2 rounded-lg flex flex-col space-y-2 bg-[#CFDFFF] items-center h-full" data-row="{row_title}" data-col="{display_beta_idx}">'
            table += '<div class="flex space-x-2 items-center justify-center">'
            table += '<span class="cursor-pointer"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" class="w-5 h-5"><path fill-rule="evenodd" d="M4.5 5.653c0-1.426 1.529-2.33 2.779-1.643l11.54 6.348c1.295.712 1.295 2.573 0 3.285L7.28 19.991c-1.25.687-2.779-.217-2.779-1.643V5.653z" clip-rule="evenodd"></path></svg></span>'
            table += '</div>'
            table += f'<audio src="audios/complex_emotion_emotext/{emotion}_{beta}_emotext{sentence_idx}.wav"></audio>'
            table += '</div>'

    table += '</div>'
    html += table


html += '<h1 class="section-title">Emotion Selection (Complex Emotions)</h1>'

html += '<p class="section-desc">This section shows examples of selecting emotions for a <b> neutral text </b> with complex emotions. While usual TTS frameworks speech emotions is entirely decided by text All emotion direction vectors are obtained with <b> two-shot </b> (Two pairs of emotional and neutral clip). </p>'

table = '''<div class="simple-emo-grid grid grid-rows-3 lg:grid-rows-3 gap-5" style="grid-template-columns: repeat(7, 1fr);">'''

emotions_cap = ['Original', 'Empathy', 'Charisma']

row_titles = ['Sentence 1', 'Sentence 2', 'Sentence 3', 'Sentence 4']
col_titles = ['Original', 'Empathy', 'Charisma']

table = '''<div class="complex-emo-selection grid grid-rows-5 lg:grid-rows-5 gap-5" style="grid-template-columns: auto repeat(3, 1fr);">'''
table += '<div class="col-span-1"></div>'  # empty cell for the top-left corner

# Add column titles
for title in col_titles:
    table += f'<div class="col-title p-2 rounded-lg bg-[#CFDFFF] font-bold text-center">{title}</div>'

# Add row titles and cells
for row_idx, row_title in enumerate(row_titles):
    table += f'<div class="row-title p-2 rounded-lg bg-[#CFDFFF] font-bold text-center">{row_title}</div>'
    for col_idx, col_title in enumerate(col_titles):
        table += f'<div class="cell p-2 rounded-lg flex flex-col space-y-2 bg-[#CFDFFF] items-center h-full" data-row="{row_idx+1}" data-col="{col_idx+1}">'
        table += '<div class="flex space-x-2 items-center justify-center">'
        table += '<span class="cursor-pointer"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" class="w-5 h-5"><path fill-rule="evenodd" d="M4.5 5.653c0-1.426 1.529-2.33 2.779-1.643l11.54 6.348c1.295.712 1.295 2.573 0 3.285L7.28 19.991c-1.25.687-2.779-.217-2.779-1.643V5.653z" clip-rule="evenodd"></path></svg></span>'
        table += '</div>'
        table += f'<audio src="audios/neutral_audios/{emotions_cap[col_idx].lower()}_{row_idx}.wav"></audio>'
        table += '</div>'

table += '</div>'
html += table

html += '<h1 class="section-title">Emotion Enhancement (Open-Ended Text Emotion Description)</h1>'

html += '<p class="section-desc">This section shows examples of enhancing an <b> emotional text </b> with fine-grained emotion control based on an <b>open-ended text description of the emotion</b> with our <b>synthetic data-based and retrieval-based method</b>. Previously, without avaibility of large datasets for these emotions, it is not possible to apply emotion controls for these emotions. Our open-ended text to emotion framework based on retrieval and synthetic data makes emotion control for these emotions possible. Number in parentheses is the <b> strength </b> of the emotion control. All emotion direction vectors are obtained with <b> five-shot </b> (Five pairs of emotional and neutral clip). </p>'

emotions_cap = ['Romance', 'Desire', 'Sarcasm', 'Envy', 'Curious, Intrigued', 'Blaming', 'Grateful, Appreciative, Thankful, Indebted, Blessed', 'Desire and Excitement']

for emotion_cap in emotions_cap:

    emotion = emotion_cap.lower()
    table = '''<div class="text-enhance-grid grid grid-rows-5 lg:grid-rows-5 gap-5" style="grid-template-columns: auto repeat(7, 1fr);">'''
    # Add column titles
    strengths = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
    col_titles = ['Original <br> Clone'] + [f'{emotion_cap} <br> ({strength:.1f})' for strength in strengths[1:]]
    table += '<div class="col-span-1"></div>'  # empty cell for the top-left corner
    for title in col_titles:
        table += f'<div class="col-title p-2 rounded-lg bg-[#CFDFFF] font-bold text-center">{title}</div>'

    # Add row titles and cells
    row_titles = ['Sentence 1', 'Sentence 2', 'Sentence 3', 'Sentence 4']
    for sentence_idx, row_title in enumerate(row_titles):
        table += f'<div class="row-title p-2 rounded-lg bg-[#CFDFFF] font-bold text-center">{row_title}</div>'
        for display_beta_idx, beta in enumerate(strengths):
            table += f'<div class="cell p-2 rounded-lg flex flex-col space-y-2 bg-[#CFDFFF] items-center h-full" data-row="{row_title}" data-col="{display_beta_idx}">'
            table += '<div class="flex space-x-2 items-center justify-center">'
            table += '<span class="cursor-pointer"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" class="w-5 h-5"><path fill-rule="evenodd" d="M4.5 5.653c0-1.426 1.529-2.33 2.779-1.643l11.54 6.348c1.295.712 1.295 2.573 0 3.285L7.28 19.991c-1.25.687-2.779-.217-2.779-1.643V5.653z" clip-rule="evenodd"></path></svg></span>'
            table += '</div>'
            table += f'<audio src="audios/text2emo_emotion_emotext/{emotion}_{beta}_emotext{sentence_idx}.wav"></audio>'
            table += '</div>'

    table += '</div>'
    html += table


html += '<h1 class="section-title">Emotion Selection (Open-Ended Text Emotion Description)</h1>'

html += '<p class="section-desc">This section shows examples of selecting emotions for a <b> neutral text </b> with open-ended text descriptions of emotions. While usual TTS frameworks speech emotions is entirely decided by text All emotion direction vectors are obtained with <b> five-shot </b> (Five pairs of emotional and neutral clip). </p>'

row_titles = ['Sentence 1', 'Sentence 2', 'Sentence 3', 'Sentence 4']
emotions_cap = ['Original'] + emotions_cap
col_titles = emotions_cap

table = '''<div class="text-emo-selection grid grid-rows-5 lg:grid-rows-5 gap-5" style="grid-template-columns: auto repeat(9, 1fr); margin">'''
table += '<div class="col-span-1"></div>'  # empty cell for the top-left corner

# Add column titles
for title in col_titles:
    table += f'<div class="col-title p-2 rounded-lg bg-[#CFDFFF] font-bold text-center">{title}</div>'

# Add row titles and cells
for row_idx, row_title in enumerate(row_titles):
    table += f'<div class="row-title p-2 rounded-lg bg-[#CFDFFF] font-bold text-center">{row_title}</div>'
    for col_idx, col_title in enumerate(col_titles):
        table += f'<div class="cell p-2 rounded-lg flex flex-col space-y-2 bg-[#CFDFFF] items-center h-full" data-row="{row_idx+1}" data-col="{col_idx+1}">'
        table += '<div class="flex space-x-2 items-center justify-center">'
        table += '<span class="cursor-pointer"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" class="w-5 h-5"><path fill-rule="evenodd" d="M4.5 5.653c0-1.426 1.529-2.33 2.779-1.643l11.54 6.348c1.295.712 1.295 2.573 0 3.285L7.28 19.991c-1.25.687-2.779-.217-2.779-1.643V5.653z" clip-rule="evenodd"></path></svg></span>'
        table += '</div>'
        table += f'<audio src="audios/neutral_audios/{emotions_cap[col_idx].lower()}_{row_idx}.wav"></audio>'
        table += '</div>'

table += '</div>'
html += table

html += '<h1 class="section-title">Application: Make a Non-Empathetic Speaker Empathetic</h1>'
html += '<p class="section-desc" >In this section, we show how we can use EmoKnob to make a non-empathetic speaker empathetic. Emotion direction is obtained with single-shot (one pair of empathetic and neutral clip).</p>'

# Define the titles for the columns
speaker_types = ['Original Speaker (Contains Vulgar Language)', 'Original Clone', 'Empathetic 1', 'Empathetic 2']
audio_paths = ['audios/rick/combined_rick.m4a', 'audios/rick/another_pure_rick_morty.wav', 'audios/rick/rick_0.4.wav', 'audios/rick/rick_0.5_morty.wav']
# Create the grid container
html += '<div class="complex-emo-selection grid grid-rows-2 gap-5" style="grid-template-columns: repeat(4, 1fr);">'

# Add column titles
for speaker in speaker_types:
    html += f'<div class="col-title p-2 rounded-lg bg-[#CFDFFF] font-bold text-center">{speaker}</div>'

# Add audio cells for each speaker type
for speaker_idx, speaker in enumerate(speaker_types):
    html += f'<div class="cell p-2 rounded-lg flex flex-col space-y-2 bg-[#CFDFFF] items-center h-full">'
    html += '<div class="flex space-x-2 items-center justify-center">'
    html += '<span class="cursor-pointer"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" class="w-5 h-5"><path fill-rule="evenodd" d="M4.5 5.653c0-1.426 1.529-2.33 2.779-1.643l11.54 6.348c1.295.712 1.295 2.573 0 3.285L7.28 19.991c-1.25.687-2.779-.217-2.779-1.643V5.653z" clip-rule="evenodd"></path></svg></span>'
    html += '</div>'
    html += f'<audio src="{audio_paths[speaker_idx]}"></audio>'
    html += '</div>'

html += '</div>'

html += '</body></html>'
with open('index.html', 'w') as f:
    f.write(html)







