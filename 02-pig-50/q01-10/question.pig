-- 
-- Pregunta
-- ===========================================================================
-- 
-- Para el archivo `data.tsv` compute la cantidad de registros por letra. 
-- Escriba el resultado a la carpeta `output` del directorio actual.
--
fs -rm -f -r output;
--
-- >>> Escriba su respuesta a partir de este punto <<<
--

u = LOAD 'data.tsv' USING PigStorage('\t') 
    AS (letter:CHARARRAY, 
        date:CHARARRAY, 
        value:INT);

t0 = GROUP u BY letter;
t1 = FOREACH t0 GENERATE group as letter, COUNT(u) AS c;
t2 = FOREACH t1 GENERATE letter, c;

STORE t2 INTO 'output' USING PigStorage('\t');