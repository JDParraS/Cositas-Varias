import time, threading
from playsound import playsound
import multiprocessing
import winsound
from pygame import mixer

mixer.init()
mixer.music.load('./alarma.mp3')
Relacion=3

def pintameloTodo(Actividad, PstAct ,focusTime,descTime):
    print('Estamos actualmente en: ',Actividad,'\n')
    try:
        print('\tDatos de focusTime:\n')
        print('\t\ttiempo transcurrido:', deSaH_M_S(focusTime.tTranscurrido_S))
        print('\t\ttiempo delta:', deSaH_M_S(focusTime.tDelta))
        print('\t\ttiempo de descanso:', deSaH_M_S(focusTime.tDesc))
        print('\t\ttiempo limite:', deSaH_M_S(focusTime.tLimite),'\n')

    except:
        print('\t\tno hay focusTime por ahora\n')
    try:
        print('\tDatos de descTime:\n')
        print('\t\ttiempo transcurrido:', deSaH_M_S(descTime.tTranscurrido_S))
        print('\t\ttiempo delta:', deSaH_M_S(descTime.tDelta))
        print('\t\ttiempo de descanso:', deSaH_M_S(descTime.tDesc))
        print('\t\ttiempo limite:', deSaH_M_S(descTime.tLimite))
    except:
        print('\t\tno hay descTime por ahora\n')

def deSaH_M_S(seg:float):
    
    if seg is None:
        return 'no hay'
    segAbs = abs(seg)
    m,s = divmod(segAbs,60)
    h,m = divmod(m,60)
    if seg <0:
        return f'-{h:02.0f}:{m:02.0f}:{s:02.0f} segundos : {seg}'
    else:
        return f'{h:02.0f}:{m:02.0f}:{s:02.0f} segundos : {seg}'


class chronos():
    tTranscurrido_S=float()
    tDelta = float()
    tDesc = float()
    t=time.time()
    even=threading.Event()
    thread= threading.Thread()
    thread2 = threading.Thread()
    tLimite=float()
    terminado = False
    AlComenzada= False
    limAl = 0

    def cronom (self):
        while True:
            self.tTranscurrido_S = time.time()-self.t
            if self.tLimite is not None:
                self.tDelta= self.tLimite-self.tTranscurrido_S
            elif self.tDelta is not None:
                self.tDesc = self.tTranscurrido_S/Relacion+self.tDelta
            else:
                self.tDesc = self.tTranscurrido_S/Relacion
            if self.terminado==True:
                break
            
            if self.AlComenzada==False and self.tLimite is not None and (0 < abs(self.tDelta) <= 1):
                self.thread2.start()
                time.sleep(0.1)
                self.limAl = 1            
            time.sleep(0.5)

    
    def alarma(self):
        self.AlComenzada=True
        while True:
            if self.limAl==0:
                mixer.music.play()
            if self.terminado == True:
                mixer.music.stop()
                break
            time.sleep(0.15)

        

        
    
    def __init__(self,tLimite=None):
        self.t = time.time() ###←←←← importante recordar esto, variables de clase vs variables de objeto, cosas similares dentro de los metodos alarmacronom (el ultimo ir:if self.AlComenzada==False and self.tLimite is not None and abs(self.tDelta) <= 1)
        self.tLimite = tLimite
        self.ProcesoAlarma= multiprocessing.Process(target=playsound,args=('C:/Users/julia/Downloads/NoTeContaronMal.mp3'))
        self.AlComenzada=False
        self.thread = threading.Thread(target=self.cronom, args=(),daemon=True)
        self.thread.start()
        self.thread2 = threading.Thread(target=self.alarma, args=(),daemon=True)
        
descTime = None
focusTime = None
PstAct = None
tTot = None

while True:
    Actividad=input('ACTIVIDAD: ')
    if tTot is None:
        tTot = time.time() 
    if Actividad == 'f' and PstAct != 'f':
        focusTime=chronos()
        if descTime is not None:
            focusTime.tDelta=descTime.tDelta
            descTime.terminado=True
        PstAct = Actividad
    elif Actividad == 'd' and PstAct != 'd':
        descTime = chronos()
        if focusTime is not None:
            descTime.tLimite=focusTime.tDesc
            focusTime.terminado=True
        else:
            descTime.tLimite=0
        PstAct = Actividad
    elif Actividad == 'i':
        Actividad = PstAct
    
    else:
        Actividad = PstAct
        print('\nIntroduce comando válido\n')
        continue
    
    print('TIEMPO TOTAL:',deSaH_M_S(time.time()-tTot),'\n')
    time.sleep(0.2)
    pintameloTodo(Actividad,PstAct,focusTime,descTime)
        

