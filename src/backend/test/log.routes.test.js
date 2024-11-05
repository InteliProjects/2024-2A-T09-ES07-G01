// test/routes.test.js
const request = require('supertest');
const app = require('../src/core/app'); // Certifique-se de que este é o caminho correto para o seu arquivo Express

describe('Testando as rotas dos documentos', () => {
  it('Deve criar um item com sucesso na rota POST /item', async () => {
    const body = {
        "tipo": "Acesso à página principal",
        "descricao": "Página XXXX acessada"
      }
    const response = await request("http://localhost:3000").post('/logs').send(body);
    
    // Verifica se o status code é 201 (Created)
    expect(response.statusCode).toBe(200);

    expect(response.body).toHaveProperty('id');
    expect(response.body).toHaveProperty('ip', '127.0.0.1');
    expect(response.body).toHaveProperty('descricao', 'Página XXXX acessada');
    expect(response.body).toHaveProperty('id_tipo', 1);
    expect(response.body).toHaveProperty('atualizado_em');
    expect(response.body).toHaveProperty('criado_em');

    // Verifica se os timestamps estão no formato ISO
    expect(new Date(response.body.atualizado_em).toISOString()).toBe(response.body.atualizado_em);
    expect(new Date(response.body.criado_em).toISOString()).toBe(response.body.criado_em);
  });
});
