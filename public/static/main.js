send_button = document.getElementById('send-btn');
send_button.addEventListener('click', () =>{
    send_button.textContent = '发送中...';
    send_button.disabled = true;
    send_button.classList.add('disabled-button');
})