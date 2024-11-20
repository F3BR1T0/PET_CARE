export function redirectTo(url, time = 0) {
    setTimeout(() => {
        window.location = url
    }, time)
}

export function showAlert(message, type, id){
    const alertPlaceholder = document.getElementById(id);

    var wrapper = document.createElement('div');
    wrapper.innerHTML = '<div class="alert alert-' + type + ' alert-dismissible" role="alert">' + message + '<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>';

    alertPlaceholder.append(wrapper)
}