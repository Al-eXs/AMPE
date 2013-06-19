AMPE - Al_eXs' MPlayer2 Encoder

Repositorio GIT:
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
 |  |    |-config               Configuraci�n del MPlayer2
 |  |    |-subfont.ttf          Fuente por defecto
 |  |-mplayer2.exe              Ejecutable MPlayer2 para Windows
 |  |-mplayer2-lavc             Ejecutable MPlayer2 para Linux
 |  |-AMPE.exe                  Ejecutable del conversor
 |-img:
 |  |-AMPE.ico                  Icono del ejecutable de Windows
 |  |-icon.ico                  Icono de la aplicaci�n
 |  |-logo.png                  Logo
 |-logs:                        Carpeta para Logs de conversiones
 |-AMPE.exe                     Ejecutable de Windows
 |-AMPE                         Ejecutable de Linux
 |-README.txt                   Archivo Readme(este archivo)
 |-src:
 |  |-AMPE.py                   Codigo fuente del proyecto(en Python)

=============================

No necesita instalaci�n, esta pensado en ser usable en todos los sistemas
Windows y *nix a�n sin Python, y asi sea f�cil de ejecutar.

=============================

Changelog:

Versi�n 1.0.0:
 - Versi�n Inicial.
 
Versi�n 1.0.1:
 - Corregido fallo de items repetidos en la lista.
 - Opci�n de eliminar items de la lista.

Versi�n 1.0.2:
 - Cambio en el encodeo de MP4 de bitrate a CRF.
 - Opci�n para cambiar el bitrate del audio de salida.

Versi�n 1.0.3:
 - Determinar SO y hacer el comando para encodeo.
 - Creaci�n de logs por cada elemento encodeado.

Versi�n 1.0.4:
 - Mas opciones para la resoluci�n de salida.
 - Cola de encodeo para todos los items de la lista.
 - Cancelado correcto del proceso de encodeo.
 
Versi�n 1.0.5:
 - Nuevo cuadro de di�logo con la informaci�n de progreso.
 - Se oculta la ventana principal.
 
Versi�n 1.0.6:
 - Al cancelar se puede regresar a la ventana principal a modificar opciones encodear la misma lista.
 
Versi�n 1.0.7:
 - Modificado el m�todo de obtenci�n de datos para las barras de progreso.
 
Versi�n 1.0.8:
 - A�adido encodeo a 2 pasadas en AVI.
 - Modificado la visualizaci�n de las barras de progreso.
 
Varsi�n 1.0.9:
 - A�adido Drag 'n Drop.
 - Corregido error en las barras de progreso.
 - Corregido error con resoluciones no estandar.

 
Mejoras en proceso:
 -Configuraci�n individual de los archivos.
 -Bugfix que resulten.

