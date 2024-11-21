import {userHasRegister, makeGetRequest, setAuthorizationTokenHeader} from "./utils/api-utils.js";
import {ROUTES_API} from "./utils/global.js";
userHasRegister();

document.addEventListener("DOMContentLoaded", async function(){
    const headers = setAuthorizationTokenHeader();


    await makeGetRequest(ROUTES_API.get_pets, headers, async(response) => {
        const data = await response.json();
        console.log(data);
    });

});