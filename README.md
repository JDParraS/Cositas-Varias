# Focus_V1.Py
<p>Aplicación sencilla del método pomodoro que consiste en una alarma que cronometra el tiempo de trabajo, para luego temporizar el tiempo de descanso disponible.</p>
<p> <em><strong>Uso:</strong></em></p>
<ol>
    <li>
        Modificar el path de la linea 8 del script para indicar la ubicación de la alarma a utilizar.
    </li>
    <li>
        Si se desea modificar la razón de tiempo de trabajo : tiempo de descanso. Modificar la variable 'Relacion'. -Por default es 3, lo que quiere decir que por cada x tiempo de trabajo hay x/3 tiempo de descanso-
    </li>
    <li>
        Para correr el script correr <code>python Focus_V1.py</code> en el cmd
    </li>
    <li>
        Para indicar la actividad: 'f' para tiempo de trabajo, 'd' para tiempo de descanso, 'i' para mostrar tiempo disponible
    </li>
</ol>
<p>Ten en cuenta que el tiempo que se "deba" como descanso va a mostrarse como tiempo negativo en "tiempo delta", y va a restarse del tiemop disponible para descansar.</p>
