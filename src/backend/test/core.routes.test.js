// test/routes.test.js
const request = require('supertest');
const app = require('../src/core/app'); // Certifique-se de que este é o caminho correto para o seu arquivo Express

describe('Testando as rotas dos documentos', () => {
  it('Deve criar um item com sucesso na rota POST /item', async () => {
    const body = {
        "nome": "teste",
        "link": "http://teste.com",
        "data_publicacao": "2024-09-16",
        "tipo": "Instruções",
        "tags": ["BDR"]
    };
    const response = await request("http://localhost:3000").post('/documents/webhook/save').send(body);
    
    // Verifica se o status code é 201 (Created)
    expect(response.statusCode).toBe(201);

    // Verifica a mensagem de sucesso
    expect(response.body).toHaveProperty('message', 'Document created successfully');

    // Verifica o objeto `data`
    expect(response.body).toHaveProperty('data');

    const { data } = response.body;

    // Verifica as propriedades do objeto `data`
    expect(data).toHaveProperty('id');
    expect(data).toHaveProperty('nome', 'teste');
    expect(data).toHaveProperty('link', 'http://teste.com');
    expect(data).toHaveProperty('data_publicacao', '2024-09-16T00:00:00.000Z');
    expect(data).toHaveProperty('id_tipo', 1);
    expect(data).toHaveProperty('id_orgao', 1);
    expect(data).toHaveProperty('criado_em');
    expect(data).toHaveProperty('atualizado_em');

    // Verifica se `id`, `id_tipo` e `id_orgao` são números
    expect(typeof data.id).toBe('number');
    expect(typeof data.id_tipo).toBe('number');
    expect(typeof data.id_orgao).toBe('number');

    // Verifica se as datas estão no formato correto
    expect(new Date(data.criado_em).toISOString()).toBe(data.criado_em);
    expect(new Date(data.atualizado_em).toISOString()).toBe(data.atualizado_em);
  });
});
