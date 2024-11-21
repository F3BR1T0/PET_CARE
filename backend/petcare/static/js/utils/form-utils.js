import {validarCEP,validarTelefone,validarCpF, validarSenha, validarTexto} from './validations.js';

export function validarCampoTexto(input, feedback_id){
    input.addEventListener("blur", () => {
        if(!validarTexto(input.value)){
            input.setCustomValidity("O campo esta vazio.");
            setValidationFeedback(feedback_id, input.validationMessage);
            invalidClass(input);
        }else{
            input.setCustomValidity("");
            setValidationFeedback(feedback_id, input.validationMessage);
            validClass(input);
        }
    })
}

export function validarCampo(input, feedback, validationMethod = (value) => {}){
    input.addEventListener("blur", () => {
        const validation = validationMethod(input.value);
        if(validation != ""){
            input.setCustomValidity(validation);
            setValidationFeedback(feedback, input.validationMessage);
            invalidClass(input);
        }else{
            input.setCustomValidity("");
            setValidationFeedback(feedback, input.validationMessage);
            validClass(input);
        }
    });
}

export function validarCampoSenha(input, feedback_id){
    input.addEventListener("blur", () => {
        const validation = validarSenha(input.value);
        if(validation != ""){
            input.setCustomValidity(validation);
            setValidationFeedback(feedback_id, input.validationMessage);
            invalidClass(senha);
        }else{
            senha.setCustomValidity("")
            validClass(senha);
        }
    });
}
export function validarCampoCPF(cpf){
    cpf.addEventListener("blur", () => {
        if (!validarCpF(cpf.value)){
            cpf.setCustomValidity("CPF Invalido.");
            invalidClass(cpf);
        }else{
            cpf.setCustomValidity("");
            validClass(cpf);
        }
    })
}
export function validarCampoTelefone(telefone){
    telefone.addEventListener("blur", () => {
        if(!validarTelefone(telefone.value)){
            telefone.setCustomValidity("Telefone invalido.");
            invalidClass(telefone);
        }else{
            telefone.setCustomValidity("");
            validClass(telefone)
        }
    })
}
export function validarCampoCEP(cep){
    cep.addEventListener("blur", () => {
        if(!validarCEP(cep.value)){
            cep.setCustomValidity("Cep invalido.")
            invalidClass(cep);
        }else{
            cep.setCustomValidity("");
            validClass(cep);
        }
    })
}
export function setValidationFeedback(feedback, message){
    feedback.innerText = message;
}
function invalidClass(input){
    input.classList.add('is-invalid');
    input.classList.remove('is-valid');
}
export function validClass(input){
    input.classList.add("is-valid");
    input.classList.remove("is-invalid");
}