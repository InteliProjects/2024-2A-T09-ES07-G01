const { create, list } = require('../services/internalService');

async function createLog(req, res) {
  const requiredFields = [
    'inicio_execucao',
    'fim_execucao',
    'retorno_documentos',
    'total_documentos_sucessos',
    'total_documentos_falhos',
    'retorno_emails',
    'total_emails_sucessos',
    'total_emails_falhos',
  ];

  const missingFields = requiredFields.filter((field) => !req.body[field]);
  if (missingFields.length > 0) {
    return res.status(400).json({
      message: `Campos obrigatórios não preenchidos: ${missingFields.join(
        ', '
      )}`,
    });
  }

  try {
    const log = await create(req.body);

    return res.status(201).json(log);
  } catch (error) {
    return res.status(500).json({ message: 'Erro ao criar o log.' });
  }
}

async function listLogs(req, res) {
  try {
    const logs = await list();

    return res.status(200).json(logs);
  } catch (error) {
    return res.status(400).json({ message: error.message });
  }
}

module.exports = {
  createLog,
  listLogs,
};
