from queue import Queue

queue = Queue()

def generate_request(req):
    queue.put(req)
    print(f"Заявка {req} додана до черги.")

def process_request():
    if not queue.empty():
        req = queue.get()
        print(f"Заявка {req} оброблена!")
    else:
        print("Дана черга порожня!")

generate_request("A")
generate_request("B")
generate_request("C")

while not queue.empty():
    process_request()