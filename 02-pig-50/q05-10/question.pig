-- 
-- Pregunta
-- ===========================================================================
-- 
-- Para el archivo `data.tsv` compute Calcule la cantidad de registros en que 
-- aparece cada letra minúscula en la columna 2.
-- 
-- Escriba el resultado a la carpeta `output` del directorio actual.
-- 
fs -rm -f -r output;
--
-- >>> Escriba su respuesta a partir de este punto <<<
--
u = LOAD 'data.tsv' USING PigStorage('\t') 
    AS (letter:CHARARRAY, 
        dic:BAG{t:(p:CHARARRAY)}, 
        par:MAP[]);
       
tb0 = FOREACH u GENERATE FLATTEN(dic);
tb1 = GROUP tb0 BY $0;
tb2 = FOREACH tb1 GENERATE $0, COUNT(tb0) AS c;

STORE tb2 INTO 'output' USING PigStorage('\t');

