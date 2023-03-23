import { TattooArtist } from "./tatuador.js";
import { Appointment } from "./appointment.js";

const tatuador = new TattooArtist("Felipe", "fernanda.jpg");
const appointments = [
  new Appointment("Lucas", new Date(2023, 3, 25), "Leão"),
  new Appointment("Mariana", new Date(2023, 3, 26), "Cerejeira"),
];

document.addEventListener("DOMContentLoaded", function () {
  exibirInformacoesTatuador();
  exibirProximosAgendamentos();
});

function exibirInformacoesTatuador() {
  const photoElement = document.getElementById("tatuador-photo");
  const nameElement = document.getElementById("tatuador-name");
  const sobreElement = document.getElementById("tatuador-sobre");
  const estilosElement = document.getElementById("tatuador-estilos");

  photoElement.src = tatuador.imagePath;
  nameElement.textContent = tatuador.name;
  sobreElement.textContent = "Especialista em tatuagens realistas.";
  estilosElement.textContent = "Estilos dominados: Realismo, Retratos";
}

function exibirProximosAgendamentos() {
  const appointmentsList = document.getElementById("proximos-agendamentos");
  appointmentsList.innerHTML = "";

  for (const appointment of appointments) {
    const listItem = document.createElement("li");
    listItem.textContent = `${formatDate(appointment.date)} - ${
      appointment.clientName
    }: ${appointment.tattooDescription}`;
    appointmentsList.appendChild(listItem);
  }
}
