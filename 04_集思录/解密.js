let CryptoJS = require('crypto-js');

function jslencode(text, aes_key) {
    let key = CryptoJS.enc.Utf8.parse(aes_key);
    let iv = CryptoJS.enc.Utf8.parse("");
    let srcs = CryptoJS.enc.Utf8.parse(text);
    let encrypted = CryptoJS.AES.encrypt(srcs, key, {
        iv: iv,
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
    });
    return encrypted.ciphertext.toString(CryptoJS.enc.Hex)
}

function fn(text) {
    let aes_key = '397151C04723421F'

    return jslencode(text, aes_key)
}
