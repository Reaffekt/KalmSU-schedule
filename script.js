let tg = window.Telegram.WebApp;
tg.expand(); // Разворачивает WebView
document.getElementById("username").innerText = tg.initDataUnsafe.user?.first_name || "Гость";