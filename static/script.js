function sendMessage() {
    const input = document.getElementById('user_input');
    const message = input.value.trim();
    if (!message) return;

    const messagesDiv = document.getElementById('messages');
    messagesDiv.innerHTML += `<div><b>Kamu:</b> ${message}</div>`;
    input.value = '';

    fetch('/api/chat', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ message: message })
    })
    .then(res => res.json())
    .then(data => {
        messagesDiv.innerHTML += `<div><b>Jarvis:</b> ${data.reply}</div>`;
    });
}
