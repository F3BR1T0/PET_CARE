import {userIsAuthenticated, makeGetRequest, makePostRequest, setAuthorizationTokenHeader, tratamentosDeErro} from './api-utils.js';
import {redirectTo, showAlert} from './site-utils.js';
import {validarCampoCEP, validarCampoCPF, validarCampoTelefone} from './form-utils.js';
import {removeCarecteresNaoNumericos} from './validations.js';
import {ROUTES_API, ROUTES_SITE} from './global.js';

userIsAuthenticated();

document.addEventListener("DOMContentLoaded", () => {

    const form = document.getElementById("registrationForm");
    const name = document.getElementById("nome");
    const cpf = document.getElementById("cpf");
    const phone = document.getElementById("telefone");
    const cep = document.getElementById("cep");
    const estado = document.getElementById("estado");
    const cidade = document.getElementById("cidade");
    const alertplanceholder = "liveAlertPlaceholder";
    const pais = "Brasil";

    preenchimentoAutomaticoEstadoCidade();
    validarCampoCPF(cpf);
    validarCampoTelefone(phone);
    validarCampoCEP(cep);

    form.addEventListener("submit", async function (event) {
        event.preventDefault();  

        if (!form.checkValidity()) {
            event.stopPropagation();
            form.classList.add("was-validated");
            return;
        }

        const formData = constructFormData();

        const responseCaseOK = async(response) => {
            redirectTo(ROUTES_SITE.cadastrado_com_sucesso);
        }
        const responseCaseError = async(response) => {
            tratamentosDeErro.owner.register.already_registered(response,(message) => {showAlert(message,"danger",alertplanceholder)})
        }
        await makePostRequest(ROUTES_API.register_owner, setAuthorizationTokenHeader(), formData, responseCaseOK, responseCaseError);
    });

    function preenchimentoAutomaticoEstadoCidade(){
        cep.addEventListener("blur", async() => {
            const value = cep.value.replace(/\D/g, "");
    
            if(value.length === 8){
                const url = `https://viacep.com.br/ws/${value}/json/`;
    
                const responseCaseOK = async(response) => {
                    const data = await response.json();
                    if (data.erro){
                        console.log("cep não encontrado.");
                    }
                    estado.value = data.uf || "";
                    cidade.value = data.localidade || "";
                }
                const responseCaseError = (resonse) => {
                    console.log("Erro ao buscar cep");
                }
    
                await makeGetRequest(url, {},responseCaseOK, responseCaseError)
            }
        })
    }
    function constructFormData(){
        return {
            address: {
                city: cidade.value,
                state: estado.value,
                country: pais,
                cep: removeCarecteresNaoNumericos(cep.value)
            },
            name: name.value,
            cpf: removeCarecteresNaoNumericos(cpf.value),
            phone: removeCarecteresNaoNumericos(phone.value)
        }
    }
});
