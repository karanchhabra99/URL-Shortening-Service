
const endpoint = "https://r7e3t6bnug.execute-api.us-west-2.amazonaws.com/dev/";

const Shortener_URL = document.getElementById('Shortener_URL_id');
// Shortener_URL.style.display = 'none';

let user_URL = document.getElementById('URL'); // Assuming you have an input field with the ID 'URL'

// Function to add the protocol if missing
function addProtocol(url) {
    if (!url.startsWith('http://') && !url.startsWith('https://')) {
        url = 'http://' + url;
    }
    return url;
};

function create() {
    let user_URL = addProtocol(document.getElementById('URL').value);
    let payload = {
        "URL": user_URL,  // Fixed: Get the value of user_URL
    };
    
    fetch(endpoint, {
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
        document.getElementById('new_URL').innerHTML = "https://redirect-sug.s3.us-west-2.amazonaws.com/"+responseText["body"] // responseText;  // Fixed: Use responseText inside the function
    })
    .catch(error => {
        console.error("Error while making the request:", error);
    });
    // Shortener_URL.style.display = 'block';
    // document.getElementById('new_URL').innerHTML = JSON.stringify(payload)
}
