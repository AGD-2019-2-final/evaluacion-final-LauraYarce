-- Pregunta
-- ===========================================================================
-- 
-- Obtenga los cinco (5) valores más pequeños de la 3ra columna.
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
t0 = ORDER u BY value ASC;
t1 = FOREACH t0 GENERATE $2;
t2 = LIMIT t1 5;
STORE t2 INTO 'output' USING PigStorage('\t');