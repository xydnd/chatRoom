from tkinter import *
import socket
from threading import Thread

def send():
    send_msg = text_text.get('0.0', END)
    print(send_msg)
    s.send(bytes(send_msg,'utf-8'))
    text_text.delete('0.0', END)

def get_msg():
    while True:
        try:
            msg=s.recv(1024).decode('utf-8')
            text_message.insert(END,msg)
        except:
            break

root=Tk()
root.title("聊天室")

message_frame=Frame(width=480,height=300,bg='white')
text_frame=Frame(width=480,height=100)
send_frame=Frame(width=480,height=30)

text_message=Text(message_frame)
text_text=Text(text_frame)
button_send=Button(send_frame,text="发送",command=send)

message_frame.grid(row=0,column=0,padx=3,pady=6)
text_frame.grid(row=1,column=0,padx=3,pady=6)
send_frame.grid(row=2,column=0)

message_frame.grid_propagate(0)
text_frame.grid_propagate(0)
send_frame.grid_propagate(0)

text_message.grid()
text_text.grid()
button_send.grid()

HOST='127.0.0.1'
PORT=8888

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))

receive_thread=Thread(target=get_msg)
receive_thread.start()

root.mainloop()
