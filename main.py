from core.fujant import Fujant

fujant = Fujant()

while 1:
    audio = fujant.record_audio()
    fujant.respond(audio)