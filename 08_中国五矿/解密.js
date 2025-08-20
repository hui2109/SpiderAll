const JSEncryptLong = require('node-encrypt-js');
const crypto = require('crypto');

function fn(e, pubKey) {
    let t = new JSEncryptLong;
    t.setPublicKey(pubKey);
    e.sign = crypto.createHash('md5').update(JSON.stringify(e), 'utf8').digest('hex');
    e.timeStamp = +new Date;
    return JSON.stringify({
        param: t.encryptLong(JSON.stringify(e))
    })
}

if (require.main === module) {
    let e = {
        "inviteMethod": "",
        "businessClassfication": "",
        "mc": "",
        "lx": "ZBGG",
        "dwmc": "",
        "pageIndex": 4
    }
    console.log(fn(e));
}
