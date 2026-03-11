const crypto = require('crypto');

function _(e) {
    return crypto.createHash("md5").update(e.toString()).digest("hex")
}

function S(e, t) {
    d = "fanyideskweb";
    uu = "webfanyi";
    return _(`client=${d}&mysticTime=${e}&product=${uu}&key=${t}`);
}


function fn(data, e = "SRz6r3IGA6lj9i5zW0OYqgVZOtLDQe3e") {
    const a = (new Date).getTime();
    return {
        sign: S(a, e),
        client: "fanyideskweb",
        product: "webfanyi",
        appVersion: "1.0.0",
        vendor: "web",
        pointParam: "client,mysticTime,product",
        mysticTime: a,
        keyfrom: "fanyi.web",
        mid: 1,
        screen: 1,
        model: 1,
        network: "wifi",
        abtest: 0,
        yduuid: "abcdefg",
        i: data,
        from: "auto",
        to: "",
        useTerm: false,
        domain: "0",
        dictResult: true,
        keyid: "webfanyi"
    }
}


// 以下是解密内容
function T(e) {
    return crypto.createHash("md5").update(e).digest();
}

function fn_d(e, t = "ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl", a = "ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4") {
    if (!e) return null;

    // 使用 MD5 哈希生成密钥和 IV
    const key = T(t);      // key 已经是 16 字节的 Buffer (MD5 输出)
    const iv = T(a);       // iv 已经是 16 字节的 Buffer (MD5 输出)

    // 创建解密器
    const decipher = crypto.createDecipheriv('aes-128-cbc', key, iv);

    // 解密
    let decrypted = decipher.update(e, 'base64', 'utf-8');
    decrypted += decipher.final('utf-8');

    return JSON.parse(decrypted);
}


if (require.main === module) {
    const result = fn_d('Z21kD9ZK1ke6ugku2ccWu4n6eLnvoDT0YgGi0y3g-v0B9sYqg8L9D6UERNozYOHqnYdl2efZNyM6Trc_xS-zKtfTK4hb6JP8XwCzNh0avc8qItQUiIU_4wKKXJlIpvMvfKvJaaZzaX6VEtpkr2FdkfoT_Jgbm2GRSVj3r40autIdlImENG8hC0ZH4ww7utwuTt3Oo_ZpXg0BSq9wePSAB75-ChkiGKF9HTIPeCl2bl84SBD1XDfFCZpkKQhecYSs0JLoXOqP2ltavxRrg58Hp1q5uIgZZ_Oo2-Jmd-t1r4es40drcAq5bjmS62M2VJF8D6ojtOh9JTfNwgzD3CxYn-Pd7-TgHMyNEJEkFXTAyxzpjlFqtrCYDE3SZUYlENkqsL8Wrra1hM-1nTfiB-BLcWAdRBynNpP5_54aq_-GBsq8bB_9yEX5ovzDB4_Ry_spVVuUnb39iplMHCdCnjOD3ngiIDbl9SUz-9npjBX05ZYRdPmFPAl424qdoaxeVqnVoH8jQFPZVqaHMzu4mJg0SICDWFH7GP1zqGRbXd3ESjT_iBInl3gICt2XVuhh_nubcELkTEC6xbqEDRQkPUNMp9oC8N7JQ4SkgJyCbsmhC6FGgffKDIzkoWbb9njBHMJMR77gXDYHt9APzmKYS_IDH14bOC6UYJTGYBdBd8q0Q8qe1YSspmpPAC3P5Su6MA1XbhHu24vyCQAdW9RAUnlDiHQeDGtgN4gvMNWvZ6C8t42LSjMoNh5nok9D36xxu0fvnHcXySwzpY6ZwDyS0QXaoA==', "ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl", "ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4");
    console.log(result)
}
