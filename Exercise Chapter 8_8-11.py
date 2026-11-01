def send_messages(messages, sent_messages):
    """Memindahkan pesan dari list utama ke list sent_messages saat dikirim."""
    while messages:
        current_message = messages.pop(0)
        print(f"Mengirim pesan: {current_message}")
        sent_messages.append(current_message)

messages_to_send = ["Pesan 1", "Pesan 2", "Pesan 3"]
sent_messages = []

messages_original = ["Pesan A", "Pesan B", "Pesan C"]
sent_messages_archive = []

print("\n--- Exercise 8-11 ---")
send_messages(messages_original[:], sent_messages_archive)

print("\nKondisi List Setelah Dikirim (Menggunakan Copy):")
print(f"messages_original (tetap utuh): {messages_original}")
print(f"sent_messages_archive: {sent_messages_archive}")