export function validarCEP(value){
    value = removeCarecteresNaoNumericos(value);

    if (value.length !== 8) {
        return false;
    }
    return true;
}
export function validarCpF(value){
    value = removeCarecteresNaoNumericos(value);

    if (value.length !== 11 || /^(\d)\1+$/.test(value)) {
        return false;
    }

    let soma = 0;
    for (let i = 0; i < 9; i++) {
        soma += parseInt(value[i]) * (10 - i);
    }
    let primeiroDigito = 11 - (soma % 11);
    primeiroDigito = primeiroDigito >= 10 ? 0 : primeiroDigito;

    if (parseInt(value[9]) !== primeiroDigito) {
        return false;
    }

    soma = 0;
    for (let i = 0; i < 10; i++) {
        soma += parseInt(value[i]) * (11 - i);
    }
    let segundoDigito = 11 - (soma % 11);
    segundoDigito = segundoDigito >= 10 ? 0 : segundoDigito;

    return parseInt(value[10]) === segundoDigito;
}
export function validarTelefone(value){
    value = removeCarecteresNaoNumericos(value);

    if (value.length === 13) {
        return true;
    } 
    return false;
}
export function validarSenha(senha){
    if(senha.length !== 8) {
        return false
    }
    return true;
}
export function removeCarecteresNaoNumericos(value){
    return value.replace(/[^\d]/g, '');
}