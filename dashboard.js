import { TattooArtist } from "./tattooArtist.js";

const tatuador = new TattooArtist("Fernanda", "/profilePic/profile.jpeg");

document.getElementById("comment-form").addEventListener("submit", (event) => {
  event.preventDefault();
  const comment = document.getElementById("comment").value;
  const priceRange = document.getElementById("price-range").value;

  comentario_tatuador(tatuador, comment, priceRange);
});

document.getElementById("concordar").addEventListener("click", () => {
  concordar_com_alteracao(tatuador);
});

document.getElementById("sugerir-preco").addEventListener("click", () => {
  const novaFaixaPreco = prompt("Digite a nova faixa de preço:");
  sugerir_novo_preco(tatuador, novaFaixaPreco);
});

document
  .getElementById("resposta-agendamento")
  .addEventListener("click", () => {
    const resposta = prompt("Digite a resposta para o agendamento:");
    const dataSugerida = new Date(
      prompt("Digite a data sugerida (AAAA-MM-DD):")
    );
    resposta_agendamento(tatuador, resposta, dataSugerida);
  });

function comentario_tatuador(tatuador, comment, priceRange) {
  console.log(`Tatuador: ${tatuador.name}`);
  console.log(`Comentário: ${comment}`);
  console.log(`Faixa de preço: ${priceRange}`);
}

function exibir_conversa(conversa) {
  const conversaList = document.getElementById("conversa-list");
  conversaList.innerHTML = "";

  for (const mensagem of conversa) {
    const listItem = document.createElement("li");
    listItem.textContent = `${mensagem.sender}: ${mensagem.text}`;
    conversaList.appendChild(listItem);
  }
}

function concordar_com_alteracao(tatuador) {
  console.log(`Tatuador ${tatuador.name} concordou com a alteração.`);
}

function sugerir_novo_preco(tatuador, novaFaixaPreco) {
  console.log(
    `Tatuador ${tatuador.name} sugeriu uma nova faixa de preço: ${novaFaixaPreco}`
  );
}

function resposta_agendamento(tatuador, resposta, dataSugerida) {
  console.log(
    `Tatuador ${tatuador.name} respondeu ao agendamento: ${resposta}`
  );
  console.log(`Data sugerida: ${dataSugerida.toISOString().slice(0, 10)}`);
}

// Exemplo de uso da função exibir_conversa
const conversaExemplo = [
  { sender: "Cliente", text: "Olá, gostaria de fazer uma tatuagem de dragão." },
  { sender: "Tatuador", text: "Claro, podemos agendar para a próxima semana?" },
  { sender: "Cliente", text: "Sim, funciona para mim!" },
];

document.addEventListener("DOMContentLoaded", () => {
  exibir_conversa(conversaExemplo);
});
