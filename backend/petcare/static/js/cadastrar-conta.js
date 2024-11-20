import {makePostRequest, tratamentosDeErro, makeLogin} from './api-utils.js';
import {redirectTo, showAlert} from './site-utils.js';
import {ROUTES_API, ROUTES_SITE} from './global.js';
import {validarCampoSenha} from './form-utils.js';
const idAlertPlaceHolder = "liveAlertPlaceholder";

document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('registrationForm');
    const password = document.getElementById('password');
    const confirmPassword = document.getElementById('confirmPassword');
    const email = document.getElementById('email');

    validarCampoSenha(password);

    form.addEventListener('submit', async function (event) {
        event.preventDefault();

        if (!form.checkValidity()) {
            event.stopPropagation();
            form.classList.add('was-validated');
            return; 
        }

        const formData = {
            email: email.value,
            password: password.value
        };

        const responseCaseOk = async (response) => {
            await makeLogin(email.value, password.value);
            redirectTo(ROUTES_SITE.cadastrar_informacoes);
        }
        const responseCaseError = (response) => {
            tratamentosDeErro.accounts.register.tratarErroDeEmail(response, (message) => {showAlert(message, 'danger', idAlertPlaceHolder)})
        }

        await makePostRequest(ROUTES_API.register_account, {}, formData, responseCaseOk, responseCaseError)
    });
});
