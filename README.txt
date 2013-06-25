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
 |  |-AMPE.png                  Imágen PNG del Icono.
 |  |-icon.ico                  Icono de la aplicación.
 |  |-logo.png                  Logo.
 |-logs:                        Carpeta para Logs de conversiones.
 |-AMPE.exe                     Ejecutable de Windows.
 |-AMPE                         Ejecutable de Linux.
 |-README.txt                   Archivo Readme(este archivo)
 |-src:
 |  |-AMPE.py                   Codigo fuente del proyecto(en Python)
                                (Para ejecutarlo desde consola se necesita Python,
                                wxPython y para correr en Windows es necesario el
                                módulo win32api de Python for Windows)

=============================

No necesita instalación, esta pensado en ser usable en todos los sistemas
Windows y *nix aún sin Python, y asi sea fácil de ejecutar.

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
 
Versió.0.5:
 - Nuevo cuadro de diálogo con la información de progreso.
 - Se oculta la ventana principal.
 
Versió.0.6:
 - Al cancelar se puede regresar a la ventana principal a modificar opciones encodear la misma lista.
 
Versión 1.0.7:
 - Modificado el médo de obtencióe datos para las barras de progreso.
 
Versión 1.0.8:
 - Añadido encodeo a 2 pasadas en AVI.
 - Modificado la visualización de las barras de progreso.
 
Varsió.0.9:
 - Añadido Drag 'n Drop.
 - Corregido error en las barras de progreso.
 - Corregido error con resoluciones no estandar.
 - Se recomprime y resamplea el Audio a 2 canales @ 44.1kHz para mejor compatibilidad
   basado en el orden FL-FR-C-LFE-RL-RR, funciona bien en 2.0, 2.1, 3.0, 3.1, 5.0, 5.1, 7.0, 7.1

 
Mejoras en proceso:
 -Configuracióndividual de los archivos.
 -Drag 'n Drop en Linux.
 -Imánes en los menús en Windows.
 -Archivo de lenguaje, para traducciones posteriores.
 -Bugfix que resulten.

