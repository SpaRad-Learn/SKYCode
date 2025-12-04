from gtts import gTTS
import os
from IPython.display import Audio
def text_to_speech():
    tts = gTTS(text="Jesus Mary Joseph", lang="en", slow=False)
    tts.save("output.mp3")
    return Audio("output.mp3", autoplay=True)   