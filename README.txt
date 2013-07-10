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
 |-img:
 |  |-AMPE.ico                  Icono de la aplicación
 |  |-AMPE.png                  Imágen PNG del Icono.
 |  |-logo.png                  Logo.
 |-logs:                        Carpeta para Logs de conversiones.
 |-AMPE.exe                     Ejecutable de Windows.
 |-AMPE                         Ejecutable de Linux.
 |-README.txt                   Archivo Readme(este archivo)
 |-src:
 |  |-AMPE.py                   Codigo fuente del proyecto(en Python)
                                (Para ejecutarlo desde consola se necesita Python,
                                wxPython y para correr en Windows es necesario el
                                módulo win32api de Python para Windows)

=============================

No necesita instalación, esta pensado en ser usable en todos los sistemas
Windows y *nix aún sin Python y/o wxWidgets, y asi sea fácil de ejecutar.

=============================

Para ejecutarlo desde el código fuente(.py) es necesario tener instalado:
 - Python 2.7 
   http://www.python.org/ftp/python/2.7.5/python-2.7.5.msi
 - wxPython 2.8 o superior
   http://downloads.sourceforge.net/wxpython/wxPython2.8-win32-unicode-2.8.12.1-py27.exe
 - En el caso de Windows se necesita win32api para python
   http://sourceforge.net/projects/pywin32/files/pywin32/Build%20218/pywin32-218.win32-py2.7.exe/download
 
Se debe copiar AMPE.py a la carpeta raiz y ejecutar con Python desde ahí.

=============================

Cualquier cambio, mejora o sugerencia serán bienvenidas en
https://github.com/Al-eXs/AMPE/issues

=============================

Changelog:

Versión 1.0.0:
 - Versión Inicial.
 
Versión 1.0.1:
 - Corregido fallo de items repetidos en la lista.
 - Opción de eliminar items de la lista.

Versión 1.0.2:
 - Cambio en el encodeo de MP4 de bitrate a CRF.
 - Opción para cambiar el bitrate del audio de salida.

Versión 1.0.3:
 - Determinar SO y hacer el comando para encodeo.
 - Creación de logs por cada elemento encodeado.

Versión 1.0.4:
 - Mas opciones para la resolución de salida.
 - Cola de encodeo para todos los items de la lista.
 - Cancelado correcto del proceso de encodeo.
 
Versión 1.0.5:
 - Nuevo cuadro de diálogo con la información de progreso.
 - Se oculta la ventana principal.
 
Versión 1.0.6:
 - Al cancelar se puede regresar a la ventana principal a modificar opciones encodear la misma lista.
 
Versión 1.0.7:
 - Modificado el médo de obtencióe datos para las barras de progreso.
 
Versión 1.0.8:
 - Añadido encodeo a 2 pasadas en AVI.
 - Modificado la visualización de las barras de progreso.
 
Versión 1.0.9:
 - Añadido Drag 'n Drop(Windows)
 - Corregido error en las barras de progreso.
 - Corregido error con resoluciones no estandar.
 - Se recomprime y resamplea el Audio a 2 canales @ 44.1kHz para mejor compatibilidad
   basado en el orden FL-FR-C-LFE-RL-RR, funciona bien en 2.0, 2.1, 3.0, 3.1, 5.0, 5.1, 7.0, 7.1

Versión 1.0.10:
 - De vuelta a mostrar la consola por incompatibilidades.
 - Cambio en el Combo de selección de Resolución.
 - Fix para nombres unicode en Windows, acentos y kanjis ya no dan problemas.
   
   
   
Mejoras en proceso:
 -Configuración ividual de los archivos.
 -Drag 'n Drop en Linux.
 -Imágenes en los menús en Windows.
 -Archivo de lenguaje, para traducciones posteriores.
 -Bugfix que resulten.

