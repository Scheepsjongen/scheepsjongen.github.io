const
    staticCacheName = "static-cache-v2",
    dynamicCacheName = "dynamic-cache-v2",
    staticAssets = [
        "index.html",
        "/list/",
        "/img/*",
        "/quiz/img/*",
        "/css/style.css",
        "/assets/main.css",
        "/js/*",
    ];

async function checkCache(e) {
    return await caches.match(e) || checkOnline(e)
}

async function checkOnline(e) {
    const a = await caches.open(dynamicCacheName);
    try {
        const c = await fetch(e);
        return await a.put(e,c.clone()),c
    } catch(c) {
        const t = await a.match(e);
        return t || (-1 !== e.url.indexOf(".html") ? caches.match("./index.html") : caches.match("./img/icons/back.png"))
    }
}

self.addEventListener("install", async e => {
    const a = await caches.open(staticCacheName);
    await a.addAll(staticAssets), console.log("Service worker has been installed")
}),
self.addEventListener("activate", async e => {
    const a = (await caches.keys()).map(async e => {
        [staticCacheName, dynamicCacheName].includes(e) || await caches.delete(e)
    });
    await Promise.all(a),console.log("Service worker has been activated")
}),
self.addEventListener("fetch", e => {
    console.log(`Trying to fetch ${e.request.url}`), e.respondWith(checkCache(e.request))
});
