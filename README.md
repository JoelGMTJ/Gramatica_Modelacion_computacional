# Evidencia Generación y Limpieza de Gramática
Joel Guadalupe García Guzmán - A01713785

## Descripción
El lenguaje que yo escogí es el Chino simplificado. Escogeré este lenguaje pues lo vimos en la preparatoria y tengo un libro (Jiameng, 2004) llamado Hànyǔ el cual contiene muchas gramáticas, las cuales voy a usar para generar mi árbol de gramática

## Estructura del lenguaje
La gramática del chino simplificado se basa en la estructura sujeto-verbo-objeto, también voy a modelar la estructura de preguntas abiertas y las preguntas de si/no.
Algunas características del lenguaje es que los verbos no se conjugan en diferentes tiempos, sino que puedes agregar algunas partículas para denotar que una acción se está realizando en el presente, en el pasado o en el futuro, pero el verbo se mantiene igual.

También mencionar que para poder modelar el sistema y que no cause problemas con ninguna herramienta que pueda usar, voy a representar los caractéres con su escritura en 'pinyin', que es 
"El sistema de transcripción fonética del chino mandarín mediante el alfabeto latino" (Jiameng, 2004).
Este sistema usa acentos (ō, ó, ǒ, ò) para denotar la pronunciación y los diferentes tonos de las palabras, sin embargo, van a ser omitidos por la misma razón que pueden causar problemas con las diversas herramientas que pueda usar.

## Palabras que useré
Las palabras que usaré son las siguientes:

### Sujetos 
* `wo:` Yo
* `ta:` El/ella
* `men:` *Partícula que si la agregas a algún sujeto lo vuelves plural, por ejemplo 'women' se vuelve nosotros y 'tamen' se vuelve ellos/ellas*

### Extras
* `he:` Y (and)
* `haishi:` O (or)
* `bu:` No
* `ma:` *Partícula que vuelve una oración en pregunta*

### Pronombres interrogativos
* `shenme:` ¿Qué?
* `nali:` ¿Dónde?
* `zenme:` ¿Cómo?
* `weishenme:` ¿Por qué?

### Verbos
* `shi:` Ser
* `chi:` Comer
* `xue_xi:` Estudiar
* `hei:` Beber
* `kan:` Leer / Ver / Mirar
* `ting:` Escuchar
* `shuo:` Hablar / Decir
* `xie:` Escribir
* `qu:` Ir
* `lai:` Venir
* `zuo:` Hacer
* `mai:` Comprar
* `gong_zuo:` Trabajar

### Objetos
* `fan:` Comida / Arroz
* `hanpaopao:` Hamburguesa
* `bingqilin:` Helado
* `shui:` Agua
* `cha:` Té
* `kafei:` Café
* `pijiu:` Cerveza
* `shu:` Libro
* `quianbi:` Lápiz
* `dianying:` Película
* `yinyue:` Música
* `hanzi:` Caracteres chinos
* `moxiguwen:` Español
* `ingwen:` Inglés
* `dongxi:` Cosa / Objeto
* `mianbao:` Pan
* `pingguo:` Manzana
* `kaoshi:` Examen

## Estructuras de oraciones
Las principales estructuras que voy a usar para mi lenguaje son las siguientes:

### Oraciones simples
Una oración simple lleva el formato de:
`Sujeto + verbo + objeto`
Y una oración negativa lleva el siguiente formato:
`Sujeto + 'bu' + verbo + objeto`

### Oración interrogativa 
La estructura para una oración de interrogativa de si/no es la siguiente:
`Oración simple positiva + 'ma' + '?'`
Otra estructura es la de 'Qué prefieres' la cual es:
`Oración simple + 'haishi' + oración simple + '?'`
Mientras que para las preguntas abiertas se usa la siguiente estructura:
`Sujeto + verbo + Palabra interrogativa + '?'`



## Referencias
Jiameng, S. y Costa Vila, E. (2004). Hànyǔ 1: Chino para hispanohablantes. Libro de texto y cuaderno de ejercicios. Herder Editorial.