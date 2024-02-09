import random

# 手の選択肢
choices = ["グー", "チョキ", "パー"]

# プレイヤーとコンピュータの手
player_hand = None
computer_hand = None

# ゲームループ
while True:
  # プレイヤーの手を取得
  while True:
    player_hand = input("あなたの出す手を選択してください (グー, チョキ, パー): ")
    if player_hand in choices:
      break
    print("無効な入力です。")

  # コンピュータの手をランダムに生成
  computer_hand = random.choice(choices)

  # 勝敗判定
  if player_hand == computer_hand:
    print("引き分けです！")
  elif player_hand == "グー" and computer_hand == "チョキ":
    print("あなたの勝ちです！")
  elif player_hand == "チョキ" and computer_hand == "パー":
    print("あなたの勝ちです！")
  elif player_hand == "パー" and computer_hand == "グー":
    print("あなたの勝ちです！")
  else:
    print("あなたの負けです...")

  # もう一度プレイするか確認
  again = input("もう一度プレイしますか？ (y/n): ")
  if again != "y":
    break

print("ゲーム終了")
