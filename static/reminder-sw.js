self.addEventListener("install", (event) => {
    self.skipWaiting();
});

self.addEventListener("activate", (event) => {
    event.waitUntil(self.clients.claim());
});

self.addEventListener("message", (event) => {
    const data = event.data || {};
    if (data.type !== "SHOW_RECRUITER_NOTIFICATION") return;

    const title = data.title || "Recruitment reminder";
    const options = {
        body: data.body || "Recruitment reminder due now.",
        icon: "/app/static/icon.png",
        badge: "/app/static/icon.png",
        tag: data.tag || ("recruiter-reminder-" + Date.now()),
        renotify: true,
        requireInteraction: true,
        silent: false,
        vibrate: [260, 120, 260, 120, 480],
        timestamp: Date.now(),
        data: {
            url: data.url || "/"
        }
    };

    event.waitUntil(self.registration.showNotification(title, options));
});

self.addEventListener("notificationclick", (event) => {
    event.notification.close();
    const targetUrl = (event.notification.data && event.notification.data.url) || "/";

    event.waitUntil(
        self.clients.matchAll({ type: "window", includeUncontrolled: true }).then((clients) => {
            for (const client of clients) {
                if ("focus" in client) {
                    client.focus();
                    return;
                }
            }
            if (self.clients.openWindow) {
                return self.clients.openWindow(targetUrl);
            }
            return undefined;
        })
    );
});
