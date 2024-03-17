
const create_endpoint = "https://r7e3t6bnug.execute-api.us-west-2.amazonaws.com/dev/";
const delete_endpoint = "https://r7e3t6bnug.execute-api.us-west-2.amazonaws.com/dev/SUG-delete";


const Shortener_URL = document.getElementById('Shortener_URL_id');

function fetch_email() {
    const url = new URL(window.location.href) + '';

    const fragment = url.split('#')[1]; // Get the URL fragment

    // // Parse the fragment to extract the access token
    const params = new URLSearchParams(fragment);
    const accessToken = params.get('access_token');
    const idToken = params.get('id_token');

    // document.getElementById('new_URL').innerHTML = "accessToken"

    // document.getElementById('new_URL').innerHTML =idToken
    // Decode the base64-encoded access token
    const tokenParts = idToken.split('.');
    const payloadBase64 = tokenParts[1];
    const decodedPayload = atob(payloadBase64);

    // // // Parse the decoded payload as JSON
    // const payload = JSON.parse(decodedPayload);

    // // Extract the user email
    const payload_js = JSON.parse(decodedPayload);
    // document.getElementById('new_URL').innerHTML += "<BR><BR> Payload:" + payload_js["email"]
    // console.log('User email:', payload);
    return payload_js["email"]
};


// Function to add the protocol if missing
function addProtocol(url) {
    if (!url.startsWith('http://') && !url.startsWith('https://')) {
        url = 'http://' + url;
    }
    return url;
};

function create() {
    let email = fetch_email()
    let user_URL = addProtocol(document.getElementById('URL').value);
    let payload = {
        "URL": user_URL,  // Fixed: Get the value of user_URL
        "email": email
    };

    fetch(create_endpoint, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${idToken}`
        },
        body: JSON.stringify(payload),
        redirect: 'follow'
    })
        .then(response => response.json())
        .then(responseText => {
            console.log("Response from the server:", responseText)
            Shortener_URL.style.display = 'block'
            document.getElementById('API_Response').innerHTML = `
            <form>
            <input type="text" class="form-control" value="https://sqvreaj3o7.execute-api.us-west-2.amazonaws.com/dev/${responseText["body"]}" id="myInput">
              </form>
            <button class="btn btn-primary w-100 py-2" id="Copy_button" onclick="copy_text()">Copy Text</button>
            `
        })
        .catch(error => {
            console.error("Error while making the request:", error);
        });
    // Shortener_URL.style.display = 'block';
    // document.getElementById('new_URL').innerHTML = JSON.stringify(payload)
};


async function copy_text() {
    /* Get the text field */
    var copyText = document.getElementById("myInput").value;

    try {
        /* Copy the text inside the text field */
        await navigator.clipboard.writeText(copyText);
    
        /* Alert the copied text */
        var button = document.getElementById("Copy_button");
        button.style.backgroundColor = "#337ab7";
    } catch (err) {
        console.error('Failed to copy text: ', err);
    }
};


function delete_URL() {
    let email = fetch_email()
    // console.log()
    let delete_provided_URL = document.getElementById("D_URL").value.split("/").pop();
    let payload = {
        "UserString": delete_provided_URL,  // Fixed: Get the value of user_URL
        "email": email
    };

    fetch(delete_endpoint, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload),
        redirect: 'follow'
    })
        .then(response => response.json())
        .then(responseText => {
            console.log("Response from the server:", responseText)
            Shortener_URL.style.display = 'block'
            document.getElementById('API_Response').innerHTML = responseText["body"]// responseText;  // Fixed: Use responseText inside the function
        })
        .catch(error => {
            console.error("Error while making the request:", error);
        });
    // Shortener_URL.style.display = 'block';
    // document.getElementById('new_URL').innerHTML = JSON.stringify(payload)
}

;