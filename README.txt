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
 |  |    |-config               Configuración del MPlayer2
 |  |    |-subfont.ttf          Fuente por defecto
 |  |-mplayer2.exe              Ejecutable MPlayer2 para Windows
 |  |-mplayer2-lavc             Ejecutable MPlayer2 para Linux
 |  |-AMPE.exe                  Ejecutable del conversor
 |-img:
 |  |-AMPE.ico                  Icono del ejecutable de Windows
 |  |-icon.ico                  Icono de la aplicación
 |  |-logo.png                  Logo
 |-logs:                        Carpeta para Logs de conversiones
 |-AMPE.exe                     Ejecutable de Windows
 |-AMPE                         Ejecutable de Linux
 |-README.txt                   Archivo Readme(este archivo)
 |-src:
 |  |-AMPE.py                   Codigo fuente del proyecto(en Python)

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
 
Versión 1.0.5:
 - Nuevo cuadro de diálogo con la información de progreso.
 - Se oculta la ventana principal.
 
Versión 1.0.6:
 - Al cancelar se puede regresar a la ventana principal a modificar opciones encodear la misma lista.
 
Versión 1.0.7:
 - Modificado el método de obtención de datos para las barras de progreso.
 
Versión 1.0.8:
 - Añadido encodeo a 2 pasadas en AVI.
 - Modificado la visualización de las barras de progreso.
 
Varsión 1.0.9:
 - Añadido Drag 'n Drop.
 - Corregido error en las barras de progreso.
 - Corregido error con resoluciones no estandar.

 
Mejoras en proceso:
 -Configuración individual de los archivos.
 -Bugfix que resulten.

