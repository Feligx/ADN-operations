Este README.txt le mostrará como hacer uso de este programa,y le explicará lo que hace cada función que lo conforma.


-----------EXPLICACIÓN RÁPIDA DEL PROGRAMA---------------------------------------------


	este programa funciona como herramienta para automatizar y facilitar los procesos que ocurren con el ADN a nivel biológico, más específicamente este realiza una simulación del proceso de transcripción y traducción del ADN.
	* En cuanto a la trancripción: esta consta de un proceso donde una fracción específica de ADN se transcribe a ARNm, en este proceso, las bases nitrogenadas interactúan para formar este ARNm. De esta forma, las bases nitrogenadas se transcriben de la siguiente forma:
		- La base A (adenina) es reemplazada o reescrita como U (uracilo)
		- La base T (tiamina) es reemplazada o reescrita como A
		- La base C (citosina) es reemplazada o reescrita como G
		- La base G (guanina) es reemplazada o reescrita como C
	De esta forma el fragmento de ADN es convertido en ARN y podrá ser usado para el proceso de traducción.

	*En cuanto a la traducción: consta de la formación de proteínas a partir de la concatenación de aminoácidos, que son codificados a partir de la los codones (trios de bases nitrogenadas) que codifican para un único aminoácido.

Este programa hace la simulación de estos procesos para facilitar la tarea de hacerlo de forma manual cuando se quiere comprender o simular el proceso para un fragmento o cadena específica de ADN.



----------DESCRIPCIÓN DE LAS FUNCIONES INTEGRADAS EN EL PROGRAMA--------------------------



*IMPORTANTE* LA DESCRIPCIÓN A CONTINUACIÓN SE HARÁ EN EL ORDEN DE CRACIÓN Y FUNCIONALIDAD DE LAS FUNCIONES

*** FUNCIONES DE ADNfuncs ***

-Uppercase_it(x):
	Esta función únicamente recibe un string y de igual forma, devuelve un string pero todo en mayúsculas si se encontraba en minúsculas.

	Se emplea para poder asegurar que toda cadena de ADN que se pase al sistema, se encuentre en Mayús para poder realizar los proceos indicados por cada función.


- TRANSCRIPTION(x):
	Esta función en términos generales, realiza el proceso de transcripción que fue descrito anteriormente, es decir, realiza los cambios de las bases nitrogenadas.

	más específicamente esta función hace uso primero si la cadena que recibe como x viene en minúsculas la pasa por Upercase_it para tenerla en mayús para poder trabajar. Luego se crea una variable ARN con un str vacío y una lista BasesN con las bases nitrogenadas. Todo con el fin de en un ciclo for, revisar caracter por caracter el str que se recibió al inicio y cambiar las "bases nitrogenadas" y almacenar este nuevo str en ARN y luego retornarla.
	En caso de que el str contenga caracteres diferentes a: A, T, C, G, se imprimirá que no esta recibiendo una cadena de ADN por lo que el proceso no se lleva a cabo el proceso.


- create_LOPA():
	
	*NOTA* esta función hace uso de un archivo de txt titulado "lopa.txt" que se encuentra en la carpeta "codones"

	Esta función hace uso de larchivo de txt para lectura, crea una listta vacía (LOPAtxt) y luego lee todas las líneas del archivo y se almacenan en (LOPA_), para usar la longitud del documento como cantidad de iterciones en el ciclo for, para que dentro de este ciclo se lean leídas cada una de las líneas por separado y añadidas a la lista que habíamos generado al inicio de la función. Finalmente, esta retorna la lista con cada una de las líneas como elemento de la lista.

	*Para el entendimiento de lopa.txt vaya a la sección de archivos.

- Aminoacids():
	
	*NOTA* 	Esta función hace uso de todos los archivos hallables en la carpeta "codones" menos 'codones_.txt' y 'lopa.txt'.

	Esta función hace uso de la función create_LOPA y de la lista que este genera, se almacena en la variable 'codons', y genera un diccionario vacío. Luego se aprovecha la longitud de la lista que se recibió de create_LOPA para la cantidad de iteraciones del for. Por dentro del ciclo, se busca en cada uno de los txt elementos de codons para con ello formar un diccionrio que tiene como llave un codon y como valor el aminoácido al que codifica. Finalmente se retorna el diccionario creado.

	* Para el entendimiento de los archivos empleados en la función vaya a la sección de archivos.

- Divideincodons():

	Esta función recibe un str (ADN o ARN) y si se trata aún de ADN lo pasa por TRANSCRIPTION y si esta en minúsculas por Uppercase_it, luego divide el str en tríos de caracteres que en este caso serían codones y los añade a una lista que es lo que retorna ('codon_list').

- Search4Amino(x):
	*Esta función hace uso de la totalidad de las funciones directa o indirectamente, por lo que se recomienda leer antes las demás funciones que hacen parte del programa.

	Esta función como indica su nombre, busca por codones de la cadena de ADN/ARN que recibió los aminoácidos para los que se pueden codificar y retornará una lista con la siguiente estuctura: [Met (Metionina) *Inicio*, nombre abreviado del aminoácido (nombre completo del mismo),..., STOP]

	*NOTA* es importante notar que el proceso de 'traducción' que se simula en esta función iniciará si y solo si hay un codon de inicio (Metionina *ver codones_.txt para más proundización*) y terminará (correctamente) únicamente cuando haya un codon de terminación (STOP *ver codones_.txt para más profundización*), y además solo se hara lectura a partir de donde se halle el codon de inicio.

*** FUNCIONES DE ADNlaternative ***
- Search4Codons():
	Esta función es similar a Search4Amino de ADNfuncs, la dierencia esta en que en ugar de buscar el aminoácido a partir de un codon, esta busca los codones a partir de un aminoácido.

- ADNtest():
	Esta función genera una cadena de ADN aleatoria, para que el usuario la transcriba en ARN, y la compara con la misma cadena pero transcrita por TRANSRIPTION de ADNfuncs y si son iguales retorna que la respuesta correcta y de lo contrario, retorna respuesta incorrecta.

*** FUNCIÓN DE main ***
- MainMenu():
	esta función actúa como menú principal, ofreciendo las opciones que se pueden realizar usando las funciones del programa, y una forma rápida de acceder a estas.


----------ARCHIVOS--------------------------------------------------------


	*lopa.txt: contiene los nombres de los demás archivos de txt en la carpeta para que se pueda acceder a ellos de forma más sencilla y autómata desde las funciones, ya que si se llegase a der un hipotético nuevo aminácido, se podría colocar su archivo de txt dentro del contenido de este y automáticamente, la próxima vez que se corra el programa se evaluará para este nuevo aminoácido también.

	*codones_.txt: contiene el listado de todos los aminoácidos y los codones que codifican a estos, este no tiene gran utilidad para este programa más que el entendimiento de el usuario que quiera saber sin acceder al programa que aminoácidos son codificados por determinados codones.

	*nombre_abrev_del_aminoácido.txt: (ej: ala.txt)
	estos archivos contienen cada uno:
		- 1era línea: nombre abreviado y largo del aminoácido.
		- líneas posteriores: codones que codifican para el aminoácido en cuestión.