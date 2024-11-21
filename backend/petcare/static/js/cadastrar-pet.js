import {userHasRegister, makeGetRequest, setAuthorizationTokenHeader} from "./utils/api-utils.js";
import {registrarPrototypes, validarCampo} from "./utils/form-utils.js";
import {validarTexto} from "./utils/validations.js";
import {ROUTES_API} from "./utils/global.js";

userHasRegister();

document.addEventListener("DOMContentLoaded", async function(){
    const form = document.getElementById("registrationForm");
    const nome = document.getElementById("nome");
    const nome_feedback = document.getElementById("invalid-feedback-nome");
    const raca = document.getElementById("raca");
    const raca_feedback = document.getElementById("invalid-feedback-raca");
    const especie = document.getElementById("especie");
    const idade = document.getElementById("idade");
    const genero = document.getElementById("genero");
    const peso = document.getElementById("peso");

    validarCampo(nome, nome_feedback, validarTexto);
    validarCampo(raca, raca_feedback, validarTexto);

    registrarPrototypes();

    form.validarFormulario(() => {
        console.log('Passou');  
    })

});