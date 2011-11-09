AMPE - Al_eXs' MPlayer2 Encoder
https://github.com/Al-eXs/AMPE

=============================

AMPE es una GUI(Graphic User Interface) para usar las opciones de encodeo
del MPlayer2(www.mplayer2.org) que son mas faciles de usar que los
ejecutables de cada formato como lo son el Xvid y el x264, ya que esos
no incluyen algunas opciones como el juntar los Ordered Chapters Externos o
Segment Linking de los MKV's, y tampoco tienen opciones de incrustar en
el video los subs en ass conservando los estilos y las fonts.

=============================

Contenido:

AMPE:
 |-bin:
 |  |-mplayer:
 |  |    |-config               Configuraci�n del MPlayer2(lo genera al ejecutarse por primera vez)
 |  |    |-subfont.ttf          Fuente por defecto
 |  |-mplayer2.exe              Ejecutable MPlayer2 para Windows
 |  |-mplayer2-lavc             Ejecutable MPlayer2 para Linux
 |-img:
 |  |-AMPE.ico                  Icono del ejecutable de Windows
 |  |-icon.ico                  Icono de la aplicaci�n
 |  |-logo.png                  Logo
 |-logs:                        Carpeta para Logs de conversiones
 |-AMPE.exe                     Ejecutable para Windows
 |-AMPE                         Ejecutable para Linux
 |-Converter.exe                Ejecutable usado por AMPE.exe para la conversion
 |-README.txt                   Archivo Readme(este archivo)
 |-src:
 |  |-AMPE.py                   Codigo fuente del proyecto(en Python)

=============================

No necesita instalaci�n, esta pensado en ser usable en todos los sistemas
Windows y *nix a�n sin Python, y asi sea f�cil de ejecutar.

=============================

Changelog:

Versi�n 0.1.0:
 -Versi�n Inicial.

Mejoras en proceso:
 -Configuraci�n individual de los archivos.
 -Encodeo a 2 pasadas.
 -Bugfix que resulten.

