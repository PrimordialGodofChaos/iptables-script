import os
import time

t = 1 # Задержка

def run():
    print(chain_create())
    time.sleep(t)
    print(redirect_traffic())
    time.sleep(t)
    print(tcp_accept_rules())
    time.sleep(t)
    print(tcp_deny_rules())
    time.sleep(t)
    print(udp_accept_rules())
    time.sleep(t)
    print(udp_deny_rules())
def chain_create(): # Создаем цепочки для входящего TCP- и UDP-трафика:
    try:
        os.system('iptables -N TCP_IN')
        os.system('iptables -N UDP_IN')
        return "Correct: Chains created"
    except:
        return "Error: You can't create chains"
def redirect_traffic(): # Перенаправляем обработку входящего TCP- и UDP-трафика в новые цепочки:
    try:
        os.system('iptables -A INPUT -p tcp -j TCP_IN')
        os.system('iptables -A INPUT -p udp -j UDP_IN')
        return "Correct: Traffic redirected to new chains"
    except:
        return "Error: You can't redirect traffic to new chains"
def tcp_accept_rules(): # В цепочке для TCP-трафика создаем правила фильтрации:
    try:
        os.system('iptables -A TCP_IN -p tcp --dport 139 -m state --state NEW,RELATED,ESTABLISHED -j ACCEPT')
        os.system('iptables -A TCP_IN -p tcp --dport 445 -m state --state NEW,RELATED,ESTABLISHED -j ACCEPT')
        return "Correct: New filter's rules created"
    except:
        return "Error: You can't create new filter's rules for tcp-traffic"
def tcp_deny_rules(): # В цепочке для TCP-трафика блокируем все остальные TCP-соединения с логированием событий:
    try:
        os.system('iptables -A TCP_IN -p tcp -j LOG --log-prefix "Blocked TCP: "')
        os.system('iptables -A TCP_IN -p tcp -j REJECT')
        return 'Correct: Other tcp-connections created'
    except:
        return "Error: You can't to block other tcp-connections with to log events"
def udp_accept_rules(): # В цепочке для UDP-трафика создаем правила фильтрации:
    try:
        os.system('iptables -A UDP_IN -p udp --dport 137 -m state --state NEW,RELATED,ESTABLISHED -j ACCEPT')
        os.system('iptables -A UDP_IN -p udp --dport 138 -m state --state NEW,RELATED,ESTABLISHED -j ACCEPT')
        return "Correct: New filter's rules created"
    except:
        return "Error: You can't create new filter's rules for udp-traffic"
def udp_deny_rules(): # В цепочке для TCP-трафика блокируем все остальные UDP-соединения с логированием событий:
    try:
        os.system('iptables -A UDP_IN -p udp -j LOG --log-prefix "Blocked UDP: "')
        os.system('iptables -A UDP_IN -p udp -j REJECT')
        return 'Correct: Other udp-connections created'
    except:
        return "Error: You can't to block other udp-connections with to log events"
