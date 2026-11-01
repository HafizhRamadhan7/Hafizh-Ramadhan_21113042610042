def send_messages(messages, sent_messages):
    """Memindahkan pesan dari list utama ke list sent_messages saat dikirim."""
    while messages:
        current_message = messages.pop(0)
        print(f"Mengirim pesan: {current_message}")
        sent_messages.append(current_message)

messages_to_send = ["Pesan 1", "Pesan 2", "Pesan 3"]
sent_messages = []

print("\n--- Exercise 8-10 ---")
send_messages(messages_to_send, sent_messages)

print("\nKondisi List Setelah Dikirim:")
print(f"messages_to_send: {messages_to_send}")
print(f"sent_messages: {sent_messages}")