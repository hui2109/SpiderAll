function fn_o(n) {
    t = "",
        ['66', '72', '6f', '6d', '43', '68', '61', '72', '43', '6f', '64', '65']["forEach"](function (n) {
            t += unescape("%u00" + n)
        });
    var t, e = t;
    return String["fromCharCode"](n)
}

function fn_h(n, t) {
    for (var e = (n = n["split"](""))["length"], r = t["length"], a = "charCodeAt", i = 0; i < e; i++)
        n[i] = fn_o(n[i][a](0) ^ t[(i + 10) % r][a](0));
    return n["join"]("")
}

function fn_p(t) {
    t = encodeURIComponent(t)["replace"](/%([0-9A-F]{2})/g, function (n, t) {
        return fn_o("0x" + t)
    });
    return btoa(t)  // JS原生Base64字符串方法, 将字节转换为base64字符串
}


function fn(t) {
    // var n = i['ej']("synct");  // cookies里的synct值
    // var s = -i['ej']("syncd") || +new Date - 1000 * n;  // 算时间差, s=1448左右即可, 不需要那么精确, 因为有网络波动
    var s = 1448
    var e, r = +new Date - (s || 0) - 1661224081041, a = [];

    return undefined === t["params"] && (t["params"] = {}),
        Object["keys"](t["params"])["forEach"](function (n) {
            if (n == "analysis")
                return false;
            t["params"]["hasOwnProperty"](n) && a["push"](t["params"][n])
        }),
        a = a["sort"]()["join"](""),
        a = fn_p(a),
        a = (a += "@#" + t["url"]["replace"](t["baseURL"], "")) + ("@#" + r) + ("@#" + 3),
        e = fn_p(fn_h(a, "xyz517cda96efgh")),
    -1 == t["url"]["indexOf"]("analysis") && (t["url"] += (-1 != t["url"]["indexOf"]("?") ? "&" : "?") + "analysis" + "=" + encodeURIComponent(e)),
        e
}


if (require.main === module) {
    var t = {
        "url": "/indexV2/getIndexRank",
        "params": {
            "setting": 0,
            "genre": "36"
        },
        "baseURL": "https://api.qimai.cn",
    }
    console.log(fn(t));
}
