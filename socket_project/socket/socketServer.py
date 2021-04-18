from threading import Thread
import socket

#连接的用户名称和地址用字典保存
clientname={}
addresses={}
#定义服务器可以连接的client数量
accept_num=10

HOST='127.0.0.1'
PORT=8888

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))

#循环向用户发送消息
def brodcast(msg,name=''):
    for conn in clientname:
        conn.send(bytes(name,'utf-8')+msg)

#消息处理
def handle_client(conn,addr):
    name=conn.recv(1024).decode("utf-8")
    clientname[conn]=name
    welcome=f"\n欢迎{name}进入聊天室\n"
    #def __init__(self, value=b'', encoding=None, errors='strict'):
    brodcast(bytes(welcome,'utf-8'))
    while True:
        try:
            msg=conn.recv(1024)
            brodcast(msg,name)
        except:
            conn.close()
            del clientname[conn]
            brodcast(bytes(f"\n{name}离开聊天室\n",'utf-8'))

if __name__ == '__main__':
    s.listen(accept_num)
    print("服务器已经开启，正在监听用户的请求...")
    while True:
        conn,addr = s.accept()
        print(addr,"已经建立连接\n")
        #获取的连接，服务器发送消息给客户端
        conn.send("欢迎来到聊天室，请输入你的名称进行聊天\n".encode('utf-8'))
        addresses[conn]=addr
        #要支持多个用户发送，故用多线程
        Thread(target=handle_client,args=(conn,addr)).start()






