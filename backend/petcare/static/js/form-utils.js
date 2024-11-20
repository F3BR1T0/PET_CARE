import {validarCEP,validarTelefone,validarCpF, validarSenha} from './validations.js';

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
export function validarCampoSenha(senha){
    senha.addEventListener("blur", () => {
        if(!validarSenha(senha.value)){
            senha.setCustomValidity("Senha invalida.")
            invalidClass(senha);
        }else{
            senha.setCustomValidity("")
            validClass(senha);
        }
    });
}
function invalidClass(input){
    input.classList.add('is-invalid');
    input.classList.remove('is-valid');
}
function validClass(input){
    input.classList.add("is-valid");
    input.classList.remove("is-invalid");
}