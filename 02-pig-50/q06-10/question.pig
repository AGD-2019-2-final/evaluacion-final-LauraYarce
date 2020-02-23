-- 
-- Pregunta
-- ===========================================================================
-- 
-- Para el archivo `data.tsv` Calcule la cantidad de registros por clave de la 
-- columna 3. En otras palabras, cuántos registros hay que tengan la clave 
-- `aaa`?
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
       
tb0 = FOREACH u GENERATE FLATTEN(par);
tb1 = FOREACH tb0 GENERATE $0;
tb2 = GROUP tb1 BY $0;
tb3 = FOREACH tb2 GENERATE $0, COUNT(tb1) AS c;

STORE tb3 INTO 'output' USING PigStorage(',');