import {makePostRequest, tratamentosDeErro, makeLogin} from './api-utils.js';
import {showAlert} from "./site-utils.js";
const registerAccountRoute = "/accounts/";
const loginAccountRoute = "/accounts/login";
const pageLogin = "/login";
const continuarCadastro = "/cadastrar/informacoes";
const idAlertPlaceHolder = "liveAlertPlaceholder";

document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('registrationForm');
    const password = document.getElementById('password');
    const confirmPassword = document.getElementById('confirmPassword');
    const email = document.getElementById('email');

    form.addEventListener('submit', async function (event) {
        event.preventDefault();

        if (password.value !== confirmPassword.value) {
            confirmPassword.setCustomValidity('As senhas não coincidem.');
        } else {
            confirmPassword.setCustomValidity('');
        }

        if (!form.checkValidity()) {
            event.stopPropagation();
            form.classList.add('was-validated');
            return; 
        }

        const formData = {
            email: email.value,
            password: password.value
        };

        const responseCaseOk = (response) => {
            console.log("OK");
            console.log(response);
        }
        const responseCaseError = (response) => {
            tratamentosDeErro.accounts.register.tratarErroDeEmail(response, (message) => {showAlert(message, 'danger', idAlertPlaceHolder)})
        }
        const responseCaseErrorCatch = () => {
            console.log("catdh");
        }

        await makePostRequest(registerAccountRoute, {}, formData, responseCaseOk, responseCaseError, responseCaseErrorCatch)
    });
});
