const alertPlaceholder = document.getElementById('liveAlertPlaceholder')
const messageErrors = {
    'account with this email already exists.': 'Este email já está cadastrado. Você será redirecionado para a página de login.'
};

document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('registrationForm');
    const password = document.getElementById('password');
    const confirmPassword = document.getElementById('confirmPassword');
    const email = document.getElementById('email');
    const url = '/accounts/'

    form.addEventListener('submit', async function (event) {
        event.preventDefault(); // Impede o envio padrão do formulário

        // Validação personalizada: verificar se as senhas coincidem
        if (password.value !== confirmPassword.value) {
            confirmPassword.setCustomValidity('As senhas não coincidem.');
        } else {
            confirmPassword.setCustomValidity('');
        }

        // Ativar validações do Bootstrap
        if (!form.checkValidity()) {
            event.stopPropagation();
            form.classList.add('was-validated');
            return; // Sai do fluxo se o formulário não for válido
        }

        // Dados a serem enviados para a API
        const formData = {
            email: email.value,
            password: password.value
        };

        await makeRequest(formData, url)
    });
});


async function makeRequest(formData, url){
    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
            'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });

        if (response.ok) {
            const data = await response.json();
            window.location.href = '/cadastrar/informacoes'; // Redireciona para a página de sucesso
        } else {
            const errorData = await response.json();
            
            if (errorData.email && errorData.email.length > 0) {
                const errorMessage = errorData.email[0]; 
                const erroMessageTraduzida = messageErrors[errorMessage]
                
                lanceAlert(erroMessageTraduzida, 'danger');

                if (errorMessage === 'account with this email already exists.') {
                    setTimeout(() => {
                    window.location.href = '/login';
                    }, 3000);
                }
            }else {
                lanceAlert('Erro desconhecido', 'danger');
            }
        }
    } catch (error) {
        console.error('Erro na requisição:', error);
        lanceAlert('Erro de servidor, procure o suporte.', 'danger');
    }
}

function lanceAlert(message, type){
    var wrapper = document.createElement('div')
    wrapper.innerHTML = '<div class="alert alert-' + type + ' alert-dismissible" role="alert">' + message + '<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>'

    alertPlaceholder.append(wrapper)
}
