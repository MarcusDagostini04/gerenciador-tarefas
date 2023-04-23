-- cria a tabela tarefas
CREATE TABLE tarefas (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    descricao TEXT NOT NULL
);

-- lista de títulos e descrições fictícias
DO $$
DECLARE
    titulos TEXT[] := ARRAY[
        'Tarefa importante',
        'Tarefa urgente',
        'Tarefa rotineira',
        'Tarefa de baixa prioridade',
        'Tarefa em andamento',
        'Tarefa concluida',
        'Tarefa pendente',
        'Tarefa adiada',
        'Tarefa esquecida',
        'Tarefa revisada'
    ];
    descricoes TEXT[] := ARRAY[
        'Esta tarefa e muito importante e precisa ser feita o quanto antes',
        'Esta tarefa e urgente e deve ser resolvida imediatamente',
        'Esta tarefa e rotineira e deve ser realizada periodicamente',
        'Esta tarefa tem baixa prioridade e pode ser realizada depois de outras tarefas mais importantes',
        'Esta tarefa ja esta em andamento e precisa ser concluida',
        'Esta tarefa ja foi concluida com sucesso',
        'Esta tarefa este pendente e ainda nao comecou',
        'Esta tarefa foi adiada para uma data posterior',
        'Esta tarefa foi esquecida e precisa ser retomada',
        'Esta tarefa foi revisada e precisa de ajustes'
    ];
BEGIN
    -- loop para criar 10 registros
    FOR i IN 1..10 LOOP
        INSERT INTO tarefas (titulo, descricao)
        VALUES (titulos[i], descricoes[i]);
    END LOOP;
END $$;
