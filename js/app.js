window.addEventListener("load", () => {
    "serviceWorker" in navigator&&navigator.serviceWorker.register("/js/sw.js").then(e => {
        console.log("Service worker successfully registered", e)
    }).catch(e => {
        console.log("Service worker registration failed", e)
    })
});
