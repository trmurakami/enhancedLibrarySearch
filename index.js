let speechText;
let predictOutput;
let theButton;
let vocab;
let vocabPath = 'Tokenizer/tokenizer_dictionary_old.json';
let tokenizer;
let model;
let modelPath = 'Model_js/model.json';

// For some reason the L2 regularization in tf does not 
// connect to the L2 regularizer in tfjs
class L2 {
    static className = 'L2';
    constructor(config) {
       return tf.regularizers.l2(config)
    }
}
tf.serialization.registerClass(L2);

// load the tokenizer from json
async function loadTokenizer() {
    let tknzr = fetch(vocabPath).then(response => {
        return response.json();
    })
    return tknzr;
  }

// Load the model from json
async function loadModel() {
    const model = tf.loadLayersModel(modelPath);
    return model;
  }


// tokenize function to convert input text to list of tokenized segments
function tokenize(text) {
    text = text.toLowerCase();
    var split_text = text.split(' ');
    var tokens = [];
    split_text.forEach(element => {
        if (tokenizer[element] != undefined) {
            tokens.push(tokenizer[element]);
          }
    });
    // create a list of slices of the list of tokens
    let i = 0;
    tokenized_text_segments = [];
    while (i+100 < Math.max(tokens.length, 256)) {
        var new_slice = tokens.slice(i,i+256);
        while (new_slice.length < 256) {
            new_slice.push(0);
          }
        tokenized_text_segments.push(new_slice);
        i = i + 50;
    }
    return tokenized_text_segments;
  }

async function predictParty() {
    const prob = tf.tidy(() => {
        speechText = document.getElementById('userInput').value;
        var x = tokenize(speechText)
        x = model.predict(tf.tensor2d(x, [x.length, 256]));

        x.mean(0).print();
        console.log(x);
        x = x.arraySync();
        console.log(x);
        // x = tf.mean(x);
        //x = x.arraySync();
        return x
    })
    const classNames = ['SDG01', 'SDG02', 'SDG03', 'SDG04', 'SDG05', 'SDG06', 'SDG07', 'SDG08', 'SDG09', 'SDG10', 'SDG11', 'SDG12', 'SDG13', 'SDG14', 'SDG15', 'SDG16'];

    function getMostProbableClass(probabilities) {
        const maxProbability = Math.max(...probabilities);
        const predictedClass = probabilities.indexOf(maxProbability);
        return predictedClass;
      }

// Função para encontrar as K classes mais prováveis
function getTopKClasses(probabilities, k) {
    const topK = probabilities
      .map((probability, index) => ({ probability, index }))
      .sort((a, b) => b.probability - a.probability)
      .slice(0, k);
    return topK.map((item) => item.index);
  }
  


// Mostrar os resultados no HTML
const table = document.getElementById('predictions-table');

for (let i = 0; i < prob.length; i++) {
  const exampleProbabilities = prob[i];
  const mostProbableClass = getMostProbableClass(exampleProbabilities);
  const top3Classes = getTopKClasses(exampleProbabilities, 3);

  const row = table.insertRow();
  const exampleCell = row.insertCell(0);
  const mostProbableCell = row.insertCell(1);
  const probabilityCell = row.insertCell(2);
  const top3Cell = row.insertCell(3);

  exampleCell.innerHTML = `${i + 1}`;
  mostProbableCell.innerHTML = '<img src="images/'+classNames[mostProbableClass]+'.png" width="80" height="80" alt="'+classNames[mostProbableClass]+'" />';
  probabilityCell.innerHTML = exampleProbabilities[mostProbableClass].toFixed(4);
  top3Cell.innerHTML = top3Classes.map((classIndex) => `${classNames[classIndex]} (${exampleProbabilities[classIndex].toFixed(4)})`).join(', ');
}


}


function predictSpeech() {
    predictParty().then((x) => {predictOutput.innerHTML = x;});
}


// function addSample() {
//     if (sampleSelction.value = 'NHS1'){
//         document.getElementById('userInput').value = 'The NHS has been ruined by this government. Years of Tory austerity has brought the NHS to its knees.';
//     } else if (samplesSelection.value = "rivers"){
//         document.getElementById('userInput').value = "For reasons which they could not comprehend, and in pursuance of a decision by default, on which they were never consulted, they found themselves made strangers in their own country. They found their wives unable to obtain hospital beds in childbirth, their children unable to obtain school places, their homes and neighbourhoods changed beyond recognition, their plans and prospects for the future defeated; at work they found that employers hesitated to apply to the immigrant worker the standards of discipline and competence required of the native-born worker; they began to hear, as time went by, more and more voices which told them that they were now the unwanted. On top of this, they now learn that a one-way privilege is to be established by Act of Parliament; a law which cannot, and is not intended to, operate to protect them or redress their grievances, is to be enacted to give the stranger, the disgruntled and the agent provocateur the power to pillory them for their private actions."
//     }
// }



async function init() {
    sampleSelction = document.getElementById('samples');

    predictOutput = document.getElementById('result');
    
    theButton = document.getElementById("predict-btn");

    theButton.innerHTML = `Loading...`;

    tokenizer = await loadTokenizer();

    theButton.innerHTML = `Loading......`;

    model = await loadModel();

    theButton.disabled = false;
    theButton.addEventListener("click", predictSpeech);
    
    theButton.innerHTML = `Predict! (This may take a moment...)`;
}

init();