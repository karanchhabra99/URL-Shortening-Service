
const url = new URL(window.location.href)+ '';

const fragment = url.split('#')[1]; // Get the URL fragment

// Parse the fragment to extract the access token
const params = new URLSearchParams(fragment);
const accessToken = params.get('access_token');

document.getElementById('new_URL').innerHTML =accessToken
// Decode the base64-encoded access token
const tokenParts = accessToken.split('.');
const payloadBase64 = tokenParts[1];
const decodedPayload = atob(payloadBase64);

// // Parse the decoded payload as JSON
// const payload = JSON.parse(decodedPayload);

// // Extract the user email
// const email = payload.email;
document.getElementById('new_URL').innerHTML += "<BR><BR> " + payload 
console.log('User email:', payload);