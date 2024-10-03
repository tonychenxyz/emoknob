html = '''<html><head><link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>&#x1F39B;&#xFE0F;</text></svg>">
<title>EmoKnob: Enhance Voice Cloning with Fine-Grained Emotion Control</title>

<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@100..900&display=swap" rel="stylesheet">
<link rel="stylesheet" type="text/css" href="styles.css"><script src="scripts.js"></script></head>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-THMQKT633M"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-THMQKT633M');
</script>

<body>'''

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


html += '<h1 class="page-title" style="font-size:40px"><span class="emo-knob-title">&#x1F39B;&#xFE0F; EmoKnob</span> Enhance Voice Cloning with Fine-Grained Emotion Control</h1>'
html += '<div class="author-section" style="text-align: center; margin-top: 20px; margin-bottom: 30px;">'
html += '<p class="authors" style="font-size: 25px; margin-bottom: 15px; text-align: center;"><a href="https://tonychen.xyz/" style="text-decoration: none; color: hsl(204, 86%, 53%) !important;">Haozhe Chen</a>, <a href="https://www.cs.columbia.edu/speech/people.cgi?p=run" style="text-decoration: none; color: hsl(204, 86%, 53%) !important;">Run Chen</a>, and <a href="https://www.cs.columbia.edu/~julia/" style="text-decoration: none; color: hsl(204, 86%, 53%) !important;">Julia Hirschberg</a></p>'
html += '<p style="font-size: 25px; margin-top: 10px; text-align: center;">Columbia University</p>'

html += '<div class="button-container" style="display: flex; justify-content: center; gap: 15px;">'
html += '<a href="https://arxiv.org/abs/2410.00316" class="button" style="background-color: #E0FEE4; color: black; padding: 10px 20px; text-decoration: none; border-radius: 5px; font-weight: bold;">Paper</a>'
html += '<a href="https://github.com/tonychenxyz/emoknob" class="button" style="background-color: #E0FEE4; color: black; padding: 10px 20px; text-decoration: none; border-radius: 5px; font-weight: bold;">GitHub</a>'
html += '<a href="https://huggingface.co/spaces/tonychenxyz/emo-knob" class="button" style="background-color: #E0FEE4; color: black; padding: 10px 20px; text-decoration: none; border-radius: 5px; font-weight: bold;">Demo</a>'
html += '</div>'
html += '</div>'

html += '<div style="text-align: center; margin: 0px 0;">'
html += "<video class='teasers' controls>"
html += '<source src="assets/emoknob-teaser-vid.webm" type="video/webm">'
html += 'Your browser does not support the video tag.'
html += '</video>'

html += "<img src='assets/emo-knob-teaser-1.svg' alt='EmoKnob Teaser' class='teasers'>"
html += '</div>'



html += '<h1 class="section-title">Abstract</h1>'

html += '<p class="section-desc">While recent advances in Text-to-Speech (TTS) technology produce natural and expressive speech, they lack the option for users to select emotion and control intensity. We propose EmoKnob, a framework that allows fine-grained emotion control in speech synthesis with few-shot demonstrative samples of arbitrary emotion. Our framework leverages the expressive speaker representation space made possible by recent advances in foundation voice cloning models. Based on the few-shot capability of our emotion control framework, we propose two methods to apply emotion control on emotions described by open-ended text, enabling an intuitive interface for controlling a diverse array of nuanced emotions. To facilitate a more systematic emotional speech synthesis field, we introduce a set of evaluation metrics designed to rigorously assess the faithfulness and recognizability of emotion control frameworks. Through objective and subjective evaluations, we show that our emotion control framework effectively embeds emotions into speech and surpasses emotion expressiveness of commercial TTS services.</p>'

html += '<h1 class="section-title">Method</h1>'

html += '<div style="text-align: center; margin: 20px 0;">'
html += '<img src="assets/method.svg" alt="EmoKnob Method" style="width: 70%; height: auto;">'
html += '</div>'

html += '<ol class="section-desc" style="list-style-type: decimal; padding-left: 40px;">'
html += '<li><strong>Emotion Direction Extraction:</strong> We extract an emotion direction vector from a few demonstrative emotional speech samples and their neutral counterparts.</li>'
html += '<li><strong>Apply Emotion Control:</strong> We apply the extracted emotion direction to a target speech with controllable strength, allowing fine-grained emotion adjustment.</li>'
html += '</li>'
html += '</ol>'

html += '<div style="text-align: center; margin: 20px 0;">'
html += '<img src="assets/open-ended-method-1.svg" alt="Retrieval-based Emotion Control" style="width: 70%; height: auto;">'
html += '</div>'

html += '<p class="section-desc">The capability to apply emotion control with few-shot samples allows us to develop systems that apply emotion control based on open-ended text descriptions. We developed two systems:</p>'

html += '<ol class="section-desc" style="list-style-type: decimal; padding-left: 40px; margin-top: -20px;">'
html += '<li><strong>Retrieval-based Emotion Control:</strong> This system retrieves the most similar emotion from a pre-defined set of samples based on the input text description and transcripts.</li>'
html += '<li><strong>Synthetic-data-based Emotion Control:</strong> This system uses emotional text to generate emotional speech with existing TTS models and transfer the emotion to emotion control.</li>'
html += '</ol>'




html += '<h1 class="section-title">Example Clips</h1>'
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

html += '<h1 class="section-title">Citation</h1>'
html += '<p class="section-desc">If you find this work useful, please consider citing our paper:</p>'
html += '<div class="citation-container" style="background-color: #f0f0f0; margin-left: 20%; margin-right: 20%; padding: 20px; border-radius: 10px;">'
html += '<pre class="citation" style="overflow-x: auto;">'
html += '@misc{chen2024emoknobenhancevoicecloning,\n'
html += '      title={EmoKnob: Enhance Voice Cloning with Fine-Grained Emotion Control},\n'
html += '      author={Haozhe Chen and Run Chen and Julia Hirschberg},\n'
html += '      year={2024},\n'
html += '      eprint={2410.00316},\n'
html += '      archivePrefix={arXiv},\n'
html += '      primaryClass={cs.CL},\n'
html += '      url={https://arxiv.org/abs/2410.00316},\n'
html += '}'
html += '</pre>'
html += '</div>'


html += '</body></html>'
with open('index.html', 'w') as f:
    f.write(html)







