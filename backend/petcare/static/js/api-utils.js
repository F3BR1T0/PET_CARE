import {getMessageOrDefault} from './tradutor.js';
import {redirectTo} from './site-utils.js';

const routeLogin = "/login";

export async function makePostRequest(url, headers = {}, formData = {}, responseCaseOk = (data) => {}, responseCaseError = (data) => {}, responseCaseErrorCatch = () => {}){
    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
            'Content-Type': 'application/json',
            ...headers
            },
            body: JSON.stringify(formData)
        });
        if (response.ok) {
            responseCaseOk(response);
        } else {
            responseCaseError(response);
        }
    } catch (error) {
        console.error('Erro na requisição:', error);
        responseCaseErrorCatch()
    }
}
export async function makeGetRequest(url, headers = {}, responseCaseOk = (response) => {}, responseCaseError = (response) => {}, responseCaseErrorCatch = () => {}) {
    try {
        const response = await fetch(url, {
            method: 'GET',
            headers: {
            'Content-Type': 'application/json',
            ...headers
            }
        });
        if (response.ok) {
            responseCaseOk(response);
        } else {
            responseCaseError(response);
        }
    } catch (error) {
        console.error('Erro na requisição:', error);
        responseCaseErrorCatch()
    }
}

export const tratamentosDeErro = {
    accounts: {
        register : {
            tratarErroDeEmail : async(response, callback) => {
                const data = await response.json();
                if (data.email && data.email.length > 0) {
                    const message = data.email[0]; 
                    const messageTraduzida = getMessageOrDefault(message);
                    
                    callback(messageTraduzida.message);
    
                    if (messageTraduzida.id == 1 ) {
                        redirectTo(routeLogin, 3000);
                    }
                }
            }
        },
        unauthorized: (response) => {
            if(response.status == 401) {
                redirectTo(routeLogin)
            }
        }
    }
}

export async function userIsAuthenticated(){
    const url = "/accounts/me";
    const responseCaseError = (data) => {
        tratamentosDeErro.accounts.unauthorized(data);
    }
    await makeGetRequest(url, 'GET',null, responseCaseError)
    
}

export async function makeLogin(email, password) {
    const data = {
        email,
        password
    };
    console.log(data);
}