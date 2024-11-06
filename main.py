from node_coin import NodeCoin
from node import Node
from max_heap import Transaction

if __name__ == "__main__":
    node_coin = NodeCoin()
    while True:
        input_data = input().strip()
        splash = input_data.split(" ")

        if len(splash) <= 1:
            print("-1")
            continue

        user_option = int(splash[0])
        when = Node(splash[1]).date_dating(splash[1])

        if user_option == 1:
            mucha = float(splash[2])
            node = node_coin.get_max(when)
            if node is None:
                node = Node(when)
                node_coin.insert(node)
            transaction_num = node.transaction_num
            node.transaction_num += 1
            node.root.insert(Transaction(mucha, transaction_num))

        elif user_option == 2:
            node = node_coin.get_max(when)
            if node is not None and not node.root.isEmpty():
                max_transaction = node.root.transactions[1]
                print(f"{max_transaction.t_amt} {max_transaction.t_num}")
            else:
                print("-1")

        elif user_option == 3:
            node = node_coin.get_max(when)
            if node is not None and not node.root.isEmpty():
                node.root.removeMax()
            else:
                print("-1")

        elif user_option == 4:
          node = node_coin.get_max(when)
          if node.root.isEmpty():
              print("-1")
          else:
            all_t = node_coin.get_all(when)
            print(all_t)

        else:
            print("-1")
