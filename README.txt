AMPE - Al_eXs' MPlayer2/MPV Encoder

Repositorio GIT:
https://github.com/Al-eXs/AMPE

=============================

AMPE es una GUI(Graphic User Interface) para usar las opciones de encodeo
del MP2ayer2/MPV que son mas faciles de usar que los
ejecutables de cada formato como lo son el Xvid y el x264, ya que esos
no incluyen algunas opciones como el juntar los Ordered Chapters Externos o
Segment Linking de los MKV's, y tampoco tienen opciones de incrustar en
el video los subs en ass conservando los estilos y las fonts.

=============================

Contenido:

AMPE:
 |-bin:
 |  |-mpv2.exe                  Ejecutable MPV para Windows.
 |  |-mpv-lavc                  Ejecutable MPV para Linux.
 |  |-AMPE.exe                  Ejecutable del conversor.
 |-img:
 |  |-AMPE.ico                  Icono del ejecutable de Windows.
 |  |-AMPE.png                  Im�gen PNG del Icono.
 |  |-icon.ico                  Icono de la aplicaci�n.
 |  |-logo.png                  Logo.
 |-logs:                        Carpeta para Logs de conversiones.
 |-AMPE.exe                     Ejecutable de Windows.
 |-AMPE                         Ejecutable de Linux.
 |-README.txt                   Archivo Readme(este archivo)
 |-src:
 |  |-AMPE.py                   Codigo fuente del proyecto(en Python)
                                (Para ejecutarlo desde consola se necesita Python,
                                wxPython y para correr en Windows es necesario el
                                m�dulo win32api de Python for Windows)

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
 - Se recomprime y resamplea el Audio a 2 canales @ 44.1kHz para mejor compatibilidad
   basado en el orden FL-FR-C-LFE-RL-RR, funciona bien en 2.0, 2.1, 3.0, 3.1, 5.0, 5.1, 7.0, 7.1

 
Mejoras en proceso:
 -Configuraci�n individual de los archivos.
 -Drag 'n Drop en Linux.
 -Im�genes en los men�s en Windows.
 -Archivo de lenguaje, para traducciones posteriores.
 -Bugfix que resulten.

