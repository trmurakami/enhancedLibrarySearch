let model;

// Carrega o modelo
async function loadModel() {
  model = await tf.loadLayersModel('py/Model_js/model.json');
  console.log('Modelo carregado com sucesso!');
}

// Função para pré-processar o texto e adicionar padding
function preprocessText(text, maxSequenceLength) {
  // Implemente o pré-processamento necessário para o seu caso
  // Certifique-se de que todas as sequências tenham o mesmo tamanho
  // e que estejam na mesma escala usada durante o treinamento do modelo.

  // Exemplo simples (não adequado para todos os modelos):
  const words = text.trim().split(' ');
  const paddedWords = words.slice(0, maxSequenceLength).concat(new Array(maxSequenceLength - words.length).fill(''));
  return paddedWords.join(' ');
}

// Consulta o modelo com o texto inserido pelo usuário
async function predict() {
  const input = document.getElementById('text-input').value;
  const maxSequenceLength = 128; // Tamanho máximo das sequências usado durante o treinamento

  const preprocessedInput = preprocessText(input, maxSequenceLength);

  // Converte o texto pré-processado para um tensor 2D
  const tensorInput = tf.tensor2d([preprocessedInput.split(' ').map(Number)], [1, maxSequenceLength]);

  // Faz a previsão usando o modelo
  const predictions = await model.predict(tensorInput);
  const label = predictions.argMax(1).dataSync();
  const resultElement = document.getElementById('result');
  resultElement.innerText = `Previsão: ${label}`;

  tensorInput.dispose();
  predictions.dispose();
}

// Carrega o modelo ao carregar a página
loadModel();

