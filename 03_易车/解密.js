const crypto = require('crypto');

function fn(serialId) {
    let new_date = new Date()
    let t = {
        "cid": "508",
        "timestamp": new_date.getTime(),
        "paramsKey": "f48aa2d0-31e0-42a6-a7a0-64ba148262f0",
        "ver": "v10.80.0",
        "cityId": "2501",
        "serialId": serialId
    }

    return {
        "x-platform": "pc",
        "x-timestamp": t.timestamp,
        "cid": t.cid,
        "x-sign": get_x_sign(t),
        "x-city-id": t.cityId,
        "x-ip-address": "175.152.181.225",
        "x-user-guid": "a49e4841-0183-4562-a299-29fb1a49d8ac",
        "reqid": f(new_date)
    }
}

function get_x_sign(t) {
    let n = "";
    let data = {
        "cityId": t.cityId,
        "serialId": t.serialId
    }

    let i = JSON.stringify(data)
    let o = "19DDD1FBDFF065D3A4DA777D2D7A81EC";
    n = "cid=" + t.cid + "&param=" + i + o + t.timestamp
    return crypto.createHash('md5').update(n).digest('hex');
}

function f(e) {
    return crypto.createHash('md5').update(Math.random() + e).digest('hex');
}

if (require.main === module) {
    console.log(fn())
}
