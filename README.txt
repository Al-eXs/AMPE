AMPE - Al_eXs' MPlayer2 Encoder

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
 |  |    |-config               Configuración del MPlayer2(lo genera al ejecutarse por primera vez)
 |  |    |-subfont.ttf          Fuente por defecto
 |  |-mplayer2.exe              Ejecutable MPlayer2 para Windows
 |  |-mplayer2-lavc             Ejecutable MPlayer2 para *nix
 |-img:
 |  |-AMPE.ico                  Icono del ejecutable de Windows
 |  |-icon.ico                  Icono de la aplicación
 |  |-logo.png                  Logo
 |-logs:                        Carpeta para Logs de conversiones
 |-AMPE.exe                     Ejecutable para Windows
 |-AMPE                         Ejecutable para *nix
 |-Converter.exe                Ejecutable llamado por AMPE.exe para la conversion
 |-README.txt                   Archivo Readme(este archivo)
 |-src:
 |  |-AMPE.py                   Codigo fuente del proyecto(en Python)

=============================

No necesita instalación, esta pensado en ser usable en todos los sistemas
Windows y *nix aún sin Python, y asi sea fácil de ejecutar.

=============================

Changelog:

Versión 0.1.0:
 -Versión Inicial.

Mejoras en proceso:
 -Configuración individual de los archivos.
 -Encodeo a 2 pasadas.
 -Bugfix que resulten.

